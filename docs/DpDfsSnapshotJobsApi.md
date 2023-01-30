# xms_client.DpDfsSnapshotJobsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dp_dfs_snapshot_jobs**](DpDfsSnapshotJobsApi.md#list_dp_dfs_snapshot_jobs) | **GET** /dp-dfs-snapshot-jobs/ | 


# **list_dp_dfs_snapshot_jobs**
> DpDfsSnapshotJobsResp list_dp_dfs_snapshot_jobs(limit=limit, offset=offset, q=q, sort=sort, dp_dfs_snapshot_policy_id=dp_dfs_snapshot_policy_id)



List dp dfs snapshot jobs

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
api_instance = xms_client.DpDfsSnapshotJobsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
dp_dfs_snapshot_policy_id = 789 # int | dp dfs snapshot policy (optional)

try:
    api_response = api_instance.list_dp_dfs_snapshot_jobs(limit=limit, offset=offset, q=q, sort=sort, dp_dfs_snapshot_policy_id=dp_dfs_snapshot_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotJobsApi->list_dp_dfs_snapshot_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **dp_dfs_snapshot_policy_id** | **int**| dp dfs snapshot policy | [optional] 

### Return type

[**DpDfsSnapshotJobsResp**](DpDfsSnapshotJobsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

