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


class DpVolumeGroupSnapshotReplicationPoliciesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_dp_volume_group_snapshot_replication_policy(self, body, **kwargs):  # noqa: E501
        """create_dp_volume_group_snapshot_replication_policy  # noqa: E501

        Create dp volume group snapshot replication policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dp_volume_group_snapshot_replication_policy(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param DpVolumeGroupSnapshotReplicationPolicyCreateReq body: policy info (required)
        :return: DpVolumeGroupSnapshotReplicationPolicyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_dp_volume_group_snapshot_replication_policy_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_dp_volume_group_snapshot_replication_policy_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_dp_volume_group_snapshot_replication_policy_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_dp_volume_group_snapshot_replication_policy  # noqa: E501

        Create dp volume group snapshot replication policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dp_volume_group_snapshot_replication_policy_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param DpVolumeGroupSnapshotReplicationPolicyCreateReq body: policy info (required)
        :return: DpVolumeGroupSnapshotReplicationPolicyResp
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
                    " to method create_dp_volume_group_snapshot_replication_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_dp_volume_group_snapshot_replication_policy`")  # noqa: E501

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
            '/dp-volume-group-snapshot-replication-policies/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DpVolumeGroupSnapshotReplicationPolicyResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dp_volume_group_snapshot_replication_policy(self, policy_id, **kwargs):  # noqa: E501
        """delete_dp_volume_group_snapshot_replication_policy  # noqa: E501

        Delete dp volume group snapshot replication policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dp_volume_group_snapshot_replication_policy(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int policy_id: resource id (required)
        :param bool force: force delete or not
        :return: DpVolumeGroupSnapshotReplicationPolicyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_dp_volume_group_snapshot_replication_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dp_volume_group_snapshot_replication_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def delete_dp_volume_group_snapshot_replication_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """delete_dp_volume_group_snapshot_replication_policy  # noqa: E501

        Delete dp volume group snapshot replication policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dp_volume_group_snapshot_replication_policy_with_http_info(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int policy_id: resource id (required)
        :param bool force: force delete or not
        :return: DpVolumeGroupSnapshotReplicationPolicyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'force']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dp_volume_group_snapshot_replication_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `delete_dp_volume_group_snapshot_replication_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']  # noqa: E501

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
            '/dp-volume-group-snapshot-replication-policies/{policy_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DpVolumeGroupSnapshotReplicationPolicyResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dp_volume_group_snapshot_replication_policy(self, policy_id, **kwargs):  # noqa: E501
        """get_dp_volume_group_snapshot_replication_policy  # noqa: E501

        Get dp volume group snapshot replication policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dp_volume_group_snapshot_replication_policy(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int policy_id: resource id (required)
        :return: DpVolumeGroupSnapshotReplicationPolicyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dp_volume_group_snapshot_replication_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dp_volume_group_snapshot_replication_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def get_dp_volume_group_snapshot_replication_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """get_dp_volume_group_snapshot_replication_policy  # noqa: E501

        Get dp volume group snapshot replication policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dp_volume_group_snapshot_replication_policy_with_http_info(policy_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int policy_id: resource id (required)
        :return: DpVolumeGroupSnapshotReplicationPolicyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dp_volume_group_snapshot_replication_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `get_dp_volume_group_snapshot_replication_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']  # noqa: E501

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
            '/dp-volume-group-snapshot-replication-policies/{policy_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DpVolumeGroupSnapshotReplicationPolicyResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dp_volume_group_snapshot_replication_policies(self, **kwargs):  # noqa: E501
        """list_dp_volume_group_snapshot_replication_policies  # noqa: E501

        List dp volume group snapshot replication policies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dp_volume_group_snapshot_replication_policies(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :param int dp_site_id: related site id
        :param int volume_group_id: related volume group id
        :return: DpVolumeGroupSnapshotReplicationPoliciesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_dp_volume_group_snapshot_replication_policies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_dp_volume_group_snapshot_replication_policies_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_dp_volume_group_snapshot_replication_policies_with_http_info(self, **kwargs):  # noqa: E501
        """list_dp_volume_group_snapshot_replication_policies  # noqa: E501

        List dp volume group snapshot replication policies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dp_volume_group_snapshot_replication_policies_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :param int dp_site_id: related site id
        :param int volume_group_id: related volume group id
        :return: DpVolumeGroupSnapshotReplicationPoliciesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'q', 'sort', 'dp_site_id', 'volume_group_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_dp_volume_group_snapshot_replication_policies" % key
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
        if 'dp_site_id' in params:
            query_params.append(('dp_site_id', params['dp_site_id']))  # noqa: E501
        if 'volume_group_id' in params:
            query_params.append(('volume_group_id', params['volume_group_id']))  # noqa: E501

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
            '/dp-volume-group-snapshot-replication-policies/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DpVolumeGroupSnapshotReplicationPoliciesResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dp_volume_group_snapshot_replication_policy(self, policy_id, body, **kwargs):  # noqa: E501
        """update_dp_volume_group_snapshot_replication_policy  # noqa: E501

        Update dp volume group snapshot replication policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dp_volume_group_snapshot_replication_policy(policy_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int policy_id: resource id (required)
        :param DpVolumeGroupSnapshotReplicationPolicyUpdateReq body: policy info (required)
        :return: DpVolumeGroupSnapshotReplicationPolicyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_dp_volume_group_snapshot_replication_policy_with_http_info(policy_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dp_volume_group_snapshot_replication_policy_with_http_info(policy_id, body, **kwargs)  # noqa: E501
            return data

    def update_dp_volume_group_snapshot_replication_policy_with_http_info(self, policy_id, body, **kwargs):  # noqa: E501
        """update_dp_volume_group_snapshot_replication_policy  # noqa: E501

        Update dp volume group snapshot replication policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dp_volume_group_snapshot_replication_policy_with_http_info(policy_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int policy_id: resource id (required)
        :param DpVolumeGroupSnapshotReplicationPolicyUpdateReq body: policy info (required)
        :return: DpVolumeGroupSnapshotReplicationPolicyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dp_volume_group_snapshot_replication_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `update_dp_volume_group_snapshot_replication_policy`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dp_volume_group_snapshot_replication_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']  # noqa: E501

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
            '/dp-volume-group-snapshot-replication-policies/{policy_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DpVolumeGroupSnapshotReplicationPolicyResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
