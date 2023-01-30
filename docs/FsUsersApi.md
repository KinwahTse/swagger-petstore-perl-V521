# xms_client.FsUsersApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fs_user**](FsUsersApi.md#create_fs_user) | **POST** /fs-users/ | 
[**delete_fs_user**](FsUsersApi.md#delete_fs_user) | **DELETE** /fs-users/{fs_user_id} | 
[**get_fs_user**](FsUsersApi.md#get_fs_user) | **GET** /fs-users/{fs_user_id} | 
[**list_fs_users**](FsUsersApi.md#list_fs_users) | **GET** /fs-users/ | 
[**update_fs_user**](FsUsersApi.md#update_fs_user) | **PATCH** /fs-users/{fs_user_id} | 


# **create_fs_user**
> FSUserResp create_fs_user(body, cluster_id=cluster_id, allow_path_create=allow_path_create)



create file storage user

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsUsersApi(xms_client.ApiClient(configuration))
body = xms_client.FSUserCreateReq() # FSUserCreateReq | user info
cluster_id = 'cluster_id_example' # str | cluster id (optional)
allow_path_create = true # bool | allow create path for s3 when not existed (optional)

try:
    api_response = api_instance.create_fs_user(body, cluster_id=cluster_id, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsUsersApi->create_fs_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSUserCreateReq**](FSUserCreateReq.md)| user info | 
 **cluster_id** | **str**| cluster id | [optional] 
 **allow_path_create** | **bool**| allow create path for s3 when not existed | [optional] 

### Return type

[**FSUserResp**](FSUserResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fs_user**
> delete_fs_user(fs_user_id)



delete file storage user

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsUsersApi(xms_client.ApiClient(configuration))
fs_user_id = 789 # int | user id

try:
    api_instance.delete_fs_user(fs_user_id)
except ApiException as e:
    print("Exception when calling FsUsersApi->delete_fs_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_user_id** | **int**| user id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fs_user**
> FSUserResp get_fs_user(fs_user_id)



get file storage user

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsUsersApi(xms_client.ApiClient(configuration))
fs_user_id = 789 # int | user id

try:
    api_response = api_instance.get_fs_user(fs_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsUsersApi->get_fs_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_user_id** | **int**| user id | 

### Return type

[**FSUserResp**](FSUserResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fs_users**
> FSUsersResp list_fs_users(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, security=security, fs_user_group_id=fs_user_group_id, not_fs_user_group_id=not_fs_user_group_id, not_dfs_smb_share_id=not_dfs_smb_share_id, not_dfs_ftp_share=not_dfs_ftp_share, s3_enabled=s3_enabled, user_id=user_id)



List file storage users

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsUsersApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
security = 'security_example' # str | security of file storage users (optional)
fs_user_group_id = 789 # int | file storage user group id (optional)
not_fs_user_group_id = 789 # int | file storage user group id (optional)
not_dfs_smb_share_id = 789 # int | id of dfs smb share users not in (optional)
not_dfs_ftp_share = true # bool | value must be true, means available add to ftp share (optional)
s3_enabled = true # bool | is s3 enabled (optional)
user_id = 789 # int | user id (optional)

try:
    api_response = api_instance.list_fs_users(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, security=security, fs_user_group_id=fs_user_group_id, not_fs_user_group_id=not_fs_user_group_id, not_dfs_smb_share_id=not_dfs_smb_share_id, not_dfs_ftp_share=not_dfs_ftp_share, s3_enabled=s3_enabled, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsUsersApi->list_fs_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **security** | **str**| security of file storage users | [optional] 
 **fs_user_group_id** | **int**| file storage user group id | [optional] 
 **not_fs_user_group_id** | **int**| file storage user group id | [optional] 
 **not_dfs_smb_share_id** | **int**| id of dfs smb share users not in | [optional] 
 **not_dfs_ftp_share** | **bool**| value must be true, means available add to ftp share | [optional] 
 **s3_enabled** | **bool**| is s3 enabled | [optional] 
 **user_id** | **int**| user id | [optional] 

### Return type

[**FSUsersResp**](FSUsersResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fs_user**
> FSUserResp update_fs_user(fs_user_id, body, allow_path_create=allow_path_create)



update file storage user

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsUsersApi(xms_client.ApiClient(configuration))
fs_user_id = 789 # int | user id
body = xms_client.FSUserUpdateReq() # FSUserUpdateReq | user info
allow_path_create = true # bool | allow create path for s3 when not existed (optional)

try:
    api_response = api_instance.update_fs_user(fs_user_id, body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsUsersApi->update_fs_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_user_id** | **int**| user id | 
 **body** | [**FSUserUpdateReq**](FSUserUpdateReq.md)| user info | 
 **allow_path_create** | **bool**| allow create path for s3 when not existed | [optional] 

### Return type

[**FSUserResp**](FSUserResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

