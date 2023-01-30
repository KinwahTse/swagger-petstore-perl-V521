# xms_client.VmFlavorsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vm_flavor**](VmFlavorsApi.md#get_vm_flavor) | **GET** /vm-flavors/{vm_flavor_id} | 
[**list_vm_flavors**](VmFlavorsApi.md#list_vm_flavors) | **GET** /vm-flavors/ | 


# **get_vm_flavor**
> VMFlavorResp get_vm_flavor(vm_flavor_id)



Get vm flavor

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
api_instance = xms_client.VmFlavorsApi(xms_client.ApiClient(configuration))
vm_flavor_id = 789 # int | vm flavor id

try:
    api_response = api_instance.get_vm_flavor(vm_flavor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmFlavorsApi->get_vm_flavor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_flavor_id** | **int**| vm flavor id | 

### Return type

[**VMFlavorResp**](VMFlavorResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vm_flavors**
> VMFlavorsResp list_vm_flavors(limit=limit, offset=offset)



List vm flavors

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
api_instance = xms_client.VmFlavorsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_vm_flavors(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmFlavorsApi->list_vm_flavors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**VMFlavorsResp**](VMFlavorsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

