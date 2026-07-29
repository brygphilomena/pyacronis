from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IPostable,
)
from pyacronis.models.acronis import (
    Tenant,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdBrandLogoEndpoint(
    AcronisEndpoint,
    IPostable[Tenant, AcronisRequestParams],
):
    """Represents the /tenants/{tenant_id}/brand/logo endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "logo", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Tenant)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> bytes:
        """
        Performs a GET request against the /tenants/{tenant_id}/brand/logo endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            bytes: The raw response body.
        """
        return super()._make_request("GET", data=data, params=params).content

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Tenant:
        """
        Performs a POST request against the /tenants/{tenant_id}/brand/logo endpoint.

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
