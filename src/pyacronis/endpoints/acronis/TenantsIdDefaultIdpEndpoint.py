from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IPuttable,
)
from pyacronis.models.acronis import (
    Tenant,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdDefaultIdpEndpoint(
    AcronisEndpoint,
    IPuttable[Tenant, AcronisRequestParams],
):
    """Represents the /tenants/{tenant_id}/default_idp endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "default_idp", parent_endpoint=parent_endpoint)
        IPuttable.__init__(self, Tenant)

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Tenant:
        """
        Performs a PUT request against the /tenants/{tenant_id}/default_idp endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Tenant: The parsed response data.
        """
        return self._parse_one(
            Tenant,
            super()._make_request("PUT", data=data, params=params).json(),
        )
