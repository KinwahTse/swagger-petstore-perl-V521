# xms_client.IdentityPlatformsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_platform**](IdentityPlatformsApi.md#create_identity_platform) | **POST** /identity-platforms/ | 
[**delete_identity_platform**](IdentityPlatformsApi.md#delete_identity_platform) | **DELETE** /identity-platforms/{identity_platform_id} | 
[**get_identity_platform**](IdentityPlatformsApi.md#get_identity_platform) | **GET** /identity-platforms/{identity_platform_id} | 
[**list_identity_platforms**](IdentityPlatformsApi.md#list_identity_platforms) | **GET** /identity-platforms/ | 
[**login_sso_types**](IdentityPlatformsApi.md#login_sso_types) | **GET** /identity-platforms/types | 
[**regenerate_identity_key**](IdentityPlatformsApi.md#regenerate_identity_key) | **POST** /identity-platforms/{identity_platform_id}:regenerate | 
[**update_identity_platform**](IdentityPlatformsApi.md#update_identity_platform) | **PATCH** /identity-platforms/{identity_platform_id} | 


# **create_identity_platform**
> IdentityPlatformResp create_identity_platform(body)



Create identity platform

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
api_instance = xms_client.IdentityPlatformsApi(xms_client.ApiClient(configuration))
body = xms_client.IdentityPlatformCreateReq() # IdentityPlatformCreateReq | identity platform info

try:
    api_response = api_instance.create_identity_platform(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityPlatformsApi->create_identity_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityPlatformCreateReq**](IdentityPlatformCreateReq.md)| identity platform info | 

### Return type

[**IdentityPlatformResp**](IdentityPlatformResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_platform**
> delete_identity_platform(identity_platform_id)



Delete identity platform

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
api_instance = xms_client.IdentityPlatformsApi(xms_client.ApiClient(configuration))
identity_platform_id = 789 # int | identity platform id

try:
    api_instance.delete_identity_platform(identity_platform_id)
except ApiException as e:
    print("Exception when calling IdentityPlatformsApi->delete_identity_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_platform_id** | **int**| identity platform id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_platform**
> IdentityPlatformResp get_identity_platform(identity_platform_id)



Get a identity platform

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
api_instance = xms_client.IdentityPlatformsApi(xms_client.ApiClient(configuration))
identity_platform_id = 789 # int | identity platform id

try:
    api_response = api_instance.get_identity_platform(identity_platform_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityPlatformsApi->get_identity_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_platform_id** | **int**| identity platform id | 

### Return type

[**IdentityPlatformResp**](IdentityPlatformResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_platforms**
> IdentityPlatformsResp list_identity_platforms(limit=limit, offset=offset)



List identity platforms

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
api_instance = xms_client.IdentityPlatformsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_identity_platforms(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityPlatformsApi->list_identity_platforms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**IdentityPlatformsResp**](IdentityPlatformsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_sso_types**
> LoginSsoTypesResp login_sso_types()



List SSO Protocol Types

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
api_instance = xms_client.IdentityPlatformsApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.login_sso_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityPlatformsApi->login_sso_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginSsoTypesResp**](LoginSsoTypesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_identity_key**
> IdentityPlatformResp regenerate_identity_key(identity_platform_id)



regenereate a identity platform key

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
api_instance = xms_client.IdentityPlatformsApi(xms_client.ApiClient(configuration))
identity_platform_id = 789 # int | identity platform id

try:
    api_response = api_instance.regenerate_identity_key(identity_platform_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityPlatformsApi->regenerate_identity_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_platform_id** | **int**| identity platform id | 

### Return type

[**IdentityPlatformResp**](IdentityPlatformResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_identity_platform**
> IdentityPlatformResp update_identity_platform(identity_platform_id, body)



Update a identity platform

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
api_instance = xms_client.IdentityPlatformsApi(xms_client.ApiClient(configuration))
identity_platform_id = 789 # int | identity platform id
body = xms_client.IdentityPlatformUpdateReq() # IdentityPlatformUpdateReq | identity platform info

try:
    api_response = api_instance.update_identity_platform(identity_platform_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityPlatformsApi->update_identity_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_platform_id** | **int**| identity platform id | 
 **body** | [**IdentityPlatformUpdateReq**](IdentityPlatformUpdateReq.md)| identity platform info | 

### Return type

[**IdentityPlatformResp**](IdentityPlatformResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

