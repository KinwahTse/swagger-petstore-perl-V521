# xms_client.RoleMappingsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_mapping**](RoleMappingsApi.md#create_role_mapping) | **POST** /role-mappings/ | 
[**delete_role_mapping**](RoleMappingsApi.md#delete_role_mapping) | **DELETE** /role-mappings/{role_mapping_id} | 
[**get_role_mapping**](RoleMappingsApi.md#get_role_mapping) | **GET** /role-mappings/{role_mapping_id} | 
[**list_role_mappings**](RoleMappingsApi.md#list_role_mappings) | **GET** /role-mappings/ | 
[**update_role_mapping**](RoleMappingsApi.md#update_role_mapping) | **PATCH** /role-mappings/{role_mapping_id} | 


# **create_role_mapping**
> RoleMappingResp create_role_mapping(body)



Create role mapping

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
api_instance = xms_client.RoleMappingsApi(xms_client.ApiClient(configuration))
body = xms_client.RoleMappingCreateReq() # RoleMappingCreateReq | role mapping info

try:
    api_response = api_instance.create_role_mapping(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleMappingsApi->create_role_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleMappingCreateReq**](RoleMappingCreateReq.md)| role mapping info | 

### Return type

[**RoleMappingResp**](RoleMappingResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_mapping**
> delete_role_mapping(role_mapping_id)



Delete role mapping

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
api_instance = xms_client.RoleMappingsApi(xms_client.ApiClient(configuration))
role_mapping_id = 789 # int | role mapping id

try:
    api_instance.delete_role_mapping(role_mapping_id)
except ApiException as e:
    print("Exception when calling RoleMappingsApi->delete_role_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_mapping_id** | **int**| role mapping id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_mapping**
> RoleMappingResp get_role_mapping(role_mapping_id)



Get a role mapping

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
api_instance = xms_client.RoleMappingsApi(xms_client.ApiClient(configuration))
role_mapping_id = 789 # int | role mapping id

try:
    api_response = api_instance.get_role_mapping(role_mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleMappingsApi->get_role_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_mapping_id** | **int**| role mapping id | 

### Return type

[**RoleMappingResp**](RoleMappingResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_mappings**
> RoleMappingsResp list_role_mappings(limit=limit, offset=offset, identity_platform_id=identity_platform_id)



List role mappings

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
api_instance = xms_client.RoleMappingsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
identity_platform_id = 789 # int | identity platform id (optional)

try:
    api_response = api_instance.list_role_mappings(limit=limit, offset=offset, identity_platform_id=identity_platform_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleMappingsApi->list_role_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **identity_platform_id** | **int**| identity platform id | [optional] 

### Return type

[**RoleMappingsResp**](RoleMappingsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_mapping**
> RoleMappingResp update_role_mapping(role_mapping_id, body)



Update a role mapping

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
api_instance = xms_client.RoleMappingsApi(xms_client.ApiClient(configuration))
role_mapping_id = 789 # int | role mapping id
body = xms_client.RoleMappingUpdateReq() # RoleMappingUpdateReq | role mapping info

try:
    api_response = api_instance.update_role_mapping(role_mapping_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleMappingsApi->update_role_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_mapping_id** | **int**| role mapping id | 
 **body** | [**RoleMappingUpdateReq**](RoleMappingUpdateReq.md)| role mapping info | 

### Return type

[**RoleMappingResp**](RoleMappingResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

