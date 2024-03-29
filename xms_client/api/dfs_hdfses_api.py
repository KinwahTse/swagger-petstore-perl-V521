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


class DfsHdfsesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_dfs_hdfs_ac_ls(self, dfs_hdfs_id, body, **kwargs):  # noqa: E501
        """add_dfs_hdfs_ac_ls  # noqa: E501

        add dfs hdfs acls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_dfs_hdfs_ac_ls(dfs_hdfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: hdfs id (required)
        :param DfsHdfsAddACLsReq body: dfs hdfs info (required)
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_dfs_hdfs_ac_ls_with_http_info(dfs_hdfs_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_dfs_hdfs_ac_ls_with_http_info(dfs_hdfs_id, body, **kwargs)  # noqa: E501
            return data

    def add_dfs_hdfs_ac_ls_with_http_info(self, dfs_hdfs_id, body, **kwargs):  # noqa: E501
        """add_dfs_hdfs_ac_ls  # noqa: E501

        add dfs hdfs acls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_dfs_hdfs_ac_ls_with_http_info(dfs_hdfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: hdfs id (required)
        :param DfsHdfsAddACLsReq body: dfs hdfs info (required)
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_hdfs_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_dfs_hdfs_ac_ls" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_hdfs_id' is set
        if ('dfs_hdfs_id' not in params or
                params['dfs_hdfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_hdfs_id` when calling `add_dfs_hdfs_ac_ls`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_dfs_hdfs_ac_ls`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_hdfs_id' in params:
            path_params['dfs_hdfs_id'] = params['dfs_hdfs_id']  # noqa: E501

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
            '/dfs-hdfses/{dfs_hdfs_id}:add-acls', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsHdfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_dfs_hdfs(self, body, **kwargs):  # noqa: E501
        """create_dfs_hdfs  # noqa: E501

        Create dfs hdfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dfs_hdfs(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param DfsHdfsCreateReq body: hdfs info (required)
        :param bool allow_path_create: allow create path when not existed
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_dfs_hdfs_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_dfs_hdfs_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_dfs_hdfs_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_dfs_hdfs  # noqa: E501

        Create dfs hdfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dfs_hdfs_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param DfsHdfsCreateReq body: hdfs info (required)
        :param bool allow_path_create: allow create path when not existed
        :return: DfsHdfsResp
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
                    " to method create_dfs_hdfs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_dfs_hdfs`")  # noqa: E501

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
            '/dfs-hdfses/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsHdfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dfs_hdfs(self, dfs_hdfs_id, **kwargs):  # noqa: E501
        """delete_dfs_hdfs  # noqa: E501

        delete dfs hdfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dfs_hdfs(dfs_hdfs_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: dfs hdfs id (required)
        :param bool force: force delete or not
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_dfs_hdfs_with_http_info(dfs_hdfs_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dfs_hdfs_with_http_info(dfs_hdfs_id, **kwargs)  # noqa: E501
            return data

    def delete_dfs_hdfs_with_http_info(self, dfs_hdfs_id, **kwargs):  # noqa: E501
        """delete_dfs_hdfs  # noqa: E501

        delete dfs hdfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dfs_hdfs_with_http_info(dfs_hdfs_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: dfs hdfs id (required)
        :param bool force: force delete or not
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_hdfs_id', 'force']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dfs_hdfs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_hdfs_id' is set
        if ('dfs_hdfs_id' not in params or
                params['dfs_hdfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_hdfs_id` when calling `delete_dfs_hdfs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_hdfs_id' in params:
            path_params['dfs_hdfs_id'] = params['dfs_hdfs_id']  # noqa: E501

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
            '/dfs-hdfses/{dfs_hdfs_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsHdfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dfs_hdfs(self, dfs_hdfs_id, **kwargs):  # noqa: E501
        """get_dfs_hdfs  # noqa: E501

        Get dfs hdfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_hdfs(dfs_hdfs_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: dfs hdfs id (required)
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dfs_hdfs_with_http_info(dfs_hdfs_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dfs_hdfs_with_http_info(dfs_hdfs_id, **kwargs)  # noqa: E501
            return data

    def get_dfs_hdfs_with_http_info(self, dfs_hdfs_id, **kwargs):  # noqa: E501
        """get_dfs_hdfs  # noqa: E501

        Get dfs hdfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_hdfs_with_http_info(dfs_hdfs_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: dfs hdfs id (required)
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_hdfs_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dfs_hdfs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_hdfs_id' is set
        if ('dfs_hdfs_id' not in params or
                params['dfs_hdfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_hdfs_id` when calling `get_dfs_hdfs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_hdfs_id' in params:
            path_params['dfs_hdfs_id'] = params['dfs_hdfs_id']  # noqa: E501

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
            '/dfs-hdfses/{dfs_hdfs_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsHdfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dfs_hdfses(self, **kwargs):  # noqa: E501
        """list_dfs_hdfses  # noqa: E501

        List dfs hdfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dfs_hdfses(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str cluster_id: cluster id
        :param str path: related dfs path
        :param int dfs_gateway_zone_id: dfs gateway zone id
        :param str q: query param of search
        :param str sort: sort param of search
        :return: DfsHdfsesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_dfs_hdfses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_dfs_hdfses_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_dfs_hdfses_with_http_info(self, **kwargs):  # noqa: E501
        """list_dfs_hdfses  # noqa: E501

        List dfs hdfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dfs_hdfses_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str cluster_id: cluster id
        :param str path: related dfs path
        :param int dfs_gateway_zone_id: dfs gateway zone id
        :param str q: query param of search
        :param str sort: sort param of search
        :return: DfsHdfsesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'cluster_id', 'path', 'dfs_gateway_zone_id', 'q', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_dfs_hdfses" % key
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
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501
        if 'dfs_gateway_zone_id' in params:
            query_params.append(('dfs_gateway_zone_id', params['dfs_gateway_zone_id']))  # noqa: E501
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
            '/dfs-hdfses/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsHdfsesResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_dfs_hdfs_ac_ls(self, dfs_hdfs_id, body, **kwargs):  # noqa: E501
        """remove_dfs_hdfs_ac_ls  # noqa: E501

        remove dfs hdfs acls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_dfs_hdfs_ac_ls(dfs_hdfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: dfs hdfs id (required)
        :param DfsHdfsRemoveACLsReq body: hdfs acls info (required)
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_dfs_hdfs_ac_ls_with_http_info(dfs_hdfs_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_dfs_hdfs_ac_ls_with_http_info(dfs_hdfs_id, body, **kwargs)  # noqa: E501
            return data

    def remove_dfs_hdfs_ac_ls_with_http_info(self, dfs_hdfs_id, body, **kwargs):  # noqa: E501
        """remove_dfs_hdfs_ac_ls  # noqa: E501

        remove dfs hdfs acls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_dfs_hdfs_ac_ls_with_http_info(dfs_hdfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: dfs hdfs id (required)
        :param DfsHdfsRemoveACLsReq body: hdfs acls info (required)
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_hdfs_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_dfs_hdfs_ac_ls" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_hdfs_id' is set
        if ('dfs_hdfs_id' not in params or
                params['dfs_hdfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_hdfs_id` when calling `remove_dfs_hdfs_ac_ls`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `remove_dfs_hdfs_ac_ls`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_hdfs_id' in params:
            path_params['dfs_hdfs_id'] = params['dfs_hdfs_id']  # noqa: E501

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
            '/dfs-hdfses/{dfs_hdfs_id}:remove-acls', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsHdfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dfs_hdfs(self, dfs_hdfs_id, body, **kwargs):  # noqa: E501
        """update_dfs_hdfs  # noqa: E501

        Update dfs hdfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dfs_hdfs(dfs_hdfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: hdfs id (required)
        :param DfsHdfsUpdateReq body: dfs hdfs info (required)
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_dfs_hdfs_with_http_info(dfs_hdfs_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dfs_hdfs_with_http_info(dfs_hdfs_id, body, **kwargs)  # noqa: E501
            return data

    def update_dfs_hdfs_with_http_info(self, dfs_hdfs_id, body, **kwargs):  # noqa: E501
        """update_dfs_hdfs  # noqa: E501

        Update dfs hdfs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dfs_hdfs_with_http_info(dfs_hdfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: hdfs id (required)
        :param DfsHdfsUpdateReq body: dfs hdfs info (required)
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_hdfs_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dfs_hdfs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_hdfs_id' is set
        if ('dfs_hdfs_id' not in params or
                params['dfs_hdfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_hdfs_id` when calling `update_dfs_hdfs`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dfs_hdfs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_hdfs_id' in params:
            path_params['dfs_hdfs_id'] = params['dfs_hdfs_id']  # noqa: E501

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
            '/dfs-hdfses/{dfs_hdfs_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsHdfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dfs_hdfs_ac_ls(self, dfs_hdfs_id, body, **kwargs):  # noqa: E501
        """update_dfs_hdfs_ac_ls  # noqa: E501

        Update dfs hdfs ACL  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dfs_hdfs_ac_ls(dfs_hdfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: hdfs id (required)
        :param DfsHdfsUpdateACLsReq body: hdfs acls info (required)
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_dfs_hdfs_ac_ls_with_http_info(dfs_hdfs_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dfs_hdfs_ac_ls_with_http_info(dfs_hdfs_id, body, **kwargs)  # noqa: E501
            return data

    def update_dfs_hdfs_ac_ls_with_http_info(self, dfs_hdfs_id, body, **kwargs):  # noqa: E501
        """update_dfs_hdfs_ac_ls  # noqa: E501

        Update dfs hdfs ACL  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dfs_hdfs_ac_ls_with_http_info(dfs_hdfs_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_hdfs_id: hdfs id (required)
        :param DfsHdfsUpdateACLsReq body: hdfs acls info (required)
        :return: DfsHdfsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_hdfs_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dfs_hdfs_ac_ls" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_hdfs_id' is set
        if ('dfs_hdfs_id' not in params or
                params['dfs_hdfs_id'] is None):
            raise ValueError("Missing the required parameter `dfs_hdfs_id` when calling `update_dfs_hdfs_ac_ls`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dfs_hdfs_ac_ls`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_hdfs_id' in params:
            path_params['dfs_hdfs_id'] = params['dfs_hdfs_id']  # noqa: E501

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
            '/dfs-hdfses/{dfs_hdfs_id}:update-acls', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsHdfsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
