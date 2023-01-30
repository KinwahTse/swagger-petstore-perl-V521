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


class DfsRootfsesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_dfs_rootfs(self, body, **kwargs):  # noqa: E501
        """create_dfs_rootfs  # noqa: E501

        Create dfs rootfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dfs_rootfs(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param DfsRootfsCreateReq body: rootfs info (required)
        :return: DfsRootfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_dfs_rootfs_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_dfs_rootfs_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_dfs_rootfs_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_dfs_rootfs  # noqa: E501

        Create dfs rootfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dfs_rootfs_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param DfsRootfsCreateReq body: rootfs info (required)
        :return: DfsRootfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dfs_rootfs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_dfs_rootfs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/dfs-rootfses/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsRootfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dfs_rootfs(self, dfs_rootfs_id, **kwargs):  # noqa: E501
        """delete_dfs_rootfs  # noqa: E501

        delete dfs rootfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dfs_rootfs(dfs_rootfs_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_rootfs_id: rootfs id (required)
        :param bool force: force delete
        :return: DfsRootfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_dfs_rootfs_with_http_info(dfs_rootfs_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dfs_rootfs_with_http_info(dfs_rootfs_id, **kwargs)  # noqa: E501
            return data

    def delete_dfs_rootfs_with_http_info(self, dfs_rootfs_id, **kwargs):  # noqa: E501
        """delete_dfs_rootfs  # noqa: E501

        delete dfs rootfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dfs_rootfs_with_http_info(dfs_rootfs_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_rootfs_id: rootfs id (required)
        :param bool force: force delete
        :return: DfsRootfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_rootfs_id', 'force']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dfs_rootfs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_rootfs_id' is set
        if ('dfs_rootfs_id' not in params or
                params['dfs_rootfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_rootfs_id` when calling `delete_dfs_rootfs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_rootfs_id' in params:
            path_params['dfs_rootfs_id'] = params['dfs_rootfs_id']  # noqa: E501

        query_params = []
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

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
            '/dfs-rootfses/{dfs_rootfs_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsRootfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dfs_rootfs(self, dfs_rootfs_id, **kwargs):  # noqa: E501
        """get_dfs_rootfs  # noqa: E501

        Get dfs rootfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_rootfs(dfs_rootfs_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_rootfs_id: rootfs id (required)
        :return: DfsRootfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dfs_rootfs_with_http_info(dfs_rootfs_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dfs_rootfs_with_http_info(dfs_rootfs_id, **kwargs)  # noqa: E501
            return data

    def get_dfs_rootfs_with_http_info(self, dfs_rootfs_id, **kwargs):  # noqa: E501
        """get_dfs_rootfs  # noqa: E501

        Get dfs rootfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_rootfs_with_http_info(dfs_rootfs_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_rootfs_id: rootfs id (required)
        :return: DfsRootfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_rootfs_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dfs_rootfs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_rootfs_id' is set
        if ('dfs_rootfs_id' not in params or
                params['dfs_rootfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_rootfs_id` when calling `get_dfs_rootfs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_rootfs_id' in params:
            path_params['dfs_rootfs_id'] = params['dfs_rootfs_id']  # noqa: E501

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
            '/dfs-rootfses/{dfs_rootfs_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsRootfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dfs_rootfs_samples(self, dfs_rootfs_id, **kwargs):  # noqa: E501
        """get_dfs_rootfs_samples  # noqa: E501

        get a dfs rootfs's samples  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_rootfs_samples(dfs_rootfs_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_rootfs_id: dfs rootfs id (required)
        :param str duration_begin: duration begin timestamp
        :param str duration_end: duration end timestamp
        :param str period: samples period
        :return: DfsRootfsSamplesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dfs_rootfs_samples_with_http_info(dfs_rootfs_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dfs_rootfs_samples_with_http_info(dfs_rootfs_id, **kwargs)  # noqa: E501
            return data

    def get_dfs_rootfs_samples_with_http_info(self, dfs_rootfs_id, **kwargs):  # noqa: E501
        """get_dfs_rootfs_samples  # noqa: E501

        get a dfs rootfs's samples  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_rootfs_samples_with_http_info(dfs_rootfs_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_rootfs_id: dfs rootfs id (required)
        :param str duration_begin: duration begin timestamp
        :param str duration_end: duration end timestamp
        :param str period: samples period
        :return: DfsRootfsSamplesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_rootfs_id', 'duration_begin', 'duration_end', 'period']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dfs_rootfs_samples" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_rootfs_id' is set
        if ('dfs_rootfs_id' not in params or
                params['dfs_rootfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_rootfs_id` when calling `get_dfs_rootfs_samples`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_rootfs_id' in params:
            path_params['dfs_rootfs_id'] = params['dfs_rootfs_id']  # noqa: E501

        query_params = []
        if 'duration_begin' in params:
            query_params.append(('duration_begin', params['duration_begin']))  # noqa: E501
        if 'duration_end' in params:
            query_params.append(('duration_end', params['duration_end']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501

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
            '/dfs-rootfses/{dfs_rootfs_id}/samples', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsRootfsSamplesResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dfs_rootfses(self, **kwargs):  # noqa: E501
        """list_dfs_rootfses  # noqa: E501

        List dfs rootfses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dfs_rootfses(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :param str cluster_id: cluster id
        :param int pool_id: pool id
        :param int fs_user_id: fs user id
        :param int fs_user_group_id: fs user group id
        :param int fs_client_id: fs client id
        :param int fs_client_group_id: fs client group id
        :return: DfsRootfsesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_dfs_rootfses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_dfs_rootfses_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_dfs_rootfses_with_http_info(self, **kwargs):  # noqa: E501
        """list_dfs_rootfses  # noqa: E501

        List dfs rootfses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dfs_rootfses_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :param str cluster_id: cluster id
        :param int pool_id: pool id
        :param int fs_user_id: fs user id
        :param int fs_user_group_id: fs user group id
        :param int fs_client_id: fs client id
        :param int fs_client_group_id: fs client group id
        :return: DfsRootfsesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'q', 'sort', 'cluster_id', 'pool_id', 'fs_user_id', 'fs_user_group_id', 'fs_client_id', 'fs_client_group_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_dfs_rootfses" % key
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
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'cluster_id' in params:
            query_params.append(('cluster_id', params['cluster_id']))  # noqa: E501
        if 'pool_id' in params:
            query_params.append(('pool_id', params['pool_id']))  # noqa: E501
        if 'fs_user_id' in params:
            query_params.append(('fs_user_id', params['fs_user_id']))  # noqa: E501
        if 'fs_user_group_id' in params:
            query_params.append(('fs_user_group_id', params['fs_user_group_id']))  # noqa: E501
        if 'fs_client_id' in params:
            query_params.append(('fs_client_id', params['fs_client_id']))  # noqa: E501
        if 'fs_client_group_id' in params:
            query_params.append(('fs_client_group_id', params['fs_client_group_id']))  # noqa: E501

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
            '/dfs-rootfses/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsRootfsesResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_dfs_worm_log_path(self, dfs_rootfs_id, body, **kwargs):  # noqa: E501
        """set_dfs_worm_log_path  # noqa: E501

        Set dfs worm log path  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_dfs_worm_log_path(dfs_rootfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_rootfs_id: rootfs id (required)
        :param DfsRootfsSetWormLogPathReq body: worm log path (required)
        :param bool allow_path_create: allow create path when not existed
        :return: DfsRootfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_dfs_worm_log_path_with_http_info(dfs_rootfs_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.set_dfs_worm_log_path_with_http_info(dfs_rootfs_id, body, **kwargs)  # noqa: E501
            return data

    def set_dfs_worm_log_path_with_http_info(self, dfs_rootfs_id, body, **kwargs):  # noqa: E501
        """set_dfs_worm_log_path  # noqa: E501

        Set dfs worm log path  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_dfs_worm_log_path_with_http_info(dfs_rootfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_rootfs_id: rootfs id (required)
        :param DfsRootfsSetWormLogPathReq body: worm log path (required)
        :param bool allow_path_create: allow create path when not existed
        :return: DfsRootfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_rootfs_id', 'body', 'allow_path_create']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_dfs_worm_log_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_rootfs_id' is set
        if ('dfs_rootfs_id' not in params or
                params['dfs_rootfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_rootfs_id` when calling `set_dfs_worm_log_path`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_dfs_worm_log_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_rootfs_id' in params:
            path_params['dfs_rootfs_id'] = params['dfs_rootfs_id']  # noqa: E501

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
            '/dfs-rootfses/{dfs_rootfs_id}:set-worm-log-path', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsRootfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dfs_rootfs_active_pool(self, dfs_rootfs_id, body, **kwargs):  # noqa: E501
        """update_dfs_rootfs_active_pool  # noqa: E501

        Update dfs rootfs active pools  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dfs_rootfs_active_pool(dfs_rootfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_rootfs_id: rootfs id (required)
        :param DfsRootfsUpdateActivePoolReq body: active pool ids (required)
        :return: DfsRootfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_dfs_rootfs_active_pool_with_http_info(dfs_rootfs_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dfs_rootfs_active_pool_with_http_info(dfs_rootfs_id, body, **kwargs)  # noqa: E501
            return data

    def update_dfs_rootfs_active_pool_with_http_info(self, dfs_rootfs_id, body, **kwargs):  # noqa: E501
        """update_dfs_rootfs_active_pool  # noqa: E501

        Update dfs rootfs active pools  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dfs_rootfs_active_pool_with_http_info(dfs_rootfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_rootfs_id: rootfs id (required)
        :param DfsRootfsUpdateActivePoolReq body: active pool ids (required)
        :return: DfsRootfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_rootfs_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dfs_rootfs_active_pool" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_rootfs_id' is set
        if ('dfs_rootfs_id' not in params or
                params['dfs_rootfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_rootfs_id` when calling `update_dfs_rootfs_active_pool`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dfs_rootfs_active_pool`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_rootfs_id' in params:
            path_params['dfs_rootfs_id'] = params['dfs_rootfs_id']  # noqa: E501

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
            '/dfs-rootfses/{dfs_rootfs_id}:update-active-pools', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsRootfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
