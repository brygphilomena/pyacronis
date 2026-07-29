from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    AccessPoliciesList,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class UsersIdAccessPoliciesEndpoint(
    AcronisEndpoint,
    IGettable[AccessPoliciesList, AcronisRequestParams],
    IPuttable[AccessPoliciesList, AcronisRequestParams],
):
    """Represents the /users/{user_id}/access_policies endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "access_policies", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, AccessPoliciesList)
        IPuttable.__init__(self, AccessPoliciesList)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> AccessPoliciesList:
        """
        Performs a GET request against the /users/{user_id}/access_policies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AccessPoliciesList: The parsed response data.
        """
        return self._parse_one(
            AccessPoliciesList,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> AccessPoliciesList:
        """
        Performs a PUT request against the /users/{user_id}/access_policies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AccessPoliciesList: The parsed response data.
        """
        return self._parse_one(
            AccessPoliciesList,
            super()._make_request("PUT", data=data, params=params).json(),
        )
