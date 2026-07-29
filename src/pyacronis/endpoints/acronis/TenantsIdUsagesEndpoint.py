from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
)
from pyacronis.models.acronis import (
    Usage,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdUsagesEndpoint(
    AcronisEndpoint,
    IGettable[Usage, AcronisRequestParams],
):
    """Represents the /tenants/{tenant_id}/usages endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "usages", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Usage)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Usage:
        """
        Performs a GET request against the /tenants/{tenant_id}/usages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Usage: The parsed response data.
        """
        return self._parse_many(
            Usage,
            super()._make_request("GET", data=data, params=params).json().get("items", []),
        )
