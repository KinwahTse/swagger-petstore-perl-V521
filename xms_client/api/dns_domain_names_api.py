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


class DnsDomainNamesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_dns_domain_name(self, dns_domain_name, **kwargs):  # noqa: E501
        """create_dns_domain_name  # noqa: E501

        Create a DNS domain name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dns_domain_name(dns_domain_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param DNSDomainNameCreateReq dns_domain_name: DNS domain name info (required)
        :return: DNSDomainNameResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_dns_domain_name_with_http_info(dns_domain_name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_dns_domain_name_with_http_info(dns_domain_name, **kwargs)  # noqa: E501
            return data

    def create_dns_domain_name_with_http_info(self, dns_domain_name, **kwargs):  # noqa: E501
        """create_dns_domain_name  # noqa: E501

        Create a DNS domain name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dns_domain_name_with_http_info(dns_domain_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param DNSDomainNameCreateReq dns_domain_name: DNS domain name info (required)
        :return: DNSDomainNameResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dns_domain_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dns_domain_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dns_domain_name' is set
        if ('dns_domain_name' not in params or
                params['dns_domain_name'] is None):
            raise ValueError("Missing the required parameter `dns_domain_name` when calling `create_dns_domain_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dns_domain_name' in params:
            body_params = params['dns_domain_name']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/dns-domain-names/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DNSDomainNameResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_dns_domain_name(self, name_id, **kwargs):  # noqa: E501
        """delete_dns_domain_name  # noqa: E501

        Delete a DNS domain nam.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dns_domain_name(name_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int name_id: DNS domain name id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_dns_domain_name_with_http_info(name_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dns_domain_name_with_http_info(name_id, **kwargs)  # noqa: E501
            return data

    def delete_dns_domain_name_with_http_info(self, name_id, **kwargs):  # noqa: E501
        """delete_dns_domain_name  # noqa: E501

        Delete a DNS domain nam.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_dns_domain_name_with_http_info(name_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int name_id: DNS domain name id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dns_domain_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name_id' is set
        if ('name_id' not in params or
                params['name_id'] is None):
            raise ValueError("Missing the required parameter `name_id` when calling `delete_dns_domain_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name_id' in params:
            path_params['name_id'] = params['name_id']  # noqa: E501

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
            '/dns-domain-names/{name_id}', 'DELETE',
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

    def get_dns_domain_name(self, name_id, **kwargs):  # noqa: E501
        """get_dns_domain_name  # noqa: E501

        Get a dns domain name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dns_domain_name(name_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int name_id: dns domain name id (required)
        :return: DNSDomainNameResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_dns_domain_name_with_http_info(name_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dns_domain_name_with_http_info(name_id, **kwargs)  # noqa: E501
            return data

    def get_dns_domain_name_with_http_info(self, name_id, **kwargs):  # noqa: E501
        """get_dns_domain_name  # noqa: E501

        Get a dns domain name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_dns_domain_name_with_http_info(name_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int name_id: dns domain name id (required)
        :return: DNSDomainNameResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dns_domain_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name_id' is set
        if ('name_id' not in params or
                params['name_id'] is None):
            raise ValueError("Missing the required parameter `name_id` when calling `get_dns_domain_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name_id' in params:
            path_params['name_id'] = params['name_id']  # noqa: E501

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
            '/dns-domain-names/{name_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DNSDomainNameResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dns_domain_names(self, **kwargs):  # noqa: E501
        """list_dns_domain_names  # noqa: E501

        List dns domain names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dns_domain_names(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param int dns_zone_id: dns zone id
        :return: DNSDomainNamesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_dns_domain_names_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_dns_domain_names_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_dns_domain_names_with_http_info(self, **kwargs):  # noqa: E501
        """list_dns_domain_names  # noqa: E501

        List dns domain names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_dns_domain_names_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param int dns_zone_id: dns zone id
        :return: DNSDomainNamesResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'dns_zone_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_dns_domain_names" % key
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
        if 'dns_zone_id' in params:
            query_params.append(('dns_zone_id', params['dns_zone_id']))  # noqa: E501

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
            '/dns-domain-names/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DNSDomainNamesResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_dns_domain_name(self, name_id, dns_domain_name, **kwargs):  # noqa: E501
        """update_dns_domain_name  # noqa: E501

        Update a DNS domain name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dns_domain_name(name_id, dns_domain_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int name_id: DNS domain name id (required)
        :param DNSDomainNameUpdateReq dns_domain_name: DNS domain name info (required)
        :return: DNSDomainNameResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_dns_domain_name_with_http_info(name_id, dns_domain_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_dns_domain_name_with_http_info(name_id, dns_domain_name, **kwargs)  # noqa: E501
            return data

    def update_dns_domain_name_with_http_info(self, name_id, dns_domain_name, **kwargs):  # noqa: E501
        """update_dns_domain_name  # noqa: E501

        Update a DNS domain name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_dns_domain_name_with_http_info(name_id, dns_domain_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int name_id: DNS domain name id (required)
        :param DNSDomainNameUpdateReq dns_domain_name: DNS domain name info (required)
        :return: DNSDomainNameResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name_id', 'dns_domain_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dns_domain_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name_id' is set
        if ('name_id' not in params or
                params['name_id'] is None):
            raise ValueError("Missing the required parameter `name_id` when calling `update_dns_domain_name`")  # noqa: E501
        # verify the required parameter 'dns_domain_name' is set
        if ('dns_domain_name' not in params or
                params['dns_domain_name'] is None):
            raise ValueError("Missing the required parameter `dns_domain_name` when calling `update_dns_domain_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name_id' in params:
            path_params['name_id'] = params['name_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dns_domain_name' in params:
            body_params = params['dns_domain_name']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenInHeader', 'tokenInQuery']  # noqa: E501

        return self.api_client.call_api(
            '/dns-domain-names/{name_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DNSDomainNameResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
