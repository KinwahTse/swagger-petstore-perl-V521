# xms_client.OsdsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_osd**](OsdsApi.md#activate_osd) | **POST** /osds/{osd_id}:activate | 
[**create_osd**](OsdsApi.md#create_osd) | **POST** /osds/ | 
[**delete_osd**](OsdsApi.md#delete_osd) | **DELETE** /osds/{osd_id} | 
[**get_chunks**](OsdsApi.md#get_chunks) | **GET** /osds/{osd_id}/chunks | 
[**get_osd**](OsdsApi.md#get_osd) | **GET** /osds/{osd_id} | 
[**get_osd_predictions**](OsdsApi.md#get_osd_predictions) | **GET** /osds/{osd_id}/predictions | 
[**get_osd_samples**](OsdsApi.md#get_osd_samples) | **GET** /osds/{osd_id}/samples | 
[**list_osds**](OsdsApi.md#list_osds) | **GET** /osds/ | 
[**maintain_osd**](OsdsApi.md#maintain_osd) | **POST** /osds/{osd_id}:maintain | 
[**rebuild_osd**](OsdsApi.md#rebuild_osd) | **POST** /osds/{osd_id}:rebuild | 
[**switch_osd_role**](OsdsApi.md#switch_osd_role) | **POST** /osds/{osd_id}:switch-role | 
[**unmaintain_osd**](OsdsApi.md#unmaintain_osd) | **POST** /osds/{osd_id}:unmaintain | 
[**unset_osd_isolation**](OsdsApi.md#unset_osd_isolation) | **POST** /osds/{osd_id}:unset-isolation | 
[**update_osd_numa_node**](OsdsApi.md#update_osd_numa_node) | **POST** /osds/{osd_id}:update-numa-node | 


# **activate_osd**
> OsdResp activate_osd(osd_id)



Try to activate osd

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id

try:
    api_response = api_instance.activate_osd(osd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->activate_osd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 

### Return type

[**OsdResp**](OsdResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_osd**
> OsdResp create_osd(body)



Create osd service on specific disk

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
body = xms_client.OsdCreateReq() # OsdCreateReq | osd info

try:
    api_response = api_instance.create_osd(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->create_osd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OsdCreateReq**](OsdCreateReq.md)| osd info | 

### Return type

[**OsdResp**](OsdResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_osd**
> OsdResp delete_osd(osd_id)



remove an osd from cluster

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id

try:
    api_response = api_instance.delete_osd(osd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->delete_osd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 

### Return type

[**OsdResp**](OsdResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunks**
> ChunksResp get_chunks(osd_id)



get chunks of and osd

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | The id of the osd

try:
    api_response = api_instance.get_chunks(osd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->get_chunks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| The id of the osd | 

### Return type

[**ChunksResp**](ChunksResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_osd**
> OsdResp get_osd(osd_id)



get an osd

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id

try:
    api_response = api_instance.get_osd(osd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->get_osd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 

### Return type

[**OsdResp**](OsdResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_osd_predictions**
> OsdPredictionsResp get_osd_predictions(osd_id)



get a osd's prediction

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id

try:
    api_response = api_instance.get_osd_predictions(osd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->get_osd_predictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 

### Return type

[**OsdPredictionsResp**](OsdPredictionsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_osd_samples**
> OsdSamplesResp get_osd_samples(osd_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a osd's samples

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_osd_samples(osd_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->get_osd_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**OsdSamplesResp**](OsdSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_osds**
> OsdsResp list_osds(limit=limit, offset=offset, host_id=host_id, cluster_id=cluster_id, pool_id=pool_id, bind_pool_id=bind_pool_id, osd_group_id=osd_group_id, type=type, role=role, status_class=status_class, with_compound=with_compound, with_hybrid=with_hybrid, cache_disk_id=cache_disk_id, q=q, sort=sort)



List all osds in the cluster

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
host_id = 789 # int | host id (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
pool_id = 789 # int | pool id (optional)
bind_pool_id = 789 # int | bind pool id (optional)
osd_group_id = 789 # int | osd group id (optional)
type = 'type_example' # str | osd type: HDD, SSD, Hybrid (optional)
role = 'role_example' # str | osd role: index or data (optional)
status_class = 'status_class_example' # str | osd status class: active, warning, error, offline, doing (optional)
with_compound = true # bool | with compound osd (optional)
with_hybrid = true # bool | with hybrid osd (optional)
cache_disk_id = 789 # int | cache disk id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_osds(limit=limit, offset=offset, host_id=host_id, cluster_id=cluster_id, pool_id=pool_id, bind_pool_id=bind_pool_id, osd_group_id=osd_group_id, type=type, role=role, status_class=status_class, with_compound=with_compound, with_hybrid=with_hybrid, cache_disk_id=cache_disk_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->list_osds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **host_id** | **int**| host id | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **pool_id** | **int**| pool id | [optional] 
 **bind_pool_id** | **int**| bind pool id | [optional] 
 **osd_group_id** | **int**| osd group id | [optional] 
 **type** | **str**| osd type: HDD, SSD, Hybrid | [optional] 
 **role** | **str**| osd role: index or data | [optional] 
 **status_class** | **str**| osd status class: active, warning, error, offline, doing | [optional] 
 **with_compound** | **bool**| with compound osd | [optional] 
 **with_hybrid** | **bool**| with hybrid osd | [optional] 
 **cache_disk_id** | **int**| cache disk id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**OsdsResp**](OsdsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintain_osd**
> OsdResp maintain_osd(osd_id)



Put osd in maintained status

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id

try:
    api_response = api_instance.maintain_osd(osd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->maintain_osd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 

### Return type

[**OsdResp**](OsdResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild_osd**
> OsdResp rebuild_osd(osd_id, body)



rebuild an osd from cluster pool

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id
body = xms_client.OsdRebuildReq() # OsdRebuildReq | osd info

try:
    api_response = api_instance.rebuild_osd(osd_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->rebuild_osd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 
 **body** | [**OsdRebuildReq**](OsdRebuildReq.md)| osd info | 

### Return type

[**OsdResp**](OsdResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_osd_role**
> OsdResp switch_osd_role(osd_id)



Switch osd role to compound

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id

try:
    api_response = api_instance.switch_osd_role(osd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->switch_osd_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 

### Return type

[**OsdResp**](OsdResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmaintain_osd**
> OsdResp unmaintain_osd(osd_id)



Put osd out of maintained status

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id

try:
    api_response = api_instance.unmaintain_osd(osd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->unmaintain_osd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 

### Return type

[**OsdResp**](OsdResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_osd_isolation**
> OsdResp unset_osd_isolation(osd_id)



Unset osd in isolation status

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id

try:
    api_response = api_instance.unset_osd_isolation(osd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->unset_osd_isolation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 

### Return type

[**OsdResp**](OsdResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_osd_numa_node**
> OsdResp update_osd_numa_node(osd_id, body)



Update osd numa node

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
api_instance = xms_client.OsdsApi(xms_client.ApiClient(configuration))
osd_id = 789 # int | osd id
body = xms_client.OsdUpdateNumaNodeReq() # OsdUpdateNumaNodeReq | osd numa node

try:
    api_response = api_instance.update_osd_numa_node(osd_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdsApi->update_osd_numa_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osd_id** | **int**| osd id | 
 **body** | [**OsdUpdateNumaNodeReq**](OsdUpdateNumaNodeReq.md)| osd numa node | 

### Return type

[**OsdResp**](OsdResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

