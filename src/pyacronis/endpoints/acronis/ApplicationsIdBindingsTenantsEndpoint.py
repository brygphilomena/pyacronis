from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.ApplicationsIdBindingsTenantsIdEndpoint import ApplicationsIdBindingsTenantsIdEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class ApplicationsIdBindingsTenantsEndpoint(
    AcronisEndpoint,
):
    """Represents the /applications/{application_id}/bindings/tenants endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "tenants", parent_endpoint=parent_endpoint)

    def id(self, id: str) -> ApplicationsIdBindingsTenantsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ApplicationsIdBindingsTenantsIdEndpoint
        object to move down the chain.

        Parameters:
            id (str): The ID to set.
        Returns:
            ApplicationsIdBindingsTenantsIdEndpoint: The initialized ApplicationsIdBindingsTenantsIdEndpoint object.
        """
        child = ApplicationsIdBindingsTenantsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
