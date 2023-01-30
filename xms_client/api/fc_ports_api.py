# coding: utf-8

"""
    XMS API

    XMS is the controller of distributed storage system  # noqa: E501

    OpenAPI spec version: XSCALEROS_5.2.100.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from xms_client.api_client import ApiClient


class FcPortsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def clear_fc_port_err_code(self, fc_port_id, **kwargs):  # noqa: E501
        """clear_fc_port_err_code  # noqa: E501

        Clear fc port errcode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.clear_fc_port_err_code(fc_port_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fc_port_id: fc port id (required)
        :return: FCPortResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.clear_fc_port_err_code_with_http_info(fc_port_id, **kwargs)  # noqa: E501
        else:
            (data) = self.clear_fc_port_err_code_with_http_info(fc_port_id, **kwargs)  # noqa: E501
            return data

    def clear_fc_port_err_code_with_http_info(self, fc_port_id, **kwargs):  # noqa: E501
        """clear_fc_port_err_code  # noqa: E501

        Clear fc port errcode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.clear_fc_port_err_code_with_http_info(fc_port_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fc_port_id: fc port id (required)
        :return: FCPortResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fc_port_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clear_fc_port_err_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fc_port_id' is set
        if ('fc_port_id' not in params or
                params['fc_port_id'] is None):
            raise ValueError("Missing the required parameter `fc_port_id` when calling `clear_fc_port_err_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fc_port_id' in params:
            path_params['fc_port_id'] = params['fc_port_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/fc-ports/{fc_port_id}:clear-err-code', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FCPortResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fc_port(self, fc_port_id, **kwargs):  # noqa: E501
        """get_fc_port  # noqa: E501

        Get fc port  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fc_port(fc_port_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fc_port_id: fc port id (required)
        :return: FCPortResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fc_port_with_http_info(fc_port_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fc_port_with_http_info(fc_port_id, **kwargs)  # noqa: E501
            return data

    def get_fc_port_with_http_info(self, fc_port_id, **kwargs):  # noqa: E501
        """get_fc_port  # noqa: E501

        Get fc port  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fc_port_with_http_info(fc_port_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fc_port_id: fc port id (required)
        :return: FCPortResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fc_port_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fc_port" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fc_port_id' is set
        if ('fc_port_id' not in params or
                params['fc_port_id'] is None):
            raise ValueError("Missing the required parameter `fc_port_id` when calling `get_fc_port`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fc_port_id' in params:
            path_params['fc_port_id'] = params['fc_port_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/fc-ports/{fc_port_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FCPortResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_fc_ports(self, **kwargs):  # noqa: E501
        """list_fc_ports  # noqa: E501

        List fc ports  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_fc_ports(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str cluster_id: cluster id
        :param str q: query param of search
        :param str sort: sort param of search
        :return: FCPortsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_fc_ports_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_fc_ports_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_fc_ports_with_http_info(self, **kwargs):  # noqa: E501
        """list_fc_ports  # noqa: E501

        List fc ports  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_fc_ports_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str cluster_id: cluster id
        :param str q: query param of search
        :param str sort: sort param of search
        :return: FCPortsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'cluster_id', 'q', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_fc_ports" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'cluster_id' in params:
            query_params.append(('cluster_id', params['cluster_id']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/fc-ports/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FCPortsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_fc_port(self, fc_port_id, **kwargs):  # noqa: E501
        """reset_fc_port  # noqa: E501

        Reset fc port  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_fc_port(fc_port_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fc_port_id: fc port id (required)
        :return: FCPortResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.reset_fc_port_with_http_info(fc_port_id, **kwargs)  # noqa: E501
        else:
            (data) = self.reset_fc_port_with_http_info(fc_port_id, **kwargs)  # noqa: E501
            return data

    def reset_fc_port_with_http_info(self, fc_port_id, **kwargs):  # noqa: E501
        """reset_fc_port  # noqa: E501

        Reset fc port  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_fc_port_with_http_info(fc_port_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fc_port_id: fc port id (required)
        :return: FCPortResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fc_port_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_fc_port" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fc_port_id' is set
        if ('fc_port_id' not in params or
                params['fc_port_id'] is None):
            raise ValueError("Missing the required parameter `fc_port_id` when calling `reset_fc_port`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fc_port_id' in params:
            path_params['fc_port_id'] = params['fc_port_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/fc-ports/{fc_port_id}:reset', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FCPortResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_fc_port(self, fc_port_id, **kwargs):  # noqa: E501
        """set_fc_port  # noqa: E501

        Set fc port  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_fc_port(fc_port_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fc_port_id: fc port id (required)
        :return: FCPortResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_fc_port_with_http_info(fc_port_id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_fc_port_with_http_info(fc_port_id, **kwargs)  # noqa: E501
            return data

    def set_fc_port_with_http_info(self, fc_port_id, **kwargs):  # noqa: E501
        """set_fc_port  # noqa: E501

        Set fc port  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_fc_port_with_http_info(fc_port_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fc_port_id: fc port id (required)
        :return: FCPortResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fc_port_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_fc_port" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fc_port_id' is set
        if ('fc_port_id' not in params or
                params['fc_port_id'] is None):
            raise ValueError("Missing the required parameter `fc_port_id` when calling `set_fc_port`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fc_port_id' in params:
            path_params['fc_port_id'] = params['fc_port_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/fc-ports/{fc_port_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FCPortResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
