# xms_client.DfsGatewaysApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dfs_gateway**](DfsGatewaysApi.md#get_dfs_gateway) | **GET** /dfs-gateways/{dfs_gateway_id} | 
[**get_dfs_gateway_samples**](DfsGatewaysApi.md#get_dfs_gateway_samples) | **GET** /dfs-gateways/{dfs_gateway_id}/samples | 
[**list_dfs_gateway_connections**](DfsGatewaysApi.md#list_dfs_gateway_connections) | **GET** /dfs-gateways/{dfs_gateway_id}/connections | 
[**list_dfs_gateways**](DfsGatewaysApi.md#list_dfs_gateways) | **GET** /dfs-gateways/ | 


# **get_dfs_gateway**
> DfsGatewayResp get_dfs_gateway(dfs_gateway_id)



Get dfs gateway

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
api_instance = xms_client.DfsGatewaysApi(xms_client.ApiClient(configuration))
dfs_gateway_id = 789 # int | gateway id

try:
    api_response = api_instance.get_dfs_gateway(dfs_gateway_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewaysApi->get_dfs_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_id** | **int**| gateway id | 

### Return type

[**DfsGatewayResp**](DfsGatewayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_gateway_samples**
> DfsGatewaySamplesResp get_dfs_gateway_samples(dfs_gateway_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a dfs gateway's samples

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
api_instance = xms_client.DfsGatewaysApi(xms_client.ApiClient(configuration))
dfs_gateway_id = 789 # int | dfs gateway id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_dfs_gateway_samples(dfs_gateway_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewaysApi->get_dfs_gateway_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_id** | **int**| dfs gateway id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**DfsGatewaySamplesResp**](DfsGatewaySamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_gateway_connections**
> DfsGatewayConnectionsResp list_dfs_gateway_connections(dfs_gateway_id, types=types)



list client connections of dfs gateway

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
api_instance = xms_client.DfsGatewaysApi(xms_client.ApiClient(configuration))
dfs_gateway_id = 789 # int | dfs gateway id
types = 'types_example' # str | share types, value is smb|nfs|ftp|s3 (optional)

try:
    api_response = api_instance.list_dfs_gateway_connections(dfs_gateway_id, types=types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewaysApi->list_dfs_gateway_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_id** | **int**| dfs gateway id | 
 **types** | **str**| share types, value is smb|nfs|ftp|s3 | [optional] 

### Return type

[**DfsGatewayConnectionsResp**](DfsGatewayConnectionsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_gateways**
> DfsGatewaysResp list_dfs_gateways(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, dfs_gateway_group_id=dfs_gateway_group_id)



List dfs gateways

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
api_instance = xms_client.DfsGatewaysApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
dfs_gateway_group_id = 789 # int | dfs gateway group id (optional)

try:
    api_response = api_instance.list_dfs_gateways(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, dfs_gateway_group_id=dfs_gateway_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewaysApi->list_dfs_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **dfs_gateway_group_id** | **int**| dfs gateway group id | [optional] 

### Return type

[**DfsGatewaysResp**](DfsGatewaysResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

