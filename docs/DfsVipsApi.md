# xms_client.DfsVipsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dfs_vip**](DfsVipsApi.md#get_dfs_vip) | **GET** /dfs-vips/{dfs_vip_id} | 
[**list_dfs_vi_ps**](DfsVipsApi.md#list_dfs_vi_ps) | **GET** /dfs-vips/ | 
[**move_dfs_vip**](DfsVipsApi.md#move_dfs_vip) | **POST** /dfs-vips/{dfs_vip_id} | 


# **get_dfs_vip**
> DfsVIPResp get_dfs_vip(dfs_vip_id)



Get dfs vip

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
api_instance = xms_client.DfsVipsApi(xms_client.ApiClient(configuration))
dfs_vip_id = 789 # int | vip id

try:
    api_response = api_instance.get_dfs_vip(dfs_vip_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsVipsApi->get_dfs_vip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_vip_id** | **int**| vip id | 

### Return type

[**DfsVIPResp**](DfsVIPResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_vi_ps**
> DfsVIPsResp list_dfs_vi_ps(limit=limit, offset=offset, cluster_id=cluster_id, dfs_gateway_group_id=dfs_gateway_group_id, dfs_gateway_zone_id=dfs_gateway_zone_id, primary_gateway_id=primary_gateway_id)



List dfs vips

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
api_instance = xms_client.DfsVipsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
dfs_gateway_group_id = 789 # int | dfs vip group id (optional)
dfs_gateway_zone_id = 789 # int | dfs gateway zone id (optional)
primary_gateway_id = 789 # int | primary gateway id (optional)

try:
    api_response = api_instance.list_dfs_vi_ps(limit=limit, offset=offset, cluster_id=cluster_id, dfs_gateway_group_id=dfs_gateway_group_id, dfs_gateway_zone_id=dfs_gateway_zone_id, primary_gateway_id=primary_gateway_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsVipsApi->list_dfs_vi_ps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **dfs_gateway_group_id** | **int**| dfs vip group id | [optional] 
 **dfs_gateway_zone_id** | **int**| dfs gateway zone id | [optional] 
 **primary_gateway_id** | **int**| primary gateway id | [optional] 

### Return type

[**DfsVIPsResp**](DfsVIPsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_dfs_vip**
> DfsVIPResp move_dfs_vip(dfs_vip_id, body=body)



move vip to another dfs gateway

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
api_instance = xms_client.DfsVipsApi(xms_client.ApiClient(configuration))
dfs_vip_id = 789 # int | vip id
body = xms_client.DfsVIPMoveReq() # DfsVIPMoveReq | moving vip info (optional)

try:
    api_response = api_instance.move_dfs_vip(dfs_vip_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsVipsApi->move_dfs_vip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_vip_id** | **int**| vip id | 
 **body** | [**DfsVIPMoveReq**](DfsVIPMoveReq.md)| moving vip info | [optional] 

### Return type

[**DfsVIPResp**](DfsVIPResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

