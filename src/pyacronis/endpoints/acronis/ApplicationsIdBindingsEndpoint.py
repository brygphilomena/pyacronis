from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.ApplicationsIdBindingsTenantsEndpoint import ApplicationsIdBindingsTenantsEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class ApplicationsIdBindingsEndpoint(
    AcronisEndpoint,
):
    """Represents the /applications/{application_id}/bindings endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "bindings", parent_endpoint=parent_endpoint)
        self.tenants = self._register_child_endpoint(ApplicationsIdBindingsTenantsEndpoint(client, parent_endpoint=self))
