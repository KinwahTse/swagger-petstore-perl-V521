# xms_client.DfsS3BucketConnectionsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dfs_s3_bucket_connections**](DfsS3BucketConnectionsApi.md#list_dfs_s3_bucket_connections) | **GET** /dfs-s3-bucket-connections/ | 


# **list_dfs_s3_bucket_connections**
> DfsS3BucketConnectionsResp list_dfs_s3_bucket_connections(limit=limit, offset=offset, bucket_id=bucket_id)



List dfs s3 Bucket connections

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
api_instance = xms_client.DfsS3BucketConnectionsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
bucket_id = 789 # int | bucket id (optional)

try:
    api_response = api_instance.list_dfs_s3_bucket_connections(limit=limit, offset=offset, bucket_id=bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3BucketConnectionsApi->list_dfs_s3_bucket_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **bucket_id** | **int**| bucket id | [optional] 

### Return type

[**DfsS3BucketConnectionsResp**](DfsS3BucketConnectionsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

