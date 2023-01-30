# xms_client.AccessTokensApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_token**](AccessTokensApi.md#create_access_token) | **POST** /access-tokens/ | 
[**delete_access_token**](AccessTokensApi.md#delete_access_token) | **DELETE** /access-tokens/{access_token_id} | 
[**get_access_token**](AccessTokensApi.md#get_access_token) | **GET** /access-tokens/{access_token_id} | 
[**list_access_tokens**](AccessTokensApi.md#list_access_tokens) | **GET** /access-tokens/ | 
[**regenerate_access_token**](AccessTokensApi.md#regenerate_access_token) | **POST** /access-tokens/{access_token_id}:regenerate | 
[**update_access_token**](AccessTokensApi.md#update_access_token) | **PATCH** /access-tokens/{access_token_id} | 
[**validate_access_token**](AccessTokensApi.md#validate_access_token) | **POST** /access-tokens:validate | 


# **create_access_token**
> AccessTokenCreateResp create_access_token(body)



Create an access token

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
api_instance = xms_client.AccessTokensApi(xms_client.ApiClient(configuration))
body = xms_client.AccessTokenCreateReq() # AccessTokenCreateReq | access token info

try:
    api_response = api_instance.create_access_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->create_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenCreateReq**](AccessTokenCreateReq.md)| access token info | 

### Return type

[**AccessTokenCreateResp**](AccessTokenCreateResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_token**
> delete_access_token(access_token_id)



delete an access token

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
api_instance = xms_client.AccessTokensApi(xms_client.ApiClient(configuration))
access_token_id = 789 # int | access token id

try:
    api_instance.delete_access_token(access_token_id)
except ApiException as e:
    print("Exception when calling AccessTokensApi->delete_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_id** | **int**| access token id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_token**
> AccessTokenResp get_access_token(access_token_id)



get an access Token

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
api_instance = xms_client.AccessTokensApi(xms_client.ApiClient(configuration))
access_token_id = 789 # int | access token id

try:
    api_response = api_instance.get_access_token(access_token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->get_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_id** | **int**| access token id | 

### Return type

[**AccessTokenResp**](AccessTokenResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_tokens**
> AccessTokensResp list_access_tokens(limit=limit, offset=offset, user_id=user_id, role=role, all=all)



List access tokens

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
api_instance = xms_client.AccessTokensApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
user_id = 789 # int | The id of user access tokens belong to (optional)
role = 'role_example' # str | filter access tokens by role (optional)
all = true # bool | show all access tokens (optional)

try:
    api_response = api_instance.list_access_tokens(limit=limit, offset=offset, user_id=user_id, role=role, all=all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->list_access_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **user_id** | **int**| The id of user access tokens belong to | [optional] 
 **role** | **str**| filter access tokens by role | [optional] 
 **all** | **bool**| show all access tokens | [optional] 

### Return type

[**AccessTokensResp**](AccessTokensResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_access_token**
> AccessTokenCreateResp regenerate_access_token(access_token_id)



regenereate an access token UUID

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
api_instance = xms_client.AccessTokensApi(xms_client.ApiClient(configuration))
access_token_id = 789 # int | access token id

try:
    api_response = api_instance.regenerate_access_token(access_token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->regenerate_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_id** | **int**| access token id | 

### Return type

[**AccessTokenCreateResp**](AccessTokenCreateResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_token**
> AccessTokenResp update_access_token(access_token_id, body)



update an access token

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
api_instance = xms_client.AccessTokensApi(xms_client.ApiClient(configuration))
access_token_id = 789 # int | access token id
body = xms_client.AccessTokenUpdateReq() # AccessTokenUpdateReq | access token info

try:
    api_response = api_instance.update_access_token(access_token_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->update_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_id** | **int**| access token id | 
 **body** | [**AccessTokenUpdateReq**](AccessTokenUpdateReq.md)| access token info | 

### Return type

[**AccessTokenResp**](AccessTokenResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_access_token**
> AccessTokenResp validate_access_token(subject_access_token)



validate an access token

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
api_instance = xms_client.AccessTokensApi(xms_client.ApiClient(configuration))
subject_access_token = 'subject_access_token_example' # str | access token to be validated

try:
    api_response = api_instance.validate_access_token(subject_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->validate_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_access_token** | **str**| access token to be validated | 

### Return type

[**AccessTokenResp**](AccessTokenResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

