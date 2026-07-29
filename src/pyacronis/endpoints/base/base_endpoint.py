from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
    from pydantic import BaseModel
    from requests import Response

    from pyacronis.clients.base_client import AcronisClient
    from pyacronis.types import (
        RequestData,
        RequestMethod,
        RequestParams,
    )

TChildEndpoint = TypeVar("TChildEndpoint", bound="AcronisEndpoint")
TModel = TypeVar("TModel", bound="BaseModel")


class AcronisEndpoint:
    """
    AcronisEndpoint is a base class for all Acronis API endpoint classes.
    It provides a generic implementation for interacting with the Acronis API,
    handling requests, parsing responses into model instances, and managing pagination.

    AcronisEndpoint makes use of a generic type variable TModel, which represents
    the expected AcronisModel type for the endpoint. This allows for type-safe
    handling of model instances throughout the class.

    Each derived class should specify the AcronisModel type it will be working with
    when inheriting from AcronisEndpoint. For example:
    class CompanyEndpoint(AcronisEndpoint[CompanyModel]).

    AcronisEndpoint provides methods for making API requests and handles pagination
    using the PaginatedResponse class. By default, most CRUD methods raise a
    NotImplementedError, which should be overridden in derived classes to provide
    endpoint-specific implementations.

    AcronisEndpoint also supports handling nested endpoints, which are referred to as
    child endpoints. Child endpoints can be registered and accessed through their parent
    endpoint, allowing for easy navigation through related resources in the API.

    Args:
        client: The AcronisAPIClient instance.
        endpoint_url (str): The base URL for the specific endpoint.
        parent_endpoint (AcronisEndpoint, optional): The parent endpoint, if applicable.

    Attributes:
        client (AcronisAPIClient): The AcronisAPIClient instance.
        endpoint_url (str): The base URL for the specific endpoint.
        _parent_endpoint (AcronisEndpoint): The parent endpoint, if applicable.
        model_parser (ModelParser): An instance of the ModelParser class used for parsing API responses.
        _model (Type[TModel]): The model class for the endpoint.
        _id (int): The ID of the current resource, if applicable.
        _child_endpoints (List[AcronisEndpoint]): A list of registered child endpoints.

    Generic Type:
        TModel: The model class for the endpoint.
    """

    def __init__(
        self,
        client: AcronisClient,
        endpoint_url: str,
        parent_endpoint: AcronisEndpoint | None = None,
    ) -> None:
        """
        Initialize a AcronisEndpoint instance with the client and endpoint base.

        Args:
            client: The AcronisAPIClient instance.
            endpoint_base (str): The base URL for the specific endpoint.
        """
        self.client = client
        self.endpoint_base = endpoint_url
        self._parent_endpoint = parent_endpoint
        self._id = None
        self._child_endpoints: list[AcronisEndpoint] = []

    def _register_child_endpoint(self, child_endpoint: TChildEndpoint) -> TChildEndpoint:
        """
        Register a child endpoint to the current endpoint.

        Args:
            child_endpoint (AcronisEndpoint): The child endpoint instance.

        Returns:
            AcronisEndpoint: The registered child endpoint.
        """
        self._child_endpoints.append(child_endpoint)
        return child_endpoint

    def _url_join(self, *args) -> str:  # noqa: ANN002
        """
        Join URL parts into a single URL string.

        Args:
            *args: The URL parts to join.

        Returns:
            str: The joined URL string.
        """
        url_parts = [str(arg).strip("/") for arg in args]
        return "/".join(url_parts)

    def _get_replaced_url(self) -> str:
        if self._id is None:
            return self.endpoint_base
        return self.endpoint_base.replace("{id}", str(self._id))

    def _make_request(
        self,
        method: RequestMethod,
        endpoint: AcronisEndpoint | None = None,
        data: RequestData | None = None,
        params: RequestParams | None = None,
        headers: dict[str, str] | None = None,
        stream: bool = False,  # noqa: FBT001, FBT002
    ) -> Response:
        """
        Make an API request using the specified method, endpoint, data, and parameters.
        This function isn't intended for use outside of this class.
        Please use the available CRUD methods as intended.

        Args:
            method (str): The HTTP method to use for the request (e.g., GET, POST, PUT, etc.).
            endpoint (str, optional): The endpoint to make the request to.
            data (dict, optional): The request data to send.
            params (dict, optional): The query parameters to include in the request.

        Returns:
            The Response object (see requests.Response).

        Raises:
            Exception: If the request returns a status code >= 400.
        """
        url = self._get_endpoint_url()
        if endpoint:
            url = self._url_join(url, endpoint)

        return self.client._make_request(method, url, data, params, headers, stream)

    def _build_url(self, other_endpoint: AcronisEndpoint) -> str:
        if other_endpoint._parent_endpoint is not None:
            parent_url = self._build_url(other_endpoint._parent_endpoint)
            if other_endpoint._parent_endpoint._id is not None:
                return self._url_join(
                    parent_url,
                    other_endpoint._get_replaced_url(),
                )
            else:  # noqa: RET505
                return self._url_join(parent_url, other_endpoint._get_replaced_url())
        else:
            return self._url_join(self.client._get_url(), other_endpoint._get_replaced_url())

    def _get_endpoint_url(self) -> str:
        return self._build_url(self)

    def _parse_many(self, model_type: type[TModel], data: list[dict[str, Any]]) -> list[TModel]:
        print(data)
        for d in data:
            print(model_type.model_validate(d))
        return [model_type.model_validate(d) for d in data]

    def _parse_one(self, model_type: type[TModel], data: dict[str, Any]) -> TModel:
        return model_type.model_validate(data)
