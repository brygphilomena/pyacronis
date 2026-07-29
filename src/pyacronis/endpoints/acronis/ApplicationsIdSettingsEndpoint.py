from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.ApplicationsIdSettingsTenantsEndpoint import ApplicationsIdSettingsTenantsEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class ApplicationsIdSettingsEndpoint(
    AcronisEndpoint,
):
    """Represents the /applications/{application_id}/settings endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "settings", parent_endpoint=parent_endpoint)
        self.tenants = self._register_child_endpoint(ApplicationsIdSettingsTenantsEndpoint(client, parent_endpoint=self))
