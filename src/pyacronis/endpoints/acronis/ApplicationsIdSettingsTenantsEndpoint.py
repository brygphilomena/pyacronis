from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.ApplicationsIdSettingsTenantsIdEndpoint import ApplicationsIdSettingsTenantsIdEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class ApplicationsIdSettingsTenantsEndpoint(
    AcronisEndpoint,
):
    """Represents the /applications/{application_id}/settings/tenants endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "tenants", parent_endpoint=parent_endpoint)

    def id(self, id: str) -> ApplicationsIdSettingsTenantsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ApplicationsIdSettingsTenantsIdEndpoint
        object to move down the chain.

        Parameters:
            id (str): The ID to set.
        Returns:
            ApplicationsIdSettingsTenantsIdEndpoint: The initialized ApplicationsIdSettingsTenantsIdEndpoint object.
        """
        child = ApplicationsIdSettingsTenantsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
