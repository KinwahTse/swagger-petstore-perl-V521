# xms_client.DfsFilesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dfs_file**](DfsFilesApi.md#delete_dfs_file) | **POST** /dfs-files:delete | 
[**get_dfs_log_report**](DfsFilesApi.md#get_dfs_log_report) | **GET** /dfs-files/log-report | 
[**list_dfs_files**](DfsFilesApi.md#list_dfs_files) | **GET** /dfs-files/ | 
[**list_dfs_files_0**](DfsFilesApi.md#list_dfs_files_0) | **POST** /dfs-files/ | 
[**stat_dfs_file**](DfsFilesApi.md#stat_dfs_file) | **GET** /dfs-files/:stat | 
[**stat_dfs_file_0**](DfsFilesApi.md#stat_dfs_file_0) | **POST** /dfs-files/:stat | 


# **delete_dfs_file**
> delete_dfs_file(body)



delete dfs file from rootfs

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
api_instance = xms_client.DfsFilesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsFileDeleteReq() # DfsFileDeleteReq | active pool ids

try:
    api_instance.delete_dfs_file(body)
except ApiException as e:
    print("Exception when calling DfsFilesApi->delete_dfs_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsFileDeleteReq**](DfsFileDeleteReq.md)| active pool ids | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_log_report**
> str get_dfs_log_report(dfs_rootfs_id, paths)



Get report of a gfs log

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
api_instance = xms_client.DfsFilesApi(xms_client.ApiClient(configuration))
dfs_rootfs_id = 789 # int | dfs rootfs id
paths = 'paths_example' # str | dfs log path

try:
    api_response = api_instance.get_dfs_log_report(dfs_rootfs_id, paths)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFilesApi->get_dfs_log_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_rootfs_id** | **int**| dfs rootfs id | 
 **paths** | **str**| dfs log path | 

### Return type

**str**

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_files**
> DfsFilesResp list_dfs_files(rootfs_id=rootfs_id, limit=limit, path=path, start=start, prefix=prefix, type=type, worm=worm, reverse=reverse, page_up=page_up, hidden=hidden)



List dfs files in a directory

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
api_instance = xms_client.DfsFilesApi(xms_client.ApiClient(configuration))
rootfs_id = 789 # int | dfs rootfs id (optional)
limit = 789 # int | paging param (optional)
path = 'path_example' # str | parent path (optional)
start = 'start_example' # str | start file for list (optional)
prefix = 'prefix_example' # str | prefix to filter file or directory (optional)
type = 'type_example' # str | filter by file or dir type (optional)
worm = true # bool | check dir worm before enable filter (optional)
reverse = true # bool | sort reverse (optional)
page_up = true # bool | query last page instead of next (optional)
hidden = true # bool | show hidden files (optional)

try:
    api_response = api_instance.list_dfs_files(rootfs_id=rootfs_id, limit=limit, path=path, start=start, prefix=prefix, type=type, worm=worm, reverse=reverse, page_up=page_up, hidden=hidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFilesApi->list_dfs_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rootfs_id** | **int**| dfs rootfs id | [optional] 
 **limit** | **int**| paging param | [optional] 
 **path** | **str**| parent path | [optional] 
 **start** | **str**| start file for list | [optional] 
 **prefix** | **str**| prefix to filter file or directory | [optional] 
 **type** | **str**| filter by file or dir type | [optional] 
 **worm** | **bool**| check dir worm before enable filter | [optional] 
 **reverse** | **bool**| sort reverse | [optional] 
 **page_up** | **bool**| query last page instead of next | [optional] 
 **hidden** | **bool**| show hidden files | [optional] 

### Return type

[**DfsFilesResp**](DfsFilesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_files_0**
> DfsFilesResp list_dfs_files_0(rootfs_id=rootfs_id, limit=limit, path=path, start=start, prefix=prefix, type=type, worm=worm, reverse=reverse, page_up=page_up, hidden=hidden)



List dfs files in a directory

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
api_instance = xms_client.DfsFilesApi(xms_client.ApiClient(configuration))
rootfs_id = 789 # int | dfs rootfs id (optional)
limit = 789 # int | paging param (optional)
path = 'path_example' # str | parent path (optional)
start = 'start_example' # str | start file for list (optional)
prefix = 'prefix_example' # str | prefix to filter file or directory (optional)
type = 'type_example' # str | filter by file or dir type (optional)
worm = true # bool | check dir worm before enable filter (optional)
reverse = true # bool | sort reverse (optional)
page_up = true # bool | query last page instead of next (optional)
hidden = true # bool | show hidden files (optional)

try:
    api_response = api_instance.list_dfs_files_0(rootfs_id=rootfs_id, limit=limit, path=path, start=start, prefix=prefix, type=type, worm=worm, reverse=reverse, page_up=page_up, hidden=hidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFilesApi->list_dfs_files_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rootfs_id** | **int**| dfs rootfs id | [optional] 
 **limit** | **int**| paging param | [optional] 
 **path** | **str**| parent path | [optional] 
 **start** | **str**| start file for list | [optional] 
 **prefix** | **str**| prefix to filter file or directory | [optional] 
 **type** | **str**| filter by file or dir type | [optional] 
 **worm** | **bool**| check dir worm before enable filter | [optional] 
 **reverse** | **bool**| sort reverse | [optional] 
 **page_up** | **bool**| query last page instead of next | [optional] 
 **hidden** | **bool**| show hidden files | [optional] 

### Return type

[**DfsFilesResp**](DfsFilesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stat_dfs_file**
> DfsFileResp stat_dfs_file(rootfs_id=rootfs_id, path=path)



Get dfs file Stat

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
api_instance = xms_client.DfsFilesApi(xms_client.ApiClient(configuration))
rootfs_id = 789 # int | dfs rootfs id (optional)
path = 'path_example' # str | parent path (optional)

try:
    api_response = api_instance.stat_dfs_file(rootfs_id=rootfs_id, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFilesApi->stat_dfs_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rootfs_id** | **int**| dfs rootfs id | [optional] 
 **path** | **str**| parent path | [optional] 

### Return type

[**DfsFileResp**](DfsFileResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stat_dfs_file_0**
> DfsFileResp stat_dfs_file_0(rootfs_id=rootfs_id, path=path)



Get dfs file Stat

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
api_instance = xms_client.DfsFilesApi(xms_client.ApiClient(configuration))
rootfs_id = 789 # int | dfs rootfs id (optional)
path = 'path_example' # str | parent path (optional)

try:
    api_response = api_instance.stat_dfs_file_0(rootfs_id=rootfs_id, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFilesApi->stat_dfs_file_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rootfs_id** | **int**| dfs rootfs id | [optional] 
 **path** | **str**| parent path | [optional] 

### Return type

[**DfsFileResp**](DfsFileResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

