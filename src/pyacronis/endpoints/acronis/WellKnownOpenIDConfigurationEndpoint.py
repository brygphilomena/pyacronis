from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
)
from pyacronis.models.acronis import (
    OpenIDConfiguration,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class WellKnownOpenIDConfigurationEndpoint(
    AcronisEndpoint,
    IGettable[OpenIDConfiguration, AcronisRequestParams],
):
    """Represents the /.well-known/openid-configuration endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "openid-configuration", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, OpenIDConfiguration)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> OpenIDConfiguration:
        """
        Performs a GET request against the /.well-known/openid-configuration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpenIDConfiguration: The parsed response data.
        """
        return self._parse_one(
            OpenIDConfiguration,
            super()._make_request("GET", data=data, params=params).json(),
        )
