from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.TenantsIdMfaStatusEndpoint import TenantsIdMfaStatusEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdMfaEndpoint(
    AcronisEndpoint,
):
    """Represents the /tenants/{tenant_id}/mfa endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "mfa", parent_endpoint=parent_endpoint)
        self.status = self._register_child_endpoint(TenantsIdMfaStatusEndpoint(client, parent_endpoint=self))
