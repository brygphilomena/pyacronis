from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    OfferingItemPrice,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdOfferingItemsPricingEndpoint(
    AcronisEndpoint,
    IGettable[OfferingItemPrice, AcronisRequestParams],
    IPuttable[OfferingItemPrice, AcronisRequestParams],
):
    """Represents the /tenants/{tenant_id}/offering_items/pricing endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "pricing", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, OfferingItemPrice)
        IPuttable.__init__(self, OfferingItemPrice)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[OfferingItemPrice]:
        """
        Performs a GET request against the /tenants/{tenant_id}/offering_items/pricing endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OfferingItemPrice]: The parsed response data.
        """
        return self._parse_many(
            OfferingItemPrice,
            super()._make_request("GET", data=data, params=params).json().get("items", []),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[OfferingItemPrice]:
        """
        Performs a PUT request against the /tenants/{tenant_id}/offering_items/pricing endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OfferingItemPrice]: The parsed response data.
        """
        return self._parse_many(
            OfferingItemPrice,
            super()._make_request("PUT", data=data, params=params).json().get("items", []),
        )
