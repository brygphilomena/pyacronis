from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.TenantsIdOfferingItemsAvailableForChildEndpoint import TenantsIdOfferingItemsAvailableForChildEndpoint
from pyacronis.endpoints.acronis.TenantsIdOfferingItemsPricingEndpoint import TenantsIdOfferingItemsPricingEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    OfferingItemList,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdOfferingItemsEndpoint(
    AcronisEndpoint,
    IGettable[OfferingItemList, AcronisRequestParams],
    IPuttable[OfferingItemList, AcronisRequestParams],
):
    """Represents the /tenants/{tenant_id}/offering_items endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "offering_items", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, OfferingItemList)
        IPuttable.__init__(self, OfferingItemList)
        self.available_for_child = self._register_child_endpoint(TenantsIdOfferingItemsAvailableForChildEndpoint(client, parent_endpoint=self))
        self.pricing = self._register_child_endpoint(TenantsIdOfferingItemsPricingEndpoint(client, parent_endpoint=self))

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> OfferingItemList:
        """
        Performs a GET request against the /tenants/{tenant_id}/offering_items endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OfferingItemList: The parsed response data.
        """
        return self._parse_one(
            OfferingItemList,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> OfferingItemList:
        """
        Performs a PUT request against the /tenants/{tenant_id}/offering_items endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OfferingItemList: The parsed response data.
        """
        return self._parse_one(
            OfferingItemList,
            super()._make_request("PUT", data=data, params=params).json(),
        )
