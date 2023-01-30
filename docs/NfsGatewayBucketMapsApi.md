# xms_client.NfsGatewayBucketMapsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_nfs_gateway_s3_bucket_maps**](NfsGatewayBucketMapsApi.md#list_nfs_gateway_s3_bucket_maps) | **GET** /nfs-gateway-bucket-maps/ | 


# **list_nfs_gateway_s3_bucket_maps**
> NFSGatewayBucketMapsResp list_nfs_gateway_s3_bucket_maps(limit=limit, offset=offset, nfs_gateway_id=nfs_gateway_id, os_bucket_id=os_bucket_id, cluster_id=cluster_id)



List nfs gateway s3 bucket maps

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
api_instance = xms_client.NfsGatewayBucketMapsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
nfs_gateway_id = 789 # int | nfs gateway id (optional)
os_bucket_id = 789 # int | s3 bucket id (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_nfs_gateway_s3_bucket_maps(limit=limit, offset=offset, nfs_gateway_id=nfs_gateway_id, os_bucket_id=os_bucket_id, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewayBucketMapsApi->list_nfs_gateway_s3_bucket_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **nfs_gateway_id** | **int**| nfs gateway id | [optional] 
 **os_bucket_id** | **int**| s3 bucket id | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**NFSGatewayBucketMapsResp**](NFSGatewayBucketMapsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

