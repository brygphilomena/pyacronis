from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.InfraIdEndpoint import InfraIdEndpoint
from pyacronis.interfaces import (
    IPostable,
)
from pyacronis.models.acronis import (
    Infra,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class InfraEndpoint(
    AcronisEndpoint,
    IPostable[Infra, AcronisRequestParams],
):
    """Represents the /infra endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "infra", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Infra)

    def id(self, id: str) -> InfraIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized InfraIdEndpoint
        object to move down the chain.

        Parameters:
            id (str): The ID to set.
        Returns:
            InfraIdEndpoint: The initialized InfraIdEndpoint object.
        """
        child = InfraIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[dict]:
        """
        Performs a GET request against the /infra endpoint.

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
    ) -> Infra:
        """
        Performs a POST request against the /infra endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Infra: The parsed response data.
        """
        return self._parse_one(
            Infra,
            super()._make_request("POST", data=data, params=params).json(),
        )
