# xms_client.HostInitializationsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_initialization**](HostInitializationsApi.md#host_initialization) | **POST** /host-initializations/ | 


# **host_initialization**
> HostInitializationResp host_initialization(body)



Create host initialization

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
api_instance = xms_client.HostInitializationsApi(xms_client.ApiClient(configuration))
body = xms_client.HostInitializationReq() # HostInitializationReq | host initialization info

try:
    api_response = api_instance.host_initialization(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostInitializationsApi->host_initialization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostInitializationReq**](HostInitializationReq.md)| host initialization info | 

### Return type

[**HostInitializationResp**](HostInitializationResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

