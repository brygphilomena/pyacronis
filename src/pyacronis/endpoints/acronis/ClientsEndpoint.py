from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.ClientsIdEndpoint import ClientsIdEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPostable,
)
from pyacronis.models.acronis import (
    Client,
    ClientPostResult,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class ClientsEndpoint(
    AcronisEndpoint,
    IGettable[Client, AcronisRequestParams],
    IPostable[ClientPostResult, AcronisRequestParams],
):
    """Represents the /clients endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "clients", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Client)
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
    ) -> list[Client]:
        """
        Performs a GET request against the /clients endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Client]: The parsed response data.
        """
        return self._parse_many(
            Client,
            super()._make_request("GET", data=data, params=params).json().get("items", []),
        )

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
