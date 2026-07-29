from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class UsersIdPasswordEndpoint(
    AcronisEndpoint,
):
    """Represents the /users/{user_id}/password endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "password", parent_endpoint=parent_endpoint)

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> None:
        """
        Performs a POST request against the /users/{user_id}/password endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            None: This endpoint returns an empty response body.
        """
        super()._make_request("POST", data=data, params=params)
        return None
