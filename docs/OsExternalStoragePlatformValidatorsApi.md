# xms_client.OsExternalStoragePlatformValidatorsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_os_ex_storage_platform_validator**](OsExternalStoragePlatformValidatorsApi.md#create_os_ex_storage_platform_validator) | **POST** /os-external-storage-platform-validators/ | 
[**get_os_ex_storage_platform_validator**](OsExternalStoragePlatformValidatorsApi.md#get_os_ex_storage_platform_validator) | **GET** /os-external-storage-platform-validators/{validator_id} | 


# **create_os_ex_storage_platform_validator**
> OSExStoragePlatformValidatorResp create_os_ex_storage_platform_validator(body, cluster_id=cluster_id)



Create os external storage platform validator

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
api_instance = xms_client.OsExternalStoragePlatformValidatorsApi(xms_client.ApiClient(configuration))
body = xms_client.OSExStoragePlatformValidatorCreateReq() # OSExStoragePlatformValidatorCreateReq | external storage platform validator info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_os_ex_storage_platform_validator(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsExternalStoragePlatformValidatorsApi->create_os_ex_storage_platform_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OSExStoragePlatformValidatorCreateReq**](OSExStoragePlatformValidatorCreateReq.md)| external storage platform validator info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSExStoragePlatformValidatorResp**](OSExStoragePlatformValidatorResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_ex_storage_platform_validator**
> OSExStoragePlatformValidatorResp get_os_ex_storage_platform_validator(validator_id)



Get a os external storage platform validator

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
api_instance = xms_client.OsExternalStoragePlatformValidatorsApi(xms_client.ApiClient(configuration))
validator_id = 789 # int | external storage platform validator id

try:
    api_response = api_instance.get_os_ex_storage_platform_validator(validator_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsExternalStoragePlatformValidatorsApi->get_os_ex_storage_platform_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validator_id** | **int**| external storage platform validator id | 

### Return type

[**OSExStoragePlatformValidatorResp**](OSExStoragePlatformValidatorResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

