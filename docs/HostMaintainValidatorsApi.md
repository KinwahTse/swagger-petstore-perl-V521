# xms_client.HostMaintainValidatorsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_host_maintain_validator**](HostMaintainValidatorsApi.md#create_host_maintain_validator) | **POST** /host-maintain-validators/ | 
[**get_host_maintain_validator**](HostMaintainValidatorsApi.md#get_host_maintain_validator) | **GET** /host-maintain-validators/{host_maintain_validator_id} | 


# **create_host_maintain_validator**
> HostMaintainValidatorResp create_host_maintain_validator(body)



Create host maintain validator

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
api_instance = xms_client.HostMaintainValidatorsApi(xms_client.ApiClient(configuration))
body = xms_client.HostMaintainValidatorCreateReq() # HostMaintainValidatorCreateReq | host maintain validator info

try:
    api_response = api_instance.create_host_maintain_validator(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostMaintainValidatorsApi->create_host_maintain_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostMaintainValidatorCreateReq**](HostMaintainValidatorCreateReq.md)| host maintain validator info | 

### Return type

[**HostMaintainValidatorResp**](HostMaintainValidatorResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_maintain_validator**
> HostMaintainValidatorResp get_host_maintain_validator(host_maintain_validator_id)



Get host maintain validator

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
api_instance = xms_client.HostMaintainValidatorsApi(xms_client.ApiClient(configuration))
host_maintain_validator_id = 789 # int | host maintain validator id

try:
    api_response = api_instance.get_host_maintain_validator(host_maintain_validator_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostMaintainValidatorsApi->get_host_maintain_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_maintain_validator_id** | **int**| host maintain validator id | 

### Return type

[**HostMaintainValidatorResp**](HostMaintainValidatorResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

