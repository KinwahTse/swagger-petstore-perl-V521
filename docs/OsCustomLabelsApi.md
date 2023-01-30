# xms_client.OsCustomLabelsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_os_custom_label**](OsCustomLabelsApi.md#get_os_custom_label) | **GET** /os-custom-labels/{os_custom_label_id} | 
[**list_os_custom_labels**](OsCustomLabelsApi.md#list_os_custom_labels) | **GET** /os-custom-labels/ | 


# **get_os_custom_label**
> OSCustomLabelResp get_os_custom_label(os_custom_label_id)



Get object storage custom label

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
api_instance = xms_client.OsCustomLabelsApi(xms_client.ApiClient(configuration))
os_custom_label_id = 789 # int | os custom label id

try:
    api_response = api_instance.get_os_custom_label(os_custom_label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsCustomLabelsApi->get_os_custom_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_custom_label_id** | **int**| os custom label id | 

### Return type

[**OSCustomLabelResp**](OSCustomLabelResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_custom_labels**
> OSCustomLabelsResp list_os_custom_labels(bucket_id=bucket_id, category=category, cluster_id=cluster_id, limit=limit, offset=offset)



List object storage custom labels

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
api_instance = xms_client.OsCustomLabelsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id (optional)
category = 'category_example' # str | label category: meta, default, tagging (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_os_custom_labels(bucket_id=bucket_id, category=category, cluster_id=cluster_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsCustomLabelsApi->list_os_custom_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | [optional] 
 **category** | **str**| label category: meta, default, tagging | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**OSCustomLabelsResp**](OSCustomLabelsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

