# coding: utf-8

"""
    Echo Server API

    Echo Server API

    The version of the OpenAPI document: 0.1.0
    Contact: team@openapitools.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import StrictBool, StrictInt, StrictStr

from typing import Optional


from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType

from multiprocessing.pool import ApplyResult


class FormApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def test_form_integer_boolean_string(
        self,
        integer_form: Optional[StrictInt] = None,
        boolean_form: Optional[StrictBool] = None,
        string_form: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> str:
        """Test form parameter(s)
        Test form parameter(s)
                This method makes a synchronous HTTP request by default.
        :param integer_form:
        :type integer_form: int
        :param boolean_form:
        :type boolean_form: bool
        :param string_form:
        :type string_form: str
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

        _param = self._test_form_integer_boolean_string_serialize(
            integer_form=integer_form,
            boolean_form=boolean_form,
            string_form=string_form,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def test_form_integer_boolean_string_with_http_info(
        self,
        integer_form: Optional[StrictInt] = None,
        boolean_form: Optional[StrictBool] = None,
        string_form: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[str]:
        """Test form parameter(s)
        Test form parameter(s)
                This method makes a synchronous HTTP request by default.
        :param integer_form:
        :type integer_form: int
        :param boolean_form:
        :type boolean_form: bool
        :param string_form:
        :type string_form: str
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

        _param = self._test_form_integer_boolean_string_serialize(
            integer_form=integer_form,
            boolean_form=boolean_form,
            string_form=string_form,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def test_form_integer_boolean_string_without_preload_content(
        self,
        integer_form: Optional[StrictInt] = None,
        boolean_form: Optional[StrictBool] = None,
        string_form: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Test form parameter(s)
        Test form parameter(s)
                This method makes a synchronous HTTP request by default.
        :param integer_form:
        :type integer_form: int
        :param boolean_form:
        :type boolean_form: bool
        :param string_form:
        :type string_form: str
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

        _param = self._test_form_integer_boolean_string_serialize(
            integer_form=integer_form,
            boolean_form=boolean_form,
            string_form=string_form,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    @validate_call
    def test_form_integer_boolean_string_with_async(
        self,
        integer_form: Optional[StrictInt] = None,
        boolean_form: Optional[StrictBool] = None,
        string_form: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApplyResult:
        """Test form parameter(s)
        Test form parameter(s)
                This method makes a synchronous HTTP request by default.
        :param integer_form:
        :type integer_form: int
        :param boolean_form:
        :type boolean_form: bool
        :param string_form:
        :type string_form: str
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

        _param = self._test_form_integer_boolean_string_serialize(
            integer_form=integer_form,
            boolean_form=boolean_form,
            string_form=string_form,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str"
            
        }
        def callback(*args):
            response_data = self.api_client.call_api(*args)
            response_data.read()
            return self.api_client.response_deserialize(
                response_data=response_data,
                response_types_map=_response_types_map,
            ).data
        return self.api_client.pool.apply_async(
            callback,
            _param + (_request_timeout,)
        )


    @validate_call
    def test_form_integer_boolean_string_with_http_info_async(
        self,
        integer_form: Optional[StrictInt] = None,
        boolean_form: Optional[StrictBool] = None,
        string_form: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApplyResult:
        """Test form parameter(s)
        Test form parameter(s)
                This method makes a synchronous HTTP request by default.
        :param integer_form:
        :type integer_form: int
        :param boolean_form:
        :type boolean_form: bool
        :param string_form:
        :type string_form: str
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

        _param = self._test_form_integer_boolean_string_serialize(
            integer_form=integer_form,
            boolean_form=boolean_form,
            string_form=string_form,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str"
            
        }
        def callback(*args):
            response_data = self.api_client.call_api(*args)
            response_data.read()
            return self.api_client.response_deserialize(
                response_data=response_data,
                response_types_map=_response_types_map,
            )
        return self.api_client.pool.apply_async(
            callback,
            _param + (_request_timeout,)
        )


    def _test_form_integer_boolean_string_serialize(
        self,
        integer_form,
        boolean_form,
        string_form,
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
        if integer_form is not None:
            _form_params.append(('integer_form', integer_form))
        if boolean_form is not None:
            _form_params.append(('boolean_form', boolean_form))
        if string_form is not None:
            _form_params.append(('string_form', string_form))
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'text/plain'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/x-www-form-urlencoded'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/form/integer/boolean/string',
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




    @validate_call
    def test_form_oneof(
        self,
        form1: Optional[StrictStr] = None,
        form2: Optional[StrictInt] = None,
        form3: Optional[StrictStr] = None,
        form4: Optional[StrictBool] = None,
        id: Optional[StrictInt] = None,
        name: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> str:
        """Test form parameter(s) for oneOf schema
        Test form parameter(s) for oneOf schema
                This method makes a synchronous HTTP request by default.
        :param form1:
        :type form1: str
        :param form2:
        :type form2: int
        :param form3:
        :type form3: str
        :param form4:
        :type form4: bool
        :param id:
        :type id: int
        :param name:
        :type name: str
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

        _param = self._test_form_oneof_serialize(
            form1=form1,
            form2=form2,
            form3=form3,
            form4=form4,
            id=id,
            name=name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def test_form_oneof_with_http_info(
        self,
        form1: Optional[StrictStr] = None,
        form2: Optional[StrictInt] = None,
        form3: Optional[StrictStr] = None,
        form4: Optional[StrictBool] = None,
        id: Optional[StrictInt] = None,
        name: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[str]:
        """Test form parameter(s) for oneOf schema
        Test form parameter(s) for oneOf schema
                This method makes a synchronous HTTP request by default.
        :param form1:
        :type form1: str
        :param form2:
        :type form2: int
        :param form3:
        :type form3: str
        :param form4:
        :type form4: bool
        :param id:
        :type id: int
        :param name:
        :type name: str
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

        _param = self._test_form_oneof_serialize(
            form1=form1,
            form2=form2,
            form3=form3,
            form4=form4,
            id=id,
            name=name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def test_form_oneof_without_preload_content(
        self,
        form1: Optional[StrictStr] = None,
        form2: Optional[StrictInt] = None,
        form3: Optional[StrictStr] = None,
        form4: Optional[StrictBool] = None,
        id: Optional[StrictInt] = None,
        name: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Test form parameter(s) for oneOf schema
        Test form parameter(s) for oneOf schema
                This method makes a synchronous HTTP request by default.
        :param form1:
        :type form1: str
        :param form2:
        :type form2: int
        :param form3:
        :type form3: str
        :param form4:
        :type form4: bool
        :param id:
        :type id: int
        :param name:
        :type name: str
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

        _param = self._test_form_oneof_serialize(
            form1=form1,
            form2=form2,
            form3=form3,
            form4=form4,
            id=id,
            name=name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    @validate_call
    def test_form_oneof_with_async(
        self,
        form1: Optional[StrictStr] = None,
        form2: Optional[StrictInt] = None,
        form3: Optional[StrictStr] = None,
        form4: Optional[StrictBool] = None,
        id: Optional[StrictInt] = None,
        name: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApplyResult:
        """Test form parameter(s) for oneOf schema
        Test form parameter(s) for oneOf schema
                This method makes a synchronous HTTP request by default.
        :param form1:
        :type form1: str
        :param form2:
        :type form2: int
        :param form3:
        :type form3: str
        :param form4:
        :type form4: bool
        :param id:
        :type id: int
        :param name:
        :type name: str
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

        _param = self._test_form_oneof_serialize(
            form1=form1,
            form2=form2,
            form3=form3,
            form4=form4,
            id=id,
            name=name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str"
            
        }
        def callback(*args):
            response_data = self.api_client.call_api(*args)
            response_data.read()
            return self.api_client.response_deserialize(
                response_data=response_data,
                response_types_map=_response_types_map,
            ).data
        return self.api_client.pool.apply_async(
            callback,
            _param + (_request_timeout,)
        )


    @validate_call
    def test_form_oneof_with_http_info_async(
        self,
        form1: Optional[StrictStr] = None,
        form2: Optional[StrictInt] = None,
        form3: Optional[StrictStr] = None,
        form4: Optional[StrictBool] = None,
        id: Optional[StrictInt] = None,
        name: Optional[StrictStr] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApplyResult:
        """Test form parameter(s) for oneOf schema
        Test form parameter(s) for oneOf schema
                This method makes a synchronous HTTP request by default.
        :param form1:
        :type form1: str
        :param form2:
        :type form2: int
        :param form3:
        :type form3: str
        :param form4:
        :type form4: bool
        :param id:
        :type id: int
        :param name:
        :type name: str
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

        _param = self._test_form_oneof_serialize(
            form1=form1,
            form2=form2,
            form3=form3,
            form4=form4,
            id=id,
            name=name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str"
            
        }
        def callback(*args):
            response_data = self.api_client.call_api(*args)
            response_data.read()
            return self.api_client.response_deserialize(
                response_data=response_data,
                response_types_map=_response_types_map,
            )
        return self.api_client.pool.apply_async(
            callback,
            _param + (_request_timeout,)
        )


    def _test_form_oneof_serialize(
        self,
        form1,
        form2,
        form3,
        form4,
        id,
        name,
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
        if form1 is not None:
            _form_params.append(('form1', form1))
        if form2 is not None:
            _form_params.append(('form2', form2))
        if form3 is not None:
            _form_params.append(('form3', form3))
        if form4 is not None:
            _form_params.append(('form4', form4))
        if id is not None:
            _form_params.append(('id', id))
        if name is not None:
            _form_params.append(('name', name))
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'text/plain'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/x-www-form-urlencoded'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/form/oneof',
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


