# xms_client.DpFsSnapshotJobsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dp_fs_snapshot_job**](DpFsSnapshotJobsApi.md#get_dp_fs_snapshot_job) | **GET** /dp-fs-snapshot-jobs/{job_id} | 
[**list_dp_fs_snapshot_jobs**](DpFsSnapshotJobsApi.md#list_dp_fs_snapshot_jobs) | **GET** /dp-fs-snapshot-jobs/ | 


# **get_dp_fs_snapshot_job**
> DpFSSnapshotJobResp get_dp_fs_snapshot_job(job_id)



Get dp fs snapshot job

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
api_instance = xms_client.DpFsSnapshotJobsApi(xms_client.ApiClient(configuration))
job_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_fs_snapshot_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpFsSnapshotJobsApi->get_dp_fs_snapshot_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| resource id | 

### Return type

[**DpFSSnapshotJobResp**](DpFSSnapshotJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_fs_snapshot_jobs**
> DpFSSnapshotJobsResp list_dp_fs_snapshot_jobs(limit=limit, offset=offset, q=q, sort=sort, fs_folder_id=fs_folder_id, fs_snapshot_id=fs_snapshot_id, dp_fs_snapshot_policy_id=dp_fs_snapshot_policy_id)



List dp fs snapshot jobs

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
api_instance = xms_client.DpFsSnapshotJobsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
fs_folder_id = 789 # int | fs folder (optional)
fs_snapshot_id = 789 # int | fs snapshot (optional)
dp_fs_snapshot_policy_id = 789 # int | dp fs snapshot policy (optional)

try:
    api_response = api_instance.list_dp_fs_snapshot_jobs(limit=limit, offset=offset, q=q, sort=sort, fs_folder_id=fs_folder_id, fs_snapshot_id=fs_snapshot_id, dp_fs_snapshot_policy_id=dp_fs_snapshot_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpFsSnapshotJobsApi->list_dp_fs_snapshot_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **fs_folder_id** | **int**| fs folder | [optional] 
 **fs_snapshot_id** | **int**| fs snapshot | [optional] 
 **dp_fs_snapshot_policy_id** | **int**| dp fs snapshot policy | [optional] 

### Return type

[**DpFSSnapshotJobsResp**](DpFSSnapshotJobsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

