# xms_client.BlockVolumeGroupSnapshotsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_block_volume_group_snapshot**](BlockVolumeGroupSnapshotsApi.md#create_block_volume_group_snapshot) | **POST** /block-volume-group-snapshots/ | 
[**delete_block_volume_group_snapshot**](BlockVolumeGroupSnapshotsApi.md#delete_block_volume_group_snapshot) | **DELETE** /block-volume-group-snapshots/{block_volume_group_snapshot_id} | 
[**get_block_volume_group_snapshot**](BlockVolumeGroupSnapshotsApi.md#get_block_volume_group_snapshot) | **GET** /block-volume-group-snapshots/{block_volume_group_snapshot_id} | 
[**list_block_volume_group_snapshots**](BlockVolumeGroupSnapshotsApi.md#list_block_volume_group_snapshots) | **GET** /block-volume-group-snapshots/ | 
[**update_block_volume_group_snapshot**](BlockVolumeGroupSnapshotsApi.md#update_block_volume_group_snapshot) | **PATCH** /block-volume-group-snapshots/{block_volume_group_snapshot_id} | 


# **create_block_volume_group_snapshot**
> VolumeGroupSnapshotResp create_block_volume_group_snapshot(body, cluster_id=cluster_id)



Create block volume group snapshot

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
api_instance = xms_client.BlockVolumeGroupSnapshotsApi(xms_client.ApiClient(configuration))
body = xms_client.VolumeGroupSnapshotCreateReq() # VolumeGroupSnapshotCreateReq | volume group snapshot info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_block_volume_group_snapshot(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupSnapshotsApi->create_block_volume_group_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VolumeGroupSnapshotCreateReq**](VolumeGroupSnapshotCreateReq.md)| volume group snapshot info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**VolumeGroupSnapshotResp**](VolumeGroupSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_block_volume_group_snapshot**
> VolumeGroupSnapshotResp delete_block_volume_group_snapshot(block_volume_group_snapshot_id)



Delete a block volume group snapshot

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
api_instance = xms_client.BlockVolumeGroupSnapshotsApi(xms_client.ApiClient(configuration))
block_volume_group_snapshot_id = 789 # int | block volume group snapshot id

try:
    api_response = api_instance.delete_block_volume_group_snapshot(block_volume_group_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupSnapshotsApi->delete_block_volume_group_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_group_snapshot_id** | **int**| block volume group snapshot id | 

### Return type

[**VolumeGroupSnapshotResp**](VolumeGroupSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_volume_group_snapshot**
> VolumeGroupSnapshotResp get_block_volume_group_snapshot(block_volume_group_snapshot_id)



get block volume group snapshot

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
api_instance = xms_client.BlockVolumeGroupSnapshotsApi(xms_client.ApiClient(configuration))
block_volume_group_snapshot_id = 789 # int | the block volume group snapshot id

try:
    api_response = api_instance.get_block_volume_group_snapshot(block_volume_group_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupSnapshotsApi->get_block_volume_group_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_group_snapshot_id** | **int**| the block volume group snapshot id | 

### Return type

[**VolumeGroupSnapshotResp**](VolumeGroupSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_block_volume_group_snapshots**
> VolumeGroupSnapshotsResp list_block_volume_group_snapshots(cluster_id=cluster_id, block_volume_group_id=block_volume_group_id, name=name, passive=passive, limit=limit, offset=offset, q=q, sort=sort)



List block volume group snapshots

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
api_instance = xms_client.BlockVolumeGroupSnapshotsApi(xms_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | cluster id (optional)
block_volume_group_id = 789 # int | related volume group id (optional)
name = 'name_example' # str | name of volume group snapshot (optional)
passive = true # bool | passive or not (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_block_volume_group_snapshots(cluster_id=cluster_id, block_volume_group_id=block_volume_group_id, name=name, passive=passive, limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupSnapshotsApi->list_block_volume_group_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| cluster id | [optional] 
 **block_volume_group_id** | **int**| related volume group id | [optional] 
 **name** | **str**| name of volume group snapshot | [optional] 
 **passive** | **bool**| passive or not | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**VolumeGroupSnapshotsResp**](VolumeGroupSnapshotsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_block_volume_group_snapshot**
> VolumeGroupSnapshotResp update_block_volume_group_snapshot(block_volume_group_snapshot_id, body)



Update block volume group snapshot

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
api_instance = xms_client.BlockVolumeGroupSnapshotsApi(xms_client.ApiClient(configuration))
block_volume_group_snapshot_id = 789 # int | the block volume group snapshot id
body = xms_client.VolumeGroupSnapshotUpdateReq() # VolumeGroupSnapshotUpdateReq | volume group snapshot info

try:
    api_response = api_instance.update_block_volume_group_snapshot(block_volume_group_snapshot_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupSnapshotsApi->update_block_volume_group_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_group_snapshot_id** | **int**| the block volume group snapshot id | 
 **body** | [**VolumeGroupSnapshotUpdateReq**](VolumeGroupSnapshotUpdateReq.md)| volume group snapshot info | 

### Return type

[**VolumeGroupSnapshotResp**](VolumeGroupSnapshotResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

