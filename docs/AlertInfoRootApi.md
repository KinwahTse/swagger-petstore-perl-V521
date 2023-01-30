# xms_client.AlertInfoRootApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_alert_info_root**](AlertInfoRootApi.md#ack_alert_info_root) | **POST** /alert-info-root/:ack | 
[**get_alert_info_root**](AlertInfoRootApi.md#get_alert_info_root) | **GET** /alert-info-root/ | 
[**resolve_alert_info_root**](AlertInfoRootApi.md#resolve_alert_info_root) | **POST** /alert-info-root/:resolve | 


# **ack_alert_info_root**
> AlertInfoRootResp ack_alert_info_root()



set the acked status of all alert infos

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
api_instance = xms_client.AlertInfoRootApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.ack_alert_info_root()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfoRootApi->ack_alert_info_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertInfoRootResp**](AlertInfoRootResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_info_root**
> AlertInfoRootResp get_alert_info_root()



get the alert info root

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
api_instance = xms_client.AlertInfoRootApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.get_alert_info_root()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfoRootApi->get_alert_info_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertInfoRootResp**](AlertInfoRootResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_alert_info_root**
> AlertInfoRootResp resolve_alert_info_root()



set the resolved status of all alert infos

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
api_instance = xms_client.AlertInfoRootApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.resolve_alert_info_root()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfoRootApi->resolve_alert_info_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertInfoRootResp**](AlertInfoRootResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

