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
from pydantic import StrictStr

from typing import List

from petstore_api.models.user import User

from petstore_api.api_client import ApiClient
from petstore_api.api_response import ApiResponse
from petstore_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UserApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def create_user(
        self,
        user: Annotated[User, Field(description="Created user object")],
        **kwargs,
    ) -> None:
        """Create user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param user: Created user object (required)
        :type user: User
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        data = self.create_user_with_http_info.raw_function(
            user,
            **kwargs,
        )
        return data.data

    @validate_call
    def create_user_with_http_info(
        self,
        user: Annotated[User, Field(description="Created user object")],
        **kwargs,
    ) -> ApiResponse[None]:
        """Create user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param user: Created user object (required)
        :type user: User
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
        :rtype: None
        """

        _hosts = [
            'http://petstore.swagger.io/v2',
            'http://path-server-test.petstore.local/v2',
            'http://{server}.swagger.io:{port}/v2'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'user'
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
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % _key
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
        if _params['user'] is not None:
            _body_params = _params['user']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {}

        return self.api_client.call_api(
            '/user', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    def create_users_with_array_input(
        self,
        user: Annotated[List[User], Field(description="List of user object")],
        **kwargs,
    ) -> None:
        """Creates list of users with given input array  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param user: List of user object (required)
        :type user: List[User]
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        data = self.create_users_with_array_input_with_http_info.raw_function(
            user,
            **kwargs,
        )
        return data.data

    @validate_call
    def create_users_with_array_input_with_http_info(
        self,
        user: Annotated[List[User], Field(description="List of user object")],
        **kwargs,
    ) -> ApiResponse[None]:
        """Creates list of users with given input array  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param user: List of user object (required)
        :type user: List[User]
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'user'
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
                    " to method create_users_with_array_input" % _key
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
        if _params['user'] is not None:
            _body_params = _params['user']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {}

        return self.api_client.call_api(
            '/user/createWithArray', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    def create_users_with_list_input(
        self,
        user: Annotated[List[User], Field(description="List of user object")],
        **kwargs,
    ) -> None:
        """Creates list of users with given input array  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param user: List of user object (required)
        :type user: List[User]
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        data = self.create_users_with_list_input_with_http_info.raw_function(
            user,
            **kwargs,
        )
        return data.data

    @validate_call
    def create_users_with_list_input_with_http_info(
        self,
        user: Annotated[List[User], Field(description="List of user object")],
        **kwargs,
    ) -> ApiResponse[None]:
        """Creates list of users with given input array  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param user: List of user object (required)
        :type user: List[User]
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'user'
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
                    " to method create_users_with_list_input" % _key
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
        if _params['user'] is not None:
            _body_params = _params['user']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {}

        return self.api_client.call_api(
            '/user/createWithList', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    def delete_user(
        self,
        username: Annotated[StrictStr, Field(description="The name that needs to be deleted")],
        **kwargs,
    ) -> None:
        """Delete user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param username: The name that needs to be deleted (required)
        :type username: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        data = self.delete_user_with_http_info.raw_function(
            username,
            **kwargs,
        )
        return data.data

    @validate_call
    def delete_user_with_http_info(
        self,
        username: Annotated[StrictStr, Field(description="The name that needs to be deleted")],
        **kwargs,
    ) -> ApiResponse[None]:
        """Delete user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param username: The name that needs to be deleted (required)
        :type username: str
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'username'
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
                    " to method delete_user" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['username'] is not None:
            _path_params['username'] = _params['username']


        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {}

        return self.api_client.call_api(
            '/user/{username}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    def get_user_by_name(
        self,
        username: Annotated[StrictStr, Field(description="The name that needs to be fetched. Use user1 for testing.")],
        **kwargs,
    ) -> User:
        """Get user by user name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param username: The name that needs to be fetched. Use user1 for testing. (required)
        :type username: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: User
        """

        data = self.get_user_by_name_with_http_info.raw_function(
            username,
            **kwargs,
        )
        return data.data

    @validate_call
    def get_user_by_name_with_http_info(
        self,
        username: Annotated[StrictStr, Field(description="The name that needs to be fetched. Use user1 for testing.")],
        **kwargs,
    ) -> ApiResponse[User]:
        """Get user by user name  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param username: The name that needs to be fetched. Use user1 for testing. (required)
        :type username: str
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
        :rtype: tuple(User, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'username'
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
                    " to method get_user_by_name" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['username'] is not None:
            _path_params['username'] = _params['username']


        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "User",
            '400': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/user/{username}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    def login_user(
        self,
        username: Annotated[StrictStr, Field(description="The user name for login")],
        password: Annotated[StrictStr, Field(description="The password for login in clear text")],
        **kwargs,
    ) -> str:
        """Logs user into the system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param username: The user name for login (required)
        :type username: str
        :param password: The password for login in clear text (required)
        :type password: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: str
        """

        data = self.login_user_with_http_info.raw_function(
            username,
            password,
            **kwargs,
        )
        return data.data

    @validate_call
    def login_user_with_http_info(
        self,
        username: Annotated[StrictStr, Field(description="The user name for login")],
        password: Annotated[StrictStr, Field(description="The password for login in clear text")],
        **kwargs,
    ) -> ApiResponse[str]:
        """Logs user into the system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param username: The user name for login (required)
        :type username: str
        :param password: The password for login in clear text (required)
        :type password: str
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
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'username',
            'password'
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
                    " to method login_user" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get('username') is not None:  # noqa: E501
            _query_params.append(('username', _params['username']))

        if _params.get('password') is not None:  # noqa: E501
            _query_params.append(('password', _params['password']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str",
            '400': None,
        }

        return self.api_client.call_api(
            '/user/login', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    def logout_user(
        self,
        **kwargs,
    ) -> None:
        """Logs out current logged in user session  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        data = self.logout_user_with_http_info.raw_function(
            **kwargs,
        )
        return data.data

    @validate_call
    def logout_user_with_http_info(
        self,
        **kwargs,
    ) -> ApiResponse[None]:
        """Logs out current logged in user session  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default.

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
        :rtype: None
        """

        _params = locals()

        _all_params = [
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
                    " to method logout_user" % _key
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
        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {}

        return self.api_client.call_api(
            '/user/logout', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    def update_user(
        self,
        username: Annotated[StrictStr, Field(description="name that need to be deleted")],
        user: Annotated[User, Field(description="Updated user object")],
        **kwargs,
    ) -> None:
        """Updated user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param username: name that need to be deleted (required)
        :type username: str
        :param user: Updated user object (required)
        :type user: User
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        data = self.update_user_with_http_info.raw_function(
            username,
            user,
            **kwargs,
        )
        return data.data

    @validate_call
    def update_user_with_http_info(
        self,
        username: Annotated[StrictStr, Field(description="name that need to be deleted")],
        user: Annotated[User, Field(description="Updated user object")],
        **kwargs,
    ) -> ApiResponse[None]:
        """Updated user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default.

        :param username: name that need to be deleted (required)
        :type username: str
        :param user: Updated user object (required)
        :type user: User
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'username',
            'user'
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
                    " to method update_user" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['username'] is not None:
            _path_params['username'] = _params['username']


        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        if _params['user'] is not None:
            _body_params = _params['user']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {}

        return self.api_client.call_api(
            '/user/{username}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
