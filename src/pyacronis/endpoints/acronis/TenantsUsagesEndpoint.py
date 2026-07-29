from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsUsagesEndpoint(
    AcronisEndpoint,
):
    """Represents the /tenants/usages endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "usages", parent_endpoint=parent_endpoint)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[dict]:
        """
        Performs a GET request against the /tenants/usages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[dict]: The `items` from the response body, as returned by the API.
        """
        return super()._make_request("GET", data=data, params=params).json().get("items", [])

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[dict]:
        """
        Performs a PUT request against the /tenants/usages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[dict]: The `items` from the response body, as returned by the API.
        """
        return super()._make_request("PUT", data=data, params=params).json().get("items", [])
