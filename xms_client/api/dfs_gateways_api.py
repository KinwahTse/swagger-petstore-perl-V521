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


class DfsGatewaysApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_dfs_gateway(self, dfs_gateway_id, **kwargs):  # noqa: E501
        """get_dfs_gateway  # noqa: E501

        Get dfs gateway  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_gateway(dfs_gateway_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_gateway_id: gateway id (required)
        :return: DfsGatewayResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dfs_gateway_with_http_info(dfs_gateway_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dfs_gateway_with_http_info(dfs_gateway_id, **kwargs)  # noqa: E501
            return data

    def get_dfs_gateway_with_http_info(self, dfs_gateway_id, **kwargs):  # noqa: E501
        """get_dfs_gateway  # noqa: E501

        Get dfs gateway  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_gateway_with_http_info(dfs_gateway_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_gateway_id: gateway id (required)
        :return: DfsGatewayResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_gateway_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dfs_gateway" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_gateway_id' is set
        if ('dfs_gateway_id' not in params or
                params['dfs_gateway_id'] is None):
            raise ValueError("Missing the required parameter `dfs_gateway_id` when calling `get_dfs_gateway`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_gateway_id' in params:
            path_params['dfs_gateway_id'] = params['dfs_gateway_id']  # noqa: E501

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
            '/dfs-gateways/{dfs_gateway_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsGatewayResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dfs_gateway_samples(self, dfs_gateway_id, **kwargs):  # noqa: E501
        """get_dfs_gateway_samples  # noqa: E501

        get a dfs gateway's samples  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_gateway_samples(dfs_gateway_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_gateway_id: dfs gateway id (required)
        :param str duration_begin: duration begin timestamp
        :param str duration_end: duration end timestamp
        :param str period: samples period
        :return: DfsGatewaySamplesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dfs_gateway_samples_with_http_info(dfs_gateway_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dfs_gateway_samples_with_http_info(dfs_gateway_id, **kwargs)  # noqa: E501
            return data

    def get_dfs_gateway_samples_with_http_info(self, dfs_gateway_id, **kwargs):  # noqa: E501
        """get_dfs_gateway_samples  # noqa: E501

        get a dfs gateway's samples  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dfs_gateway_samples_with_http_info(dfs_gateway_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_gateway_id: dfs gateway id (required)
        :param str duration_begin: duration begin timestamp
        :param str duration_end: duration end timestamp
        :param str period: samples period
        :return: DfsGatewaySamplesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_gateway_id', 'duration_begin', 'duration_end', 'period']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dfs_gateway_samples" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_gateway_id' is set
        if ('dfs_gateway_id' not in params or
                params['dfs_gateway_id'] is None):
            raise ValueError("Missing the required parameter `dfs_gateway_id` when calling `get_dfs_gateway_samples`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_gateway_id' in params:
            path_params['dfs_gateway_id'] = params['dfs_gateway_id']  # noqa: E501

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
            '/dfs-gateways/{dfs_gateway_id}/samples', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsGatewaySamplesResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dfs_gateway_connections(self, dfs_gateway_id, **kwargs):  # noqa: E501
        """list_dfs_gateway_connections  # noqa: E501

        list client connections of dfs gateway  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dfs_gateway_connections(dfs_gateway_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_gateway_id: dfs gateway id (required)
        :param str types: share types, value is smb|nfs|ftp|s3
        :return: DfsGatewayConnectionsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_dfs_gateway_connections_with_http_info(dfs_gateway_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_dfs_gateway_connections_with_http_info(dfs_gateway_id, **kwargs)  # noqa: E501
            return data

    def list_dfs_gateway_connections_with_http_info(self, dfs_gateway_id, **kwargs):  # noqa: E501
        """list_dfs_gateway_connections  # noqa: E501

        list client connections of dfs gateway  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dfs_gateway_connections_with_http_info(dfs_gateway_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dfs_gateway_id: dfs gateway id (required)
        :param str types: share types, value is smb|nfs|ftp|s3
        :return: DfsGatewayConnectionsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dfs_gateway_id', 'types']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_dfs_gateway_connections" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dfs_gateway_id' is set
        if ('dfs_gateway_id' not in params or
                params['dfs_gateway_id'] is None):
            raise ValueError("Missing the required parameter `dfs_gateway_id` when calling `list_dfs_gateway_connections`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dfs_gateway_id' in params:
            path_params['dfs_gateway_id'] = params['dfs_gateway_id']  # noqa: E501

        query_params = []
        if 'types' in params:
            query_params.append(('types', params['types']))  # noqa: E501

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
            '/dfs-gateways/{dfs_gateway_id}/connections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsGatewayConnectionsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dfs_gateways(self, **kwargs):  # noqa: E501
        """list_dfs_gateways  # noqa: E501

        List dfs gateways  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dfs_gateways(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :param str cluster_id: cluster id
        :param int dfs_gateway_group_id: dfs gateway group id
        :return: DfsGatewaysResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_dfs_gateways_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_dfs_gateways_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_dfs_gateways_with_http_info(self, **kwargs):  # noqa: E501
        """list_dfs_gateways  # noqa: E501

        List dfs gateways  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dfs_gateways_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :param str cluster_id: cluster id
        :param int dfs_gateway_group_id: dfs gateway group id
        :return: DfsGatewaysResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'q', 'sort', 'cluster_id', 'dfs_gateway_group_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_dfs_gateways" % key
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
        if 'dfs_gateway_group_id' in params:
            query_params.append(('dfs_gateway_group_id', params['dfs_gateway_group_id']))  # noqa: E501

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
            '/dfs-gateways/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DfsGatewaysResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
