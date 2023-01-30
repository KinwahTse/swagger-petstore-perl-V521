# xms_client.LicensesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_license**](LicensesApi.md#disable_license) | **POST** /licenses/{license_id}:disable | 
[**download_license_key**](LicensesApi.md#download_license_key) | **GET** /licenses/key | 
[**get_license**](LicensesApi.md#get_license) | **GET** /licenses/{license_id} | 
[**get_license_summary**](LicensesApi.md#get_license_summary) | **GET** /licenses/summary | 
[**list_licenses**](LicensesApi.md#list_licenses) | **GET** /licenses/ | 
[**register_license**](LicensesApi.md#register_license) | **POST** /licenses/ | 


# **disable_license**
> LicenseResp disable_license(license_id, force=force)



disable license

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
api_instance = xms_client.LicensesApi(xms_client.ApiClient(configuration))
license_id = 789 # int | the license id
force = true # bool | force disable not expired license (optional)

try:
    api_response = api_instance.disable_license(license_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensesApi->disable_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **int**| the license id | 
 **force** | **bool**| force disable not expired license | [optional] 

### Return type

[**LicenseResp**](LicenseResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_license_key**
> str download_license_key()



get license key file

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = xms_client.LicensesApi()

try:
    api_response = api_instance.download_license_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensesApi->download_license_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license**
> LicenseResp get_license(license_id)



get license

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
api_instance = xms_client.LicensesApi(xms_client.ApiClient(configuration))
license_id = 789 # int | the license id

try:
    api_response = api_instance.get_license(license_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensesApi->get_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **int**| the license id | 

### Return type

[**LicenseResp**](LicenseResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_summary**
> LicenseSummaryResp get_license_summary()



Get licenses sumary

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = xms_client.LicensesApi()

try:
    api_response = api_instance.get_license_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensesApi->get_license_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseSummaryResp**](LicenseSummaryResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_licenses**
> LicensesResp list_licenses(limit=limit, offset=offset, q=q, sort=sort, active=active)



List licenses

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = xms_client.LicensesApi()
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
active = true # bool | filter license by active status (optional)

try:
    api_response = api_instance.list_licenses(limit=limit, offset=offset, q=q, sort=sort, active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensesApi->list_licenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **active** | **bool**| filter license by active status | [optional] 

### Return type

[**LicensesResp**](LicensesResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_license**
> LicenseResp register_license(license, force=force, dry_run=dry_run)



Activate product license

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
api_instance = xms_client.LicensesApi(xms_client.ApiClient(configuration))
license = '/path/to/file.txt' # file | license info
force = true # bool | force activate (optional)
dry_run = true # bool | dry run upload license file (optional)

try:
    api_response = api_instance.register_license(license, force=force, dry_run=dry_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensesApi->register_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license** | **file**| license info | 
 **force** | **bool**| force activate | [optional] 
 **dry_run** | **bool**| dry run upload license file | [optional] 

### Return type

[**LicenseResp**](LicenseResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

