# xms_client.OsBuiltinBluRaysApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_os_builtin_blu_ray**](OsBuiltinBluRaysApi.md#create_os_builtin_blu_ray) | **POST** /os-builtin-blu-rays/ | 
[**delete_os_builtin_blu_ray**](OsBuiltinBluRaysApi.md#delete_os_builtin_blu_ray) | **DELETE** /os-builtin-blu-rays/{builtin_blu_ray_id} | 
[**get_os_builtin_blu_ray**](OsBuiltinBluRaysApi.md#get_os_builtin_blu_ray) | **GET** /os-builtin-blu-rays/{builtin_blu_ray_id} | 
[**list_os_builtin_blu_rays**](OsBuiltinBluRaysApi.md#list_os_builtin_blu_rays) | **GET** /os-builtin-blu-rays/ | 
[**update_os_builtin_blu_ray**](OsBuiltinBluRaysApi.md#update_os_builtin_blu_ray) | **PATCH** /os-builtin-blu-rays/{builtin_blu_ray_id} | 


# **create_os_builtin_blu_ray**
> OSBuiltinBluRayResp create_os_builtin_blu_ray(body)



Create an os builtin blu ray

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
api_instance = xms_client.OsBuiltinBluRaysApi(xms_client.ApiClient(configuration))
body = xms_client.OSBuiltinBluRayCreateReq() # OSBuiltinBluRayCreateReq | builtin blu ray info

try:
    api_response = api_instance.create_os_builtin_blu_ray(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBuiltinBluRaysApi->create_os_builtin_blu_ray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OSBuiltinBluRayCreateReq**](OSBuiltinBluRayCreateReq.md)| builtin blu ray info | 

### Return type

[**OSBuiltinBluRayResp**](OSBuiltinBluRayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_os_builtin_blu_ray**
> delete_os_builtin_blu_ray(builtin_blu_ray_id)



Delete an os builtin blu ray

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
api_instance = xms_client.OsBuiltinBluRaysApi(xms_client.ApiClient(configuration))
builtin_blu_ray_id = 789 # int | builtin blu ray id

try:
    api_instance.delete_os_builtin_blu_ray(builtin_blu_ray_id)
except ApiException as e:
    print("Exception when calling OsBuiltinBluRaysApi->delete_os_builtin_blu_ray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **builtin_blu_ray_id** | **int**| builtin blu ray id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_builtin_blu_ray**
> OSBuiltinBluRayResp get_os_builtin_blu_ray(builtin_blu_ray_id)



Get an os builtin blu ray

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
api_instance = xms_client.OsBuiltinBluRaysApi(xms_client.ApiClient(configuration))
builtin_blu_ray_id = 789 # int | builtin blu ray id

try:
    api_response = api_instance.get_os_builtin_blu_ray(builtin_blu_ray_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBuiltinBluRaysApi->get_os_builtin_blu_ray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **builtin_blu_ray_id** | **int**| builtin blu ray id | 

### Return type

[**OSBuiltinBluRayResp**](OSBuiltinBluRayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_builtin_blu_rays**
> OSBuiltinBluRaysResp list_os_builtin_blu_rays(limit=limit, offset=offset, q=q, sort=sort)



List os builtin blu rays

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
api_instance = xms_client.OsBuiltinBluRaysApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_os_builtin_blu_rays(limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBuiltinBluRaysApi->list_os_builtin_blu_rays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**OSBuiltinBluRaysResp**](OSBuiltinBluRaysResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_os_builtin_blu_ray**
> OSBuiltinBluRayResp update_os_builtin_blu_ray(builtin_blu_ray_id, body)



update os builtin blu ray

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
api_instance = xms_client.OsBuiltinBluRaysApi(xms_client.ApiClient(configuration))
builtin_blu_ray_id = 789 # int | builtin blu ray id
body = xms_client.OSBuiltinBluRayUpdateReq() # OSBuiltinBluRayUpdateReq | builtin blu ray info

try:
    api_response = api_instance.update_os_builtin_blu_ray(builtin_blu_ray_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBuiltinBluRaysApi->update_os_builtin_blu_ray: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **builtin_blu_ray_id** | **int**| builtin blu ray id | 
 **body** | [**OSBuiltinBluRayUpdateReq**](OSBuiltinBluRayUpdateReq.md)| builtin blu ray info | 

### Return type

[**OSBuiltinBluRayResp**](OSBuiltinBluRayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

