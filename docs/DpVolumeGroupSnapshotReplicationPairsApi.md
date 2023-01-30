# xms_client.DpVolumeGroupSnapshotReplicationPairsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**async_failover_dp_volume_group_snapshot_replication_pair**](DpVolumeGroupSnapshotReplicationPairsApi.md#async_failover_dp_volume_group_snapshot_replication_pair) | **POST** /dp-volume-group-snapshot-replication-pairs/{pair_id}:async-failover | 
[**create_dp_volume_group_snapshot_replication_pair**](DpVolumeGroupSnapshotReplicationPairsApi.md#create_dp_volume_group_snapshot_replication_pair) | **POST** /dp-volume-group-snapshot-replication-pairs/ | 
[**delete_dp_volume_group_snapshot_replication_pair**](DpVolumeGroupSnapshotReplicationPairsApi.md#delete_dp_volume_group_snapshot_replication_pair) | **DELETE** /dp-volume-group-snapshot-replication-pairs/{pair_id} | 
[**get_dp_volume_group_snapshot_replication_pair**](DpVolumeGroupSnapshotReplicationPairsApi.md#get_dp_volume_group_snapshot_replication_pair) | **GET** /dp-volume-group-snapshot-replication-pairs/{pair_id} | 
[**list_dp_volume_group_snapshot_replication_pair**](DpVolumeGroupSnapshotReplicationPairsApi.md#list_dp_volume_group_snapshot_replication_pair) | **GET** /dp-volume-group-snapshot-replication-pairs/ | 
[**pause_dp_volume_group_snapshot_replication_pair**](DpVolumeGroupSnapshotReplicationPairsApi.md#pause_dp_volume_group_snapshot_replication_pair) | **POST** /dp-volume-group-snapshot-replication-pairs/{pair_id}:pause | 
[**resume_dp_volume_group_snapshot_replication_pair**](DpVolumeGroupSnapshotReplicationPairsApi.md#resume_dp_volume_group_snapshot_replication_pair) | **POST** /dp-volume-group-snapshot-replication-pairs/{pair_id}:resume | 
[**update_dp_volume_group_snapshot_replication_pair**](DpVolumeGroupSnapshotReplicationPairsApi.md#update_dp_volume_group_snapshot_replication_pair) | **PATCH** /dp-volume-group-snapshot-replication-pairs/{pair_id} | 


# **async_failover_dp_volume_group_snapshot_replication_pair**
> DpVolumeGroupSnapshotReplicationPairsResp async_failover_dp_volume_group_snapshot_replication_pair(pair_id)



switch the roles of the pair

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.async_failover_dp_volume_group_snapshot_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationPairsApi->async_failover_dp_volume_group_snapshot_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpVolumeGroupSnapshotReplicationPairsResp**](DpVolumeGroupSnapshotReplicationPairsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dp_volume_group_snapshot_replication_pair**
> DpVolumeGroupSnapshotReplicationPairResp create_dp_volume_group_snapshot_replication_pair(body)



Create dp volume group snapshot replication pair

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationPairsApi(xms_client.ApiClient(configuration))
body = xms_client.DpVolumeGroupSnapshotReplicationPairCreateReq() # DpVolumeGroupSnapshotReplicationPairCreateReq | pair info

try:
    api_response = api_instance.create_dp_volume_group_snapshot_replication_pair(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationPairsApi->create_dp_volume_group_snapshot_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpVolumeGroupSnapshotReplicationPairCreateReq**](DpVolumeGroupSnapshotReplicationPairCreateReq.md)| pair info | 

### Return type

[**DpVolumeGroupSnapshotReplicationPairResp**](DpVolumeGroupSnapshotReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_volume_group_snapshot_replication_pair**
> delete_dp_volume_group_snapshot_replication_pair(pair_id, force=force)



Delete dp volume group snapshot replication pair

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id
force = true # bool | force delete volume group pair or not (optional)

try:
    api_instance.delete_dp_volume_group_snapshot_replication_pair(pair_id, force=force)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationPairsApi->delete_dp_volume_group_snapshot_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 
 **force** | **bool**| force delete volume group pair or not | [optional] 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_volume_group_snapshot_replication_pair**
> DpVolumeGroupSnapshotReplicationPairResp get_dp_volume_group_snapshot_replication_pair(pair_id)



Get dp volume group snapshot replication pair

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_volume_group_snapshot_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationPairsApi->get_dp_volume_group_snapshot_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpVolumeGroupSnapshotReplicationPairResp**](DpVolumeGroupSnapshotReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_volume_group_snapshot_replication_pair**
> DpVolumeGroupSnapshotReplicationPairsResp list_dp_volume_group_snapshot_replication_pair(volume_group_id=volume_group_id, dp_volume_group_snapshot_replication_policy_id=dp_volume_group_snapshot_replication_policy_id)



List dp volume group snapshot replication pairs

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationPairsApi(xms_client.ApiClient(configuration))
volume_group_id = 789 # int | related volume group id (optional)
dp_volume_group_snapshot_replication_policy_id = 789 # int | related policy id (optional)

try:
    api_response = api_instance.list_dp_volume_group_snapshot_replication_pair(volume_group_id=volume_group_id, dp_volume_group_snapshot_replication_policy_id=dp_volume_group_snapshot_replication_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationPairsApi->list_dp_volume_group_snapshot_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_group_id** | **int**| related volume group id | [optional] 
 **dp_volume_group_snapshot_replication_policy_id** | **int**| related policy id | [optional] 

### Return type

[**DpVolumeGroupSnapshotReplicationPairsResp**](DpVolumeGroupSnapshotReplicationPairsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_dp_volume_group_snapshot_replication_pair**
> DpVolumeGroupSnapshotReplicationPairsResp pause_dp_volume_group_snapshot_replication_pair(pair_id)



pause periodic sync

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.pause_dp_volume_group_snapshot_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationPairsApi->pause_dp_volume_group_snapshot_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpVolumeGroupSnapshotReplicationPairsResp**](DpVolumeGroupSnapshotReplicationPairsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_dp_volume_group_snapshot_replication_pair**
> DpVolumeGroupSnapshotReplicationPairResp resume_dp_volume_group_snapshot_replication_pair(pair_id)



resume periodic sync

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.resume_dp_volume_group_snapshot_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationPairsApi->resume_dp_volume_group_snapshot_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpVolumeGroupSnapshotReplicationPairResp**](DpVolumeGroupSnapshotReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dp_volume_group_snapshot_replication_pair**
> DpVolumeGroupSnapshotReplicationPairResp update_dp_volume_group_snapshot_replication_pair(pair_id, body)



Update dp volume group snapshot replication pair

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id
body = xms_client.DpVolumeGroupSnapshotReplicationPairUpdateReq() # DpVolumeGroupSnapshotReplicationPairUpdateReq | pair info

try:
    api_response = api_instance.update_dp_volume_group_snapshot_replication_pair(pair_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationPairsApi->update_dp_volume_group_snapshot_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 
 **body** | [**DpVolumeGroupSnapshotReplicationPairUpdateReq**](DpVolumeGroupSnapshotReplicationPairUpdateReq.md)| pair info | 

### Return type

[**DpVolumeGroupSnapshotReplicationPairResp**](DpVolumeGroupSnapshotReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

