# xms_client.FsClientGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fs_clients**](FsClientGroupsApi.md#add_fs_clients) | **PUT** /fs-client-groups/{fs_client_group_id}/fs-clients | 
[**create_fs_client_group**](FsClientGroupsApi.md#create_fs_client_group) | **POST** /fs-client-groups/ | 
[**delete_fs_client_group**](FsClientGroupsApi.md#delete_fs_client_group) | **DELETE** /fs-client-groups/{fs_client_group_id} | 
[**get_fs_client_group**](FsClientGroupsApi.md#get_fs_client_group) | **GET** /fs-client-groups/{fs_client_group_id} | 
[**list_fs_client_groups**](FsClientGroupsApi.md#list_fs_client_groups) | **GET** /fs-client-groups/ | 
[**remove_fs_clients**](FsClientGroupsApi.md#remove_fs_clients) | **DELETE** /fs-client-groups/{fs_client_group_id}/fs-clients | 
[**update_fs_client_group**](FsClientGroupsApi.md#update_fs_client_group) | **PATCH** /fs-client-groups/{fs_client_group_id} | 


# **add_fs_clients**
> FSClientGroupResp add_fs_clients(fs_client_group_id, body)



add clients to file storage client group

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
api_instance = xms_client.FsClientGroupsApi(xms_client.ApiClient(configuration))
fs_client_group_id = 789 # int | client group id
body = xms_client.FSClientGroupAddClientsReq() # FSClientGroupAddClientsReq | clients info

try:
    api_response = api_instance.add_fs_clients(fs_client_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsClientGroupsApi->add_fs_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_client_group_id** | **int**| client group id | 
 **body** | [**FSClientGroupAddClientsReq**](FSClientGroupAddClientsReq.md)| clients info | 

### Return type

[**FSClientGroupResp**](FSClientGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fs_client_group**
> FSClientGroupResp create_fs_client_group(body, cluster_id=cluster_id)



Create file storage client group

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
api_instance = xms_client.FsClientGroupsApi(xms_client.ApiClient(configuration))
body = xms_client.FSClientGroupCreateReq() # FSClientGroupCreateReq | client group info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_fs_client_group(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsClientGroupsApi->create_fs_client_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSClientGroupCreateReq**](FSClientGroupCreateReq.md)| client group info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**FSClientGroupResp**](FSClientGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fs_client_group**
> delete_fs_client_group(fs_client_group_id)



delete file storage client group

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
api_instance = xms_client.FsClientGroupsApi(xms_client.ApiClient(configuration))
fs_client_group_id = 789 # int | client group id

try:
    api_instance.delete_fs_client_group(fs_client_group_id)
except ApiException as e:
    print("Exception when calling FsClientGroupsApi->delete_fs_client_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_client_group_id** | **int**| client group id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fs_client_group**
> FSClientGroupResp get_fs_client_group(fs_client_group_id)



Get file storage client group

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
api_instance = xms_client.FsClientGroupsApi(xms_client.ApiClient(configuration))
fs_client_group_id = 789 # int | client group id

try:
    api_response = api_instance.get_fs_client_group(fs_client_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsClientGroupsApi->get_fs_client_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_client_group_id** | **int**| client group id | 

### Return type

[**FSClientGroupResp**](FSClientGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fs_client_groups**
> FSClientGroupsResp list_fs_client_groups(limit=limit, offset=offset, cluster_id=cluster_id, q=q, sort=sort, fs_client_id=fs_client_id, not_dfs_nfs_share_id=not_dfs_nfs_share_id)



List file storage client groups

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
api_instance = xms_client.FsClientGroupsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
fs_client_id = 789 # int | file storage client id (optional)
not_dfs_nfs_share_id = 789 # int | id of dfs nfs share client groups not in (optional)

try:
    api_response = api_instance.list_fs_client_groups(limit=limit, offset=offset, cluster_id=cluster_id, q=q, sort=sort, fs_client_id=fs_client_id, not_dfs_nfs_share_id=not_dfs_nfs_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsClientGroupsApi->list_fs_client_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **fs_client_id** | **int**| file storage client id | [optional] 
 **not_dfs_nfs_share_id** | **int**| id of dfs nfs share client groups not in | [optional] 

### Return type

[**FSClientGroupsResp**](FSClientGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_fs_clients**
> FSClientGroupResp remove_fs_clients(fs_client_group_id, body)



remove clients from file storage client group

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
api_instance = xms_client.FsClientGroupsApi(xms_client.ApiClient(configuration))
fs_client_group_id = 789 # int | client group id
body = xms_client.FSClientGroupRemoveClientsReq() # FSClientGroupRemoveClientsReq | clients info

try:
    api_response = api_instance.remove_fs_clients(fs_client_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsClientGroupsApi->remove_fs_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_client_group_id** | **int**| client group id | 
 **body** | [**FSClientGroupRemoveClientsReq**](FSClientGroupRemoveClientsReq.md)| clients info | 

### Return type

[**FSClientGroupResp**](FSClientGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fs_client_group**
> FSClientGroupResp update_fs_client_group(fs_client_group_id, body)



Update file storage client group

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
api_instance = xms_client.FsClientGroupsApi(xms_client.ApiClient(configuration))
fs_client_group_id = 789 # int | client group id
body = xms_client.FSClientGroupUpdateReq() # FSClientGroupUpdateReq | client group info

try:
    api_response = api_instance.update_fs_client_group(fs_client_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsClientGroupsApi->update_fs_client_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_client_group_id** | **int**| client group id | 
 **body** | [**FSClientGroupUpdateReq**](FSClientGroupUpdateReq.md)| client group info | 

### Return type

[**FSClientGroupResp**](FSClientGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

