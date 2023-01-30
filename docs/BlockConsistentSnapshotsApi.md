# xms_client.BlockConsistentSnapshotsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_block_consistent_snapshot**](BlockConsistentSnapshotsApi.md#create_block_consistent_snapshot) | **POST** /block-consistent-snapshots/ | 
[**delete_block_consistent_snapshot**](BlockConsistentSnapshotsApi.md#delete_block_consistent_snapshot) | **DELETE** /block-consistent-snapshots/{consistent_snapshot_id} | 
[**get_block_consistent_snapshot**](BlockConsistentSnapshotsApi.md#get_block_consistent_snapshot) | **GET** /block-consistent-snapshots/{block_consistent_snapshot_id} | 
[**list_block_consistent_snapshots**](BlockConsistentSnapshotsApi.md#list_block_consistent_snapshots) | **GET** /block-consistent-snapshots/ | 


# **create_block_consistent_snapshot**
> ConsistentSnapshotResp create_block_consistent_snapshot(body)



Create block consistent snapshot

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
api_instance = xms_client.BlockConsistentSnapshotsApi(xms_client.ApiClient(configuration))
body = xms_client.ConsistentSnapshotCreateReq() # ConsistentSnapshotCreateReq | consistent snapshot info

try:
    api_response = api_instance.create_block_consistent_snapshot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockConsistentSnapshotsApi->create_block_consistent_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConsistentSnapshotCreateReq**](ConsistentSnapshotCreateReq.md)| consistent snapshot info | 

### Return type

[**ConsistentSnapshotResp**](ConsistentSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_block_consistent_snapshot**
> SnapshotResp delete_block_consistent_snapshot(consistent_snapshot_id)



Delete block consistent snapshot

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
api_instance = xms_client.BlockConsistentSnapshotsApi(xms_client.ApiClient(configuration))
consistent_snapshot_id = 789 # int | consistent snapshot id

try:
    api_response = api_instance.delete_block_consistent_snapshot(consistent_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockConsistentSnapshotsApi->delete_block_consistent_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consistent_snapshot_id** | **int**| consistent snapshot id | 

### Return type

[**SnapshotResp**](SnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_consistent_snapshot**
> SnapshotResp get_block_consistent_snapshot(block_consistent_snapshot_id)



get block consistent snapshot

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
api_instance = xms_client.BlockConsistentSnapshotsApi(xms_client.ApiClient(configuration))
block_consistent_snapshot_id = 789 # int | the block consistent snapshot id

try:
    api_response = api_instance.get_block_consistent_snapshot(block_consistent_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockConsistentSnapshotsApi->get_block_consistent_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_consistent_snapshot_id** | **int**| the block consistent snapshot id | 

### Return type

[**SnapshotResp**](SnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_block_consistent_snapshots**
> ConsistentSnapshotsResp list_block_consistent_snapshots(limit=limit, offset=offset, q=q, sort=sort)



List block consistent snapshots

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
api_instance = xms_client.BlockConsistentSnapshotsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_block_consistent_snapshots(limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockConsistentSnapshotsApi->list_block_consistent_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**ConsistentSnapshotsResp**](ConsistentSnapshotsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

