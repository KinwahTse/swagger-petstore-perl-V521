# xms_client.PoolsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_osds_to_pool**](PoolsApi.md#add_osds_to_pool) | **PUT** /pools/{pool_id}/osds | 
[**calc_capacity**](PoolsApi.md#calc_capacity) | **POST** /pools/:calc-capacity | 
[**check_full**](PoolsApi.md#check_full) | **POST** /pools/:check-full | 
[**create_pool**](PoolsApi.md#create_pool) | **POST** /pools/ | 
[**delete_pool**](PoolsApi.md#delete_pool) | **DELETE** /pools/{pool_id} | 
[**disable_pool_device_type_check**](PoolsApi.md#disable_pool_device_type_check) | **POST** /pools/{pool_id}:disable-device-type-check | 
[**disable_pool_numa**](PoolsApi.md#disable_pool_numa) | **POST** /pools/{pool_id}:disable-numa | 
[**enable_pool_device_type_check**](PoolsApi.md#enable_pool_device_type_check) | **POST** /pools/{pool_id}:enable-device-type-check | 
[**enable_pool_numa**](PoolsApi.md#enable_pool_numa) | **POST** /pools/{pool_id}:enable-numa | 
[**get_pool**](PoolsApi.md#get_pool) | **GET** /pools/{pool_id} | 
[**get_pool_predictions**](PoolsApi.md#get_pool_predictions) | **GET** /pools/{pool_id}/predictions | 
[**get_pool_samples**](PoolsApi.md#get_pool_samples) | **GET** /pools/{pool_id}/samples | 
[**get_pool_topology**](PoolsApi.md#get_pool_topology) | **GET** /pools/{pool_id}/topology | 
[**initialize_empty_pool**](PoolsApi.md#initialize_empty_pool) | **POST** /pools/{pool_id}:initialize | 
[**list_pools**](PoolsApi.md#list_pools) | **GET** /pools/ | 
[**remove_osds_from_pool**](PoolsApi.md#remove_osds_from_pool) | **DELETE** /pools/{pool_id}/osds | 
[**reweight_pool**](PoolsApi.md#reweight_pool) | **POST** /pools/{pool_id}:reweight | 
[**switch_pool_role**](PoolsApi.md#switch_pool_role) | **POST** /pools/{pool_id}:switch-role | 
[**update_ec_pool_crush_rule**](PoolsApi.md#update_ec_pool_crush_rule) | **POST** /pools/{pool_id}:update-ec-crush-rule | 
[**update_pool**](PoolsApi.md#update_pool) | **PATCH** /pools/{pool_id} | 
[**update_pool_gc_policy**](PoolsApi.md#update_pool_gc_policy) | **POST** /pools/{pool_id}:update-gc-policy | 


# **add_osds_to_pool**
> PoolResp add_osds_to_pool(pool_id, body)



Add osds to pool

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id
body = xms_client.OsdsAddReq() # OsdsAddReq | osd infos

try:
    api_response = api_instance.add_osds_to_pool(pool_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->add_osds_to_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 
 **body** | [**OsdsAddReq**](OsdsAddReq.md)| osd infos | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calc_capacity**
> PoolCapacityResp calc_capacity(body)



calculate pool capacity

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
body = xms_client.PoolCapacityReq() # PoolCapacityReq | pool info

try:
    api_response = api_instance.calc_capacity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->calc_capacity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoolCapacityReq**](PoolCapacityReq.md)| pool info | 

### Return type

[**PoolCapacityResp**](PoolCapacityResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_full**
> PoolFullCheckResp check_full(body)



checks if pools are full

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
body = xms_client.PoolFullCheckReq() # PoolFullCheckReq | pool ids

try:
    api_response = api_instance.check_full(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->check_full: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoolFullCheckReq**](PoolFullCheckReq.md)| pool ids | 

### Return type

[**PoolFullCheckResp**](PoolFullCheckResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pool**
> PoolResp create_pool(body, cluster_id=cluster_id)



Create pool

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
body = xms_client.PoolCreateReq() # PoolCreateReq | the pool info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_pool(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->create_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoolCreateReq**](PoolCreateReq.md)| the pool info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pool**
> PoolResp delete_pool(pool_id, force=force)



Delete pool

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_pool(pool_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->delete_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_pool_device_type_check**
> PoolResp disable_pool_device_type_check(pool_id)



Disable device type check when add osd

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id

try:
    api_response = api_instance.disable_pool_device_type_check(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->disable_pool_device_type_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_pool_numa**
> PoolResp disable_pool_numa(pool_id)



Disable pool numa

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id

try:
    api_response = api_instance.disable_pool_numa(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->disable_pool_numa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_pool_device_type_check**
> PoolResp enable_pool_device_type_check(pool_id)



Enable device type check when add osd

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id

try:
    api_response = api_instance.enable_pool_device_type_check(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->enable_pool_device_type_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_pool_numa**
> PoolResp enable_pool_numa(pool_id)



Enable pool numa

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id

try:
    api_response = api_instance.enable_pool_numa(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->enable_pool_numa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool**
> PoolResp get_pool(pool_id)



get pool

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id

try:
    api_response = api_instance.get_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->get_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_predictions**
> PoolPredictionsResp get_pool_predictions(pool_id)



get a pool's prediction

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id

try:
    api_response = api_instance.get_pool_predictions(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->get_pool_predictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 

### Return type

[**PoolPredictionsResp**](PoolPredictionsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_samples**
> PoolSamplesResp get_pool_samples(pool_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get pool's samples

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_pool_samples(pool_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->get_pool_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**PoolSamplesResp**](PoolSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_topology**
> PoolTopologyResp get_pool_topology(pool_id)



get pool topology

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id

try:
    api_response = api_instance.get_pool_topology(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->get_pool_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 

### Return type

[**PoolTopologyResp**](PoolTopologyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_empty_pool**
> PoolResp initialize_empty_pool(pool_id, body)



initialize an empty pool

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id
body = xms_client.EmptyPoolInitializeReq() # EmptyPoolInitializeReq | the pool info

try:
    api_response = api_instance.initialize_empty_pool(pool_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->initialize_empty_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 
 **body** | [**EmptyPoolInitializeReq**](EmptyPoolInitializeReq.md)| the pool info | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pools**
> PoolsResp list_pools(limit=limit, offset=offset, all=all, protection_domain_id=protection_domain_id, cluster_id=cluster_id, compound_osd_only=compound_osd_only, osd_group_id=osd_group_id, pool_type=pool_type, pool_role=pool_role, pool_mode=pool_mode, stretched=stretched, with_compound=with_compound, is_cache=is_cache, os_policy_id=os_policy_id, storage_class_id=storage_class_id, storage_class_pool_type=storage_class_pool_type, q=q, sort=sort)



List pools

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
all = true # bool | show all pools (optional)
protection_domain_id = 789 # int | protection domain id (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
compound_osd_only = true # bool | filter pool with only compound osds (optional)
osd_group_id = 789 # int | osd group id (optional)
pool_type = 'pool_type_example' # str | filter pool by type (optional)
pool_role = 'pool_role_example' # str | filter pool by role (optional)
pool_mode = 'pool_mode_example' # str | filter pool by pool_mode (optional)
stretched = true # bool | filter stretched pool (optional)
with_compound = true # bool | with compound pool (optional)
is_cache = true # bool | list cache pool (optional)
os_policy_id = 789 # int | filter data pool by object storage policy id (optional)
storage_class_id = 789 # int | filter data pool by os storage class id (optional)
storage_class_pool_type = 'storage_class_pool_type_example' # str | storage class pool type(active inactive) to query (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_pools(limit=limit, offset=offset, all=all, protection_domain_id=protection_domain_id, cluster_id=cluster_id, compound_osd_only=compound_osd_only, osd_group_id=osd_group_id, pool_type=pool_type, pool_role=pool_role, pool_mode=pool_mode, stretched=stretched, with_compound=with_compound, is_cache=is_cache, os_policy_id=os_policy_id, storage_class_id=storage_class_id, storage_class_pool_type=storage_class_pool_type, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->list_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **all** | **bool**| show all pools | [optional] 
 **protection_domain_id** | **int**| protection domain id | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **compound_osd_only** | **bool**| filter pool with only compound osds | [optional] 
 **osd_group_id** | **int**| osd group id | [optional] 
 **pool_type** | **str**| filter pool by type | [optional] 
 **pool_role** | **str**| filter pool by role | [optional] 
 **pool_mode** | **str**| filter pool by pool_mode | [optional] 
 **stretched** | **bool**| filter stretched pool | [optional] 
 **with_compound** | **bool**| with compound pool | [optional] 
 **is_cache** | **bool**| list cache pool | [optional] 
 **os_policy_id** | **int**| filter data pool by object storage policy id | [optional] 
 **storage_class_id** | **int**| filter data pool by os storage class id | [optional] 
 **storage_class_pool_type** | **str**| storage class pool type(active inactive) to query | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**PoolsResp**](PoolsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_osds_from_pool**
> PoolResp remove_osds_from_pool(pool_id, body)



Remove multiple osds from a pool

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id
body = xms_client.OsdsRemoveReq() # OsdsRemoveReq | osd infos

try:
    api_response = api_instance.remove_osds_from_pool(pool_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->remove_osds_from_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 
 **body** | [**OsdsRemoveReq**](OsdsRemoveReq.md)| osd infos | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reweight_pool**
> PoolResp reweight_pool(pool_id)



Reweight a pool

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id

try:
    api_response = api_instance.reweight_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->reweight_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_pool_role**
> PoolResp switch_pool_role(pool_id)



Switch pool role to compound

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id

try:
    api_response = api_instance.switch_pool_role(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->switch_pool_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ec_pool_crush_rule**
> PoolResp update_ec_pool_crush_rule(pool_id, body)



update crush rule with EC pool

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id
body = xms_client.ECPoolUpdateCrushRuleReq() # ECPoolUpdateCrushRuleReq | crush rule info

try:
    api_response = api_instance.update_ec_pool_crush_rule(pool_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->update_ec_pool_crush_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 
 **body** | [**ECPoolUpdateCrushRuleReq**](ECPoolUpdateCrushRuleReq.md)| crush rule info | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pool**
> PoolResp update_pool(pool_id, body)



update pool info

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id
body = xms_client.PoolUpdateReq() # PoolUpdateReq | pool info

try:
    api_response = api_instance.update_pool(pool_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->update_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 
 **body** | [**PoolUpdateReq**](PoolUpdateReq.md)| pool info | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pool_gc_policy**
> PoolResp update_pool_gc_policy(pool_id, body)



update pool gc policy

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
api_instance = xms_client.PoolsApi(xms_client.ApiClient(configuration))
pool_id = 789 # int | pool id
body = xms_client.PoolGCPolicyReq() # PoolGCPolicyReq | pool gc policy

try:
    api_response = api_instance.update_pool_gc_policy(pool_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->update_pool_gc_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| pool id | 
 **body** | [**PoolGCPolicyReq**](PoolGCPolicyReq.md)| pool gc policy | 

### Return type

[**PoolResp**](PoolResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

