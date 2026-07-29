from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.ApplicationsIdEndpoint import ApplicationsIdEndpoint
from pyacronis.interfaces import (
    IGettable,
)
from pyacronis.models.acronis import (
    Application,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class ApplicationsEndpoint(
    AcronisEndpoint,
    IGettable[Application, AcronisRequestParams],
):
    """Represents the /applications endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "applications", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Application)

    def id(self, id: str) -> ApplicationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ApplicationsIdEndpoint
        object to move down the chain.

        Parameters:
            id (str): The ID to set.
        Returns:
            ApplicationsIdEndpoint: The initialized ApplicationsIdEndpoint object.
        """
        child = ApplicationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[Application]:
        """
        Performs a GET request against the /applications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Application]: The parsed response data.
        """
        return self._parse_many(
            Application,
            super()._make_request("GET", data=data, params=params).json().get("items", []),
        )
