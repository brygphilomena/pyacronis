from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class RegistrationTokensIdEndpoint(
    AcronisEndpoint,
):
    """Represents the /registration_tokens/{token_id} endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

    def delete(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /registration_tokens/{token_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            None: This endpoint returns an empty response body.
        """
        super()._make_request("DELETE", data=data, params=params)
        return None
