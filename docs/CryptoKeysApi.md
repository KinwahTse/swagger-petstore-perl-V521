# xms_client.CryptoKeysApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_crypto_key**](CryptoKeysApi.md#create_crypto_key) | **POST** /crypto-keys/ | 
[**download_crypto_key**](CryptoKeysApi.md#download_crypto_key) | **GET** /crypto-keys/{key_id}/key | 
[**get_crypto_key**](CryptoKeysApi.md#get_crypto_key) | **GET** /crypto-keys/{key_id} | 
[**list_crypto_keys**](CryptoKeysApi.md#list_crypto_keys) | **GET** /crypto-keys/ | 
[**update_crypto_key**](CryptoKeysApi.md#update_crypto_key) | **PATCH** /crypto-keys/{key_id} | 


# **create_crypto_key**
> CryptoKeyResp create_crypto_key(name, key=key)



Create a crypto key

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
api_instance = xms_client.CryptoKeysApi(xms_client.ApiClient(configuration))
name = 'name_example' # str | crypto key name
key = 'key_example' # str | crypto key (optional)

try:
    api_response = api_instance.create_crypto_key(name, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoKeysApi->create_crypto_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| crypto key name | 
 **key** | **str**| crypto key | [optional] 

### Return type

[**CryptoKeyResp**](CryptoKeyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_crypto_key**
> str download_crypto_key(key_id, password=password)



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
api_instance = xms_client.CryptoKeysApi(xms_client.ApiClient(configuration))
key_id = 789 # int | crypto key id
password = 'password_example' # str | password (optional)

try:
    api_response = api_instance.download_crypto_key(key_id, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoKeysApi->download_crypto_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**| crypto key id | 
 **password** | **str**| password | [optional] 

### Return type

**str**

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_key**
> CryptoKeyResp get_crypto_key(key_id)



Get a crypto key

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
api_instance = xms_client.CryptoKeysApi(xms_client.ApiClient(configuration))
key_id = 789 # int | crypto key id

try:
    api_response = api_instance.get_crypto_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoKeysApi->get_crypto_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**| crypto key id | 

### Return type

[**CryptoKeyResp**](CryptoKeyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crypto_keys**
> CryptoKeysResp list_crypto_keys(limit=limit, offset=offset, q=q, sort=sort)



List crypto keys

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
api_instance = xms_client.CryptoKeysApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_crypto_keys(limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoKeysApi->list_crypto_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**CryptoKeysResp**](CryptoKeysResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crypto_key**
> CryptoKeyResp update_crypto_key(key_id, body)



Update a crypto key

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
api_instance = xms_client.CryptoKeysApi(xms_client.ApiClient(configuration))
key_id = 789 # int | crypto key id
body = xms_client.CryptoKeyUpdateReq() # CryptoKeyUpdateReq | crypto key info

try:
    api_response = api_instance.update_crypto_key(key_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoKeysApi->update_crypto_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**| crypto key id | 
 **body** | [**CryptoKeyUpdateReq**](CryptoKeyUpdateReq.md)| crypto key info | 

### Return type

[**CryptoKeyResp**](CryptoKeyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

