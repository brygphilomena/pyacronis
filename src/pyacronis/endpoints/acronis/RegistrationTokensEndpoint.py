from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.RegistrationTokensIdEndpoint import RegistrationTokensIdEndpoint
from pyacronis.interfaces import (
    IGettable,
    IPostable,
)
from pyacronis.models.acronis import (
    RegistrationToken,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class RegistrationTokensEndpoint(
    AcronisEndpoint,
    IGettable[RegistrationToken, AcronisRequestParams],
    IPostable[RegistrationToken, AcronisRequestParams],
):
    """Represents the /registration_tokens endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "registration_tokens", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, RegistrationToken)
        IPostable.__init__(self, RegistrationToken)

    def id(self, id: str) -> RegistrationTokensIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized RegistrationTokensIdEndpoint
        object to move down the chain.

        Parameters:
            id (str): The ID to set.
        Returns:
            RegistrationTokensIdEndpoint: The initialized RegistrationTokensIdEndpoint object.
        """
        child = RegistrationTokensIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> list[RegistrationToken]:
        """
        Performs a GET request against the /registration_tokens endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RegistrationToken]: The parsed response data.
        """
        return self._parse_many(
            RegistrationToken,
            super()._make_request("GET", data=data, params=params).json().get("items", []),
        )

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> RegistrationToken:
        """
        Performs a POST request against the /registration_tokens endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RegistrationToken: The parsed response data.
        """
        return self._parse_one(
            RegistrationToken,
            super()._make_request("POST", data=data, params=params).json(),
        )
