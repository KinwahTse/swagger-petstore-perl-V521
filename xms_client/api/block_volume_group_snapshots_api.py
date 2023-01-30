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


class BlockVolumeGroupSnapshotsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_block_volume_group_snapshot(self, body, **kwargs):  # noqa: E501
        """create_block_volume_group_snapshot  # noqa: E501

        Create block volume group snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_block_volume_group_snapshot(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param VolumeGroupSnapshotCreateReq body: volume group snapshot info (required)
        :param str cluster_id: cluster id
        :return: VolumeGroupSnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_block_volume_group_snapshot_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_block_volume_group_snapshot_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_block_volume_group_snapshot_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_block_volume_group_snapshot  # noqa: E501

        Create block volume group snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_block_volume_group_snapshot_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param VolumeGroupSnapshotCreateReq body: volume group snapshot info (required)
        :param str cluster_id: cluster id
        :return: VolumeGroupSnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'cluster_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_block_volume_group_snapshot" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_block_volume_group_snapshot`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in params:
            query_params.append(('cluster_id', params['cluster_id']))  # noqa: E501

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
            '/block-volume-group-snapshots/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VolumeGroupSnapshotResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_block_volume_group_snapshot(self, block_volume_group_snapshot_id, **kwargs):  # noqa: E501
        """delete_block_volume_group_snapshot  # noqa: E501

        Delete a block volume group snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_block_volume_group_snapshot(block_volume_group_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int block_volume_group_snapshot_id: block volume group snapshot id (required)
        :return: VolumeGroupSnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_block_volume_group_snapshot_with_http_info(block_volume_group_snapshot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_block_volume_group_snapshot_with_http_info(block_volume_group_snapshot_id, **kwargs)  # noqa: E501
            return data

    def delete_block_volume_group_snapshot_with_http_info(self, block_volume_group_snapshot_id, **kwargs):  # noqa: E501
        """delete_block_volume_group_snapshot  # noqa: E501

        Delete a block volume group snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_block_volume_group_snapshot_with_http_info(block_volume_group_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int block_volume_group_snapshot_id: block volume group snapshot id (required)
        :return: VolumeGroupSnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['block_volume_group_snapshot_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_block_volume_group_snapshot" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'block_volume_group_snapshot_id' is set
        if ('block_volume_group_snapshot_id' not in params or
                params['block_volume_group_snapshot_id'] is None):
            raise ValueError("Missing the required parameter `block_volume_group_snapshot_id` when calling `delete_block_volume_group_snapshot`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'block_volume_group_snapshot_id' in params:
            path_params['block_volume_group_snapshot_id'] = params['block_volume_group_snapshot_id']  # noqa: E501

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
            '/block-volume-group-snapshots/{block_volume_group_snapshot_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VolumeGroupSnapshotResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_block_volume_group_snapshot(self, block_volume_group_snapshot_id, **kwargs):  # noqa: E501
        """get_block_volume_group_snapshot  # noqa: E501

        get block volume group snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_block_volume_group_snapshot(block_volume_group_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int block_volume_group_snapshot_id: the block volume group snapshot id (required)
        :return: VolumeGroupSnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_block_volume_group_snapshot_with_http_info(block_volume_group_snapshot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_block_volume_group_snapshot_with_http_info(block_volume_group_snapshot_id, **kwargs)  # noqa: E501
            return data

    def get_block_volume_group_snapshot_with_http_info(self, block_volume_group_snapshot_id, **kwargs):  # noqa: E501
        """get_block_volume_group_snapshot  # noqa: E501

        get block volume group snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_block_volume_group_snapshot_with_http_info(block_volume_group_snapshot_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int block_volume_group_snapshot_id: the block volume group snapshot id (required)
        :return: VolumeGroupSnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['block_volume_group_snapshot_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_block_volume_group_snapshot" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'block_volume_group_snapshot_id' is set
        if ('block_volume_group_snapshot_id' not in params or
                params['block_volume_group_snapshot_id'] is None):
            raise ValueError("Missing the required parameter `block_volume_group_snapshot_id` when calling `get_block_volume_group_snapshot`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'block_volume_group_snapshot_id' in params:
            path_params['block_volume_group_snapshot_id'] = params['block_volume_group_snapshot_id']  # noqa: E501

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
            '/block-volume-group-snapshots/{block_volume_group_snapshot_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VolumeGroupSnapshotResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_block_volume_group_snapshots(self, **kwargs):  # noqa: E501
        """list_block_volume_group_snapshots  # noqa: E501

        List block volume group snapshots  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_block_volume_group_snapshots(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :param int block_volume_group_id: related volume group id
        :param str name: name of volume group snapshot
        :param bool passive: passive or not
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :return: VolumeGroupSnapshotsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_block_volume_group_snapshots_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_block_volume_group_snapshots_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_block_volume_group_snapshots_with_http_info(self, **kwargs):  # noqa: E501
        """list_block_volume_group_snapshots  # noqa: E501

        List block volume group snapshots  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_block_volume_group_snapshots_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :param int block_volume_group_id: related volume group id
        :param str name: name of volume group snapshot
        :param bool passive: passive or not
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :return: VolumeGroupSnapshotsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id', 'block_volume_group_id', 'name', 'passive', 'limit', 'offset', 'q', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_block_volume_group_snapshots" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in params:
            query_params.append(('cluster_id', params['cluster_id']))  # noqa: E501
        if 'block_volume_group_id' in params:
            query_params.append(('block_volume_group_id', params['block_volume_group_id']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'passive' in params:
            query_params.append(('passive', params['passive']))  # noqa: E501
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
            '/block-volume-group-snapshots/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VolumeGroupSnapshotsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_block_volume_group_snapshot(self, block_volume_group_snapshot_id, body, **kwargs):  # noqa: E501
        """update_block_volume_group_snapshot  # noqa: E501

        Update block volume group snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_block_volume_group_snapshot(block_volume_group_snapshot_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int block_volume_group_snapshot_id: the block volume group snapshot id (required)
        :param VolumeGroupSnapshotUpdateReq body: volume group snapshot info (required)
        :return: VolumeGroupSnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_block_volume_group_snapshot_with_http_info(block_volume_group_snapshot_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_block_volume_group_snapshot_with_http_info(block_volume_group_snapshot_id, body, **kwargs)  # noqa: E501
            return data

    def update_block_volume_group_snapshot_with_http_info(self, block_volume_group_snapshot_id, body, **kwargs):  # noqa: E501
        """update_block_volume_group_snapshot  # noqa: E501

        Update block volume group snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_block_volume_group_snapshot_with_http_info(block_volume_group_snapshot_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int block_volume_group_snapshot_id: the block volume group snapshot id (required)
        :param VolumeGroupSnapshotUpdateReq body: volume group snapshot info (required)
        :return: VolumeGroupSnapshotResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['block_volume_group_snapshot_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_block_volume_group_snapshot" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'block_volume_group_snapshot_id' is set
        if ('block_volume_group_snapshot_id' not in params or
                params['block_volume_group_snapshot_id'] is None):
            raise ValueError("Missing the required parameter `block_volume_group_snapshot_id` when calling `update_block_volume_group_snapshot`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_block_volume_group_snapshot`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'block_volume_group_snapshot_id' in params:
            path_params['block_volume_group_snapshot_id'] = params['block_volume_group_snapshot_id']  # noqa: E501

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
            '/block-volume-group-snapshots/{block_volume_group_snapshot_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VolumeGroupSnapshotResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
