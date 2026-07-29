from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IPostable,
)
from pyacronis.models.acronis import (
    CheckPasswordResult,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class UsersCheckPasswordEndpoint(
    AcronisEndpoint,
    IPostable[CheckPasswordResult, AcronisRequestParams],
):
    """Represents the /users/check_password endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "check_password", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, CheckPasswordResult)

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> CheckPasswordResult:
        """
        Performs a POST request against the /users/check_password endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CheckPasswordResult: The parsed response data.
        """
        return self._parse_one(
            CheckPasswordResult,
            super()._make_request("POST", data=data, params=params).json(),
        )
