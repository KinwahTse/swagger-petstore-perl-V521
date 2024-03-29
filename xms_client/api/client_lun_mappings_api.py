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


class ClientLunMappingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_client_lun_mapping(self, client_lun_mapping_id, **kwargs):  # noqa: E501
        """get_client_lun_mapping  # noqa: E501

        get a client lun mapping  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_client_lun_mapping(client_lun_mapping_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int client_lun_mapping_id: client lun mapping id (required)
        :return: ClientLunMappingResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_client_lun_mapping_with_http_info(client_lun_mapping_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_client_lun_mapping_with_http_info(client_lun_mapping_id, **kwargs)  # noqa: E501
            return data

    def get_client_lun_mapping_with_http_info(self, client_lun_mapping_id, **kwargs):  # noqa: E501
        """get_client_lun_mapping  # noqa: E501

        get a client lun mapping  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_client_lun_mapping_with_http_info(client_lun_mapping_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int client_lun_mapping_id: client lun mapping id (required)
        :return: ClientLunMappingResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_lun_mapping_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_client_lun_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_lun_mapping_id' is set
        if ('client_lun_mapping_id' not in params or
                params['client_lun_mapping_id'] is None):
            raise ValueError("Missing the required parameter `client_lun_mapping_id` when calling `get_client_lun_mapping`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_lun_mapping_id' in params:
            path_params['client_lun_mapping_id'] = params['client_lun_mapping_id']  # noqa: E501

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
            '/client-lun-mappings/{client_lun_mapping_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientLunMappingResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_client_lun_mappings(self, mapping_group_id, **kwargs):  # noqa: E501
        """list_client_lun_mappings  # noqa: E501

        List client lun mappings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_client_lun_mappings(mapping_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int mapping_group_id: mapping group id (required)
        :param int limit: paging param
        :param int offset: paging param
        :return: ClientLunMappingsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_client_lun_mappings_with_http_info(mapping_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_client_lun_mappings_with_http_info(mapping_group_id, **kwargs)  # noqa: E501
            return data

    def list_client_lun_mappings_with_http_info(self, mapping_group_id, **kwargs):  # noqa: E501
        """list_client_lun_mappings  # noqa: E501

        List client lun mappings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_client_lun_mappings_with_http_info(mapping_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int mapping_group_id: mapping group id (required)
        :param int limit: paging param
        :param int offset: paging param
        :return: ClientLunMappingsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mapping_group_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_client_lun_mappings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mapping_group_id' is set
        if ('mapping_group_id' not in params or
                params['mapping_group_id'] is None):
            raise ValueError("Missing the required parameter `mapping_group_id` when calling `list_client_lun_mappings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'mapping_group_id' in params:
            query_params.append(('mapping_group_id', params['mapping_group_id']))  # noqa: E501

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
            '/client-lun-mappings/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClientLunMappingsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
