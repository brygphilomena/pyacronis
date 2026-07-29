from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.ApplicationsIdBindingsEndpoint import ApplicationsIdBindingsEndpoint
from pyacronis.endpoints.acronis.ApplicationsIdSettingsEndpoint import ApplicationsIdSettingsEndpoint
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


class ApplicationsIdEndpoint(
    AcronisEndpoint,
    IGettable[Application, AcronisRequestParams],
):
    """Represents the /applications/{application_id} endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Application)
        self.bindings = self._register_child_endpoint(ApplicationsIdBindingsEndpoint(client, parent_endpoint=self))
        self.settings = self._register_child_endpoint(ApplicationsIdSettingsEndpoint(client, parent_endpoint=self))

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Application:
        """
        Performs a GET request against the /applications/{application_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Application: The parsed response data.
        """
        return self._parse_one(
            Application,
            super()._make_request("GET", data=data, params=params).json(),
        )
