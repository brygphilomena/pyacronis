from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    Setting,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class ApplicationsIdSettingsTenantsIdNameEndpoint(
    AcronisEndpoint,
    IGettable[Setting, AcronisRequestParams],
    IPuttable[Setting, AcronisRequestParams],
):
    """Represents the /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name} endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Setting)
        IPuttable.__init__(self, Setting)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Setting:
        """
        Performs a GET request against the /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Setting: The parsed response data.
        """
        return self._parse_one(
            Setting,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Setting:
        """
        Performs a PUT request against the /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Setting: The parsed response data.
        """
        return self._parse_one(
            Setting,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            None: This endpoint returns an empty response body.
        """
        super()._make_request("DELETE", data=data, params=params)
        return None
