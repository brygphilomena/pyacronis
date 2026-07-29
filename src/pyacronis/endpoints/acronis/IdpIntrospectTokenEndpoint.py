from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IPostable,
)
from pyacronis.models.acronis import (
    TokenIntrospectionResponse,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class IdpIntrospectTokenEndpoint(
    AcronisEndpoint,
    IPostable[TokenIntrospectionResponse, AcronisRequestParams],
):
    """Represents the /idp/introspect_token endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "introspect_token", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, TokenIntrospectionResponse)

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> TokenIntrospectionResponse:
        """
        Performs a POST request against the /idp/introspect_token endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TokenIntrospectionResponse: The parsed response data.
        """
        return self._parse_one(
            TokenIntrospectionResponse,
            super()._make_request("POST", data=data, params=params).json(),
        )
