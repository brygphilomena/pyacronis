from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    MfaTenantStatus,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdMfaStatusEndpoint(
    AcronisEndpoint,
    IGettable[MfaTenantStatus, AcronisRequestParams],
    IPuttable[MfaTenantStatus, AcronisRequestParams],
):
    """Represents the /tenants/{tenant_id}/mfa/status endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "status", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, MfaTenantStatus)
        IPuttable.__init__(self, MfaTenantStatus)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> MfaTenantStatus:
        """
        Performs a GET request against the /tenants/{tenant_id}/mfa/status endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MfaTenantStatus: The parsed response data.
        """
        return self._parse_one(
            MfaTenantStatus,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> MfaTenantStatus:
        """
        Performs a PUT request against the /tenants/{tenant_id}/mfa/status endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MfaTenantStatus: The parsed response data.
        """
        return self._parse_one(
            MfaTenantStatus,
            super()._make_request("PUT", data=data, params=params).json(),
        )
