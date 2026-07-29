from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
)
from pyacronis.models.acronis import (
    UserMe,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class UsersMeEndpoint(
    AcronisEndpoint,
    IGettable[UserMe, AcronisRequestParams],
):
    """Represents the /users/me endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "me", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, UserMe)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> UserMe:
        """
        Performs a GET request against the /users/me endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UserMe: The parsed response data.
        """
        return self._parse_one(
            UserMe,
            super()._make_request("GET", data=data, params=params).json(),
        )
