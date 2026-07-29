from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.IdpTokenEndpoint import IdpTokenEndpoint
from pyacronis.endpoints.acronis.IdpRevokeTokenEndpoint import IdpRevokeTokenEndpoint
from pyacronis.endpoints.acronis.IdpIntrospectTokenEndpoint import IdpIntrospectTokenEndpoint
from pyacronis.endpoints.acronis.IdpOttEndpoint import IdpOttEndpoint
from pyacronis.endpoints.acronis.IdpLogoutEndpoint import IdpLogoutEndpoint
from pyacronis.endpoints.acronis.IdpDeviceAuthorizationEndpoint import IdpDeviceAuthorizationEndpoint
from pyacronis.endpoints.acronis.IdpExternalLoginEndpoint import IdpExternalLoginEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class IdpEndpoint(
    AcronisEndpoint,
):
    """Represents the /idp endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "idp", parent_endpoint=parent_endpoint)
        self.token = self._register_child_endpoint(IdpTokenEndpoint(client, parent_endpoint=self))
        self.revoke_token = self._register_child_endpoint(IdpRevokeTokenEndpoint(client, parent_endpoint=self))
        self.introspect_token = self._register_child_endpoint(IdpIntrospectTokenEndpoint(client, parent_endpoint=self))
        self.ott = self._register_child_endpoint(IdpOttEndpoint(client, parent_endpoint=self))
        self.logout = self._register_child_endpoint(IdpLogoutEndpoint(client, parent_endpoint=self))
        self.device_authorization = self._register_child_endpoint(IdpDeviceAuthorizationEndpoint(client, parent_endpoint=self))
        self.external_login = self._register_child_endpoint(IdpExternalLoginEndpoint(client, parent_endpoint=self))
