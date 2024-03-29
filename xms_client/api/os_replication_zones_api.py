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


class OsReplicationZonesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_os_replication_zone(self, body, **kwargs):  # noqa: E501
        """create_os_replication_zone  # noqa: E501

        Create a os replication zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_os_replication_zone(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param OSReplicationZoneCreateReq body: os replication zone info (required)
        :param str cluster_id: cluster id
        :return: OSReplicationZoneResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_os_replication_zone_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_os_replication_zone_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_os_replication_zone_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_os_replication_zone  # noqa: E501

        Create a os replication zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_os_replication_zone_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param OSReplicationZoneCreateReq body: os replication zone info (required)
        :param str cluster_id: cluster id
        :return: OSReplicationZoneResp
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
                    " to method create_os_replication_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_os_replication_zone`")  # noqa: E501

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
            '/os-replication-zones/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OSReplicationZoneResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_os_replication_zone(self, zone_uuid, **kwargs):  # noqa: E501
        """delete_os_replication_zone  # noqa: E501

        Delete a os replication zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_os_replication_zone(zone_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str zone_uuid: os replication zone uuid (required)
        :return: OSReplicationZoneResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_os_replication_zone_with_http_info(zone_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_os_replication_zone_with_http_info(zone_uuid, **kwargs)  # noqa: E501
            return data

    def delete_os_replication_zone_with_http_info(self, zone_uuid, **kwargs):  # noqa: E501
        """delete_os_replication_zone  # noqa: E501

        Delete a os replication zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_os_replication_zone_with_http_info(zone_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str zone_uuid: os replication zone uuid (required)
        :return: OSReplicationZoneResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone_uuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_os_replication_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone_uuid' is set
        if ('zone_uuid' not in params or
                params['zone_uuid'] is None):
            raise ValueError("Missing the required parameter `zone_uuid` when calling `delete_os_replication_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_uuid' in params:
            path_params['zone_uuid'] = params['zone_uuid']  # noqa: E501

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
            '/os-replication-zones/{zone_uuid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OSReplicationZoneResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_os_replication_zone(self, zone_uuid, **kwargs):  # noqa: E501
        """get_os_replication_zone  # noqa: E501

        Get a os replication zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_os_replication_zone(zone_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str zone_uuid: os replication zone uuid (required)
        :return: OSReplicationZoneRecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_os_replication_zone_with_http_info(zone_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_os_replication_zone_with_http_info(zone_uuid, **kwargs)  # noqa: E501
            return data

    def get_os_replication_zone_with_http_info(self, zone_uuid, **kwargs):  # noqa: E501
        """get_os_replication_zone  # noqa: E501

        Get a os replication zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_os_replication_zone_with_http_info(zone_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str zone_uuid: os replication zone uuid (required)
        :return: OSReplicationZoneRecordResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone_uuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_os_replication_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone_uuid' is set
        if ('zone_uuid' not in params or
                params['zone_uuid'] is None):
            raise ValueError("Missing the required parameter `zone_uuid` when calling `get_os_replication_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_uuid' in params:
            path_params['zone_uuid'] = params['zone_uuid']  # noqa: E501

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
            '/os-replication-zones/{zone_uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OSReplicationZoneRecordResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_os_replication_zone_samples(self, zone_uuid, **kwargs):  # noqa: E501
        """get_os_replication_zone_samples  # noqa: E501

        get an os replication zone's samples  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_os_replication_zone_samples(zone_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str zone_uuid: os replication zone uuid (required)
        :param str duration_begin: duration begin timestamp
        :param str duration_end: duration end timestamp
        :param str period: samples period
        :return: OSReplicationZoneSamplesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_os_replication_zone_samples_with_http_info(zone_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_os_replication_zone_samples_with_http_info(zone_uuid, **kwargs)  # noqa: E501
            return data

    def get_os_replication_zone_samples_with_http_info(self, zone_uuid, **kwargs):  # noqa: E501
        """get_os_replication_zone_samples  # noqa: E501

        get an os replication zone's samples  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_os_replication_zone_samples_with_http_info(zone_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str zone_uuid: os replication zone uuid (required)
        :param str duration_begin: duration begin timestamp
        :param str duration_end: duration end timestamp
        :param str period: samples period
        :return: OSReplicationZoneSamplesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone_uuid', 'duration_begin', 'duration_end', 'period']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_os_replication_zone_samples" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone_uuid' is set
        if ('zone_uuid' not in params or
                params['zone_uuid'] is None):
            raise ValueError("Missing the required parameter `zone_uuid` when calling `get_os_replication_zone_samples`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_uuid' in params:
            path_params['zone_uuid'] = params['zone_uuid']  # noqa: E501

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
            '/os-replication-zones/{zone_uuid}/samples', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OSReplicationZoneSamplesResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_os_replication_zones(self, **kwargs):  # noqa: E501
        """list_os_replication_zones  # noqa: E501

        List os replication zones  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_os_replication_zones(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str marker: paging param
        :param str replication_uuid: os replication uuid
        :param str os_zone_uuid: os zone uuid
        :param str cluster_id: cluster id
        :return: OSReplicationZoneRecordsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_os_replication_zones_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_os_replication_zones_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_os_replication_zones_with_http_info(self, **kwargs):  # noqa: E501
        """list_os_replication_zones  # noqa: E501

        List os replication zones  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_os_replication_zones_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str marker: paging param
        :param str replication_uuid: os replication uuid
        :param str os_zone_uuid: os zone uuid
        :param str cluster_id: cluster id
        :return: OSReplicationZoneRecordsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'marker', 'replication_uuid', 'os_zone_uuid', 'cluster_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_os_replication_zones" % key
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
        if 'marker' in params:
            query_params.append(('marker', params['marker']))  # noqa: E501
        if 'replication_uuid' in params:
            query_params.append(('replication_uuid', params['replication_uuid']))  # noqa: E501
        if 'os_zone_uuid' in params:
            query_params.append(('os_zone_uuid', params['os_zone_uuid']))  # noqa: E501
        if 'cluster_id' in params:
            query_params.append(('cluster_id', params['cluster_id']))  # noqa: E501

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
            '/os-replication-zones/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OSReplicationZoneRecordsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_os_replication_zone(self, zone_uuid, **kwargs):  # noqa: E501
        """update_os_replication_zone  # noqa: E501

        Update an os replication zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_os_replication_zone(zone_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str zone_uuid: os replication zone uuid (required)
        :return: OSReplicationZoneResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_os_replication_zone_with_http_info(zone_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_os_replication_zone_with_http_info(zone_uuid, **kwargs)  # noqa: E501
            return data

    def update_os_replication_zone_with_http_info(self, zone_uuid, **kwargs):  # noqa: E501
        """update_os_replication_zone  # noqa: E501

        Update an os replication zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_os_replication_zone_with_http_info(zone_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str zone_uuid: os replication zone uuid (required)
        :return: OSReplicationZoneResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone_uuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_os_replication_zone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone_uuid' is set
        if ('zone_uuid' not in params or
                params['zone_uuid'] is None):
            raise ValueError("Missing the required parameter `zone_uuid` when calling `update_os_replication_zone`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_uuid' in params:
            path_params['zone_uuid'] = params['zone_uuid']  # noqa: E501

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
            '/os-replication-zones/{zone_uuid}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OSReplicationZoneResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
