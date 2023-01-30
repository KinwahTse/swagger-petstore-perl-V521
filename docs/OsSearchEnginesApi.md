# xms_client.OsSearchEnginesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_os_search_gateways**](OsSearchEnginesApi.md#add_os_search_gateways) | **POST** /os-search-engines/{os_search_engine_id}:add-os-search-gateways | 
[**change_os_search_engine**](OsSearchEnginesApi.md#change_os_search_engine) | **PATCH** /os-search-engines/{os_search_engine_id} | 
[**create_os_search_engine**](OsSearchEnginesApi.md#create_os_search_engine) | **POST** /os-search-engines/ | 
[**delete_os_search_engine**](OsSearchEnginesApi.md#delete_os_search_engine) | **DELETE** /os-search-engines/{os_search_engine_id} | 
[**get_os_search_engine**](OsSearchEnginesApi.md#get_os_search_engine) | **GET** /os-search-engines/{os_search_engine_id} | 
[**get_os_search_engine_samples**](OsSearchEnginesApi.md#get_os_search_engine_samples) | **GET** /os-search-engines/{os_search_engine_id}/samples | 
[**list_os_search_engines**](OsSearchEnginesApi.md#list_os_search_engines) | **GET** /os-search-engines/ | 
[**remove_os_search_gateways**](OsSearchEnginesApi.md#remove_os_search_gateways) | **POST** /os-search-engines/{os_search_engine_id}:remove-os-search-gateways | 
[**start_os_search_engine**](OsSearchEnginesApi.md#start_os_search_engine) | **POST** /os-search-engines/{os_search_engine_id}:start | 
[**stop_os_search_engine**](OsSearchEnginesApi.md#stop_os_search_engine) | **POST** /os-search-engines/{os_search_engine_id}:stop | 


# **add_os_search_gateways**
> OSSearchEngineResp add_os_search_gateways(os_search_engine_id, body)



Create new OS Search gateways on OS search engine

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
api_instance = xms_client.OsSearchEnginesApi(xms_client.ApiClient(configuration))
os_search_engine_id = 789 # int | OS search engine id
body = xms_client.OSSearchEngineAddGatewaysReq() # OSSearchEngineAddGatewaysReq | os search gateways info

try:
    api_response = api_instance.add_os_search_gateways(os_search_engine_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchEnginesApi->add_os_search_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_search_engine_id** | **int**| OS search engine id | 
 **body** | [**OSSearchEngineAddGatewaysReq**](OSSearchEngineAddGatewaysReq.md)| os search gateways info | 

### Return type

[**OSSearchEngineResp**](OSSearchEngineResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_os_search_engine**
> OSSearchEngineResp change_os_search_engine(os_search_engine_id, body)



change OS search engine falvor or data size

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
api_instance = xms_client.OsSearchEnginesApi(xms_client.ApiClient(configuration))
os_search_engine_id = 789 # int | OS search engine id
body = xms_client.OSSearchEngineUpdateReq() # OSSearchEngineUpdateReq | os search gateways info

try:
    api_response = api_instance.change_os_search_engine(os_search_engine_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchEnginesApi->change_os_search_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_search_engine_id** | **int**| OS search engine id | 
 **body** | [**OSSearchEngineUpdateReq**](OSSearchEngineUpdateReq.md)| os search gateways info | 

### Return type

[**OSSearchEngineResp**](OSSearchEngineResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_os_search_engine**
> OSSearchEngineResp create_os_search_engine(body, cluster_id=cluster_id)



Create OS search engine

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
api_instance = xms_client.OsSearchEnginesApi(xms_client.ApiClient(configuration))
body = xms_client.OSSearchEngineCreateReq() # OSSearchEngineCreateReq | OS search engine info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_os_search_engine(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchEnginesApi->create_os_search_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OSSearchEngineCreateReq**](OSSearchEngineCreateReq.md)| OS search engine info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSSearchEngineResp**](OSSearchEngineResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_os_search_engine**
> OSSearchEngineResp delete_os_search_engine(os_search_engine_id)



delete OS search engine

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
api_instance = xms_client.OsSearchEnginesApi(xms_client.ApiClient(configuration))
os_search_engine_id = 789 # int | OS search engine id

try:
    api_response = api_instance.delete_os_search_engine(os_search_engine_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchEnginesApi->delete_os_search_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_search_engine_id** | **int**| OS search engine id | 

### Return type

[**OSSearchEngineResp**](OSSearchEngineResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_search_engine**
> OSSearchEngineResp get_os_search_engine(os_search_engine_id)



Get a OS search engine

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
api_instance = xms_client.OsSearchEnginesApi(xms_client.ApiClient(configuration))
os_search_engine_id = 789 # int | OS search engine id

try:
    api_response = api_instance.get_os_search_engine(os_search_engine_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchEnginesApi->get_os_search_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_search_engine_id** | **int**| OS search engine id | 

### Return type

[**OSSearchEngineResp**](OSSearchEngineResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_search_engine_samples**
> OSSearchEngineSamplesResp get_os_search_engine_samples(os_search_engine_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get an object storage search engine's samples

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
api_instance = xms_client.OsSearchEnginesApi(xms_client.ApiClient(configuration))
os_search_engine_id = 789 # int | OS search engine id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_os_search_engine_samples(os_search_engine_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchEnginesApi->get_os_search_engine_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_search_engine_id** | **int**| OS search engine id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**OSSearchEngineSamplesResp**](OSSearchEngineSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_search_engines**
> OSSearchEnginesResp list_os_search_engines(cluster_id=cluster_id, limit=limit, offset=offset)



List OS search engine

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
api_instance = xms_client.OsSearchEnginesApi(xms_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | cluster id (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_os_search_engines(cluster_id=cluster_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchEnginesApi->list_os_search_engines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| cluster id | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**OSSearchEnginesResp**](OSSearchEnginesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_os_search_gateways**
> OSSearchEngineResp remove_os_search_gateways(os_search_engine_id, body)



remove OS search gateways from OS search engine

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
api_instance = xms_client.OsSearchEnginesApi(xms_client.ApiClient(configuration))
os_search_engine_id = 789 # int | OS search engine id
body = xms_client.OSSearchEngineRemoveGatewaysReq() # OSSearchEngineRemoveGatewaysReq | os search gateways info

try:
    api_response = api_instance.remove_os_search_gateways(os_search_engine_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchEnginesApi->remove_os_search_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_search_engine_id** | **int**| OS search engine id | 
 **body** | [**OSSearchEngineRemoveGatewaysReq**](OSSearchEngineRemoveGatewaysReq.md)| os search gateways info | 

### Return type

[**OSSearchEngineResp**](OSSearchEngineResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_os_search_engine**
> OSSearchEngineResp start_os_search_engine(os_search_engine_id)



start OS search gateways from OS search engine

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
api_instance = xms_client.OsSearchEnginesApi(xms_client.ApiClient(configuration))
os_search_engine_id = 789 # int | OS search engine id

try:
    api_response = api_instance.start_os_search_engine(os_search_engine_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchEnginesApi->start_os_search_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_search_engine_id** | **int**| OS search engine id | 

### Return type

[**OSSearchEngineResp**](OSSearchEngineResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_os_search_engine**
> OSSearchEngineResp stop_os_search_engine(os_search_engine_id)



stop OS search gateways from OS search engine

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
api_instance = xms_client.OsSearchEnginesApi(xms_client.ApiClient(configuration))
os_search_engine_id = 789 # int | OS search engine id

try:
    api_response = api_instance.stop_os_search_engine(os_search_engine_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSearchEnginesApi->stop_os_search_engine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_search_engine_id** | **int**| OS search engine id | 

### Return type

[**OSSearchEngineResp**](OSSearchEngineResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

