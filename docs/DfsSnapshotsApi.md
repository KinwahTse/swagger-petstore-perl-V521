# xms_client.DfsSnapshotsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dfs_snapshot**](DfsSnapshotsApi.md#create_dfs_snapshot) | **POST** /dfs-snapshots/ | 
[**delete_dfs_snapshot**](DfsSnapshotsApi.md#delete_dfs_snapshot) | **DELETE** /dfs-snapshots/{dfs_snapshot_id} | 
[**get_dfs_snapshot**](DfsSnapshotsApi.md#get_dfs_snapshot) | **GET** /dfs-snapshots/{dfs_snapshot_id} | 
[**get_dfs_snapshots_over_view_page**](DfsSnapshotsApi.md#get_dfs_snapshots_over_view_page) | **GET** /dfs-snapshots/overview | 
[**list_dfs_snapshots**](DfsSnapshotsApi.md#list_dfs_snapshots) | **GET** /dfs-snapshots/ | 
[**rollback_dfs_snapshot**](DfsSnapshotsApi.md#rollback_dfs_snapshot) | **POST** /dfs-snapshots/{dfs_snapshot_id}:rollback | 
[**update_dfs_snapshot**](DfsSnapshotsApi.md#update_dfs_snapshot) | **PATCH** /dfs-snapshots/{dfs_snapshot_id} | 


# **create_dfs_snapshot**
> DfsSnapshotResp create_dfs_snapshot(body, allow_path_create=allow_path_create)



Create dfs snapshot

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
api_instance = xms_client.DfsSnapshotsApi(xms_client.ApiClient(configuration))
body = xms_client.DfsSnapshotCreateReq() # DfsSnapshotCreateReq | dfs snapshot info
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.create_dfs_snapshot(body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSnapshotsApi->create_dfs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsSnapshotCreateReq**](DfsSnapshotCreateReq.md)| dfs snapshot info | 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DfsSnapshotResp**](DfsSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_snapshot**
> DfsSnapshotResp delete_dfs_snapshot(dfs_snapshot_id)



Delete a dfs snapshot

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
api_instance = xms_client.DfsSnapshotsApi(xms_client.ApiClient(configuration))
dfs_snapshot_id = 789 # int | dfs snapshot id

try:
    api_response = api_instance.delete_dfs_snapshot(dfs_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSnapshotsApi->delete_dfs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_snapshot_id** | **int**| dfs snapshot id | 

### Return type

[**DfsSnapshotResp**](DfsSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_snapshot**
> DfsSnapshotResp get_dfs_snapshot(dfs_snapshot_id)



get dfs snapshot

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
api_instance = xms_client.DfsSnapshotsApi(xms_client.ApiClient(configuration))
dfs_snapshot_id = 789 # int | the dfs snapshot id

try:
    api_response = api_instance.get_dfs_snapshot(dfs_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSnapshotsApi->get_dfs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_snapshot_id** | **int**| the dfs snapshot id | 

### Return type

[**DfsSnapshotResp**](DfsSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_snapshots_over_view_page**
> DfsSnapShotsOverviewPageResp get_dfs_snapshots_over_view_page()



get dfs snapshots overview page

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
api_instance = xms_client.DfsSnapshotsApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.get_dfs_snapshots_over_view_page()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSnapshotsApi->get_dfs_snapshots_over_view_page: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DfsSnapShotsOverviewPageResp**](DfsSnapShotsOverviewPageResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_snapshots**
> DfsSnapshotsResp list_dfs_snapshots(cluster_id=cluster_id, dfs_path_id=dfs_path_id, dp_dfs_snapshot_id=dp_dfs_snapshot_id, path=path, name=name, limit=limit, offset=offset, q=q, sort=sort)



List dfs snapshots

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
api_instance = xms_client.DfsSnapshotsApi(xms_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | cluster id (optional)
dfs_path_id = 789 # int | related dfs path id (optional)
dp_dfs_snapshot_id = 789 # int | dp dfs snapshot id (optional)
path = 'path_example' # str | related dfs path (optional)
name = 'name_example' # str | name of dfs snapshot (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dfs_snapshots(cluster_id=cluster_id, dfs_path_id=dfs_path_id, dp_dfs_snapshot_id=dp_dfs_snapshot_id, path=path, name=name, limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSnapshotsApi->list_dfs_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| cluster id | [optional] 
 **dfs_path_id** | **int**| related dfs path id | [optional] 
 **dp_dfs_snapshot_id** | **int**| dp dfs snapshot id | [optional] 
 **path** | **str**| related dfs path | [optional] 
 **name** | **str**| name of dfs snapshot | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DfsSnapshotsResp**](DfsSnapshotsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_dfs_snapshot**
> DfsSnapshotResp rollback_dfs_snapshot(dfs_snapshot_id, body)



Rollback dfs snapshot

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
api_instance = xms_client.DfsSnapshotsApi(xms_client.ApiClient(configuration))
dfs_snapshot_id = 789 # int | dfs snapshot id
body = xms_client.DfsSnapshotRollbackReq() # DfsSnapshotRollbackReq | snapshot rollback info

try:
    api_response = api_instance.rollback_dfs_snapshot(dfs_snapshot_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSnapshotsApi->rollback_dfs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_snapshot_id** | **int**| dfs snapshot id | 
 **body** | [**DfsSnapshotRollbackReq**](DfsSnapshotRollbackReq.md)| snapshot rollback info | 

### Return type

[**DfsSnapshotResp**](DfsSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_snapshot**
> DfsSnapshotResp update_dfs_snapshot(dfs_snapshot_id, body)



Update dfs snapshot

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
api_instance = xms_client.DfsSnapshotsApi(xms_client.ApiClient(configuration))
dfs_snapshot_id = 789 # int | dfs snapshot id
body = xms_client.DfsSnapshotUpdateReq() # DfsSnapshotUpdateReq | dfs snapshot info

try:
    api_response = api_instance.update_dfs_snapshot(dfs_snapshot_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSnapshotsApi->update_dfs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_snapshot_id** | **int**| dfs snapshot id | 
 **body** | [**DfsSnapshotUpdateReq**](DfsSnapshotUpdateReq.md)| dfs snapshot info | 

### Return type

[**DfsSnapshotResp**](DfsSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

