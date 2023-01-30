# xms_client.DfsGatewayZonesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dfs_gateway_zone**](DfsGatewayZonesApi.md#create_dfs_gateway_zone) | **POST** /dfs-gateway-zones/ | 
[**delete_dfs_gateway_zone**](DfsGatewayZonesApi.md#delete_dfs_gateway_zone) | **DELETE** /dfs-gateway-zones/{dfs_gateway_zone_id} | 
[**get_dfs_gateway_zone**](DfsGatewayZonesApi.md#get_dfs_gateway_zone) | **GET** /dfs-gateway-zones/{dfs_gateway_zone_id} | 
[**get_dfs_gateway_zone_samples**](DfsGatewayZonesApi.md#get_dfs_gateway_zone_samples) | **GET** /dfs-gateway-zones/{dfs_gateway_zone_id}/samples | 
[**list_dfs_gateway_zones**](DfsGatewayZonesApi.md#list_dfs_gateway_zones) | **GET** /dfs-gateway-zones/ | 
[**update_dfs_gateway_zone**](DfsGatewayZonesApi.md#update_dfs_gateway_zone) | **PATCH** /dfs-gateway-zones/{dfs_gateway_zone_id} | 


# **create_dfs_gateway_zone**
> DfsGatewayZoneResp create_dfs_gateway_zone(body, cluster_id=cluster_id)



Create dfs gateway zone

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
api_instance = xms_client.DfsGatewayZonesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsGatewayZoneCreateReq() # DfsGatewayZoneCreateReq | gateway zone info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_dfs_gateway_zone(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayZonesApi->create_dfs_gateway_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsGatewayZoneCreateReq**](DfsGatewayZoneCreateReq.md)| gateway zone info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**DfsGatewayZoneResp**](DfsGatewayZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_gateway_zone**
> DfsGatewayZoneResp delete_dfs_gateway_zone(dfs_gateway_zone_id, force=force)



delete dfs gateway zone

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
api_instance = xms_client.DfsGatewayZonesApi(xms_client.ApiClient(configuration))
dfs_gateway_zone_id = 789 # int | gateway zone id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_dfs_gateway_zone(dfs_gateway_zone_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayZonesApi->delete_dfs_gateway_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_zone_id** | **int**| gateway zone id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DfsGatewayZoneResp**](DfsGatewayZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_gateway_zone**
> DfsGatewayZoneResp get_dfs_gateway_zone(dfs_gateway_zone_id)



Get dfs gateway zone

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
api_instance = xms_client.DfsGatewayZonesApi(xms_client.ApiClient(configuration))
dfs_gateway_zone_id = 789 # int | gateway zone id

try:
    api_response = api_instance.get_dfs_gateway_zone(dfs_gateway_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayZonesApi->get_dfs_gateway_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_zone_id** | **int**| gateway zone id | 

### Return type

[**DfsGatewayZoneResp**](DfsGatewayZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_gateway_zone_samples**
> DfsGatewayZoneSamplesResp get_dfs_gateway_zone_samples(dfs_gateway_zone_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a dfs gateway zone's samples

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
api_instance = xms_client.DfsGatewayZonesApi(xms_client.ApiClient(configuration))
dfs_gateway_zone_id = 789 # int | dfs gateway zone id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_dfs_gateway_zone_samples(dfs_gateway_zone_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayZonesApi->get_dfs_gateway_zone_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_zone_id** | **int**| dfs gateway zone id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**DfsGatewayZoneSamplesResp**](DfsGatewayZoneSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_gateway_zones**
> DfsGatewayZonesResp list_dfs_gateway_zones(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id)



List dfs gateway zones

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
api_instance = xms_client.DfsGatewayZonesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_dfs_gateway_zones(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayZonesApi->list_dfs_gateway_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**DfsGatewayZonesResp**](DfsGatewayZonesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_gateway_zone**
> DfsGatewayZoneResp update_dfs_gateway_zone(dfs_gateway_zone_id, body)



Update dfs gateway zone

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
api_instance = xms_client.DfsGatewayZonesApi(xms_client.ApiClient(configuration))
dfs_gateway_zone_id = 789 # int | gateway zone id
body = xms_client.DfsGatewayZoneUpdateReq() # DfsGatewayZoneUpdateReq | gateway zone info

try:
    api_response = api_instance.update_dfs_gateway_zone(dfs_gateway_zone_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayZonesApi->update_dfs_gateway_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_zone_id** | **int**| gateway zone id | 
 **body** | [**DfsGatewayZoneUpdateReq**](DfsGatewayZoneUpdateReq.md)| gateway zone info | 

### Return type

[**DfsGatewayZoneResp**](DfsGatewayZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

