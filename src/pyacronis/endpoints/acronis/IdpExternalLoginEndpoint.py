from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class IdpExternalLoginEndpoint(
    AcronisEndpoint,
):
    """Represents the /idp/external-login endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "external-login", parent_endpoint=parent_endpoint)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> str:
        """
        Performs a GET request against the /idp/external-login endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            str: The raw response body.
        """
        return super()._make_request("GET", data=data, params=params).text
