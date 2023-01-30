# xms_client.VirtualMachinesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_virtual_machine**](VirtualMachinesApi.md#get_virtual_machine) | **GET** /virtual-machines/{virtual_machine_id} | 
[**list_virtual_machines**](VirtualMachinesApi.md#list_virtual_machines) | **GET** /virtual-machines/ | 
[**update_virtual_machine**](VirtualMachinesApi.md#update_virtual_machine) | **PATCH** /virtual-machines/{virtual_machine_id} | 


# **get_virtual_machine**
> VirtualMachineResp get_virtual_machine(virtual_machine_id)



Get virtual machine

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
api_instance = xms_client.VirtualMachinesApi(xms_client.ApiClient(configuration))
virtual_machine_id = 789 # int | virtual machine id

try:
    api_response = api_instance.get_virtual_machine(virtual_machine_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->get_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| virtual machine id | 

### Return type

[**VirtualMachineResp**](VirtualMachineResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machines**
> VirtualMachinesResp list_virtual_machines(limit=limit, offset=offset)



List virtual machines

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
api_instance = xms_client.VirtualMachinesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_virtual_machines(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->list_virtual_machines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**VirtualMachinesResp**](VirtualMachinesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_machine**
> VirtualMachineResp update_virtual_machine(virtual_machine_id, cpu_num=cpu_num)



Update virtual machine

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
api_instance = xms_client.VirtualMachinesApi(xms_client.ApiClient(configuration))
virtual_machine_id = 789 # int | virtual machine id
cpu_num = 789 # int | new cpu number (optional)

try:
    api_response = api_instance.update_virtual_machine(virtual_machine_id, cpu_num=cpu_num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachinesApi->update_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| virtual machine id | 
 **cpu_num** | **int**| new cpu number | [optional] 

### Return type

[**VirtualMachineResp**](VirtualMachineResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

