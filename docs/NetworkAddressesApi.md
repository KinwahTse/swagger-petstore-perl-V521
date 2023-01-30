# xms_client.NetworkAddressesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_network_address**](NetworkAddressesApi.md#get_network_address) | **GET** /network-addresses/{network_address_id} | 
[**list_network_addresses**](NetworkAddressesApi.md#list_network_addresses) | **GET** /network-addresses/ | 


# **get_network_address**
> NetworkAddressResp get_network_address(network_address_id)



Get a network address

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
api_instance = xms_client.NetworkAddressesApi(xms_client.ApiClient(configuration))
network_address_id = 789 # int | network address id

try:
    api_response = api_instance.get_network_address(network_address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkAddressesApi->get_network_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_address_id** | **int**| network address id | 

### Return type

[**NetworkAddressResp**](NetworkAddressResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_addresses**
> NetworkAddressesResp list_network_addresses(limit=limit, offset=offset, network_interface_id=network_interface_id, host_id=host_id, role=role, vip_group_id=vip_group_id)



List network addresses

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
api_instance = xms_client.NetworkAddressesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
network_interface_id = 789 # int | network interface id (optional)
host_id = 789 # int | host id (optional)
role = 'role_example' # str | network address role (optional)
vip_group_id = 789 # int | vip group id (optional)

try:
    api_response = api_instance.list_network_addresses(limit=limit, offset=offset, network_interface_id=network_interface_id, host_id=host_id, role=role, vip_group_id=vip_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkAddressesApi->list_network_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **network_interface_id** | **int**| network interface id | [optional] 
 **host_id** | **int**| host id | [optional] 
 **role** | **str**| network address role | [optional] 
 **vip_group_id** | **int**| vip group id | [optional] 

### Return type

[**NetworkAddressesResp**](NetworkAddressesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

