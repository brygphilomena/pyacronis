from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    TenantUsages,
    UsagePutResultItem,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsUsagesEndpoint(
    AcronisEndpoint,
    IGettable[TenantUsages, AcronisRequestParams],
    IPuttable[UsagePutResultItem, AcronisRequestParams],
):
    """Represents the /tenants/usages endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "usages", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, TenantUsages)
        IPuttable.__init__(self, UsagePutResultItem)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[TenantUsages]:
        """
        Performs a GET request against the /tenants/usages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TenantUsages]: The parsed response data.
        """
        return self._parse_many(
            TenantUsages,
            super()._make_request("GET", data=data, params=params).json().get("items", []),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[UsagePutResultItem]:
        """
        Performs a PUT request against the /tenants/usages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UsagePutResultItem]: The parsed response data.
        """
        return self._parse_many(
            UsagePutResultItem,
            super()._make_request("PUT", data=data, params=params).json().get("items", []),
        )
