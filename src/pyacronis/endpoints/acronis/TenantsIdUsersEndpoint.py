from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdUsersEndpoint(
    AcronisEndpoint,
):
    """Represents the /tenants/{tenant_id}/users endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "users", parent_endpoint=parent_endpoint)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[str]:
        """
        Performs a GET request against the /tenants/{tenant_id}/users endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[str]: The list of UUIDs returned by the API.
        """
        return super()._make_request("GET", data=data, params=params).json().get("items", [])
