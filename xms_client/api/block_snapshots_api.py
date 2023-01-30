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


class BlockSnapshotsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_block_snapshot(self, body, **kwargs):  # noqa: E501
        """create_block_snapshot  # noqa: E501

        Create block snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_block_snapshot(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param SnapshotCreateReq body: snapshot info (required)
        :return: SnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_block_snapshot_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_block_snapshot_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_block_snapshot_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_block_snapshot  # noqa: E501

        Create block snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_block_snapshot_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param SnapshotCreateReq body: snapshot info (required)
        :return: SnapshotResp
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
                    " to method create_block_snapshot" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_block_snapshot`")  # noqa: E501

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
            '/block-snapshots/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SnapshotResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_block_snapshot(self, snapshot_id, **kwargs):  # noqa: E501
        """delete_block_snapshot  # noqa: E501

        Delete block snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_block_snapshot(snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int snapshot_id: snapshot id (required)
        :return: SnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_block_snapshot_with_http_info(snapshot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_block_snapshot_with_http_info(snapshot_id, **kwargs)  # noqa: E501
            return data

    def delete_block_snapshot_with_http_info(self, snapshot_id, **kwargs):  # noqa: E501
        """delete_block_snapshot  # noqa: E501

        Delete block snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_block_snapshot_with_http_info(snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int snapshot_id: snapshot id (required)
        :return: SnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_block_snapshot" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'snapshot_id' is set
        if ('snapshot_id' not in params or
                params['snapshot_id'] is None):
            raise ValueError("Missing the required parameter `snapshot_id` when calling `delete_block_snapshot`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in params:
            path_params['snapshot_id'] = params['snapshot_id']  # noqa: E501

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
            '/block-snapshots/{snapshot_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SnapshotResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_block_snapshot(self, block_snapshot_id, **kwargs):  # noqa: E501
        """get_block_snapshot  # noqa: E501

        get block snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_block_snapshot(block_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int block_snapshot_id: the block snapshot id (required)
        :return: SnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_block_snapshot_with_http_info(block_snapshot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_block_snapshot_with_http_info(block_snapshot_id, **kwargs)  # noqa: E501
            return data

    def get_block_snapshot_with_http_info(self, block_snapshot_id, **kwargs):  # noqa: E501
        """get_block_snapshot  # noqa: E501

        get block snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_block_snapshot_with_http_info(block_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int block_snapshot_id: the block snapshot id (required)
        :return: SnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['block_snapshot_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_block_snapshot" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'block_snapshot_id' is set
        if ('block_snapshot_id' not in params or
                params['block_snapshot_id'] is None):
            raise ValueError("Missing the required parameter `block_snapshot_id` when calling `get_block_snapshot`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'block_snapshot_id' in params:
            path_params['block_snapshot_id'] = params['block_snapshot_id']  # noqa: E501

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
            '/block-snapshots/{block_snapshot_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SnapshotResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_block_snapshots(self, **kwargs):  # noqa: E501
        """list_block_snapshots  # noqa: E501

        List block snapshots  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_block_snapshots(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str cluster_id: cluster id
        :param int pool_id: pool id
        :param str uid: snapshot uid
        :param int block_volume_id: volume id
        :param int consistent_snapshot_id: consistent snapshot id
        :param bool reserved: show reserved snapshot or not, default not
        :param str q: query param of search
        :param str sort: sort param of search
        :param bool all: show all snapshots
        :return: SnapshotsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_block_snapshots_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_block_snapshots_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_block_snapshots_with_http_info(self, **kwargs):  # noqa: E501
        """list_block_snapshots  # noqa: E501

        List block snapshots  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_block_snapshots_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str cluster_id: cluster id
        :param int pool_id: pool id
        :param str uid: snapshot uid
        :param int block_volume_id: volume id
        :param int consistent_snapshot_id: consistent snapshot id
        :param bool reserved: show reserved snapshot or not, default not
        :param str q: query param of search
        :param str sort: sort param of search
        :param bool all: show all snapshots
        :return: SnapshotsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'cluster_id', 'pool_id', 'uid', 'block_volume_id', 'consistent_snapshot_id', 'reserved', 'q', 'sort', 'all']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_block_snapshots" % key
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
        if 'pool_id' in params:
            query_params.append(('pool_id', params['pool_id']))  # noqa: E501
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'block_volume_id' in params:
            query_params.append(('block_volume_id', params['block_volume_id']))  # noqa: E501
        if 'consistent_snapshot_id' in params:
            query_params.append(('consistent_snapshot_id', params['consistent_snapshot_id']))  # noqa: E501
        if 'reserved' in params:
            query_params.append(('reserved', params['reserved']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'all' in params:
            query_params.append(('all', params['all']))  # noqa: E501

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
            '/block-snapshots/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SnapshotsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_snapshot(self, snapshot_id, body, **kwargs):  # noqa: E501
        """update_snapshot  # noqa: E501

        Update block snapshot info  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_snapshot(snapshot_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int snapshot_id: snapshot id (required)
        :param SnapshotUpdateReq body: snapshot info (required)
        :return: SnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_snapshot_with_http_info(snapshot_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_snapshot_with_http_info(snapshot_id, body, **kwargs)  # noqa: E501
            return data

    def update_snapshot_with_http_info(self, snapshot_id, body, **kwargs):  # noqa: E501
        """update_snapshot  # noqa: E501

        Update block snapshot info  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_snapshot_with_http_info(snapshot_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int snapshot_id: snapshot id (required)
        :param SnapshotUpdateReq body: snapshot info (required)
        :return: SnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['snapshot_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_snapshot" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'snapshot_id' is set
        if ('snapshot_id' not in params or
                params['snapshot_id'] is None):
            raise ValueError("Missing the required parameter `snapshot_id` when calling `update_snapshot`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_snapshot`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'snapshot_id' in params:
            path_params['snapshot_id'] = params['snapshot_id']  # noqa: E501

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
            '/block-snapshots/{snapshot_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SnapshotResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
