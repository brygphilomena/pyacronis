import json
import typing
from base64 import b64encode
from datetime import datetime, timedelta, timezone

from pyacronis.clients.base_client import AcronisClient
from pyacronis.config import Config

if typing.TYPE_CHECKING:
    from pyacronis.endpoints.acronis.AccountsEndpoint import AccountsEndpoint
    from pyacronis.endpoints.acronis.ApplicationsEndpoint import ApplicationsEndpoint
    from pyacronis.endpoints.acronis.ClientsEndpoint import ClientsEndpoint
    from pyacronis.endpoints.acronis.IdpEndpoint import IdpEndpoint
    from pyacronis.endpoints.acronis.InfraEndpoint import InfraEndpoint
    from pyacronis.endpoints.acronis.LocationsEndpoint import LocationsEndpoint
    from pyacronis.endpoints.acronis.RegistrationTokensEndpoint import RegistrationTokensEndpoint
    from pyacronis.endpoints.acronis.ReportsEndpoint import ReportsEndpoint
    from pyacronis.endpoints.acronis.SearchEndpoint import SearchEndpoint
    from pyacronis.endpoints.acronis.TenantsEndpoint import TenantsEndpoint
    from pyacronis.endpoints.acronis.UsersEndpoint import UsersEndpoint
    from pyacronis.endpoints.acronis.WellKnownEndpoint import WellKnownEndpoint


class AcronisAPIClient(AcronisClient):
    """
    Acronis API client. Handles the connection to the Acronis API
    and the configuration of all the available endpoints.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        datacenter_url: str,
    ) -> None:
        """
        Initializes the client with the given credentials.

        Parameters:
            privatekey (str): Your Acronis API private key.
        """
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self.datacenter_url: str = datacenter_url
        self.token_expiry_time: datetime = datetime.now(tz=timezone.utc)

        # Grab first access token
        self.access_token: str = self._get_access_token()
        self.tenant_id: str = self._get_tenant_id()

    # Initializing endpoints
    @property
    def accounts(self) -> "AccountsEndpoint":
        from pyacronis.endpoints.acronis.AccountsEndpoint import AccountsEndpoint

        return AccountsEndpoint(self)

    @property
    def applications(self) -> "ApplicationsEndpoint":
        from pyacronis.endpoints.acronis.ApplicationsEndpoint import ApplicationsEndpoint

        return ApplicationsEndpoint(self)

    @property
    def clients(self) -> "ClientsEndpoint":
        from pyacronis.endpoints.acronis.ClientsEndpoint import ClientsEndpoint

        return ClientsEndpoint(self)

    @property
    def idp(self) -> "IdpEndpoint":
        from pyacronis.endpoints.acronis.IdpEndpoint import IdpEndpoint

        return IdpEndpoint(self)

    @property
    def infra(self) -> "InfraEndpoint":
        from pyacronis.endpoints.acronis.InfraEndpoint import InfraEndpoint

        return InfraEndpoint(self)

    @property
    def locations(self) -> "LocationsEndpoint":
        from pyacronis.endpoints.acronis.LocationsEndpoint import LocationsEndpoint

        return LocationsEndpoint(self)

    @property
    def registration_tokens(self) -> "RegistrationTokensEndpoint":
        from pyacronis.endpoints.acronis.RegistrationTokensEndpoint import RegistrationTokensEndpoint

        return RegistrationTokensEndpoint(self)

    @property
    def reports(self) -> "ReportsEndpoint":
        from pyacronis.endpoints.acronis.ReportsEndpoint import ReportsEndpoint

        return ReportsEndpoint(self)

    @property
    def search(self) -> "SearchEndpoint":
        from pyacronis.endpoints.acronis.SearchEndpoint import SearchEndpoint

        return SearchEndpoint(self)

    @property
    def tenants(self) -> "TenantsEndpoint":
        from pyacronis.endpoints.acronis.TenantsEndpoint import TenantsEndpoint

        return TenantsEndpoint(self)

    @property
    def users(self) -> "UsersEndpoint":
        from pyacronis.endpoints.acronis.UsersEndpoint import UsersEndpoint

        return UsersEndpoint(self)

    @property
    def well_known(self) -> "WellKnownEndpoint":
        from pyacronis.endpoints.acronis.WellKnownEndpoint import WellKnownEndpoint

        return WellKnownEndpoint(self)

    def _get_url(self) -> str:
        """
        Generates and returns the URL for the Acronis API endpoints based on the company url and codebase.
        Logs in an obtains an access token.
        Returns:
            str: API URL.
        """
        return f"{self.datacenter_url}/api/2"

    def _get_access_token(self) -> str:
        """
        Performs a request to the Acronis API to obtain an access token.
        """

        auth_response = self._make_request(
            "POST",
            f"{self._get_url()}/idp/token",
            raw={
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
