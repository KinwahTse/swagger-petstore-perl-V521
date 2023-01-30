# xms_client.OsSearchGatewaysApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_os_search_gateway_samples**](OsSearchGatewaysApi.md#get_os_search_gateway_samples) | **GET** /os-search-gateways/{gateway_id}/samples | 
[**get_os_search_gateways**](OsSearchGatewaysApi.md#get_os_search_gateways) | **GET** /os-search-gateways/{gateway_id} | 
[**list_os_search_gateways**](OsSearchGatewaysApi.md#list_os_search_gateways) | **GET** /os-search-gateways/ | 


# **get_os_search_gateway_samples**
> OSSearchGatewaySamplesResp get_os_search_gateway_samples(gateway_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a os search gateway's samples

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
api_instance = xms_client.OsSearchGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | os search gateway id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_os_search_gateway_samples(gateway_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchGatewaysApi->get_os_search_gateway_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| os search gateway id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**OSSearchGatewaySamplesResp**](OSSearchGatewaySamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_search_gateways**
> OSSearchGatewayResp get_os_search_gateways(gateway_id)



Get OS Search Gateway

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
api_instance = xms_client.OsSearchGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | os search gateway id

try:
    api_response = api_instance.get_os_search_gateways(gateway_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchGatewaysApi->get_os_search_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| os search gateway id | 

### Return type

[**OSSearchGatewayResp**](OSSearchGatewayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_search_gateways**
> OSSearchGatewaysResp list_os_search_gateways(os_search_engine_id=os_search_engine_id, cluster_id=cluster_id, q=q, sort=sort)



List OS Search Gateways

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
api_instance = xms_client.OsSearchGatewaysApi(xms_client.ApiClient(configuration))
os_search_engine_id = 789 # int | os search engine id (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_os_search_gateways(os_search_engine_id=os_search_engine_id, cluster_id=cluster_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchGatewaysApi->list_os_search_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_search_engine_id** | **int**| os search engine id | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**OSSearchGatewaysResp**](OSSearchGatewaysResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

