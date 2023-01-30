# xms_client.NetworkInterfacesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_network_interface**](NetworkInterfacesApi.md#get_network_interface) | **GET** /network-interfaces/{network_interface_id} | 
[**get_network_interface_samples**](NetworkInterfacesApi.md#get_network_interface_samples) | **GET** /network-interfaces/{network_interface_id}/samples | 
[**list_network_interfaces**](NetworkInterfacesApi.md#list_network_interfaces) | **GET** /network-interfaces/ | 


# **get_network_interface**
> NetworkInterfaceResp get_network_interface(network_interface_id)



Get a network interface

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
api_instance = xms_client.NetworkInterfacesApi(xms_client.ApiClient(configuration))
network_interface_id = 789 # int | network interface id

try:
    api_response = api_instance.get_network_interface(network_interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfacesApi->get_network_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_interface_id** | **int**| network interface id | 

### Return type

[**NetworkInterfaceResp**](NetworkInterfaceResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_interface_samples**
> NetworkInterfaceSamplesResp get_network_interface_samples(network_interface_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a network interface's Samples

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
api_instance = xms_client.NetworkInterfacesApi(xms_client.ApiClient(configuration))
network_interface_id = 789 # int | network interface id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_network_interface_samples(network_interface_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfacesApi->get_network_interface_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_interface_id** | **int**| network interface id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**NetworkInterfaceSamplesResp**](NetworkInterfaceSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_interfaces**
> NetworkInterfacesResp list_network_interfaces(limit=limit, offset=offset, master_network_interface_id=master_network_interface_id, host_id=host_id, role=role)



List network interfaces

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
api_instance = xms_client.NetworkInterfacesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
master_network_interface_id = 789 # int | master network interface id (optional)
host_id = 789 # int | host id (optional)
role = 'role_example' # str | network interface role (optional)

try:
    api_response = api_instance.list_network_interfaces(limit=limit, offset=offset, master_network_interface_id=master_network_interface_id, host_id=host_id, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkInterfacesApi->list_network_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **master_network_interface_id** | **int**| master network interface id | [optional] 
 **host_id** | **int**| host id | [optional] 
 **role** | **str**| network interface role | [optional] 

### Return type

[**NetworkInterfacesResp**](NetworkInterfacesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

