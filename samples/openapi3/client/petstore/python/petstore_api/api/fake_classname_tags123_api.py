# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_call, ValidationError
from typing import Dict, List, Optional, Tuple

from pydantic import Field
from typing_extensions import Annotated
from petstore_api.models.client import Client

from petstore_api.api_client import ApiClient
from petstore_api.api_response import ApiResponse
from petstore_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


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
    def test_classname(
        self,
        client: Annotated[Client, Field(description="client model")],
        **kwargs,
    ) -> Client:
        """To test class name in snake case  # noqa: E501

        To test class name in snake case  # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param client: client model (required)
        :type client: Client
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Client
        """

        data = self.test_classname_with_http_info.raw_function(
            client,
            **kwargs,
        )
        return data.data

    @validate_call
    def test_classname_with_http_info(
        self,
        client: Annotated[Client, Field(description="client model")],
        **kwargs,
    ) -> ApiResponse[Client]:
        """To test class name in snake case  # noqa: E501

        To test class name in snake case  # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param client: client model (required)
        :type client: Client
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Client, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'client'
        ]
        _all_params.extend(
            [
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_classname" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        if _params['client'] is not None:
            _body_params = _params['client']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings: List[str] = ['api_key_query']  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Client",
        }

        param = self.api_client.param_serialize(
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
            
            _request_auth=_params.get('_request_auth')
        )

        response_data = self.api_client.call_api(*param, _request_timeout=_params.get('_request_timeout'))
        self.api_client.read(response_data)
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


