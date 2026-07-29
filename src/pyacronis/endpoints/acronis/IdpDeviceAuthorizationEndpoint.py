from pyacronis.endpoints.base.base_endpoint import AcronisEndpoint
from pyacronis.endpoints.acronis.IdpDeviceAuthorizationApprovalEndpoint import IdpDeviceAuthorizationApprovalEndpoint
from pyacronis.interfaces import (
    IPostable,
)
from pyacronis.models.acronis import (
    DeviceAuthorizationResponse,
)
from pyacronis.types import (
    JSON,
    AcronisRequestParams,
)


class IdpDeviceAuthorizationEndpoint(
    AcronisEndpoint,
    IPostable[DeviceAuthorizationResponse, AcronisRequestParams],
):
    """Represents the /idp/device_authorization endpoint of the Acronis Account Management API."""

    def __init__(self, client, parent_endpoint=None) -> None:
        AcronisEndpoint.__init__(self, client, "device_authorization", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, DeviceAuthorizationResponse)
        self.approval = self._register_child_endpoint(IdpDeviceAuthorizationApprovalEndpoint(client, parent_endpoint=self))

    def post(
        self,
        data: JSON | None = None,
        params: AcronisRequestParams | None = None,
    ) -> DeviceAuthorizationResponse:
        """
        Performs a POST request against the /idp/device_authorization endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DeviceAuthorizationResponse: The parsed response data.
        """
        return self._parse_one(
            DeviceAuthorizationResponse,
            super()._make_request("POST", data=data, params=params).json(),
        )
