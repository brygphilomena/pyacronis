from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class UsersIdMfaStatusEndpoint(
    AcronisEndpoint,
):
    """Represents the /users/{user_id}/mfa/status endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "status", parent_endpoint=parent_endpoint)

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> None:
        """
        Performs a PUT request against the /users/{user_id}/mfa/status endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            None: This endpoint returns an empty response body.
        """
        super()._make_request("PUT", data=data, params=params)
        return None
