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


class VipsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_vip(self, vip, **kwargs):  # noqa: E501
        """create_vip  # noqa: E501

        Create a vip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_vip(vip, async=True)
        >>> result = thread.get()

        :param async bool
        :param VIPCreateReq vip: vip info (required)
        :return: VIPResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_vip_with_http_info(vip, **kwargs)  # noqa: E501
        else:
            (data) = self.create_vip_with_http_info(vip, **kwargs)  # noqa: E501
            return data

    def create_vip_with_http_info(self, vip, **kwargs):  # noqa: E501
        """create_vip  # noqa: E501

        Create a vip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_vip_with_http_info(vip, async=True)
        >>> result = thread.get()

        :param async bool
        :param VIPCreateReq vip: vip info (required)
        :return: VIPResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vip']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_vip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vip' is set
        if ('vip' not in params or
                params['vip'] is None):
            raise ValueError("Missing the required parameter `vip` when calling `create_vip`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'vip' in params:
            body_params = params['vip']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/vips/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VIPResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_vip(self, vip_id, **kwargs):  # noqa: E501
        """delete_vip  # noqa: E501

        Delete a vip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_vip(vip_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int vip_id: vip id (required)
        :return: VIPResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_vip_with_http_info(vip_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_vip_with_http_info(vip_id, **kwargs)  # noqa: E501
            return data

    def delete_vip_with_http_info(self, vip_id, **kwargs):  # noqa: E501
        """delete_vip  # noqa: E501

        Delete a vip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_vip_with_http_info(vip_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int vip_id: vip id (required)
        :return: VIPResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vip_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_vip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vip_id' is set
        if ('vip_id' not in params or
                params['vip_id'] is None):
            raise ValueError("Missing the required parameter `vip_id` when calling `delete_vip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vip_id' in params:
            path_params['vip_id'] = params['vip_id']  # noqa: E501

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
            '/vips/{vip_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VIPResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_vip(self, vip_id, **kwargs):  # noqa: E501
        """get_vip  # noqa: E501

        Get a vip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_vip(vip_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int vip_id: vip id (required)
        :return: VIPResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_vip_with_http_info(vip_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_vip_with_http_info(vip_id, **kwargs)  # noqa: E501
            return data

    def get_vip_with_http_info(self, vip_id, **kwargs):  # noqa: E501
        """get_vip  # noqa: E501

        Get a vip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_vip_with_http_info(vip_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int vip_id: vip id (required)
        :return: VIPResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vip_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vip_id' is set
        if ('vip_id' not in params or
                params['vip_id'] is None):
            raise ValueError("Missing the required parameter `vip_id` when calling `get_vip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vip_id' in params:
            path_params['vip_id'] = params['vip_id']  # noqa: E501

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
            '/vips/{vip_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VIPResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_vi_ps(self, **kwargs):  # noqa: E501
        """list_vi_ps  # noqa: E501

        List vips  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_vi_ps(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param int vip_group_id: vip_group id
        :return: VIPsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_vi_ps_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_vi_ps_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_vi_ps_with_http_info(self, **kwargs):  # noqa: E501
        """list_vi_ps  # noqa: E501

        List vips  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_vi_ps_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param int vip_group_id: vip_group id
        :return: VIPsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'vip_group_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_vi_ps" % key
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
        if 'vip_group_id' in params:
            query_params.append(('vip_group_id', params['vip_group_id']))  # noqa: E501

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
            '/vips/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VIPsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_vip(self, vip_id, **kwargs):  # noqa: E501
        """update_vip  # noqa: E501

        Update a vip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_vip(vip_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int vip_id: vip id (required)
        :return: VIPResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_vip_with_http_info(vip_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_vip_with_http_info(vip_id, **kwargs)  # noqa: E501
            return data

    def update_vip_with_http_info(self, vip_id, **kwargs):  # noqa: E501
        """update_vip  # noqa: E501

        Update a vip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_vip_with_http_info(vip_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int vip_id: vip id (required)
        :return: VIPResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vip_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_vip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vip_id' is set
        if ('vip_id' not in params or
                params['vip_id'] is None):
            raise ValueError("Missing the required parameter `vip_id` when calling `update_vip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vip_id' in params:
            path_params['vip_id'] = params['vip_id']  # noqa: E501

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
            '/vips/{vip_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VIPResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
