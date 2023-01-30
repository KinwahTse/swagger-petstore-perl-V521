# xms_client.FsUserGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fs_users**](FsUserGroupsApi.md#add_fs_users) | **PUT** /fs-user-groups/{fs_user_group_id}/fs-users | 
[**create_fs_user_group**](FsUserGroupsApi.md#create_fs_user_group) | **POST** /fs-user-groups/ | 
[**delete_fs_user_group**](FsUserGroupsApi.md#delete_fs_user_group) | **DELETE** /fs-user-groups/{fs_user_group_id} | 
[**get_fs_user_group**](FsUserGroupsApi.md#get_fs_user_group) | **GET** /fs-user-groups/{fs_user_group_id} | 
[**list_fs_user_groups**](FsUserGroupsApi.md#list_fs_user_groups) | **GET** /fs-user-groups/ | 
[**remove_fs_users**](FsUserGroupsApi.md#remove_fs_users) | **DELETE** /fs-user-groups/{fs_user_group_id}/fs-users | 
[**update_fs_user_group**](FsUserGroupsApi.md#update_fs_user_group) | **PATCH** /fs-user-groups/{fs_user_group_id} | 


# **add_fs_users**
> FSUserGroupResp add_fs_users(fs_user_group_id, body)



add users to file storage user group

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
api_instance = xms_client.FsUserGroupsApi(xms_client.ApiClient(configuration))
fs_user_group_id = 789 # int | user group id
body = xms_client.FSUserGroupAddUsersReq() # FSUserGroupAddUsersReq | users info

try:
    api_response = api_instance.add_fs_users(fs_user_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsUserGroupsApi->add_fs_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_user_group_id** | **int**| user group id | 
 **body** | [**FSUserGroupAddUsersReq**](FSUserGroupAddUsersReq.md)| users info | 

### Return type

[**FSUserGroupResp**](FSUserGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fs_user_group**
> FSUserGroupResp create_fs_user_group(body, cluster_id=cluster_id)



Create file storage user group

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
api_instance = xms_client.FsUserGroupsApi(xms_client.ApiClient(configuration))
body = xms_client.FSUserGroupCreateReq() # FSUserGroupCreateReq | user group info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_fs_user_group(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsUserGroupsApi->create_fs_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSUserGroupCreateReq**](FSUserGroupCreateReq.md)| user group info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**FSUserGroupResp**](FSUserGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fs_user_group**
> delete_fs_user_group(fs_user_group_id)



delete file storage user group

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
api_instance = xms_client.FsUserGroupsApi(xms_client.ApiClient(configuration))
fs_user_group_id = 789 # int | user group id

try:
    api_instance.delete_fs_user_group(fs_user_group_id)
except ApiException as e:
    print("Exception when calling FsUserGroupsApi->delete_fs_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_user_group_id** | **int**| user group id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fs_user_group**
> FSUserGroupResp get_fs_user_group(fs_user_group_id)



Get file storage user group

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
api_instance = xms_client.FsUserGroupsApi(xms_client.ApiClient(configuration))
fs_user_group_id = 789 # int | user group id

try:
    api_response = api_instance.get_fs_user_group(fs_user_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsUserGroupsApi->get_fs_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_user_group_id** | **int**| user group id | 

### Return type

[**FSUserGroupResp**](FSUserGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fs_user_groups**
> FSUserGroupsResp list_fs_user_groups(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, type=type, fs_user_id=fs_user_id, not_dfs_smb_share_id=not_dfs_smb_share_id)



List file storage user groups

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
api_instance = xms_client.FsUserGroupsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
type = 'type_example' # str | security type of file storage user group (optional)
fs_user_id = 789 # int | file storage user id (optional)
not_dfs_smb_share_id = 789 # int | id of dfs smb share user groups not in (optional)

try:
    api_response = api_instance.list_fs_user_groups(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, type=type, fs_user_id=fs_user_id, not_dfs_smb_share_id=not_dfs_smb_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsUserGroupsApi->list_fs_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **type** | **str**| security type of file storage user group | [optional] 
 **fs_user_id** | **int**| file storage user id | [optional] 
 **not_dfs_smb_share_id** | **int**| id of dfs smb share user groups not in | [optional] 

### Return type

[**FSUserGroupsResp**](FSUserGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_fs_users**
> FSUserGroupResp remove_fs_users(fs_user_group_id, body)



remove users from file storage user group

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
api_instance = xms_client.FsUserGroupsApi(xms_client.ApiClient(configuration))
fs_user_group_id = 789 # int | user group id
body = xms_client.FSUserGroupRemoveUsersReq() # FSUserGroupRemoveUsersReq | users info

try:
    api_response = api_instance.remove_fs_users(fs_user_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsUserGroupsApi->remove_fs_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_user_group_id** | **int**| user group id | 
 **body** | [**FSUserGroupRemoveUsersReq**](FSUserGroupRemoveUsersReq.md)| users info | 

### Return type

[**FSUserGroupResp**](FSUserGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fs_user_group**
> FSUserGroupResp update_fs_user_group(fs_user_group_id, body)



Update file storage user group

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
api_instance = xms_client.FsUserGroupsApi(xms_client.ApiClient(configuration))
fs_user_group_id = 789 # int | user group id
body = xms_client.FSUserGroupUpdateReq() # FSUserGroupUpdateReq | user group info

try:
    api_response = api_instance.update_fs_user_group(fs_user_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsUserGroupsApi->update_fs_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_user_group_id** | **int**| user group id | 
 **body** | [**FSUserGroupUpdateReq**](FSUserGroupUpdateReq.md)| user group info | 

### Return type

[**FSUserGroupResp**](FSUserGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

