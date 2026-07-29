from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
)
from pyacronis.models.acronis import (
    GlobalSearchResult,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class SearchEndpoint(
    AcronisEndpoint,
    IGettable[GlobalSearchResult, AcronisRequestParams],
):
    """Represents the /search endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "search", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, GlobalSearchResult)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[GlobalSearchResult]:
        """
        Performs a GET request against the /search endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[GlobalSearchResult]: The parsed response data.
        """
        return self._parse_many(
            GlobalSearchResult,
            super()._make_request("GET", data=data, params=params).json().get("items", []),
        )
