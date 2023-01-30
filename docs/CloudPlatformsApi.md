# xms_client.CloudPlatformsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_platform**](CloudPlatformsApi.md#create_cloud_platform) | **POST** /cloud-platforms/ | 
[**delete_cloud_platform**](CloudPlatformsApi.md#delete_cloud_platform) | **DELETE** /cloud-platforms/{cloud_platform_id} | 
[**get_cloud_platform**](CloudPlatformsApi.md#get_cloud_platform) | **GET** /cloud-platforms/{cloud_platform_id} | 
[**list_cloud_platforms**](CloudPlatformsApi.md#list_cloud_platforms) | **GET** /cloud-platforms/ | 
[**sync_cloud_platform**](CloudPlatformsApi.md#sync_cloud_platform) | **POST** /cloud-platforms/{cloud_platform_id}:sync | 
[**update_cloud_platform**](CloudPlatformsApi.md#update_cloud_platform) | **PATCH** /cloud-platforms/{cloud_platform_id} | 


# **create_cloud_platform**
> CloudPlatformResp create_cloud_platform(body)



Create cloud platform

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
api_instance = xms_client.CloudPlatformsApi(xms_client.ApiClient(configuration))
body = xms_client.CloudPlatformCreateReq() # CloudPlatformCreateReq | cloud platform info

try:
    api_response = api_instance.create_cloud_platform(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPlatformsApi->create_cloud_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudPlatformCreateReq**](CloudPlatformCreateReq.md)| cloud platform info | 

### Return type

[**CloudPlatformResp**](CloudPlatformResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_platform**
> delete_cloud_platform(cloud_platform_id)



Delete cloud platform

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
api_instance = xms_client.CloudPlatformsApi(xms_client.ApiClient(configuration))
cloud_platform_id = 789 # int | cloud platform id

try:
    api_instance.delete_cloud_platform(cloud_platform_id)
except ApiException as e:
    print("Exception when calling CloudPlatformsApi->delete_cloud_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_platform_id** | **int**| cloud platform id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_platform**
> CloudPlatformResp get_cloud_platform(cloud_platform_id)



Get a cloud platform

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
api_instance = xms_client.CloudPlatformsApi(xms_client.ApiClient(configuration))
cloud_platform_id = 789 # int | cloud platform id

try:
    api_response = api_instance.get_cloud_platform(cloud_platform_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPlatformsApi->get_cloud_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_platform_id** | **int**| cloud platform id | 

### Return type

[**CloudPlatformResp**](CloudPlatformResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_platforms**
> CloudPlatformsResp list_cloud_platforms(limit=limit, offset=offset)



List cloud platforms

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
api_instance = xms_client.CloudPlatformsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_cloud_platforms(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPlatformsApi->list_cloud_platforms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**CloudPlatformsResp**](CloudPlatformsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_cloud_platform**
> CloudPlatformResp sync_cloud_platform(cloud_platform_id)



Sync a cloud platform

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
api_instance = xms_client.CloudPlatformsApi(xms_client.ApiClient(configuration))
cloud_platform_id = 789 # int | cloud platform id

try:
    api_response = api_instance.sync_cloud_platform(cloud_platform_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPlatformsApi->sync_cloud_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_platform_id** | **int**| cloud platform id | 

### Return type

[**CloudPlatformResp**](CloudPlatformResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_platform**
> CloudPlatformResp update_cloud_platform(cloud_platform_id, body)



Update a cloud platform

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
api_instance = xms_client.CloudPlatformsApi(xms_client.ApiClient(configuration))
cloud_platform_id = 789 # int | cloud platform id
body = xms_client.CloudPlatformUpdateReq() # CloudPlatformUpdateReq | cloud platform info

try:
    api_response = api_instance.update_cloud_platform(cloud_platform_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPlatformsApi->update_cloud_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_platform_id** | **int**| cloud platform id | 
 **body** | [**CloudPlatformUpdateReq**](CloudPlatformUpdateReq.md)| cloud platform info | 

### Return type

[**CloudPlatformResp**](CloudPlatformResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

