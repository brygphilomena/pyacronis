from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.LocationsIdInfraEndpoint import LocationsIdInfraEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    Location,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class LocationsIdEndpoint(
    AcronisEndpoint,
    IGettable[Location, AcronisRequestParams],
    IPuttable[Location, AcronisRequestParams],
):
    """Represents the /locations/{location_id} endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Location)
        IPuttable.__init__(self, Location)
        self.infra = self._register_child_endpoint(LocationsIdInfraEndpoint(client, parent_endpoint=self))

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Location:
        """
        Performs a GET request against the /locations/{location_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Location: The parsed response data.
        """
        return self._parse_one(
            Location,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Location:
        """
        Performs a PUT request against the /locations/{location_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Location: The parsed response data.
        """
        return self._parse_one(
            Location,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /locations/{location_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            None: This endpoint returns an empty response body.
        """
        super()._make_request("DELETE", data=data, params=params)
        return None
