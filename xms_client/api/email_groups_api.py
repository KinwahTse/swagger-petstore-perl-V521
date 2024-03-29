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


class EmailGroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_email_group(self, body, **kwargs):  # noqa: E501
        """create_email_group  # noqa: E501

        create email group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_email_group(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param EmailGroupUpdateReq body: email group (required)
        :return: EmailGroupResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_email_group_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_email_group_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_email_group_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_email_group  # noqa: E501

        create email group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_email_group_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param EmailGroupUpdateReq body: email group (required)
        :return: EmailGroupResp
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
                    " to method create_email_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_email_group`")  # noqa: E501

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
            '/email-groups/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailGroupResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_email_group(self, group_id, **kwargs):  # noqa: E501
        """delete_email_group  # noqa: E501

        delete email group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_email_group(group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int group_id: the id of email group (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_email_group_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_email_group_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def delete_email_group_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """delete_email_group  # noqa: E501

        delete email group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_email_group_with_http_info(group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int group_id: the id of email group (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_email_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `delete_email_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/email-groups/{group_id}', 'DELETE',
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

    def get_email_group(self, group_id, **kwargs):  # noqa: E501
        """get_email_group  # noqa: E501

        get email group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_email_group(group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int group_id: the id of email group (required)
        :return: EmailGroupResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_email_group_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_email_group_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def get_email_group_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """get_email_group  # noqa: E501

        get email group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_email_group_with_http_info(group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int group_id: the id of email group (required)
        :return: EmailGroupResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_email_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_email_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/email-groups/{group_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailGroupResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_email_groups(self, **kwargs):  # noqa: E501
        """list_email_groups  # noqa: E501

        List all email groups  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_email_groups(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param int alert_group_id: alert group id
        :param str name: name of email groups
        :return: EmailGroupsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_email_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_email_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_email_groups_with_http_info(self, **kwargs):  # noqa: E501
        """list_email_groups  # noqa: E501

        List all email groups  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_email_groups_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param int alert_group_id: alert group id
        :param str name: name of email groups
        :return: EmailGroupsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'alert_group_id', 'name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_email_groups" % key
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
        if 'alert_group_id' in params:
            query_params.append(('alert_group_id', params['alert_group_id']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

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
            '/email-groups/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailGroupsResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_email_group(self, group_id, body, **kwargs):  # noqa: E501
        """update_email_group  # noqa: E501

        update email group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_email_group(group_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int group_id: the id of email group (required)
        :param EmailGroupUpdateReq body: email group (required)
        :return: EmailGroupResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_email_group_with_http_info(group_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_email_group_with_http_info(group_id, body, **kwargs)  # noqa: E501
            return data

    def update_email_group_with_http_info(self, group_id, body, **kwargs):  # noqa: E501
        """update_email_group  # noqa: E501

        update email group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_email_group_with_http_info(group_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int group_id: the id of email group (required)
        :param EmailGroupUpdateReq body: email group (required)
        :return: EmailGroupResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_email_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `update_email_group`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_email_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/email-groups/{group_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailGroupResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
