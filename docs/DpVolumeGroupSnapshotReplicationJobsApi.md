# xms_client.DpVolumeGroupSnapshotReplicationJobsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dp_volume_group_snapshot_replication_job**](DpVolumeGroupSnapshotReplicationJobsApi.md#delete_dp_volume_group_snapshot_replication_job) | **DELETE** /dp-volume-group-snapshot-replication-jobs/{job_id} | 
[**get_dp_volume_group_snapshot_replication_job**](DpVolumeGroupSnapshotReplicationJobsApi.md#get_dp_volume_group_snapshot_replication_job) | **GET** /dp-volume-group-snapshot-replication-jobs/{job_id} | 
[**list_dp_volume_group_snapshot_replication_job**](DpVolumeGroupSnapshotReplicationJobsApi.md#list_dp_volume_group_snapshot_replication_job) | **GET** /dp-volume-group-snapshot-replication-jobs/ | 


# **delete_dp_volume_group_snapshot_replication_job**
> delete_dp_volume_group_snapshot_replication_job(job_id)



Delete dp volume group snapshot replication job

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationJobsApi(xms_client.ApiClient(configuration))
job_id = 789 # int | resource id

try:
    api_instance.delete_dp_volume_group_snapshot_replication_job(job_id)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationJobsApi->delete_dp_volume_group_snapshot_replication_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| resource id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_volume_group_snapshot_replication_job**
> DpVolumeGroupSnapshotReplicationJobResp get_dp_volume_group_snapshot_replication_job(job_id)



Get dp volume group snapshot replication job

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationJobsApi(xms_client.ApiClient(configuration))
job_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_volume_group_snapshot_replication_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationJobsApi->get_dp_volume_group_snapshot_replication_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| resource id | 

### Return type

[**DpVolumeGroupSnapshotReplicationJobResp**](DpVolumeGroupSnapshotReplicationJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_volume_group_snapshot_replication_job**
> DpVolumeGroupSnapshotReplicationJobsResp list_dp_volume_group_snapshot_replication_job(dp_volume_group_snapshot_replication_pair_id=dp_volume_group_snapshot_replication_pair_id)



List dp volume group snapshot replication jobs

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
api_instance = xms_client.DpVolumeGroupSnapshotReplicationJobsApi(xms_client.ApiClient(configuration))
dp_volume_group_snapshot_replication_pair_id = 789 # int | related pair id (optional)

try:
    api_response = api_instance.list_dp_volume_group_snapshot_replication_job(dp_volume_group_snapshot_replication_pair_id=dp_volume_group_snapshot_replication_pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpVolumeGroupSnapshotReplicationJobsApi->list_dp_volume_group_snapshot_replication_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dp_volume_group_snapshot_replication_pair_id** | **int**| related pair id | [optional] 

### Return type

[**DpVolumeGroupSnapshotReplicationJobsResp**](DpVolumeGroupSnapshotReplicationJobsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

