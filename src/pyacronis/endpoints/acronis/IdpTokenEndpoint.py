from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IPostable,
)
from pyacronis.models.acronis import (
    Token,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class IdpTokenEndpoint(
    AcronisEndpoint,
    IPostable[Token, AcronisRequestParams],
):
    """Represents the /idp/token endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "token", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Token)

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Token:
        """
        Performs a POST request against the /idp/token endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Token: The parsed response data.
        """
        return self._parse_one(
            Token,
            super()._make_request("POST", data=data, params=params).json(),
        )
