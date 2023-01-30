# xms_client.DfsGatewayNetworkAddressesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dfs_gateway_network_address**](DfsGatewayNetworkAddressesApi.md#get_dfs_gateway_network_address) | **GET** /dfs-gateway-network-addresses/{dfs_gateway_network_address_id} | 
[**list_dfs_gateway_network_addresses**](DfsGatewayNetworkAddressesApi.md#list_dfs_gateway_network_addresses) | **GET** /dfs-gateway-network-addresses/ | 


# **get_dfs_gateway_network_address**
> DfsGatewayNetworkAddressResp get_dfs_gateway_network_address(dfs_gateway_network_address_id)



Get dfs gateway

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
api_instance = xms_client.DfsGatewayNetworkAddressesApi(xms_client.ApiClient(configuration))
dfs_gateway_network_address_id = 789 # int | gateway network address id

try:
    api_response = api_instance.get_dfs_gateway_network_address(dfs_gateway_network_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayNetworkAddressesApi->get_dfs_gateway_network_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_network_address_id** | **int**| gateway network address id | 

### Return type

[**DfsGatewayNetworkAddressResp**](DfsGatewayNetworkAddressResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_gateway_network_addresses**
> DfsGatewayNetworkAddressesResp list_dfs_gateway_network_addresses(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, dfs_gateway_group_id=dfs_gateway_group_id, dfs_gateway_zone_id=dfs_gateway_zone_id)



List dfs gateway network addresses

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
api_instance = xms_client.DfsGatewayNetworkAddressesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
dfs_gateway_group_id = 789 # int | dfs gateway group id (optional)
dfs_gateway_zone_id = 789 # int | dfs gateway zone id (optional)

try:
    api_response = api_instance.list_dfs_gateway_network_addresses(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, dfs_gateway_group_id=dfs_gateway_group_id, dfs_gateway_zone_id=dfs_gateway_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayNetworkAddressesApi->list_dfs_gateway_network_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **dfs_gateway_group_id** | **int**| dfs gateway group id | [optional] 
 **dfs_gateway_zone_id** | **int**| dfs gateway zone id | [optional] 

### Return type

[**DfsGatewayNetworkAddressesResp**](DfsGatewayNetworkAddressesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

