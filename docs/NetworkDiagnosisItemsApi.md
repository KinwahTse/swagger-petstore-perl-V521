# xms_client.NetworkDiagnosisItemsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_network_diagnosis_items**](NetworkDiagnosisItemsApi.md#list_network_diagnosis_items) | **GET** /network-diagnosis-items/ | 


# **list_network_diagnosis_items**
> NetworkDiagnosisItemsResp list_network_diagnosis_items(limit=limit, offset=offset, networks=networks, finished=finished)



List network diagnosis items

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
api_instance = xms_client.NetworkDiagnosisItemsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
networks = 'networks_example' # str | network type (optional)
finished = true # bool | diagnosis item finished or not (optional)

try:
    api_response = api_instance.list_network_diagnosis_items(limit=limit, offset=offset, networks=networks, finished=finished)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiagnosisItemsApi->list_network_diagnosis_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **networks** | **str**| network type | [optional] 
 **finished** | **bool**| diagnosis item finished or not | [optional] 

### Return type

[**NetworkDiagnosisItemsResp**](NetworkDiagnosisItemsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

