# xms_client.DnsDomainNamesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dns_domain_name**](DnsDomainNamesApi.md#create_dns_domain_name) | **POST** /dns-domain-names/ | 
[**delete_dns_domain_name**](DnsDomainNamesApi.md#delete_dns_domain_name) | **DELETE** /dns-domain-names/{name_id} | 
[**get_dns_domain_name**](DnsDomainNamesApi.md#get_dns_domain_name) | **GET** /dns-domain-names/{name_id} | 
[**list_dns_domain_names**](DnsDomainNamesApi.md#list_dns_domain_names) | **GET** /dns-domain-names/ | 
[**update_dns_domain_name**](DnsDomainNamesApi.md#update_dns_domain_name) | **PATCH** /dns-domain-names/{name_id} | 


# **create_dns_domain_name**
> DNSDomainNameResp create_dns_domain_name(dns_domain_name)



Create a DNS domain name.

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
api_instance = xms_client.DnsDomainNamesApi(xms_client.ApiClient(configuration))
dns_domain_name = xms_client.DNSDomainNameCreateReq() # DNSDomainNameCreateReq | DNS domain name info

try:
    api_response = api_instance.create_dns_domain_name(dns_domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsDomainNamesApi->create_dns_domain_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dns_domain_name** | [**DNSDomainNameCreateReq**](DNSDomainNameCreateReq.md)| DNS domain name info | 

### Return type

[**DNSDomainNameResp**](DNSDomainNameResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dns_domain_name**
> delete_dns_domain_name(name_id)



Delete a DNS domain nam.

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
api_instance = xms_client.DnsDomainNamesApi(xms_client.ApiClient(configuration))
name_id = 789 # int | DNS domain name id

try:
    api_instance.delete_dns_domain_name(name_id)
except ApiException as e:
    print("Exception when calling DnsDomainNamesApi->delete_dns_domain_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_id** | **int**| DNS domain name id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_domain_name**
> DNSDomainNameResp get_dns_domain_name(name_id)



Get a dns domain name

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
api_instance = xms_client.DnsDomainNamesApi(xms_client.ApiClient(configuration))
name_id = 789 # int | dns domain name id

try:
    api_response = api_instance.get_dns_domain_name(name_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsDomainNamesApi->get_dns_domain_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_id** | **int**| dns domain name id | 

### Return type

[**DNSDomainNameResp**](DNSDomainNameResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dns_domain_names**
> DNSDomainNamesResp list_dns_domain_names(limit=limit, offset=offset, dns_zone_id=dns_zone_id)



List dns domain names

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
api_instance = xms_client.DnsDomainNamesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
dns_zone_id = 789 # int | dns zone id (optional)

try:
    api_response = api_instance.list_dns_domain_names(limit=limit, offset=offset, dns_zone_id=dns_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsDomainNamesApi->list_dns_domain_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **dns_zone_id** | **int**| dns zone id | [optional] 

### Return type

[**DNSDomainNamesResp**](DNSDomainNamesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dns_domain_name**
> DNSDomainNameResp update_dns_domain_name(name_id, dns_domain_name)



Update a DNS domain name

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
api_instance = xms_client.DnsDomainNamesApi(xms_client.ApiClient(configuration))
name_id = 789 # int | DNS domain name id
dns_domain_name = xms_client.DNSDomainNameUpdateReq() # DNSDomainNameUpdateReq | DNS domain name info

try:
    api_response = api_instance.update_dns_domain_name(name_id, dns_domain_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsDomainNamesApi->update_dns_domain_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_id** | **int**| DNS domain name id | 
 **dns_domain_name** | [**DNSDomainNameUpdateReq**](DNSDomainNameUpdateReq.md)| DNS domain name info | 

### Return type

[**DNSDomainNameResp**](DNSDomainNameResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

