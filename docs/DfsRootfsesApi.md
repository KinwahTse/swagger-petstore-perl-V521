# xms_client.DfsRootfsesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dfs_rootfs**](DfsRootfsesApi.md#create_dfs_rootfs) | **POST** /dfs-rootfses/ | 
[**delete_dfs_rootfs**](DfsRootfsesApi.md#delete_dfs_rootfs) | **DELETE** /dfs-rootfses/{dfs_rootfs_id} | 
[**get_dfs_rootfs**](DfsRootfsesApi.md#get_dfs_rootfs) | **GET** /dfs-rootfses/{dfs_rootfs_id} | 
[**get_dfs_rootfs_samples**](DfsRootfsesApi.md#get_dfs_rootfs_samples) | **GET** /dfs-rootfses/{dfs_rootfs_id}/samples | 
[**list_dfs_rootfses**](DfsRootfsesApi.md#list_dfs_rootfses) | **GET** /dfs-rootfses/ | 
[**set_dfs_worm_log_path**](DfsRootfsesApi.md#set_dfs_worm_log_path) | **PATCH** /dfs-rootfses/{dfs_rootfs_id}:set-worm-log-path | 
[**update_dfs_rootfs_active_pool**](DfsRootfsesApi.md#update_dfs_rootfs_active_pool) | **PATCH** /dfs-rootfses/{dfs_rootfs_id}:update-active-pools | 


# **create_dfs_rootfs**
> DfsRootfsResp create_dfs_rootfs(body)



Create dfs rootfs

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
api_instance = xms_client.DfsRootfsesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsRootfsCreateReq() # DfsRootfsCreateReq | rootfs info

try:
    api_response = api_instance.create_dfs_rootfs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsRootfsesApi->create_dfs_rootfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsRootfsCreateReq**](DfsRootfsCreateReq.md)| rootfs info | 

### Return type

[**DfsRootfsResp**](DfsRootfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_rootfs**
> DfsRootfsResp delete_dfs_rootfs(dfs_rootfs_id, force=force)



delete dfs rootfs

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
api_instance = xms_client.DfsRootfsesApi(xms_client.ApiClient(configuration))
dfs_rootfs_id = 789 # int | rootfs id
force = true # bool | force delete (optional)

try:
    api_response = api_instance.delete_dfs_rootfs(dfs_rootfs_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsRootfsesApi->delete_dfs_rootfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_rootfs_id** | **int**| rootfs id | 
 **force** | **bool**| force delete | [optional] 

### Return type

[**DfsRootfsResp**](DfsRootfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_rootfs**
> DfsRootfsResp get_dfs_rootfs(dfs_rootfs_id)



Get dfs rootfs

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
api_instance = xms_client.DfsRootfsesApi(xms_client.ApiClient(configuration))
dfs_rootfs_id = 789 # int | rootfs id

try:
    api_response = api_instance.get_dfs_rootfs(dfs_rootfs_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsRootfsesApi->get_dfs_rootfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_rootfs_id** | **int**| rootfs id | 

### Return type

[**DfsRootfsResp**](DfsRootfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_rootfs_samples**
> DfsRootfsSamplesResp get_dfs_rootfs_samples(dfs_rootfs_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a dfs rootfs's samples

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
api_instance = xms_client.DfsRootfsesApi(xms_client.ApiClient(configuration))
dfs_rootfs_id = 789 # int | dfs rootfs id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_dfs_rootfs_samples(dfs_rootfs_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsRootfsesApi->get_dfs_rootfs_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_rootfs_id** | **int**| dfs rootfs id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**DfsRootfsSamplesResp**](DfsRootfsSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_rootfses**
> DfsRootfsesResp list_dfs_rootfses(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, pool_id=pool_id, fs_user_id=fs_user_id, fs_user_group_id=fs_user_group_id, fs_client_id=fs_client_id, fs_client_group_id=fs_client_group_id)



List dfs rootfses

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
api_instance = xms_client.DfsRootfsesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
pool_id = 789 # int | pool id (optional)
fs_user_id = 789 # int | fs user id (optional)
fs_user_group_id = 789 # int | fs user group id (optional)
fs_client_id = 789 # int | fs client id (optional)
fs_client_group_id = 789 # int | fs client group id (optional)

try:
    api_response = api_instance.list_dfs_rootfses(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, pool_id=pool_id, fs_user_id=fs_user_id, fs_user_group_id=fs_user_group_id, fs_client_id=fs_client_id, fs_client_group_id=fs_client_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsRootfsesApi->list_dfs_rootfses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **pool_id** | **int**| pool id | [optional] 
 **fs_user_id** | **int**| fs user id | [optional] 
 **fs_user_group_id** | **int**| fs user group id | [optional] 
 **fs_client_id** | **int**| fs client id | [optional] 
 **fs_client_group_id** | **int**| fs client group id | [optional] 

### Return type

[**DfsRootfsesResp**](DfsRootfsesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_dfs_worm_log_path**
> DfsRootfsResp set_dfs_worm_log_path(dfs_rootfs_id, body, allow_path_create=allow_path_create)



Set dfs worm log path

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
api_instance = xms_client.DfsRootfsesApi(xms_client.ApiClient(configuration))
dfs_rootfs_id = 789 # int | rootfs id
body = xms_client.DfsRootfsSetWormLogPathReq() # DfsRootfsSetWormLogPathReq | worm log path
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.set_dfs_worm_log_path(dfs_rootfs_id, body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsRootfsesApi->set_dfs_worm_log_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_rootfs_id** | **int**| rootfs id | 
 **body** | [**DfsRootfsSetWormLogPathReq**](DfsRootfsSetWormLogPathReq.md)| worm log path | 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DfsRootfsResp**](DfsRootfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_rootfs_active_pool**
> DfsRootfsResp update_dfs_rootfs_active_pool(dfs_rootfs_id, body)



Update dfs rootfs active pools

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
api_instance = xms_client.DfsRootfsesApi(xms_client.ApiClient(configuration))
dfs_rootfs_id = 789 # int | rootfs id
body = xms_client.DfsRootfsUpdateActivePoolReq() # DfsRootfsUpdateActivePoolReq | active pool ids

try:
    api_response = api_instance.update_dfs_rootfs_active_pool(dfs_rootfs_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsRootfsesApi->update_dfs_rootfs_active_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_rootfs_id** | **int**| rootfs id | 
 **body** | [**DfsRootfsUpdateActivePoolReq**](DfsRootfsUpdateActivePoolReq.md)| active pool ids | 

### Return type

[**DfsRootfsResp**](DfsRootfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

