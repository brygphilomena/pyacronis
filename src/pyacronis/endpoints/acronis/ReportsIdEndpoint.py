from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.ReportsIdStoredEndpoint import ReportsIdStoredEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    Report,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class ReportsIdEndpoint(
    AcronisEndpoint,
    IGettable[Report, AcronisRequestParams],
    IPuttable[Report, AcronisRequestParams],
):
    """Represents the /reports/{report_id} endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Report)
        IPuttable.__init__(self, Report)
        self.stored = self._register_child_endpoint(ReportsIdStoredEndpoint(client, parent_endpoint=self))

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Report:
        """
        Performs a GET request against the /reports/{report_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Report: The parsed response data.
        """
        return self._parse_one(
            Report,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Report:
        """
        Performs a PUT request against the /reports/{report_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Report: The parsed response data.
        """
        return self._parse_one(
            Report,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /reports/{report_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            None: This endpoint returns an empty response body.
        """
        super()._make_request("DELETE", data=data, params=params)
        return None
