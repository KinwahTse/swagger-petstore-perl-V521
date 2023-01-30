# xms_client.DfsTrashesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_dfs_trash**](DfsTrashesApi.md#close_dfs_trash) | **DELETE** /dfs-trashes/{dfs_trash_id} | 
[**empty_dfs_trash**](DfsTrashesApi.md#empty_dfs_trash) | **POST** /dfs-trashes/{dfs_trash_id}:empty | 
[**get_dfs_trash**](DfsTrashesApi.md#get_dfs_trash) | **GET** /dfs-trashes/{dfs_trash_id} | 
[**list_dfs_trash_file_jobs**](DfsTrashesApi.md#list_dfs_trash_file_jobs) | **GET** /dfs-trashes/:list_trash_file_jobs | 
[**list_dfs_trash_files**](DfsTrashesApi.md#list_dfs_trash_files) | **GET** /dfs-trashes/{dfs_trash_id}:list_trash_files | 
[**list_dfs_trash_files_0**](DfsTrashesApi.md#list_dfs_trash_files_0) | **POST** /dfs-trashes/{dfs_trash_id}:list_trash_files | 
[**list_dfs_trashes**](DfsTrashesApi.md#list_dfs_trashes) | **GET** /dfs-trashes/ | 
[**open_dfs_trash**](DfsTrashesApi.md#open_dfs_trash) | **POST** /dfs-trashes/ | 
[**remove_dfs_trash_file**](DfsTrashesApi.md#remove_dfs_trash_file) | **POST** /dfs-trashes/{dfs_trash_id}:remove-file | 
[**restore_dfs_trash_file**](DfsTrashesApi.md#restore_dfs_trash_file) | **POST** /dfs-trashes/{dfs_trash_id}:restore-file | 
[**search_dfs_trash_files**](DfsTrashesApi.md#search_dfs_trash_files) | **GET** /dfs-trashes/{dfs_trash_id}:search_trash_files | 
[**search_dfs_trash_files_0**](DfsTrashesApi.md#search_dfs_trash_files_0) | **POST** /dfs-trashes/{dfs_trash_id}:search_trash_files | 
[**update_dfs_trash**](DfsTrashesApi.md#update_dfs_trash) | **PATCH** /dfs-trashes/{dfs_trash_id} | 


# **close_dfs_trash**
> DfsTrashResp close_dfs_trash(dfs_trash_id)



Close dfs trash

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
dfs_trash_id = 789 # int | trash id

try:
    api_response = api_instance.close_dfs_trash(dfs_trash_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->close_dfs_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_trash_id** | **int**| trash id | 

### Return type

[**DfsTrashResp**](DfsTrashResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **empty_dfs_trash**
> DfsTrashResp empty_dfs_trash(dfs_trash_id, force=force)



Empty dfs trash

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
dfs_trash_id = 789 # int | trash id
force = true # bool | force empty (optional)

try:
    api_response = api_instance.empty_dfs_trash(dfs_trash_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->empty_dfs_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_trash_id** | **int**| trash id | 
 **force** | **bool**| force empty | [optional] 

### Return type

[**DfsTrashResp**](DfsTrashResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_trash**
> DfsTrashResp get_dfs_trash(dfs_trash_id)



Get dfs trash

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
dfs_trash_id = 789 # int | trash id

try:
    api_response = api_instance.get_dfs_trash(dfs_trash_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->get_dfs_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_trash_id** | **int**| trash id | 

### Return type

[**DfsTrashResp**](DfsTrashResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_trash_file_jobs**
> DfsTrashFileJobResp list_dfs_trash_file_jobs(limit=limit, offset=offset, cluster_id=cluster_id, dfs_trash_id=dfs_trash_id, path=path, action=action)



List dfs trash file job

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
dfs_trash_id = 'dfs_trash_id_example' # str | trash id (optional)
path = 'path_example' # str | path (optional)
action = 'action_example' # str | action (optional)

try:
    api_response = api_instance.list_dfs_trash_file_jobs(limit=limit, offset=offset, cluster_id=cluster_id, dfs_trash_id=dfs_trash_id, path=path, action=action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->list_dfs_trash_file_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **dfs_trash_id** | **str**| trash id | [optional] 
 **path** | **str**| path | [optional] 
 **action** | **str**| action | [optional] 

### Return type

[**DfsTrashFileJobResp**](DfsTrashFileJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_trash_files**
> DfsTrashFilesResp list_dfs_trash_files(dfs_trash_id, limit=limit, path=path, start=start, prefix=prefix)



List dfs trash files

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
dfs_trash_id = 789 # int | trash id
limit = 789 # int | paging param (optional)
path = 'path_example' # str | parent path (optional)
start = 'start_example' # str | start file for list (optional)
prefix = 'prefix_example' # str | prefix to filter file or directory (optional)

try:
    api_response = api_instance.list_dfs_trash_files(dfs_trash_id, limit=limit, path=path, start=start, prefix=prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->list_dfs_trash_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_trash_id** | **int**| trash id | 
 **limit** | **int**| paging param | [optional] 
 **path** | **str**| parent path | [optional] 
 **start** | **str**| start file for list | [optional] 
 **prefix** | **str**| prefix to filter file or directory | [optional] 

### Return type

[**DfsTrashFilesResp**](DfsTrashFilesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_trash_files_0**
> DfsTrashFilesResp list_dfs_trash_files_0(dfs_trash_id, limit=limit, path=path, start=start, prefix=prefix)



List dfs trash files

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
dfs_trash_id = 789 # int | trash id
limit = 789 # int | paging param (optional)
path = 'path_example' # str | parent path (optional)
start = 'start_example' # str | start file for list (optional)
prefix = 'prefix_example' # str | prefix to filter file or directory (optional)

try:
    api_response = api_instance.list_dfs_trash_files_0(dfs_trash_id, limit=limit, path=path, start=start, prefix=prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->list_dfs_trash_files_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_trash_id** | **int**| trash id | 
 **limit** | **int**| paging param | [optional] 
 **path** | **str**| parent path | [optional] 
 **start** | **str**| start file for list | [optional] 
 **prefix** | **str**| prefix to filter file or directory | [optional] 

### Return type

[**DfsTrashFilesResp**](DfsTrashFilesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_trashes**
> DfsTrashesResp list_dfs_trashes(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, status=status)



List dfs trashes

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
status = 'status_example' # str | status (optional)

try:
    api_response = api_instance.list_dfs_trashes(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->list_dfs_trashes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **status** | **str**| status | [optional] 

### Return type

[**DfsTrashesResp**](DfsTrashesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_dfs_trash**
> DfsTrashResp open_dfs_trash(body, allow_path_create=allow_path_create)



Create dfs trash

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsTrashOpenReq() # DfsTrashOpenReq | trash info
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.open_dfs_trash(body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->open_dfs_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsTrashOpenReq**](DfsTrashOpenReq.md)| trash info | 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DfsTrashResp**](DfsTrashResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dfs_trash_file**
> DfsTrashFileJobResp remove_dfs_trash_file(dfs_trash_id, body)



Remove dfs trash file

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
dfs_trash_id = 789 # int | trash id
body = xms_client.DfsTrashRemoveFileReq() # DfsTrashRemoveFileReq | trash info

try:
    api_response = api_instance.remove_dfs_trash_file(dfs_trash_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->remove_dfs_trash_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_trash_id** | **int**| trash id | 
 **body** | [**DfsTrashRemoveFileReq**](DfsTrashRemoveFileReq.md)| trash info | 

### Return type

[**DfsTrashFileJobResp**](DfsTrashFileJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_dfs_trash_file**
> DfsTrashFileJobResp restore_dfs_trash_file(dfs_trash_id, body, force=force)



Restore dfs trash file

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
dfs_trash_id = 789 # int | trash id
body = xms_client.DfsTrashRestoreFileReq() # DfsTrashRestoreFileReq | trash info
force = true # bool | force restore (optional)

try:
    api_response = api_instance.restore_dfs_trash_file(dfs_trash_id, body, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->restore_dfs_trash_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_trash_id** | **int**| trash id | 
 **body** | [**DfsTrashRestoreFileReq**](DfsTrashRestoreFileReq.md)| trash info | 
 **force** | **bool**| force restore | [optional] 

### Return type

[**DfsTrashFileJobResp**](DfsTrashFileJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dfs_trash_files**
> DfsTrashFilesResp search_dfs_trash_files(dfs_trash_id, limit=limit, path=path, start=start, prefix=prefix)



Search dfs trash files

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
dfs_trash_id = 789 # int | trash id
limit = 789 # int | paging param (optional)
path = 'path_example' # str | subdirectory of trash path (optional)
start = 'start_example' # str | start file for list (optional)
prefix = 'prefix_example' # str | prefix to filter file or directory (optional)

try:
    api_response = api_instance.search_dfs_trash_files(dfs_trash_id, limit=limit, path=path, start=start, prefix=prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->search_dfs_trash_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_trash_id** | **int**| trash id | 
 **limit** | **int**| paging param | [optional] 
 **path** | **str**| subdirectory of trash path | [optional] 
 **start** | **str**| start file for list | [optional] 
 **prefix** | **str**| prefix to filter file or directory | [optional] 

### Return type

[**DfsTrashFilesResp**](DfsTrashFilesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dfs_trash_files_0**
> DfsTrashFilesResp search_dfs_trash_files_0(dfs_trash_id, limit=limit, path=path, start=start, prefix=prefix)



Search dfs trash files

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
dfs_trash_id = 789 # int | trash id
limit = 789 # int | paging param (optional)
path = 'path_example' # str | subdirectory of trash path (optional)
start = 'start_example' # str | start file for list (optional)
prefix = 'prefix_example' # str | prefix to filter file or directory (optional)

try:
    api_response = api_instance.search_dfs_trash_files_0(dfs_trash_id, limit=limit, path=path, start=start, prefix=prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->search_dfs_trash_files_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_trash_id** | **int**| trash id | 
 **limit** | **int**| paging param | [optional] 
 **path** | **str**| subdirectory of trash path | [optional] 
 **start** | **str**| start file for list | [optional] 
 **prefix** | **str**| prefix to filter file or directory | [optional] 

### Return type

[**DfsTrashFilesResp**](DfsTrashFilesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_trash**
> DfsTrashResp update_dfs_trash(dfs_trash_id, body)



Update dfs trash

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
api_instance = xms_client.DfsTrashesApi(xms_client.ApiClient(configuration))
dfs_trash_id = 789 # int | trash id
body = xms_client.DfsTrashUpdateReq() # DfsTrashUpdateReq | trash info

try:
    api_response = api_instance.update_dfs_trash(dfs_trash_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTrashesApi->update_dfs_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_trash_id** | **int**| trash id | 
 **body** | [**DfsTrashUpdateReq**](DfsTrashUpdateReq.md)| trash info | 

### Return type

[**DfsTrashResp**](DfsTrashResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

