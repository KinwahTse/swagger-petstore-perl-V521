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


class FsUsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_fs_user(self, body, **kwargs):  # noqa: E501
        """create_fs_user  # noqa: E501

        create file storage user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_fs_user(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param FSUserCreateReq body: user info (required)
        :param str cluster_id: cluster id
        :param bool allow_path_create: allow create path for s3 when not existed
        :return: FSUserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_fs_user_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_fs_user_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_fs_user_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_fs_user  # noqa: E501

        create file storage user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_fs_user_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param FSUserCreateReq body: user info (required)
        :param str cluster_id: cluster id
        :param bool allow_path_create: allow create path for s3 when not existed
        :return: FSUserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'cluster_id', 'allow_path_create']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_fs_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_fs_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cluster_id' in params:
            query_params.append(('cluster_id', params['cluster_id']))  # noqa: E501
        if 'allow_path_create' in params:
            query_params.append(('allow_path_create', params['allow_path_create']))  # noqa: E501

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
            '/fs-users/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FSUserResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_fs_user(self, fs_user_id, **kwargs):  # noqa: E501
        """delete_fs_user  # noqa: E501

        delete file storage user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_fs_user(fs_user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fs_user_id: user id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_fs_user_with_http_info(fs_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_fs_user_with_http_info(fs_user_id, **kwargs)  # noqa: E501
            return data

    def delete_fs_user_with_http_info(self, fs_user_id, **kwargs):  # noqa: E501
        """delete_fs_user  # noqa: E501

        delete file storage user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_fs_user_with_http_info(fs_user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fs_user_id: user id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fs_user_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_fs_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fs_user_id' is set
        if ('fs_user_id' not in params or
                params['fs_user_id'] is None):
            raise ValueError("Missing the required parameter `fs_user_id` when calling `delete_fs_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fs_user_id' in params:
            path_params['fs_user_id'] = params['fs_user_id']  # noqa: E501

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
            '/fs-users/{fs_user_id}', 'DELETE',
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

    def get_fs_user(self, fs_user_id, **kwargs):  # noqa: E501
        """get_fs_user  # noqa: E501

        get file storage user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fs_user(fs_user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fs_user_id: user id (required)
        :return: FSUserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fs_user_with_http_info(fs_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fs_user_with_http_info(fs_user_id, **kwargs)  # noqa: E501
            return data

    def get_fs_user_with_http_info(self, fs_user_id, **kwargs):  # noqa: E501
        """get_fs_user  # noqa: E501

        get file storage user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fs_user_with_http_info(fs_user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fs_user_id: user id (required)
        :return: FSUserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fs_user_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fs_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fs_user_id' is set
        if ('fs_user_id' not in params or
                params['fs_user_id'] is None):
            raise ValueError("Missing the required parameter `fs_user_id` when calling `get_fs_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fs_user_id' in params:
            path_params['fs_user_id'] = params['fs_user_id']  # noqa: E501

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
            '/fs-users/{fs_user_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FSUserResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_fs_users(self, **kwargs):  # noqa: E501
        """list_fs_users  # noqa: E501

        List file storage users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_fs_users(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :param str cluster_id: cluster id
        :param str security: security of file storage users
        :param int fs_user_group_id: file storage user group id
        :param int not_fs_user_group_id: file storage user group id
        :param int not_dfs_smb_share_id: id of dfs smb share users not in
        :param bool not_dfs_ftp_share: value must be true, means available add to ftp share
        :param bool s3_enabled: is s3 enabled
        :param int user_id: user id
        :return: FSUsersResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_fs_users_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_fs_users_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_fs_users_with_http_info(self, **kwargs):  # noqa: E501
        """list_fs_users  # noqa: E501

        List file storage users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_fs_users_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: paging param
        :param int offset: paging param
        :param str q: query param of search
        :param str sort: sort param of search
        :param str cluster_id: cluster id
        :param str security: security of file storage users
        :param int fs_user_group_id: file storage user group id
        :param int not_fs_user_group_id: file storage user group id
        :param int not_dfs_smb_share_id: id of dfs smb share users not in
        :param bool not_dfs_ftp_share: value must be true, means available add to ftp share
        :param bool s3_enabled: is s3 enabled
        :param int user_id: user id
        :return: FSUsersResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'q', 'sort', 'cluster_id', 'security', 'fs_user_group_id', 'not_fs_user_group_id', 'not_dfs_smb_share_id', 'not_dfs_ftp_share', 's3_enabled', 'user_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_fs_users" % key
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
        if 'security' in params:
            query_params.append(('security', params['security']))  # noqa: E501
        if 'fs_user_group_id' in params:
            query_params.append(('fs_user_group_id', params['fs_user_group_id']))  # noqa: E501
        if 'not_fs_user_group_id' in params:
            query_params.append(('not_fs_user_group_id', params['not_fs_user_group_id']))  # noqa: E501
        if 'not_dfs_smb_share_id' in params:
            query_params.append(('not_dfs_smb_share_id', params['not_dfs_smb_share_id']))  # noqa: E501
        if 'not_dfs_ftp_share' in params:
            query_params.append(('not_dfs_ftp_share', params['not_dfs_ftp_share']))  # noqa: E501
        if 's3_enabled' in params:
            query_params.append(('s3_enabled', params['s3_enabled']))  # noqa: E501
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
            '/fs-users/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FSUsersResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_fs_user(self, fs_user_id, body, **kwargs):  # noqa: E501
        """update_fs_user  # noqa: E501

        update file storage user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_fs_user(fs_user_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fs_user_id: user id (required)
        :param FSUserUpdateReq body: user info (required)
        :param bool allow_path_create: allow create path for s3 when not existed
        :return: FSUserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_fs_user_with_http_info(fs_user_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_fs_user_with_http_info(fs_user_id, body, **kwargs)  # noqa: E501
            return data

    def update_fs_user_with_http_info(self, fs_user_id, body, **kwargs):  # noqa: E501
        """update_fs_user  # noqa: E501

        update file storage user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_fs_user_with_http_info(fs_user_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param int fs_user_id: user id (required)
        :param FSUserUpdateReq body: user info (required)
        :param bool allow_path_create: allow create path for s3 when not existed
        :return: FSUserResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fs_user_id', 'body', 'allow_path_create']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_fs_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fs_user_id' is set
        if ('fs_user_id' not in params or
                params['fs_user_id'] is None):
            raise ValueError("Missing the required parameter `fs_user_id` when calling `update_fs_user`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_fs_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fs_user_id' in params:
            path_params['fs_user_id'] = params['fs_user_id']  # noqa: E501

        query_params = []
        if 'allow_path_create' in params:
            query_params.append(('allow_path_create', params['allow_path_create']))  # noqa: E501

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
            '/fs-users/{fs_user_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FSUserResp',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)