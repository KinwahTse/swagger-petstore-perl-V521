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


class OsObjectsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_os_objects_by_search(self, **kwargs):  # noqa: E501
        """list_os_objects_by_search  # noqa: E501

        List object storage objects by search  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_os_objects_by_search(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_os_objects_by_search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_os_objects_by_search_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_os_objects_by_search_with_http_info(self, **kwargs):  # noqa: E501
        """list_os_objects_by_search  # noqa: E501

        List object storage objects by search  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_os_objects_by_search_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_os_objects_by_search" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/os-objects/_search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_os_objects_by_search_0(self, **kwargs):  # noqa: E501
        """list_os_objects_by_search_0  # noqa: E501

        List object storage objects by search  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_os_objects_by_search_0(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_os_objects_by_search_0_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_os_objects_by_search_0_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_os_objects_by_search_0_with_http_info(self, **kwargs):  # noqa: E501
        """list_os_objects_by_search_0  # noqa: E501

        List object storage objects by search  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_os_objects_by_search_0_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_os_objects_by_search_0" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/os-objects/_search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_os_objects_by_sql(self, **kwargs):  # noqa: E501
        """list_os_objects_by_sql  # noqa: E501

        List object storage objects by sql  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_os_objects_by_sql(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_os_objects_by_sql_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_os_objects_by_sql_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_os_objects_by_sql_with_http_info(self, **kwargs):  # noqa: E501
        """list_os_objects_by_sql  # noqa: E501

        List object storage objects by sql  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_os_objects_by_sql_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_os_objects_by_sql" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/os-objects/_sql', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_os_objects_by_sql_0(self, **kwargs):  # noqa: E501
        """list_os_objects_by_sql_0  # noqa: E501

        List object storage objects by sql  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_os_objects_by_sql_0(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_os_objects_by_sql_0_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_os_objects_by_sql_0_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_os_objects_by_sql_0_with_http_info(self, **kwargs):  # noqa: E501
        """list_os_objects_by_sql_0  # noqa: E501

        List object storage objects by sql  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_os_objects_by_sql_0_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_os_objects_by_sql_0" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/os-objects/_sql', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def report_os_objects_by_sql(self, **kwargs):  # noqa: E501
        """report_os_objects_by_sql  # noqa: E501

        Download object storage objects report by sql  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.report_os_objects_by_sql(async=True)
        >>> result = thread.get()

        :param async bool
        :param str sql: select statement
        :param str os_buckets: name of buckets joined by colon
        :param str cluster_id: cluster id
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.report_os_objects_by_sql_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.report_os_objects_by_sql_with_http_info(**kwargs)  # noqa: E501
            return data

    def report_os_objects_by_sql_with_http_info(self, **kwargs):  # noqa: E501
        """report_os_objects_by_sql  # noqa: E501

        Download object storage objects report by sql  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.report_os_objects_by_sql_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str sql: select statement
        :param str os_buckets: name of buckets joined by colon
        :param str cluster_id: cluster id
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sql', 'os_buckets', 'cluster_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method report_os_objects_by_sql" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sql' in params:
            query_params.append(('sql', params['sql']))  # noqa: E501
        if 'os_buckets' in params:
            query_params.append(('os_buckets', params['os_buckets']))  # noqa: E501
        if 'cluster_id' in params:
            query_params.append(('cluster_id', params['cluster_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/os-objects/report/_sql', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def report_os_objects_by_sql_0(self, **kwargs):  # noqa: E501
        """report_os_objects_by_sql_0  # noqa: E501

        Download object storage objects report by sql  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.report_os_objects_by_sql_0(async=True)
        >>> result = thread.get()

        :param async bool
        :param str sql: select statement
        :param str os_buckets: name of buckets joined by colon
        :param str cluster_id: cluster id
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.report_os_objects_by_sql_0_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.report_os_objects_by_sql_0_with_http_info(**kwargs)  # noqa: E501
            return data

    def report_os_objects_by_sql_0_with_http_info(self, **kwargs):  # noqa: E501
        """report_os_objects_by_sql_0  # noqa: E501

        Download object storage objects report by sql  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.report_os_objects_by_sql_0_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str sql: select statement
        :param str os_buckets: name of buckets joined by colon
        :param str cluster_id: cluster id
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sql', 'os_buckets', 'cluster_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method report_os_objects_by_sql_0" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sql' in params:
            query_params.append(('sql', params['sql']))  # noqa: E501
        if 'os_buckets' in params:
            query_params.append(('os_buckets', params['os_buckets']))  # noqa: E501
        if 'cluster_id' in params:
            query_params.append(('cluster_id', params['cluster_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/os-objects/report/_sql', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
