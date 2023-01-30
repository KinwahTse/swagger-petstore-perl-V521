# xms_client.AuthApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rsa_key**](AuthApi.md#create_rsa_key) | **POST** /auth/rsa-keys | 
[**create_token**](AuthApi.md#create_token) | **POST** /auth/tokens | 
[**get_auth_security_policy**](AuthApi.md#get_auth_security_policy) | **GET** /auth/security-policy | 
[**login**](AuthApi.md#login) | **POST** /auth/tokens:login | 
[**logout**](AuthApi.md#logout) | **POST** /auth/tokens:logout | 
[**update_auth_security_policy**](AuthApi.md#update_auth_security_policy) | **PATCH** /auth/security-policy | 
[**validate_privileged_token**](AuthApi.md#validate_privileged_token) | **POST** /auth/:validate-privileged-token | 


# **create_rsa_key**
> AuthRSAKeyResp create_rsa_key()



Create RSA key

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = xms_client.AuthApi()

try:
    api_response = api_instance.create_rsa_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_rsa_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthRSAKeyResp**](AuthRSAKeyResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token**
> TokenResp create_token(body)



creates temporary token for credentials

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = xms_client.AuthApi()
body = xms_client.TokenCreateReq() # TokenCreateReq | the identity credential

try:
    api_response = api_instance.create_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenCreateReq**](TokenCreateReq.md)| the identity credential | 

### Return type

[**TokenResp**](TokenResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_security_policy**
> AuthSecurityPolicyResp get_auth_security_policy()



setup auth security policy

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
api_instance = xms_client.AuthApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.get_auth_security_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_security_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthSecurityPolicyResp**](AuthSecurityPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> TokenResp login(body)



logs in

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = xms_client.AuthApi()
body = xms_client.AuthLoginReq() # AuthLoginReq | the identity credential

try:
    api_response = api_instance.login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthLoginReq**](AuthLoginReq.md)| the identity credential | 

### Return type

[**TokenResp**](TokenResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()



logs out

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
api_instance = xms_client.AuthApi(xms_client.ApiClient(configuration))

try:
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_security_policy**
> AuthSecurityPolicyResp update_auth_security_policy(body)



update auth security policy

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
api_instance = xms_client.AuthApi(xms_client.ApiClient(configuration))
body = xms_client.AuthSecurityPolicyUpdateReq() # AuthSecurityPolicyUpdateReq | auth security policy info

try:
    api_response = api_instance.update_auth_security_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->update_auth_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthSecurityPolicyUpdateReq**](AuthSecurityPolicyUpdateReq.md)| auth security policy info | 

### Return type

[**AuthSecurityPolicyResp**](AuthSecurityPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_privileged_token**
> PrivilegedTokenResp validate_privileged_token(body)



validate privileged token in some operations

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
api_instance = xms_client.AuthApi(xms_client.ApiClient(configuration))
body = xms_client.PrivilegedTokenReq() # PrivilegedTokenReq | privileged token info

try:
    api_response = api_instance.validate_privileged_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->validate_privileged_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PrivilegedTokenReq**](PrivilegedTokenReq.md)| privileged token info | 

### Return type

[**PrivilegedTokenResp**](PrivilegedTokenResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

