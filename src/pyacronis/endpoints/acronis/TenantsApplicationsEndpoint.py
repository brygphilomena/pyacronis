from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
)
from pyacronis.models.acronis import (
    TenantApplications,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsApplicationsEndpoint(
    AcronisEndpoint,
    IGettable[TenantApplications, AcronisRequestParams],
):
    """Represents the /tenants/applications endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "applications", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, TenantApplications)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[TenantApplications]:
        """
        Performs a GET request against the /tenants/applications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TenantApplications]: The parsed response data.
        """
        return self._parse_many(
            TenantApplications,
            super()._make_request("GET", data=data, params=params).json().get("items", []),
        )
