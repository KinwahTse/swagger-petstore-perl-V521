# xms_client.BlockVolumeMigrationJobsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_block_volume_migration_job**](BlockVolumeMigrationJobsApi.md#cancel_block_volume_migration_job) | **POST** /block-volume-migration-jobs/{block_volume_migration_job_id}:cancel | 
[**get_block_volume_migration_job**](BlockVolumeMigrationJobsApi.md#get_block_volume_migration_job) | **GET** /block-volume-migration-jobs/{block_volume_migration_job_id} | 
[**list_block_volume_migration_jobs**](BlockVolumeMigrationJobsApi.md#list_block_volume_migration_jobs) | **GET** /block-volume-migration-jobs/ | 
[**update_migration**](BlockVolumeMigrationJobsApi.md#update_migration) | **POST** /block-volume-migration-jobs/{block_volume_migration_job_id}:update | 


# **cancel_block_volume_migration_job**
> BlockVolumeMigrationJobResp cancel_block_volume_migration_job(block_volume_migration_job_id)



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
api_instance = xms_client.BlockVolumeMigrationJobsApi(xms_client.ApiClient(configuration))
block_volume_migration_job_id = 789 # int | block volume migration job id

try:
    api_response = api_instance.cancel_block_volume_migration_job(block_volume_migration_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeMigrationJobsApi->cancel_block_volume_migration_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_migration_job_id** | **int**| block volume migration job id | 

### Return type

[**BlockVolumeMigrationJobResp**](BlockVolumeMigrationJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_volume_migration_job**
> BlockVolumeMigrationJobResp get_block_volume_migration_job(block_volume_migration_job_id)



get a volume migration job

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
api_instance = xms_client.BlockVolumeMigrationJobsApi(xms_client.ApiClient(configuration))
block_volume_migration_job_id = 789 # int | volume migration job id

try:
    api_response = api_instance.get_block_volume_migration_job(block_volume_migration_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeMigrationJobsApi->get_block_volume_migration_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_migration_job_id** | **int**| volume migration job id | 

### Return type

[**BlockVolumeMigrationJobResp**](BlockVolumeMigrationJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_block_volume_migration_jobs**
> BlockVolumeMigrationJobsResp list_block_volume_migration_jobs(limit=limit, offset=offset, status=status, q=q, sort=sort)



List volume migration jobs

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
api_instance = xms_client.BlockVolumeMigrationJobsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
status = 'status_example' # str | the status of volume migration job (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_block_volume_migration_jobs(limit=limit, offset=offset, status=status, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeMigrationJobsApi->list_block_volume_migration_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **status** | **str**| the status of volume migration job | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**BlockVolumeMigrationJobsResp**](BlockVolumeMigrationJobsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_migration**
> BlockVolumeMigrationJobResp update_migration(block_volume_migration_job_id, body)



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
api_instance = xms_client.BlockVolumeMigrationJobsApi(xms_client.ApiClient(configuration))
block_volume_migration_job_id = 789 # int | block volume migration job id
body = xms_client.BlockVolumeUpdateMigrationReq() # BlockVolumeUpdateMigrationReq | volume migration udpate info

try:
    api_response = api_instance.update_migration(block_volume_migration_job_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeMigrationJobsApi->update_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_migration_job_id** | **int**| block volume migration job id | 
 **body** | [**BlockVolumeUpdateMigrationReq**](BlockVolumeUpdateMigrationReq.md)| volume migration udpate info | 

### Return type

[**BlockVolumeMigrationJobResp**](BlockVolumeMigrationJobResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

