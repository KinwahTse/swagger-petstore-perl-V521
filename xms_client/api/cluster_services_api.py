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


class ClusterServicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_cluster_service(self, service_id, **kwargs):  # noqa: E501
        """get_cluster_service  # noqa: E501

        Get a cluster service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cluster_service(service_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int service_id: clsuter service id (required)
        :return: ClusterServiceResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_cluster_service_with_http_info(service_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cluster_service_with_http_info(service_id, **kwargs)  # noqa: E501
            return data

    def get_cluster_service_with_http_info(self, service_id, **kwargs):  # noqa: E501
        """get_cluster_service  # noqa: E501

        Get a cluster service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cluster_service_with_http_info(service_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int service_id: clsuter service id (required)
        :return: ClusterServiceResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cluster_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_id' is set
        if ('service_id' not in params or
                params['service_id'] is None):
            raise ValueError("Missing the required parameter `service_id` when calling `get_cluster_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_id' in params:
            path_params['service_id'] = params['service_id']  # noqa: E501

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
            '/cluster-services/{service_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClusterServiceResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_cluster_services(self, **kwargs):  # noqa: E501
        """list_cluster_services  # noqa: E501

        List cluster services  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_cluster_services(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :return: ClusterServicesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_cluster_services_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_cluster_services_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_cluster_services_with_http_info(self, **kwargs):  # noqa: E501
        """list_cluster_services  # noqa: E501

        List cluster services  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_cluster_services_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :return: ClusterServicesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_cluster_services" % key
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
            '/cluster-services/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClusterServicesResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rebuild_cluster_service(self, service_id, **kwargs):  # noqa: E501
        """rebuild_cluster_service  # noqa: E501

        Rebuild the cluster service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.rebuild_cluster_service(service_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int service_id: clsuter service id (required)
        :return: ClusterServiceResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.rebuild_cluster_service_with_http_info(service_id, **kwargs)  # noqa: E501
        else:
            (data) = self.rebuild_cluster_service_with_http_info(service_id, **kwargs)  # noqa: E501
            return data

    def rebuild_cluster_service_with_http_info(self, service_id, **kwargs):  # noqa: E501
        """rebuild_cluster_service  # noqa: E501

        Rebuild the cluster service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.rebuild_cluster_service_with_http_info(service_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int service_id: clsuter service id (required)
        :return: ClusterServiceResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rebuild_cluster_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_id' is set
        if ('service_id' not in params or
                params['service_id'] is None):
            raise ValueError("Missing the required parameter `service_id` when calling `rebuild_cluster_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_id' in params:
            path_params['service_id'] = params['service_id']  # noqa: E501

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
            '/cluster-services/{service_id}:rebuild', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClusterServiceResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reindex_docs(self, service_id, **kwargs):  # noqa: E501
        """reindex_docs  # noqa: E501

        Reindex search docs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reindex_docs(service_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int service_id: clsuter service id (required)
        :return: ClusterServiceResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.reindex_docs_with_http_info(service_id, **kwargs)  # noqa: E501
        else:
            (data) = self.reindex_docs_with_http_info(service_id, **kwargs)  # noqa: E501
            return data

    def reindex_docs_with_http_info(self, service_id, **kwargs):  # noqa: E501
        """reindex_docs  # noqa: E501

        Reindex search docs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reindex_docs_with_http_info(service_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int service_id: clsuter service id (required)
        :return: ClusterServiceResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reindex_docs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_id' is set
        if ('service_id' not in params or
                params['service_id'] is None):
            raise ValueError("Missing the required parameter `service_id` when calling `reindex_docs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_id' in params:
            path_params['service_id'] = params['service_id']  # noqa: E501

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
            '/cluster-services/{service_id}:reindex-docs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ClusterServiceResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
