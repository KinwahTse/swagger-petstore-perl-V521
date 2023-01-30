# xms_client.LunsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lun**](LunsApi.md#get_lun) | **GET** /luns/{lun_id} | 
[**list_luns**](LunsApi.md#list_luns) | **GET** /luns/ | 


# **get_lun**
> LunResp get_lun(lun_id)



get a lun

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
api_instance = xms_client.LunsApi(xms_client.ApiClient(configuration))
lun_id = 789 # int | lun id

try:
    api_response = api_instance.get_lun(lun_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LunsApi->get_lun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lun_id** | **int**| lun id | 

### Return type

[**LunResp**](LunResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_luns**
> LunsResp list_luns(limit=limit, offset=offset, mapping_group_id=mapping_group_id, cluster_id=cluster_id)



List luns

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
api_instance = xms_client.LunsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
mapping_group_id = 789 # int | mapping group id (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_luns(limit=limit, offset=offset, mapping_group_id=mapping_group_id, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LunsApi->list_luns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **mapping_group_id** | **int**| mapping group id | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**LunsResp**](LunsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

