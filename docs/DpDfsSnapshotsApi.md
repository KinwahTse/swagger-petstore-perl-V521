# xms_client.DpDfsSnapshotsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dp_dfs_snapshot**](DpDfsSnapshotsApi.md#create_dp_dfs_snapshot) | **POST** /dp-dfs-snapshots/ | 
[**delete_dp_dfs_snapshot**](DpDfsSnapshotsApi.md#delete_dp_dfs_snapshot) | **DELETE** /dp-dfs-snapshots/{dp_dfs_snapshot_id} | 
[**get_dp_dfs_snapshot**](DpDfsSnapshotsApi.md#get_dp_dfs_snapshot) | **GET** /dp-dfs-snapshots/{dp_dfs_snapshot_id} | 
[**list_dp_dfs_snapshots**](DpDfsSnapshotsApi.md#list_dp_dfs_snapshots) | **GET** /dp-dfs-snapshots/ | 
[**list_dp_dfs_snapshots_by_dfs_path_name**](DpDfsSnapshotsApi.md#list_dp_dfs_snapshots_by_dfs_path_name) | **POST** /dp-dfs-snapshots/_search | 


# **create_dp_dfs_snapshot**
> DpDfsSnapshotResp create_dp_dfs_snapshot(body, allow_path_create=allow_path_create)



Create dp dfs snapshot

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
api_instance = xms_client.DpDfsSnapshotsApi(xms_client.ApiClient(configuration))
body = xms_client.DpDfsSnapshotCreateReq() # DpDfsSnapshotCreateReq | dp dfs snapshot info
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.create_dp_dfs_snapshot(body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotsApi->create_dp_dfs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpDfsSnapshotCreateReq**](DpDfsSnapshotCreateReq.md)| dp dfs snapshot info | 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DpDfsSnapshotResp**](DpDfsSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_dfs_snapshot**
> DpDfsSnapshotResp delete_dp_dfs_snapshot(dp_dfs_snapshot_id)



Delete a dp dfs snapshot

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
api_instance = xms_client.DpDfsSnapshotsApi(xms_client.ApiClient(configuration))
dp_dfs_snapshot_id = 789 # int | dp dfs snapshot id

try:
    api_response = api_instance.delete_dp_dfs_snapshot(dp_dfs_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotsApi->delete_dp_dfs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dp_dfs_snapshot_id** | **int**| dp dfs snapshot id | 

### Return type

[**DpDfsSnapshotResp**](DpDfsSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_dfs_snapshot**
> DpDfsSnapshotResp get_dp_dfs_snapshot(dp_dfs_snapshot_id)



get dp dfs snapshot

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
api_instance = xms_client.DpDfsSnapshotsApi(xms_client.ApiClient(configuration))
dp_dfs_snapshot_id = 789 # int | the dp dfs snapshot id

try:
    api_response = api_instance.get_dp_dfs_snapshot(dp_dfs_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotsApi->get_dp_dfs_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dp_dfs_snapshot_id** | **int**| the dp dfs snapshot id | 

### Return type

[**DpDfsSnapshotResp**](DpDfsSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_dfs_snapshots**
> DpDfsSnapshotsResp list_dp_dfs_snapshots(limit=limit, offset=offset, q=q, sort=sort, policy_id=policy_id, path_id=path_id)



List dp dfs snapshots

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
api_instance = xms_client.DpDfsSnapshotsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
policy_id = 789 # int | related dp dfs snapshot policy id (optional)
path_id = 789 # int | related dfs path id (optional)

try:
    api_response = api_instance.list_dp_dfs_snapshots(limit=limit, offset=offset, q=q, sort=sort, policy_id=policy_id, path_id=path_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotsApi->list_dp_dfs_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **policy_id** | **int**| related dp dfs snapshot policy id | [optional] 
 **path_id** | **int**| related dfs path id | [optional] 

### Return type

[**DpDfsSnapshotsResp**](DpDfsSnapshotsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_dfs_snapshots_by_dfs_path_name**
> DpDfsSnapshotsResp list_dp_dfs_snapshots_by_dfs_path_name()



List dp dfs snapshots by name

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
api_instance = xms_client.DpDfsSnapshotsApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.list_dp_dfs_snapshots_by_dfs_path_name()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotsApi->list_dp_dfs_snapshots_by_dfs_path_name: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DpDfsSnapshotsResp**](DpDfsSnapshotsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

