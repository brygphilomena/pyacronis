from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
)
from pyacronis.models.acronis import (
    ForgotLink,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class AccountsForgotLinkEndpoint(
    AcronisEndpoint,
    IGettable[ForgotLink, AcronisRequestParams],
):
    """Represents the /accounts/forgot_link endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "forgot_link", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ForgotLink)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> ForgotLink:
        """
        Performs a GET request against the /accounts/forgot_link endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ForgotLink: The parsed response data.
        """
        return self._parse_one(
            ForgotLink,
            super()._make_request("GET", data=data, params=params).json(),
        )
