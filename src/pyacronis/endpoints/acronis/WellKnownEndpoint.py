from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.WellKnownOpenIDConfigurationEndpoint import WellKnownOpenIDConfigurationEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class WellKnownEndpoint(
    AcronisEndpoint,
):
    """Represents the /.well-known endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, ".well-known", parent_endpoint=parent_endpoint)
        self.openid_configuration = self._register_child_endpoint(WellKnownOpenIDConfigurationEndpoint(client, parent_endpoint=self))
