from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.ClientsIdEndpoint import ClientsIdEndpoint
from pyacronis.interfaces import (
    IPostable,
)
from pyacronis.models.acronis import (
    ClientPostResult,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class ClientsEndpoint(
    AcronisEndpoint,
    IPostable[ClientPostResult, AcronisRequestParams],
):
    """Represents the /clients endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "clients", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, ClientPostResult)

    def id(self, id: str) -> ClientsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ClientsIdEndpoint
        object to move down the chain.

        Parameters:
            id (str): The ID to set.
        Returns:
            ClientsIdEndpoint: The initialized ClientsIdEndpoint object.
        """
        child = ClientsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[dict]:
        """
        Performs a GET request against the /clients endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[dict]: The `items` from the response body, as returned by the API.
        """
        return super()._make_request("GET", data=data, params=params).json().get("items", [])

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> ClientPostResult:
        """
        Performs a POST request against the /clients endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ClientPostResult: The parsed response data.
        """
        return self._parse_one(
            ClientPostResult,
            super()._make_request("POST", data=data, params=params).json(),
        )
