# xms_client.SslCertificatesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ssl_certificate**](SslCertificatesApi.md#create_ssl_certificate) | **POST** /ssl-certificates/ | 
[**delete_ssl_certificate**](SslCertificatesApi.md#delete_ssl_certificate) | **DELETE** /ssl-certificates/{certificate_id} | 
[**get_ssl_certificate**](SslCertificatesApi.md#get_ssl_certificate) | **GET** /ssl-certificates/{certificate_id} | 
[**list_ssl_certificates**](SslCertificatesApi.md#list_ssl_certificates) | **GET** /ssl-certificates/ | 
[**update_ssl_certificate**](SslCertificatesApi.md#update_ssl_certificate) | **PATCH** /ssl-certificates/{certificate_id} | 


# **create_ssl_certificate**
> SSLCertificateResp create_ssl_certificate(body)



Create ssl certificate

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
api_instance = xms_client.SslCertificatesApi(xms_client.ApiClient(configuration))
body = xms_client.SSLCertificateCreateReq() # SSLCertificateCreateReq | ssl certificate info

try:
    api_response = api_instance.create_ssl_certificate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslCertificatesApi->create_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SSLCertificateCreateReq**](SSLCertificateCreateReq.md)| ssl certificate info | 

### Return type

[**SSLCertificateResp**](SSLCertificateResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ssl_certificate**
> SSLCertificateResp delete_ssl_certificate(certificate_id)



Delete ssl certificate

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
api_instance = xms_client.SslCertificatesApi(xms_client.ApiClient(configuration))
certificate_id = 789 # int | certificate id

try:
    api_response = api_instance.delete_ssl_certificate(certificate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslCertificatesApi->delete_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **int**| certificate id | 

### Return type

[**SSLCertificateResp**](SSLCertificateResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssl_certificate**
> SSLCertificateResp get_ssl_certificate(certificate_id, limit=limit, offset=offset)



Get certificates

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
api_instance = xms_client.SslCertificatesApi(xms_client.ApiClient(configuration))
certificate_id = 789 # int | certificate id
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.get_ssl_certificate(certificate_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslCertificatesApi->get_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **int**| certificate id | 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**SSLCertificateResp**](SSLCertificateResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ssl_certificates**
> SSLCertificatesResp list_ssl_certificates(limit=limit, offset=offset)



List certificates

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
api_instance = xms_client.SslCertificatesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_ssl_certificates(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslCertificatesApi->list_ssl_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**SSLCertificatesResp**](SSLCertificatesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ssl_certificate**
> SSLCertificateResp update_ssl_certificate(certificate_id, body)



Update ssl certificate

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
api_instance = xms_client.SslCertificatesApi(xms_client.ApiClient(configuration))
certificate_id = 789 # int | certificate id
body = xms_client.SSLCertificateUpdateReq() # SSLCertificateUpdateReq | ssl certificate info

try:
    api_response = api_instance.update_ssl_certificate(certificate_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SslCertificatesApi->update_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **int**| certificate id | 
 **body** | [**SSLCertificateUpdateReq**](SSLCertificateUpdateReq.md)| ssl certificate info | 

### Return type

[**SSLCertificateResp**](SSLCertificateResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

