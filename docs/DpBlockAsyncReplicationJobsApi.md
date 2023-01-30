# xms_client.DpBlockAsyncReplicationJobsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dp_block_async_replication_job**](DpBlockAsyncReplicationJobsApi.md#delete_dp_block_async_replication_job) | **DELETE** /dp-block-async-replication-jobs/{job_id} | 
[**get_dp_block_async_replication_job**](DpBlockAsyncReplicationJobsApi.md#get_dp_block_async_replication_job) | **GET** /dp-block-async-replication-jobs/{job_id} | 
[**list_dp_block_async_replication_job**](DpBlockAsyncReplicationJobsApi.md#list_dp_block_async_replication_job) | **GET** /dp-block-async-replication-jobs/ | 


# **delete_dp_block_async_replication_job**
> delete_dp_block_async_replication_job(job_id)



Delete dp block async replication job

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
api_instance = xms_client.DpBlockAsyncReplicationJobsApi(xms_client.ApiClient(configuration))
job_id = 789 # int | resource id

try:
    api_instance.delete_dp_block_async_replication_job(job_id)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationJobsApi->delete_dp_block_async_replication_job: %s\n" % e)
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

# **get_dp_block_async_replication_job**
> DpBlockAsyncReplicationJobResp get_dp_block_async_replication_job(job_id)



Get dp block async replication job

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
api_instance = xms_client.DpBlockAsyncReplicationJobsApi(xms_client.ApiClient(configuration))
job_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_block_async_replication_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationJobsApi->get_dp_block_async_replication_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| resource id | 

### Return type

[**DpBlockAsyncReplicationJobResp**](DpBlockAsyncReplicationJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_block_async_replication_job**
> DpBlockAsyncReplicationJobsResp list_dp_block_async_replication_job()



List dp block async replication jobs

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
api_instance = xms_client.DpBlockAsyncReplicationJobsApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.list_dp_block_async_replication_job()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationJobsApi->list_dp_block_async_replication_job: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DpBlockAsyncReplicationJobsResp**](DpBlockAsyncReplicationJobsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

