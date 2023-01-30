# xms_client.FsGatewaysApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fs_gateway**](FsGatewaysApi.md#get_fs_gateway) | **GET** /fs-gateways/{fs_gateway_id} | 
[**list_fs_gateways**](FsGatewaysApi.md#list_fs_gateways) | **GET** /fs-gateways/ | 


# **get_fs_gateway**
> FSGatewayResp get_fs_gateway(fs_gateway_id)



Get file storage gateway

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
api_instance = xms_client.FsGatewaysApi(xms_client.ApiClient(configuration))
fs_gateway_id = 789 # int | gateway id

try:
    api_response = api_instance.get_fs_gateway(fs_gateway_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsGatewaysApi->get_fs_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_gateway_id** | **int**| gateway id | 

### Return type

[**FSGatewayResp**](FSGatewayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fs_gateways**
> FSGatewaysResp list_fs_gateways(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, fs_gateway_group_id=fs_gateway_group_id)



List file storage gateways

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
api_instance = xms_client.FsGatewaysApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
fs_gateway_group_id = 789 # int | file storage gateway group id (optional)

try:
    api_response = api_instance.list_fs_gateways(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, fs_gateway_group_id=fs_gateway_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsGatewaysApi->list_fs_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **fs_gateway_group_id** | **int**| file storage gateway group id | [optional] 

### Return type

[**FSGatewaysResp**](FSGatewaysResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

