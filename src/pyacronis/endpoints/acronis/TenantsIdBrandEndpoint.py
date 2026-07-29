from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.TenantsIdBrandLogoEndpoint import TenantsIdBrandLogoEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPostable,
    IPuttable,
)
from pyacronis.models.acronis import (
    Tenant,
    TenantBrand,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdBrandEndpoint(
    AcronisEndpoint,
    IGettable[TenantBrand, AcronisRequestParams],
    IPostable[Tenant, AcronisRequestParams],
    IPuttable[Tenant, AcronisRequestParams],
):
    """Represents the /tenants/{tenant_id}/brand endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "brand", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, TenantBrand)
        IPostable.__init__(self, Tenant)
        IPuttable.__init__(self, Tenant)
        self.logo = self._register_child_endpoint(TenantsIdBrandLogoEndpoint(client, parent_endpoint=self))

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> TenantBrand:
        """
        Performs a GET request against the /tenants/{tenant_id}/brand endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TenantBrand: The parsed response data.
        """
        return self._parse_one(
            TenantBrand,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Tenant:
        """
        Performs a POST request against the /tenants/{tenant_id}/brand endpoint.

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

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Tenant:
        """
        Performs a PUT request against the /tenants/{tenant_id}/brand endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Tenant: The parsed response data.
        """
        return self._parse_one(
            Tenant,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /tenants/{tenant_id}/brand endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            None: This endpoint returns an empty response body.
        """
        super()._make_request("DELETE", data=data, params=params)
        return None
