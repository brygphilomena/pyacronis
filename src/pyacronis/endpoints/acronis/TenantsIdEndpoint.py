from __future__ import annotations  # noqa: N999

from pyacronis.endpoints.acronis.TenantsIdApplicationsEndpoint import (
    TenantsIdApplicationsEndpoint,
)
from pyacronis.endpoints.acronis.TenantsIdBrandEndpoint import TenantsIdBrandEndpoint
from pyacronis.endpoints.acronis.TenantsIdChildrenEndpoint import (
    TenantsIdChildrenEndpoint,
)
from pyacronis.endpoints.acronis.TenantsIdDefaultIdpEndpoint import (
    TenantsIdDefaultIdpEndpoint,
)
from pyacronis.endpoints.acronis.TenantsIdEditionEndpoint import (
    TenantsIdEditionEndpoint,
)
from pyacronis.endpoints.acronis.TenantsIdLocationsEndpoint import (
    TenantsIdLocationsEndpoint,
)
from pyacronis.endpoints.acronis.TenantsIdMfaEndpoint import TenantsIdMfaEndpoint
from pyacronis.endpoints.acronis.TenantsIdOfferingItemsEndpoint import (
    TenantsIdOfferingItemsEndpoint,
)
from pyacronis.endpoints.acronis.TenantsIdPricingEndpoint import (
    TenantsIdPricingEndpoint,
)
from pyacronis.endpoints.acronis.TenantsIdRegistrationTokensEndpoint import (
    TenantsIdRegistrationTokensEndpoint,
)
from pyacronis.endpoints.acronis.TenantsIdReportsEndpoint import (
    TenantsIdReportsEndpoint,
)
from pyacronis.endpoints.acronis.TenantsIdRestoreEndpoint import (
    TenantsIdRestoreEndpoint,
)
from pyacronis.endpoints.acronis.TenantsIdUsagesEndpoint import TenantsIdUsagesEndpoint
from pyacronis.endpoints.acronis.TenantsIdUsersEndpoint import TenantsIdUsersEndpoint
from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    Tenant,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class TenantsIdEndpoint(
    AcronisEndpoint,
    IGettable[Tenant, AcronisRequestParams],
    IPuttable[Tenant, AcronisRequestParams],
):
    """Represents the /tenants/{tenant_id} endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Tenant)
        IPuttable.__init__(self, Tenant)
        self.applications = self._register_child_endpoint(TenantsIdApplicationsEndpoint(client, parent_endpoint=self))
        self.brand = self._register_child_endpoint(TenantsIdBrandEndpoint(client, parent_endpoint=self))
        self.children = self._register_child_endpoint(TenantsIdChildrenEndpoint(client, parent_endpoint=self))
        self.default_idp = self._register_child_endpoint(TenantsIdDefaultIdpEndpoint(client, parent_endpoint=self))
        self.edition = self._register_child_endpoint(TenantsIdEditionEndpoint(client, parent_endpoint=self))
        self.locations = self._register_child_endpoint(TenantsIdLocationsEndpoint(client, parent_endpoint=self))
        self.mfa = self._register_child_endpoint(TenantsIdMfaEndpoint(client, parent_endpoint=self))
        self.offering_items = self._register_child_endpoint(TenantsIdOfferingItemsEndpoint(client, parent_endpoint=self))
        self.pricing = self._register_child_endpoint(TenantsIdPricingEndpoint(client, parent_endpoint=self))
        self.registration_tokens = self._register_child_endpoint(TenantsIdRegistrationTokensEndpoint(client, parent_endpoint=self))
        self.reports = self._register_child_endpoint(TenantsIdReportsEndpoint(client, parent_endpoint=self))
        self.restore = self._register_child_endpoint(TenantsIdRestoreEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(TenantsIdUsagesEndpoint(client, parent_endpoint=self))
        self.users = self._register_child_endpoint(TenantsIdUsersEndpoint(client, parent_endpoint=self))

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Tenant:
        """
        Performs a GET request against the /tenants/{tenant_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Tenant: The parsed response data.
        """
        return self._parse_one(
            Tenant,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> Tenant:
        """
        Performs a PUT request against the /tenants/{tenant_id} endpoint.

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
        Performs a DELETE request against the /tenants/{tenant_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            None: This endpoint returns an empty response body.
        """
        super()._make_request("DELETE", data=data, params=params)
        return None
