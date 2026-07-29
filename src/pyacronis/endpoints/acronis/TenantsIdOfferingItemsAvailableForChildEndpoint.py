from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
)
from pyacronis.models.acronis import (
    OfferingItemList,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdOfferingItemsAvailableForChildEndpoint(
    AcronisEndpoint,
    IGettable[OfferingItemList, AcronisRequestParams],
):
    """Represents the /tenants/{tenant_id}/offering_items/available_for_child endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "available_for_child", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, OfferingItemList)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> OfferingItemList:
        """
        Performs a GET request against the /tenants/{tenant_id}/offering_items/available_for_child endpoint.

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
