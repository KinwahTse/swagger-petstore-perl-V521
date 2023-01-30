# xms_client.FsSnapshotsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fs_snapshot**](FsSnapshotsApi.md#create_fs_snapshot) | **POST** /fs-snapshots/ | 
[**delete_fs_snapshot**](FsSnapshotsApi.md#delete_fs_snapshot) | **DELETE** /fs-snapshots/{fs_snapshot_id} | 
[**get_fs_snapshot**](FsSnapshotsApi.md#get_fs_snapshot) | **GET** /fs-snapshots/{fs_snapshot_id} | 
[**list_fs_snapshots**](FsSnapshotsApi.md#list_fs_snapshots) | **GET** /fs-snapshots/ | 
[**update_fs_snapshot**](FsSnapshotsApi.md#update_fs_snapshot) | **PATCH** /fs-snapshots/{fs_snapshot_id} | 


# **create_fs_snapshot**
> FSSnapshotResp create_fs_snapshot(body)



Create file storage snapshot

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
api_instance = xms_client.FsSnapshotsApi(xms_client.ApiClient(configuration))
body = xms_client.FSSnapshotCreateReq() # FSSnapshotCreateReq | snapshot info

try:
    api_response = api_instance.create_fs_snapshot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSnapshotsApi->create_fs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSSnapshotCreateReq**](FSSnapshotCreateReq.md)| snapshot info | 

### Return type

[**FSSnapshotResp**](FSSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fs_snapshot**
> FSSnapshotResp delete_fs_snapshot(fs_snapshot_id, force=force)



delete file storage snapshot

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
api_instance = xms_client.FsSnapshotsApi(xms_client.ApiClient(configuration))
fs_snapshot_id = 789 # int | snapshot id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_fs_snapshot(fs_snapshot_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSnapshotsApi->delete_fs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_snapshot_id** | **int**| snapshot id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**FSSnapshotResp**](FSSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fs_snapshot**
> FSSnapshotResp get_fs_snapshot(fs_snapshot_id)



Get file storage snapshot

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
api_instance = xms_client.FsSnapshotsApi(xms_client.ApiClient(configuration))
fs_snapshot_id = 789 # int | file storage snapshot id

try:
    api_response = api_instance.get_fs_snapshot(fs_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSnapshotsApi->get_fs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_snapshot_id** | **int**| file storage snapshot id | 

### Return type

[**FSSnapshotResp**](FSSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fs_snapshots**
> FSSnapshotsResp list_fs_snapshots(limit=limit, offset=offset, q=q, cluster_id=cluster_id, sort=sort, fs_folder_id=fs_folder_id)



List file storage snapshots

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
api_instance = xms_client.FsSnapshotsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
sort = 'sort_example' # str | sort param of search (optional)
fs_folder_id = 789 # int | file storage folder id (optional)

try:
    api_response = api_instance.list_fs_snapshots(limit=limit, offset=offset, q=q, cluster_id=cluster_id, sort=sort, fs_folder_id=fs_folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSnapshotsApi->list_fs_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **fs_folder_id** | **int**| file storage folder id | [optional] 

### Return type

[**FSSnapshotsResp**](FSSnapshotsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fs_snapshot**
> FSSnapshotResp update_fs_snapshot(fs_snapshot_id, body)



Update file storage snapshot

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
api_instance = xms_client.FsSnapshotsApi(xms_client.ApiClient(configuration))
fs_snapshot_id = 789 # int | snapshot id
body = xms_client.FSSnapshotUpdateReq() # FSSnapshotUpdateReq | snapshot info

try:
    api_response = api_instance.update_fs_snapshot(fs_snapshot_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSnapshotsApi->update_fs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_snapshot_id** | **int**| snapshot id | 
 **body** | [**FSSnapshotUpdateReq**](FSSnapshotUpdateReq.md)| snapshot info | 

### Return type

[**FSSnapshotResp**](FSSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

