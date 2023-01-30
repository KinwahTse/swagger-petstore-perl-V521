# xms_client.HostEncSpecsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_host_enc_spec**](HostEncSpecsApi.md#create_host_enc_spec) | **POST** /host-enc-specs/ | 
[**delete_host_enc_spec**](HostEncSpecsApi.md#delete_host_enc_spec) | **DELETE** /host-enc-specs/{spec_id} | 
[**get_host_enc_spec**](HostEncSpecsApi.md#get_host_enc_spec) | **GET** /host-enc-specs/{spec_id} | 
[**list_host_enc_specs**](HostEncSpecsApi.md#list_host_enc_specs) | **GET** /host-enc-specs/ | 


# **create_host_enc_spec**
> HostEncSpecResp create_host_enc_spec(body)



Create a host enclosure spec

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
api_instance = xms_client.HostEncSpecsApi(xms_client.ApiClient(configuration))
body = xms_client.HostEncSpecCreateReq() # HostEncSpecCreateReq | host enclosure spec info

try:
    api_response = api_instance.create_host_enc_spec(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostEncSpecsApi->create_host_enc_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostEncSpecCreateReq**](HostEncSpecCreateReq.md)| host enclosure spec info | 

### Return type

[**HostEncSpecResp**](HostEncSpecResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_host_enc_spec**
> delete_host_enc_spec(spec_id)



Delete a host enclosure spec

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
api_instance = xms_client.HostEncSpecsApi(xms_client.ApiClient(configuration))
spec_id = 789 # int | host enclosure spec id

try:
    api_instance.delete_host_enc_spec(spec_id)
except ApiException as e:
    print("Exception when calling HostEncSpecsApi->delete_host_enc_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **int**| host enclosure spec id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_enc_spec**
> HostEncSpecResp get_host_enc_spec(spec_id)



Get host enclosure spec

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
api_instance = xms_client.HostEncSpecsApi(xms_client.ApiClient(configuration))
spec_id = 789 # int | host enclosure spec id

try:
    api_response = api_instance.get_host_enc_spec(spec_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostEncSpecsApi->get_host_enc_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_id** | **int**| host enclosure spec id | 

### Return type

[**HostEncSpecResp**](HostEncSpecResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_host_enc_specs**
> HostEncSpecsResp list_host_enc_specs(limit=limit, offset=offset, model=model, vendor=vendor)



List host enclosure specs

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
api_instance = xms_client.HostEncSpecsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
model = 'model_example' # str | host model (optional)
vendor = 'vendor_example' # str | host vendor (optional)

try:
    api_response = api_instance.list_host_enc_specs(limit=limit, offset=offset, model=model, vendor=vendor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostEncSpecsApi->list_host_enc_specs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **model** | **str**| host model | [optional] 
 **vendor** | **str**| host vendor | [optional] 

### Return type

[**HostEncSpecsResp**](HostEncSpecsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

