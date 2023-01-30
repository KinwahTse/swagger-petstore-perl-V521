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


class OsKeysApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_key(self, body, **kwargs):  # noqa: E501
        """create_key  # noqa: E501

        Create new object storage key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_key(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param ObjectStorageKeyCreateReq body: key info (required)
        :param str cluster_id: cluster id
        :return: ObjectStorageKeyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_key_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_key_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_key_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_key  # noqa: E501

        Create new object storage key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_key_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param ObjectStorageKeyCreateReq body: key info (required)
        :param str cluster_id: cluster id
        :return: ObjectStorageKeyResp
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
                    " to method create_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_key`")  # noqa: E501

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
            '/os-keys/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectStorageKeyResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_key(self, key_id, **kwargs):  # noqa: E501
        """delete_key  # noqa: E501

        Delete object storage key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_key(key_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int key_id: key id (required)
        :return: ObjectStorageKeyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_key_with_http_info(key_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_key_with_http_info(key_id, **kwargs)  # noqa: E501
            return data

    def delete_key_with_http_info(self, key_id, **kwargs):  # noqa: E501
        """delete_key  # noqa: E501

        Delete object storage key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_key_with_http_info(key_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int key_id: key id (required)
        :return: ObjectStorageKeyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_id' is set
        if ('key_id' not in params or
                params['key_id'] is None):
            raise ValueError("Missing the required parameter `key_id` when calling `delete_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key_id' in params:
            path_params['key_id'] = params['key_id']  # noqa: E501

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
            '/os-keys/{key_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectStorageKeyResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_key(self, key_id, **kwargs):  # noqa: E501
        """get_key  # noqa: E501

        get object storage key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_key(key_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int key_id: user id (required)
        :return: ObjectStorageKeyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_key_with_http_info(key_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_key_with_http_info(key_id, **kwargs)  # noqa: E501
            return data

    def get_key_with_http_info(self, key_id, **kwargs):  # noqa: E501
        """get_key  # noqa: E501

        get object storage key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_key_with_http_info(key_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int key_id: user id (required)
        :return: ObjectStorageKeyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_id' is set
        if ('key_id' not in params or
                params['key_id'] is None):
            raise ValueError("Missing the required parameter `key_id` when calling `get_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key_id' in params:
            path_params['key_id'] = params['key_id']  # noqa: E501

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
            '/os-keys/{key_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectStorageKeyResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_keys(self, **kwargs):  # noqa: E501
        """list_keys  # noqa: E501

        List object storage keys  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_keys(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :param int limit: paging param
        :param int offset: paging param
        :param int user_id: object storage user id
        :return: ObjectStorageKeysResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_keys_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_keys_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_keys_with_http_info(self, **kwargs):  # noqa: E501
        """list_keys  # noqa: E501

        List object storage keys  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_keys_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cluster_id: cluster id
        :param int limit: paging param
        :param int offset: paging param
        :param int user_id: object storage user id
        :return: ObjectStorageKeysResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id', 'limit', 'offset', 'user_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_keys" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in params:
            query_params.append(('cluster_id', params['cluster_id']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501

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
            '/os-keys/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectStorageKeysResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_key(self, key_id, body, **kwargs):  # noqa: E501
        """update_key  # noqa: E501

        Update object storage key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_key(key_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int key_id: key id (required)
        :param ObjectStorageKeyUpdateReq body: key info (required)
        :return: ObjectStorageKeyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_key_with_http_info(key_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_key_with_http_info(key_id, body, **kwargs)  # noqa: E501
            return data

    def update_key_with_http_info(self, key_id, body, **kwargs):  # noqa: E501
        """update_key  # noqa: E501

        Update object storage key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_key_with_http_info(key_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int key_id: key id (required)
        :param ObjectStorageKeyUpdateReq body: key info (required)
        :return: ObjectStorageKeyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_id' is set
        if ('key_id' not in params or
                params['key_id'] is None):
            raise ValueError("Missing the required parameter `key_id` when calling `update_key`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key_id' in params:
            path_params['key_id'] = params['key_id']  # noqa: E501

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
            '/os-keys/{key_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectStorageKeyResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
