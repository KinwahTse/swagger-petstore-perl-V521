# xms_client.NfsGatewaysApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nfs_gateway**](NfsGatewaysApi.md#create_nfs_gateway) | **POST** /nfs-gateways/ | 
[**create_nfs_gateway_bucket_map**](NfsGatewaysApi.md#create_nfs_gateway_bucket_map) | **PUT** /nfs-gateways/{gateway_id}/buckets/{bucket_id} | 
[**delete_nfs_gateway**](NfsGatewaysApi.md#delete_nfs_gateway) | **DELETE** /nfs-gateways/{gateway_id} | 
[**delete_nfs_gateway_bucket_map**](NfsGatewaysApi.md#delete_nfs_gateway_bucket_map) | **DELETE** /nfs-gateways/{gateway_id}/buckets/{bucket_id} | 
[**do_nfs_gateway**](NfsGatewaysApi.md#do_nfs_gateway) | **PUT** /nfs-gateways/{gateway_id} | 
[**get_nfs_gateway**](NfsGatewaysApi.md#get_nfs_gateway) | **GET** /nfs-gateways/{gateway_id} | 
[**get_nfs_gateway_bucket_map**](NfsGatewaysApi.md#get_nfs_gateway_bucket_map) | **GET** /nfs-gateways/{gateway_id}/buckets/{bucket_id} | 
[**get_nfs_gateway_samples**](NfsGatewaysApi.md#get_nfs_gateway_samples) | **GET** /nfs-gateways/{gateway_id}/samples | 
[**list_nfs_gateway_bucket_maps**](NfsGatewaysApi.md#list_nfs_gateway_bucket_maps) | **GET** /nfs-gateways/{gateway_id}/buckets | 
[**list_nfs_gateways**](NfsGatewaysApi.md#list_nfs_gateways) | **GET** /nfs-gateways/ | 
[**update_nfs_gateway**](NfsGatewaysApi.md#update_nfs_gateway) | **PATCH** /nfs-gateways/{gateway_id} | 
[**update_nfs_gateway_bucket_map**](NfsGatewaysApi.md#update_nfs_gateway_bucket_map) | **PATCH** /nfs-gateways/{gateway_id}/buckets/{bucket_id} | 


# **create_nfs_gateway**
> NFSGatewayResp create_nfs_gateway(body, cluster_id=cluster_id)



create nfs gateway

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
body = xms_client.NFSGatewayCreateReq() # NFSGatewayCreateReq | nfs gateway info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_nfs_gateway(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->create_nfs_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NFSGatewayCreateReq**](NFSGatewayCreateReq.md)| nfs gateway info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**NFSGatewayResp**](NFSGatewayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_gateway_bucket_map**
> NFSGatewayBucketMapResp create_nfs_gateway_bucket_map(gateway_id, bucket_id, cluster_id=cluster_id)



add bucket to nfs gateway

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | nfs gateway id
bucket_id = 789 # int | bucket id
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_nfs_gateway_bucket_map(gateway_id, bucket_id, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->create_nfs_gateway_bucket_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| nfs gateway id | 
 **bucket_id** | **int**| bucket id | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**NFSGatewayBucketMapResp**](NFSGatewayBucketMapResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nfs_gateway**
> NFSGatewayResp delete_nfs_gateway(gateway_id, force=force)



delete nfs gateway

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | nfs gateway id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_nfs_gateway(gateway_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->delete_nfs_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| nfs gateway id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**NFSGatewayResp**](NFSGatewayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nfs_gateway_bucket_map**
> NFSGatewayBucketMapResp delete_nfs_gateway_bucket_map(gateway_id, bucket_id, force=force)



remove bucket from nfs gateway

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | nfs gateway id
bucket_id = 789 # int | bucket id
force = true # bool | force delete or no (optional)

try:
    api_response = api_instance.delete_nfs_gateway_bucket_map(gateway_id, bucket_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->delete_nfs_gateway_bucket_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| nfs gateway id | 
 **bucket_id** | **int**| bucket id | 
 **force** | **bool**| force delete or no | [optional] 

### Return type

[**NFSGatewayBucketMapResp**](NFSGatewayBucketMapResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_nfs_gateway**
> NFSGatewayResp do_nfs_gateway(gateway_id, body, force=force)



start/stop nfs gateway

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | nfs gateway id
body = xms_client.NFSGatewayActionReq() # NFSGatewayActionReq | nfs gateway action info
force = true # bool | force stop or no (optional)

try:
    api_response = api_instance.do_nfs_gateway(gateway_id, body, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->do_nfs_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| nfs gateway id | 
 **body** | [**NFSGatewayActionReq**](NFSGatewayActionReq.md)| nfs gateway action info | 
 **force** | **bool**| force stop or no | [optional] 

### Return type

[**NFSGatewayResp**](NFSGatewayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_gateway**
> NFSGatewayResp get_nfs_gateway(gateway_id)



show nfs gateway

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | nfs gateway id

try:
    api_response = api_instance.get_nfs_gateway(gateway_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->get_nfs_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| nfs gateway id | 

### Return type

[**NFSGatewayResp**](NFSGatewayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_gateway_bucket_map**
> NFSGatewayBucketMapResp get_nfs_gateway_bucket_map(gateway_id, bucket_id)



get nfs gateway bucket map

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | nfs gateway id
bucket_id = 789 # int | bucket id

try:
    api_response = api_instance.get_nfs_gateway_bucket_map(gateway_id, bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->get_nfs_gateway_bucket_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| nfs gateway id | 
 **bucket_id** | **int**| bucket id | 

### Return type

[**NFSGatewayBucketMapResp**](NFSGatewayBucketMapResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_gateway_samples**
> NFSGatewaySamplesResp get_nfs_gateway_samples(gateway_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



Get nfs gateway's samples

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | gateway id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_nfs_gateway_samples(gateway_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->get_nfs_gateway_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| gateway id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**NFSGatewaySamplesResp**](NFSGatewaySamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nfs_gateway_bucket_maps**
> NFSGatewayBucketMapsResp list_nfs_gateway_bucket_maps(gateway_id, limit=limit, offset=offset, cluster_id=cluster_id)



List nfs gateway bucket maps

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | nfs gateway id
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_nfs_gateway_bucket_maps(gateway_id, limit=limit, offset=offset, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->list_nfs_gateway_bucket_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| nfs gateway id | 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**NFSGatewayBucketMapsResp**](NFSGatewayBucketMapsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nfs_gateways**
> NFSGatewaysResp list_nfs_gateways(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id)



List all nfs gateways

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_nfs_gateways(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->list_nfs_gateways: %s\n" % e)
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

[**NFSGatewaysResp**](NFSGatewaysResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_gateway**
> NFSGatewayResp update_nfs_gateway(gateway_id, body)



update nfs gateway

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | nfs gateway id
body = xms_client.NFSGatewayUpdateReq() # NFSGatewayUpdateReq | nfs gateway info

try:
    api_response = api_instance.update_nfs_gateway(gateway_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->update_nfs_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| nfs gateway id | 
 **body** | [**NFSGatewayUpdateReq**](NFSGatewayUpdateReq.md)| nfs gateway info | 

### Return type

[**NFSGatewayResp**](NFSGatewayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_gateway_bucket_map**
> NFSGatewayBucketMapResp update_nfs_gateway_bucket_map(gateway_id, bucket_id, body, force=force)



update nfs gateway bucket

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
api_instance = xms_client.NfsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | nfs gateway id
bucket_id = 789 # int | bucket id
body = xms_client.NFSGatewayBucketMapUpdateReq() # NFSGatewayBucketMapUpdateReq | nfs gateway bucket update info
force = true # bool | force update bucket map (optional)

try:
    api_response = api_instance.update_nfs_gateway_bucket_map(gateway_id, bucket_id, body, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsGatewaysApi->update_nfs_gateway_bucket_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| nfs gateway id | 
 **bucket_id** | **int**| bucket id | 
 **body** | [**NFSGatewayBucketMapUpdateReq**](NFSGatewayBucketMapUpdateReq.md)| nfs gateway bucket update info | 
 **force** | **bool**| force update bucket map | [optional] 

### Return type

[**NFSGatewayBucketMapResp**](NFSGatewayBucketMapResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

