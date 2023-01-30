# xms_client.DpBlockSnapshotJobsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dp_block_snapshot_jobs**](DpBlockSnapshotJobsApi.md#list_dp_block_snapshot_jobs) | **GET** /dp-block-snapshot-jobs/ | 


# **list_dp_block_snapshot_jobs**
> DpBlockSnapshotJobsResp list_dp_block_snapshot_jobs(limit=limit, offset=offset, q=q, sort=sort, block_volume_id=block_volume_id, block_snapshot_id=block_snapshot_id, dp_block_snapshot_policy_id=dp_block_snapshot_policy_id)



List dp block snapshot jobs

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
api_instance = xms_client.DpBlockSnapshotJobsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
block_volume_id = 789 # int | block volume (optional)
block_snapshot_id = 789 # int | object storage bucket (optional)
dp_block_snapshot_policy_id = 789 # int | dp block snapshot policy (optional)

try:
    api_response = api_instance.list_dp_block_snapshot_jobs(limit=limit, offset=offset, q=q, sort=sort, block_volume_id=block_volume_id, block_snapshot_id=block_snapshot_id, dp_block_snapshot_policy_id=dp_block_snapshot_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockSnapshotJobsApi->list_dp_block_snapshot_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **block_volume_id** | **int**| block volume | [optional] 
 **block_snapshot_id** | **int**| object storage bucket | [optional] 
 **dp_block_snapshot_policy_id** | **int**| dp block snapshot policy | [optional] 

### Return type

[**DpBlockSnapshotJobsResp**](DpBlockSnapshotJobsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

