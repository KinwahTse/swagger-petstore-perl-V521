# xms_client.OsZonePairsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_os_zone_pairs**](OsZonePairsApi.md#list_os_zone_pairs) | **GET** /os-zone-pairs/ | 


# **list_os_zone_pairs**
> OSZonePairsResp list_os_zone_pairs(min_clock_diff_abs=min_clock_diff_abs, cluster_id=cluster_id)



list os zone pairs

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
api_instance = xms_client.OsZonePairsApi(xms_client.ApiClient(configuration))
min_clock_diff_abs = 'min_clock_diff_abs_example' # str | min clock diff absolute value for zone pairs (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_os_zone_pairs(min_clock_diff_abs=min_clock_diff_abs, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZonePairsApi->list_os_zone_pairs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_clock_diff_abs** | **str**| min clock diff absolute value for zone pairs | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSZonePairsResp**](OSZonePairsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

