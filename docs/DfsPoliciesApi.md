# xms_client.DfsPoliciesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dfs_policies**](DfsPoliciesApi.md#list_dfs_policies) | **GET** /dfs-policies/ | 


# **list_dfs_policies**
> DfsPoliciesResp list_dfs_policies(limit=limit, offset=offset, dfs_rootfs_id=dfs_rootfs_id, cluster_id=cluster_id)



List dfs Policies

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
api_instance = xms_client.DfsPoliciesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
dfs_rootfs_id = 789 # int | dfs rootfs id (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_dfs_policies(limit=limit, offset=offset, dfs_rootfs_id=dfs_rootfs_id, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsPoliciesApi->list_dfs_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **dfs_rootfs_id** | **int**| dfs rootfs id | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**DfsPoliciesResp**](DfsPoliciesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

