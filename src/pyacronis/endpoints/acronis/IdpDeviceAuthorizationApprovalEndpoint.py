from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.interfaces import (
    IGettable,
)
from pyacronis.models.acronis import (
    DeviceAuthorizationApprovalResponse,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class IdpDeviceAuthorizationApprovalEndpoint(
    AcronisEndpoint,
    IGettable[DeviceAuthorizationApprovalResponse, AcronisRequestParams],
):
    """Represents the /idp/device_authorization/approval endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "approval", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, DeviceAuthorizationApprovalResponse)

    def get(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> DeviceAuthorizationApprovalResponse:
        """
        Performs a GET request against the /idp/device_authorization/approval endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DeviceAuthorizationApprovalResponse: The parsed response data.
        """
        return self._parse_one(
            DeviceAuthorizationApprovalResponse,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> None:
        """
        Performs a POST request against the /idp/device_authorization/approval endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            None: This endpoint returns an empty response body.
        """
        super()._make_request("POST", data=data, params=params)
        return None
