import json
import typing
from base64 import b64encode
from datetime import datetime, timedelta, timezone

from pyacronis.clients.base_client import AcronisClient
from pyacronis.clients.acronis_client import AcronisAPIClient
from pyacronis.config import Config



class AcronisDRAPIClient(AcronisClient):
    """
    Acronis Disaster Recovery API client. Handles the connection to the Acronis Disaster Recovery API
    and the configuration of all the available endpoints.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        datacenter_url: str,
        customer_tenant_id: str,
    ) -> None:
        """
        Initializes the client with the given credentials.

        Parameters:
            privatekey (str): Your Acronis API private key.
        """
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self.datacenter_url: str = datacenter_url
        self.customer_tenant_id: str = customer_tenant_id
        self.token_expiry_time: datetime = datetime.now(tz=timezone.utc)

        # Grab first access token
        self.access_token: str = self._get_access_token()
        self.tenant_id: str = self._get_tenant_id()

    def _get_url(self) -> str:
        """
        Generates and returns the URL for the Acronis API endpoints based on the company url and codebase.
        Logs in an obtains an access token.
        Returns:
            str: API URL.
        """
        return f"{self.datacenter_url}/api/dr/v2"

    def _get_access_token(self) -> str:
        """
        Performs a request to the Acronis DR API to obtain an access token.
        """

        scoped_data: list = {
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": self._get_access_token(), # TODO: FIX THIS ASAP TO USE THE TOKEN FROM THE ACRONIS API
            "scope": f"urn:acronis.com:tenant-id:{self.customer_tenant_id}"
        }

        auth_response = self._make_request(
            "POST",
            f"{self.datacenter_url}/api/2/idp/token",
            data={
                "grant_type": "client_credentials",
                },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": 'Basic ' + b64encode(f'{self.client_id}:{self.client_secret}'.encode('ascii')).decode('ascii'),
                },
        )
        auth_resp_json = auth_response.json()
        token = auth_resp_json["access_token"]
        expiry = datetime.fromtimestamp(timestamp=auth_resp_json["expires_on"])  # noqa: DTZ006
        expiry = expiry.replace(tzinfo=timezone.utc) if expiry.tzinfo is None else expiry.astimezone(timezone.utc)
        self.token_expiry_time = expiry
        return token

    def _get_tenant_id(self) -> str:
        """
        Performs a request to the Acronis API to obtain an the api client's tenant ID.
        """

        tenantid_response = self._make_request(
            "GET",
            f"{self._get_url()}/clients/{self.client_id}",
            headers={
                "Authorization": f"Bearer {self.access_token}",
                },
        )
        tenantid_json = tenantid_response.json()
        return tenantid_json['tenant_id']

    def _refresh_access_token_if_necessary(self):
        if datetime.now(tz=timezone.utc) > self.token_expiry_time - timedelta(seconds=60):
            self.access_token = self._get_access_token()

    def _reauthenticate(self) -> bool:
        # Called by the base client after a 401 to recover from a token that
        # expired earlier than expected (clock skew) or was revoked server-side.
        self.access_token = self._get_access_token()
        return True

    def _get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests. The access token is refreshed if necessary before returning.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.access_token}",
        }
