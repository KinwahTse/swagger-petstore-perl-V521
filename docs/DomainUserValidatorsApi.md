# xms_client.DomainUserValidatorsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain_user_validator**](DomainUserValidatorsApi.md#create_domain_user_validator) | **POST** /domain-user-validators/ | 
[**get_domain_user_validator**](DomainUserValidatorsApi.md#get_domain_user_validator) | **GET** /domain-user-validators/{domain_user_validator_id} | 


# **create_domain_user_validator**
> DomainUserValidatorResp create_domain_user_validator(body)



Create domain user validator

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
api_instance = xms_client.DomainUserValidatorsApi(xms_client.ApiClient(configuration))
body = xms_client.DomainUserValidatorCreateReq() # DomainUserValidatorCreateReq | domain user validator info

try:
    api_response = api_instance.create_domain_user_validator(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainUserValidatorsApi->create_domain_user_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainUserValidatorCreateReq**](DomainUserValidatorCreateReq.md)| domain user validator info | 

### Return type

[**DomainUserValidatorResp**](DomainUserValidatorResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_user_validator**
> DomainUserValidatorResp get_domain_user_validator(domain_user_validator_id)



Get domain_user validator

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
api_instance = xms_client.DomainUserValidatorsApi(xms_client.ApiClient(configuration))
domain_user_validator_id = 789 # int | domain user validator id

try:
    api_response = api_instance.get_domain_user_validator(domain_user_validator_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainUserValidatorsApi->get_domain_user_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_user_validator_id** | **int**| domain user validator id | 

### Return type

[**DomainUserValidatorResp**](DomainUserValidatorResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

