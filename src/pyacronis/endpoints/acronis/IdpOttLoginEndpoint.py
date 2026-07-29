from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IPostable,
)
from pyacronis.models.acronis import (
    User,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class IdpOttLoginEndpoint(
    AcronisEndpoint,
    IPostable[User, AcronisRequestParams],
):
    """Represents the /idp/ott/login endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "login", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, User)

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> User:
        """
        Performs a POST request against the /idp/ott/login endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            User: The parsed response data.
        """
        return self._parse_one(
            User,
            super()._make_request("POST", data=data, params=params).json(),
        )
