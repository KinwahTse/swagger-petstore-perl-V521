# xms_client.BlockSnapshotsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_block_snapshot**](BlockSnapshotsApi.md#create_block_snapshot) | **POST** /block-snapshots/ | 
[**delete_block_snapshot**](BlockSnapshotsApi.md#delete_block_snapshot) | **DELETE** /block-snapshots/{snapshot_id} | 
[**get_block_snapshot**](BlockSnapshotsApi.md#get_block_snapshot) | **GET** /block-snapshots/{block_snapshot_id} | 
[**list_block_snapshots**](BlockSnapshotsApi.md#list_block_snapshots) | **GET** /block-snapshots/ | 
[**update_snapshot**](BlockSnapshotsApi.md#update_snapshot) | **PATCH** /block-snapshots/{snapshot_id} | 


# **create_block_snapshot**
> SnapshotResp create_block_snapshot(body)



Create block snapshot

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
api_instance = xms_client.BlockSnapshotsApi(xms_client.ApiClient(configuration))
body = xms_client.SnapshotCreateReq() # SnapshotCreateReq | snapshot info

try:
    api_response = api_instance.create_block_snapshot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockSnapshotsApi->create_block_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnapshotCreateReq**](SnapshotCreateReq.md)| snapshot info | 

### Return type

[**SnapshotResp**](SnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_block_snapshot**
> SnapshotResp delete_block_snapshot(snapshot_id)



Delete block snapshot

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
api_instance = xms_client.BlockSnapshotsApi(xms_client.ApiClient(configuration))
snapshot_id = 789 # int | snapshot id

try:
    api_response = api_instance.delete_block_snapshot(snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockSnapshotsApi->delete_block_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **int**| snapshot id | 

### Return type

[**SnapshotResp**](SnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_snapshot**
> SnapshotResp get_block_snapshot(block_snapshot_id)



get block snapshot

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
api_instance = xms_client.BlockSnapshotsApi(xms_client.ApiClient(configuration))
block_snapshot_id = 789 # int | the block snapshot id

try:
    api_response = api_instance.get_block_snapshot(block_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockSnapshotsApi->get_block_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_snapshot_id** | **int**| the block snapshot id | 

### Return type

[**SnapshotResp**](SnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_block_snapshots**
> SnapshotsResp list_block_snapshots(limit=limit, offset=offset, cluster_id=cluster_id, pool_id=pool_id, uid=uid, block_volume_id=block_volume_id, consistent_snapshot_id=consistent_snapshot_id, reserved=reserved, q=q, sort=sort, all=all)



List block snapshots

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
api_instance = xms_client.BlockSnapshotsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
pool_id = 789 # int | pool id (optional)
uid = 'uid_example' # str | snapshot uid (optional)
block_volume_id = 789 # int | volume id (optional)
consistent_snapshot_id = 789 # int | consistent snapshot id (optional)
reserved = true # bool | show reserved snapshot or not, default not (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
all = true # bool | show all snapshots (optional)

try:
    api_response = api_instance.list_block_snapshots(limit=limit, offset=offset, cluster_id=cluster_id, pool_id=pool_id, uid=uid, block_volume_id=block_volume_id, consistent_snapshot_id=consistent_snapshot_id, reserved=reserved, q=q, sort=sort, all=all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockSnapshotsApi->list_block_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **pool_id** | **int**| pool id | [optional] 
 **uid** | **str**| snapshot uid | [optional] 
 **block_volume_id** | **int**| volume id | [optional] 
 **consistent_snapshot_id** | **int**| consistent snapshot id | [optional] 
 **reserved** | **bool**| show reserved snapshot or not, default not | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **all** | **bool**| show all snapshots | [optional] 

### Return type

[**SnapshotsResp**](SnapshotsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot**
> SnapshotResp update_snapshot(snapshot_id, body)



Update block snapshot info

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
api_instance = xms_client.BlockSnapshotsApi(xms_client.ApiClient(configuration))
snapshot_id = 789 # int | snapshot id
body = xms_client.SnapshotUpdateReq() # SnapshotUpdateReq | snapshot info

try:
    api_response = api_instance.update_snapshot(snapshot_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockSnapshotsApi->update_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **int**| snapshot id | 
 **body** | [**SnapshotUpdateReq**](SnapshotUpdateReq.md)| snapshot info | 

### Return type

[**SnapshotResp**](SnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

