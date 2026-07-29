from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.TenantsApplicationsEndpoint import TenantsApplicationsEndpoint
from pyacronis.endpoints.acronis.TenantsOfferingItemsEndpoint import TenantsOfferingItemsEndpoint
from pyacronis.endpoints.acronis.TenantsUsagesEndpoint import TenantsUsagesEndpoint
from pyacronis.endpoints.acronis.TenantsIdEndpoint import TenantsIdEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPostable,
)
from pyacronis.models.acronis import (
    Tenant,
    TenantBatch,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsEndpoint(
    AcronisEndpoint,
    IGettable[TenantBatch, AcronisRequestParams],
    IPostable[Tenant, AcronisRequestParams],
):
    """Represents the /tenants endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "tenants", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, TenantBatch)
        IPostable.__init__(self, Tenant)
        self.applications = self._register_child_endpoint(TenantsApplicationsEndpoint(client, parent_endpoint=self))
        self.offering_items = self._register_child_endpoint(TenantsOfferingItemsEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(TenantsUsagesEndpoint(client, parent_endpoint=self))

    def id(self, id: str) -> TenantsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TenantsIdEndpoint
        object to move down the chain.

        Parameters:
            id (str): The ID to set.
        Returns:
            TenantsIdEndpoint: The initialized TenantsIdEndpoint object.
        """
        child = TenantsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> TenantBatch:
        """
        Performs a GET request against the /tenants endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TenantBatch: The parsed response data.
        """
        return self._parse_one(
            TenantBatch,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Tenant:
        """
        Performs a POST request against the /tenants endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Tenant: The parsed response data.
        """
        return self._parse_one(
            Tenant,
            super()._make_request("POST", data=data, params=params).json(),
        )
