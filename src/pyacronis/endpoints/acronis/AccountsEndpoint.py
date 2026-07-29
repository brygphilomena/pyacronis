from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.AccountsForgotLinkEndpoint import AccountsForgotLinkEndpoint
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class AccountsEndpoint(
    AcronisEndpoint,
):
    """Represents the /accounts endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "accounts", parent_endpoint=parent_endpoint)
        self.forgot_link = self._register_child_endpoint(AccountsForgotLinkEndpoint(client, parent_endpoint=self))
