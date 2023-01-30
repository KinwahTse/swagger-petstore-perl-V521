# xms_client.DpBlockSnapshotRecoveryJobsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dp_block_snapshot_recovery_job**](DpBlockSnapshotRecoveryJobsApi.md#create_dp_block_snapshot_recovery_job) | **POST** /dp-block-snapshot-recovery-jobs/ | 
[**delete_dp_block_snapshot_recovery_job**](DpBlockSnapshotRecoveryJobsApi.md#delete_dp_block_snapshot_recovery_job) | **DELETE** /dp-block-snapshot-recovery-jobs/{job_id} | 
[**get_dp_block_snapshot_recovery_job**](DpBlockSnapshotRecoveryJobsApi.md#get_dp_block_snapshot_recovery_job) | **GET** /dp-block-snapshot-recovery-jobs/{job_id} | 
[**list_dp_block_snapshot_recovery_jobs**](DpBlockSnapshotRecoveryJobsApi.md#list_dp_block_snapshot_recovery_jobs) | **GET** /dp-block-snapshot-recovery-jobs/ | 


# **create_dp_block_snapshot_recovery_job**
> DpBlockSnapshotRecoveryJobResp create_dp_block_snapshot_recovery_job(body)



Create a dp block snapshot recovery job

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
api_instance = xms_client.DpBlockSnapshotRecoveryJobsApi(xms_client.ApiClient(configuration))
body = xms_client.DpBlockSnapshotRecoveryJobCreateReq() # DpBlockSnapshotRecoveryJobCreateReq | resource info

try:
    api_response = api_instance.create_dp_block_snapshot_recovery_job(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockSnapshotRecoveryJobsApi->create_dp_block_snapshot_recovery_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpBlockSnapshotRecoveryJobCreateReq**](DpBlockSnapshotRecoveryJobCreateReq.md)| resource info | 

### Return type

[**DpBlockSnapshotRecoveryJobResp**](DpBlockSnapshotRecoveryJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_block_snapshot_recovery_job**
> delete_dp_block_snapshot_recovery_job(job_id)



Delete a dp block snapshot recovery job

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
api_instance = xms_client.DpBlockSnapshotRecoveryJobsApi(xms_client.ApiClient(configuration))
job_id = 789 # int | resource id

try:
    api_instance.delete_dp_block_snapshot_recovery_job(job_id)
except ApiException as e:
    print("Exception when calling DpBlockSnapshotRecoveryJobsApi->delete_dp_block_snapshot_recovery_job: %s\n" % e)
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

# **get_dp_block_snapshot_recovery_job**
> DpBlockSnapshotRecoveryJobResp get_dp_block_snapshot_recovery_job(job_id)



Get a dp block snapshot recovery job

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
api_instance = xms_client.DpBlockSnapshotRecoveryJobsApi(xms_client.ApiClient(configuration))
job_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_block_snapshot_recovery_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockSnapshotRecoveryJobsApi->get_dp_block_snapshot_recovery_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| resource id | 

### Return type

[**DpBlockSnapshotRecoveryJobResp**](DpBlockSnapshotRecoveryJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_block_snapshot_recovery_jobs**
> DpBlockSnapshotRecoveryJobsResp list_dp_block_snapshot_recovery_jobs(limit=limit, offset=offset, q=q, sort=sort)



List dp block snapshot recovery jobs

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
api_instance = xms_client.DpBlockSnapshotRecoveryJobsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dp_block_snapshot_recovery_jobs(limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockSnapshotRecoveryJobsApi->list_dp_block_snapshot_recovery_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DpBlockSnapshotRecoveryJobsResp**](DpBlockSnapshotRecoveryJobsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

