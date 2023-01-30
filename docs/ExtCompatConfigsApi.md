# xms_client.ExtCompatConfigsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_ext_compat_conf**](ExtCompatConfigsApi.md#list_ext_compat_conf) | **GET** /ext-compat-configs/ | 
[**set_ext_compat_conf**](ExtCompatConfigsApi.md#set_ext_compat_conf) | **POST** /ext-compat-configs/ | 


# **list_ext_compat_conf**
> ExtCompatConfResp list_ext_compat_conf(ext_name=ext_name, func_name=func_name, policy=policy, host_id=host_id)



list ext compat conf

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
api_instance = xms_client.ExtCompatConfigsApi(xms_client.ApiClient(configuration))
ext_name = 'ext_name_example' # str | filter the external interface name of ext compat conf (optional)
func_name = 'func_name_example' # str | filter the function name of ext compat conf (optional)
policy = 'policy_example' # str | filter the policy of ext compat conf (optional)
host_id = 789 # int | filter the host of ext compat conf, 0 for global config (optional)

try:
    api_response = api_instance.list_ext_compat_conf(ext_name=ext_name, func_name=func_name, policy=policy, host_id=host_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtCompatConfigsApi->list_ext_compat_conf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ext_name** | **str**| filter the external interface name of ext compat conf | [optional] 
 **func_name** | **str**| filter the function name of ext compat conf | [optional] 
 **policy** | **str**| filter the policy of ext compat conf | [optional] 
 **host_id** | **int**| filter the host of ext compat conf, 0 for global config | [optional] 

### Return type

[**ExtCompatConfResp**](ExtCompatConfResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ext_compat_conf**
> SetExtCompatConfResp set_ext_compat_conf(body)



set ext compat conf

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
api_instance = xms_client.ExtCompatConfigsApi(xms_client.ApiClient(configuration))
body = xms_client.SetExtCompatConfReq() # SetExtCompatConfReq | ext compat conf

try:
    api_response = api_instance.set_ext_compat_conf(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtCompatConfigsApi->set_ext_compat_conf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetExtCompatConfReq**](SetExtCompatConfReq.md)| ext compat conf | 

### Return type

[**SetExtCompatConfResp**](SetExtCompatConfResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

