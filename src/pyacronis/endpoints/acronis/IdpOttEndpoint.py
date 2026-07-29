from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.IdpOttLoginEndpoint import IdpOttLoginEndpoint
from pyacronis.interfaces import (
    IPostable,
)
from pyacronis.models.acronis import (
    IdpOtt,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class IdpOttEndpoint(
    AcronisEndpoint,
    IPostable[IdpOtt, AcronisRequestParams],
):
    """Represents the /idp/ott endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "ott", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, IdpOtt)
        self.login = self._register_child_endpoint(IdpOttLoginEndpoint(client, parent_endpoint=self))

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> IdpOtt:
        """
        Performs a POST request against the /idp/ott endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            IdpOtt: The parsed response data.
        """
        return self._parse_one(
            IdpOtt,
            super()._make_request("POST", data=data, params=params).json(),
        )
