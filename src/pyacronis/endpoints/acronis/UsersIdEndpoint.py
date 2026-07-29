from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.UsersIdAccessPoliciesEndpoint import UsersIdAccessPoliciesEndpoint
from pyacronis.endpoints.acronis.UsersIdMfaEndpoint import UsersIdMfaEndpoint
from pyacronis.endpoints.acronis.UsersIdPasswordEndpoint import UsersIdPasswordEndpoint
from pyacronis.endpoints.acronis.UsersIdRestoreEndpoint import UsersIdRestoreEndpoint
from pyacronis.endpoints.acronis.UsersIdSendActivationEmailEndpoint import UsersIdSendActivationEmailEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPuttable,
)
from pyacronis.models.acronis import (
    User,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class UsersIdEndpoint(
    AcronisEndpoint,
    IGettable[User, AcronisRequestParams],
    IPuttable[User, AcronisRequestParams],
):
    """Represents the /users/{user_id} endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, User)
        IPuttable.__init__(self, User)
        self.access_policies = self._register_child_endpoint(UsersIdAccessPoliciesEndpoint(client, parent_endpoint=self))
        self.mfa = self._register_child_endpoint(UsersIdMfaEndpoint(client, parent_endpoint=self))
        self.password = self._register_child_endpoint(UsersIdPasswordEndpoint(client, parent_endpoint=self))
        self.restore = self._register_child_endpoint(UsersIdRestoreEndpoint(client, parent_endpoint=self))
        self.send_activation_email = self._register_child_endpoint(UsersIdSendActivationEmailEndpoint(client, parent_endpoint=self))

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> User:
        """
        Performs a GET request against the /users/{user_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            User: The parsed response data.
        """
        return self._parse_one(
            User,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> User:
        """
        Performs a PUT request against the /users/{user_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            User: The parsed response data.
        """
        return self._parse_one(
            User,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /users/{user_id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            None: This endpoint returns an empty response body.
        """
        super()._make_request("DELETE", data=data, params=params)
        return None
