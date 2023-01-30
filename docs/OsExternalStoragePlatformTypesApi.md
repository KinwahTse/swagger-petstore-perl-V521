# xms_client.OsExternalStoragePlatformTypesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_os_external_storage_platform_type**](OsExternalStoragePlatformTypesApi.md#create_os_external_storage_platform_type) | **POST** /os-external-storage-platform-types/ | 
[**get_os_external_storage_platform_type**](OsExternalStoragePlatformTypesApi.md#get_os_external_storage_platform_type) | **GET** /os-external-storage-platform-types/{external_storage_platform_type_id} | 
[**list_os_external_storage_platform_types**](OsExternalStoragePlatformTypesApi.md#list_os_external_storage_platform_types) | **GET** /os-external-storage-platform-types/ | 


# **create_os_external_storage_platform_type**
> OSExternalStoragePlatformTypeResp create_os_external_storage_platform_type(body, cluster_id=cluster_id)



Create os external storage platform type

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
api_instance = xms_client.OsExternalStoragePlatformTypesApi(xms_client.ApiClient(configuration))
body = xms_client.OSExternalStoragePlatformTypeCreateReq() # OSExternalStoragePlatformTypeCreateReq | external storage platform type info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_os_external_storage_platform_type(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsExternalStoragePlatformTypesApi->create_os_external_storage_platform_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OSExternalStoragePlatformTypeCreateReq**](OSExternalStoragePlatformTypeCreateReq.md)| external storage platform type info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSExternalStoragePlatformTypeResp**](OSExternalStoragePlatformTypeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_external_storage_platform_type**
> OSExternalStoragePlatformTypeResp get_os_external_storage_platform_type(external_storage_platform_type_id)



Get an os external storage platform type info

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
api_instance = xms_client.OsExternalStoragePlatformTypesApi(xms_client.ApiClient(configuration))
external_storage_platform_type_id = 789 # int | external storage platform type id

try:
    api_response = api_instance.get_os_external_storage_platform_type(external_storage_platform_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsExternalStoragePlatformTypesApi->get_os_external_storage_platform_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_storage_platform_type_id** | **int**| external storage platform type id | 

### Return type

[**OSExternalStoragePlatformTypeResp**](OSExternalStoragePlatformTypeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_external_storage_platform_types**
> OSExternalStoragePlatformTypesResp list_os_external_storage_platform_types(limit=limit, offset=offset, platform=platform, platform_type=platform_type, cluster_id=cluster_id)



List os external storage platform types

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
api_instance = xms_client.OsExternalStoragePlatformTypesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
platform = 'platform_example' # str | platform (optional)
platform_type = 'platform_type_example' # str | platform type (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_os_external_storage_platform_types(limit=limit, offset=offset, platform=platform, platform_type=platform_type, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsExternalStoragePlatformTypesApi->list_os_external_storage_platform_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **platform** | **str**| platform | [optional] 
 **platform_type** | **str**| platform type | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSExternalStoragePlatformTypesResp**](OSExternalStoragePlatformTypesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

