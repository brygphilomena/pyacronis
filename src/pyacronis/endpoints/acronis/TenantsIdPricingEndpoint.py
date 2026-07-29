from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    TenantPricingSettings,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdPricingEndpoint(
    AcronisEndpoint,
    IGettable[TenantPricingSettings, AcronisRequestParams],
    IPuttable[TenantPricingSettings, AcronisRequestParams],
):
    """Represents the /tenants/{tenant_id}/pricing endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "pricing", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, TenantPricingSettings)
        IPuttable.__init__(self, TenantPricingSettings)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> TenantPricingSettings:
        """
        Performs a GET request against the /tenants/{tenant_id}/pricing endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TenantPricingSettings: The parsed response data.
        """
        return self._parse_one(
            TenantPricingSettings,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> TenantPricingSettings:
        """
        Performs a PUT request against the /tenants/{tenant_id}/pricing endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TenantPricingSettings: The parsed response data.
        """
        return self._parse_one(
            TenantPricingSettings,
            super()._make_request("PUT", data=data, params=params).json(),
        )
