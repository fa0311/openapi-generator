# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from petstore_api.models.client import Client

from petstore_api.api_client import ApiClient
from petstore_api.api_response import ApiResponse
from petstore_api.rest import RESTResponseType



class FakeClassnameTags123Api:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def test_classname(
        self,
        client: Annotated[Client, Field(description="client model")],
        _request_timeout: Annotated[Union[float, Tuple[float, float], None], Field(
            description="""timeout setting for this request. If one number
                           provided, it will be total request timeout. It can
                           also be a pair (tuple) of (connection, read)
                           timeouts.""",
        )] = None,
        _request_auth: Annotated[Optional[Dict[str, Any]], Field(
            description="""set to override the auth_settings for an a single
                           request; this effectively ignores the authentication
                           in the specfor a single request.""",
        )] = None,
        _content_type: Annotated[Optional[str], Field(
            description="""force content-type for the request""",
        )] = None,
        _headers: Annotated[Optional[Dict[str, Any]], Field(
            description="""set to override the header params for an a single
                           request; this effectively ignores the header params
                           in the spec fora single request.""",
        )] = None,
        _host_index: Annotated[int, Field(
            ge=0,
            le=0,
            description="""index of the host to use, if the server has multiple
                           hosts""",
        )] = 0,
    ) -> Client:
        """To test class name in snake case
        To test class name in snake case
        :param client: client model (required)
        :type client: Client
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        """

        _param = self._test_classname_serialize(
            client=client,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Client"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def test_classname_with_http_info(
        self,
        client: Annotated[Client, Field(description="client model")],
        _request_timeout: Annotated[Union[float, Tuple[float, float], None], Field(
            description="""timeout setting for this request. If one number
                           provided, it will be total request timeout. It can
                           also be a pair (tuple) of (connection, read)
                           timeouts.""",
        )] = None,
        _request_auth: Annotated[Optional[Dict[str, Any]], Field(
            description="""set to override the auth_settings for an a single
                           request; this effectively ignores the authentication
                           in the specfor a single request.""",
        )] = None,
        _content_type: Annotated[Optional[str], Field(
            description="""force content-type for the request""",
        )] = None,
        _headers: Annotated[Optional[Dict[str, Any]], Field(
            description="""set to override the header params for an a single
                           request; this effectively ignores the header params
                           in the spec fora single request.""",
        )] = None,
        _host_index: Annotated[int, Field(
            ge=0,
            le=0,
            description="""index of the host to use, if the server has multiple
                           hosts""",
        )] = 0,
    ) -> ApiResponse[Client]:
        """To test class name in snake case
        To test class name in snake case
        :param client: client model (required)
        :type client: Client
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        """

        _param = self._test_classname_serialize(
            client=client,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Client"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def test_classname_without_preload_content(
        self,
        client: Annotated[Client, Field(description="client model")],
        _request_timeout: Annotated[Union[float, Tuple[float, float], None], Field(
            description="""timeout setting for this request. If one number
                           provided, it will be total request timeout. It can
                           also be a pair (tuple) of (connection, read)
                           timeouts.""",
        )] = None,
        _request_auth: Annotated[Optional[Dict[str, Any]], Field(
            description="""set to override the auth_settings for an a single
                           request; this effectively ignores the authentication
                           in the specfor a single request.""",
        )] = None,
        _content_type: Annotated[Optional[str], Field(
            description="""force content-type for the request""",
        )] = None,
        _headers: Annotated[Optional[Dict[str, Any]], Field(
            description="""set to override the header params for an a single
                           request; this effectively ignores the header params
                           in the spec fora single request.""",
        )] = None,
        _host_index: Annotated[int, Field(
            ge=0,
            le=0,
            description="""index of the host to use, if the server has multiple
                           hosts""",
        )] = 0,
    ) -> RESTResponseType:
        """To test class name in snake case
        To test class name in snake case
        :param client: client model (required)
        :type client: Client
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        """

        _param = self._test_classname_serialize(
            client=client,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Client"
            
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response




    def _test_classname_serialize(
        self,
        client,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if client is not None:
            _body_params = client


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'api_key_query'
        ]

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/fake_classname_test',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


