from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.LocationsIdEndpoint import LocationsIdEndpoint
from pyacronis.interfaces import (
    IPostable,
)
from pyacronis.models.acronis import (
    Location,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class LocationsEndpoint(
    AcronisEndpoint,
    IPostable[Location, AcronisRequestParams],
):
    """Represents the /locations endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "locations", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Location)

    def id(self, id: str) -> LocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized LocationsIdEndpoint
        object to move down the chain.

        Parameters:
            id (str): The ID to set.
        Returns:
            LocationsIdEndpoint: The initialized LocationsIdEndpoint object.
        """
        child = LocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[dict]:
        """
        Performs a GET request against the /locations endpoint.

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
    ) -> Location:
        """
        Performs a POST request against the /locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Location: The parsed response data.
        """
        return self._parse_one(
            Location,
            super()._make_request("POST", data=data, params=params).json(),
        )
