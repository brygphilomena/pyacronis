from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.ApplicationsIdSettingsTenantsIdNameEndpoint import ApplicationsIdSettingsTenantsIdNameEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class ApplicationsIdSettingsTenantsIdEndpoint(
    AcronisEndpoint,
):
    """Represents the /applications/{application_id}/settings/tenants/{tenant_id} endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

    def setting_name(self, id: str) -> ApplicationsIdSettingsTenantsIdNameEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ApplicationsIdSettingsTenantsIdNameEndpoint
        object to move down the chain.

        Parameters:
            id (str): The ID to set.
        Returns:
            ApplicationsIdSettingsTenantsIdNameEndpoint: The initialized ApplicationsIdSettingsTenantsIdNameEndpoint object.
        """
        child = ApplicationsIdSettingsTenantsIdNameEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
