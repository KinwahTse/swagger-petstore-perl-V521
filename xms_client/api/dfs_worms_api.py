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


class DfsWormsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_dfs_worm(self, body, **kwargs):  # noqa: E501
        """create_dfs_worm  # noqa: E501

        Create dfs worm  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dfs_worm(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param DfsWormCreateReq body: worm info (required)
        :param bool allow_path_create: allow create path when not existed
        :return: DfsWormResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_dfs_worm_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_dfs_worm_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_dfs_worm_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_dfs_worm  # noqa: E501

        Create dfs worm  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dfs_worm_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param DfsWormCreateReq body: worm info (required)
        :param bool allow_path_create: allow create path when not existed
        :return: DfsWormResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'allow_path_create']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dfs_worm" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_dfs_worm`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'allow_path_create' in params:
            query_params.append(('allow_path_create', params['allow_path_create']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/dfs-worms/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsWormResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dfs_worm(self, dfs_worm_id, **kwargs):  # noqa: E501
        """delete_dfs_worm  # noqa: E501

        delete dfs worm  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dfs_worm(dfs_worm_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_worm_id: worm id (required)
        :return: DfsWormResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_dfs_worm_with_http_info(dfs_worm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dfs_worm_with_http_info(dfs_worm_id, **kwargs)  # noqa: E501
            return data

    def delete_dfs_worm_with_http_info(self, dfs_worm_id, **kwargs):  # noqa: E501
        """delete_dfs_worm  # noqa: E501

        delete dfs worm  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dfs_worm_with_http_info(dfs_worm_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_worm_id: worm id (required)
        :return: DfsWormResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_worm_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dfs_worm" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_worm_id' is set
        if ('dfs_worm_id' not in params or
                params['dfs_worm_id'] is None):
            raise ValueError("Missing the required parameter `dfs_worm_id` when calling `delete_dfs_worm`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_worm_id' in params:
            path_params['dfs_worm_id'] = params['dfs_worm_id']  # noqa: E501

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
            '/dfs-worms/{dfs_worm_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsWormResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dfs_worm(self, dfs_worm_id, **kwargs):  # noqa: E501
        """get_dfs_worm  # noqa: E501

        get dfs worm  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_worm(dfs_worm_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_worm_id: the dfs worm id (required)
        :return: DfsWormResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dfs_worm_with_http_info(dfs_worm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dfs_worm_with_http_info(dfs_worm_id, **kwargs)  # noqa: E501
            return data

    def get_dfs_worm_with_http_info(self, dfs_worm_id, **kwargs):  # noqa: E501
        """get_dfs_worm  # noqa: E501

        get dfs worm  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_worm_with_http_info(dfs_worm_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_worm_id: the dfs worm id (required)
        :return: DfsWormResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_worm_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dfs_worm" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_worm_id' is set
        if ('dfs_worm_id' not in params or
                params['dfs_worm_id'] is None):
            raise ValueError("Missing the required parameter `dfs_worm_id` when calling `get_dfs_worm`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_worm_id' in params:
            path_params['dfs_worm_id'] = params['dfs_worm_id']  # noqa: E501

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
            '/dfs-worms/{dfs_worm_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsWormResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dfs_worms(self, **kwargs):  # noqa: E501
        """list_dfs_worms  # noqa: E501

        List dfs worms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dfs_worms(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :param int dfs_path_id: related dfs path id
        :param str path: related dfs path
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :return: DfsWormsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_dfs_worms_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_dfs_worms_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_dfs_worms_with_http_info(self, **kwargs):  # noqa: E501
        """list_dfs_worms  # noqa: E501

        List dfs worms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dfs_worms_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :param int dfs_path_id: related dfs path id
        :param str path: related dfs path
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :return: DfsWormsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id', 'dfs_path_id', 'path', 'limit', 'offset', 'q', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_dfs_worms" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in params:
            query_params.append(('cluster_id', params['cluster_id']))  # noqa: E501
        if 'dfs_path_id' in params:
            query_params.append(('dfs_path_id', params['dfs_path_id']))  # noqa: E501
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
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
            '/dfs-worms/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsWormsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dfs_worm(self, dfs_worm_id, body, **kwargs):  # noqa: E501
        """update_dfs_worm  # noqa: E501

        Update dfs worm  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dfs_worm(dfs_worm_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_worm_id: dfs worm id (required)
        :param DfsWormUpdateReq body: dfs worm info (required)
        :return: DfsWormResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_dfs_worm_with_http_info(dfs_worm_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dfs_worm_with_http_info(dfs_worm_id, body, **kwargs)  # noqa: E501
            return data

    def update_dfs_worm_with_http_info(self, dfs_worm_id, body, **kwargs):  # noqa: E501
        """update_dfs_worm  # noqa: E501

        Update dfs worm  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dfs_worm_with_http_info(dfs_worm_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_worm_id: dfs worm id (required)
        :param DfsWormUpdateReq body: dfs worm info (required)
        :return: DfsWormResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_worm_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dfs_worm" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_worm_id' is set
        if ('dfs_worm_id' not in params or
                params['dfs_worm_id'] is None):
            raise ValueError("Missing the required parameter `dfs_worm_id` when calling `update_dfs_worm`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dfs_worm`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_worm_id' in params:
            path_params['dfs_worm_id'] = params['dfs_worm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/dfs-worms/{dfs_worm_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsWormResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
