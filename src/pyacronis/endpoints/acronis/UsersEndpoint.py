from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.UsersCheckLoginEndpoint import UsersCheckLoginEndpoint
from pyacronis.endpoints.acronis.UsersCheckPasswordEndpoint import UsersCheckPasswordEndpoint
from pyacronis.endpoints.acronis.UsersMeEndpoint import UsersMeEndpoint
from pyacronis.endpoints.acronis.UsersIdEndpoint import UsersIdEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPostable,
)
from pyacronis.models.acronis import (
    User,
    UserBatch,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class UsersEndpoint(
    AcronisEndpoint,
    IGettable[UserBatch, AcronisRequestParams],
    IPostable[User, AcronisRequestParams],
):
    """Represents the /users endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "users", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, UserBatch)
        IPostable.__init__(self, User)
        self.check_login = self._register_child_endpoint(UsersCheckLoginEndpoint(client, parent_endpoint=self))
        self.check_password = self._register_child_endpoint(UsersCheckPasswordEndpoint(client, parent_endpoint=self))
        self.me = self._register_child_endpoint(UsersMeEndpoint(client, parent_endpoint=self))

    def id(self, id: str) -> UsersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized UsersIdEndpoint
        object to move down the chain.

        Parameters:
            id (str): The ID to set.
        Returns:
            UsersIdEndpoint: The initialized UsersIdEndpoint object.
        """
        child = UsersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> UserBatch:
        """
        Performs a GET request against the /users endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UserBatch: The parsed response data.
        """
        return self._parse_one(
            UserBatch,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> User:
        """
        Performs a POST request against the /users endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            User: The parsed response data.
        """
        return self._parse_one(
            User,
            super()._make_request("POST", data=data, params=params).json(),
        )
