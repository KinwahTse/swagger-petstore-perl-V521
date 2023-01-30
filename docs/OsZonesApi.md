# xms_client.OsZonesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_storage_zone**](OsZonesApi.md#create_object_storage_zone) | **POST** /os-zones/ | 
[**delete_object_storage_zone**](OsZonesApi.md#delete_object_storage_zone) | **DELETE** /os-zones/{zone_uuid} | 
[**get_object_storage_zone**](OsZonesApi.md#get_object_storage_zone) | **GET** /os-zones/{zone_uuid} | 
[**get_object_storage_zone_samples**](OsZonesApi.md#get_object_storage_zone_samples) | **GET** /os-zones/{zone_uuid}/samples | 
[**list_object_storage_zones**](OsZonesApi.md#list_object_storage_zones) | **GET** /os-zones/ | 
[**update_os_zones_clock_diff**](OsZonesApi.md#update_os_zones_clock_diff) | **POST** /os-zones/{zone_uuid} | 


# **create_object_storage_zone**
> ObjectStorageZoneResp create_object_storage_zone(body, cluster_id=cluster_id)



Create a object storage zone

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
api_instance = xms_client.OsZonesApi(xms_client.ApiClient(configuration))
body = xms_client.ObjectStorageZoneCreateReq() # ObjectStorageZoneCreateReq | zone info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_object_storage_zone(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZonesApi->create_object_storage_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectStorageZoneCreateReq**](ObjectStorageZoneCreateReq.md)| zone info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**ObjectStorageZoneResp**](ObjectStorageZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_storage_zone**
> ObjectStorageZoneResp delete_object_storage_zone(zone_uuid, force=force)



Delete a object storage zone

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
api_instance = xms_client.OsZonesApi(xms_client.ApiClient(configuration))
zone_uuid = 'zone_uuid_example' # str | os zone uuid
force = true # bool | delete os zone forcefully or not (optional)

try:
    api_response = api_instance.delete_object_storage_zone(zone_uuid, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZonesApi->delete_object_storage_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_uuid** | **str**| os zone uuid | 
 **force** | **bool**| delete os zone forcefully or not | [optional] 

### Return type

[**ObjectStorageZoneResp**](ObjectStorageZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_zone**
> ObjectStorageZoneRecordResp get_object_storage_zone(zone_uuid)



Get object storage zone

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
api_instance = xms_client.OsZonesApi(xms_client.ApiClient(configuration))
zone_uuid = 'zone_uuid_example' # str | object storage zone uuid

try:
    api_response = api_instance.get_object_storage_zone(zone_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZonesApi->get_object_storage_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_uuid** | **str**| object storage zone uuid | 

### Return type

[**ObjectStorageZoneRecordResp**](ObjectStorageZoneRecordResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_zone_samples**
> ObjectStorageZoneSamplesResp get_object_storage_zone_samples(zone_uuid, duration_begin=duration_begin, duration_end=duration_end, period=period)



get an object storage zone's Samples

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
api_instance = xms_client.OsZonesApi(xms_client.ApiClient(configuration))
zone_uuid = 'zone_uuid_example' # str | object storage zone uuid
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_object_storage_zone_samples(zone_uuid, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZonesApi->get_object_storage_zone_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_uuid** | **str**| object storage zone uuid | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**ObjectStorageZoneSamplesResp**](ObjectStorageZoneSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_object_storage_zones**
> ObjectStorageZonesRecordResp list_object_storage_zones(limit=limit, offset=offset, q=q, sort=sort, local=local, master=master, name=name, cluster_id=cluster_id)



List object storage zones

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
api_instance = xms_client.OsZonesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
local = true # bool | local or non-local zones (optional)
master = true # bool | master or non-master zones (optional)
name = 'name_example' # str | name of zone (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_object_storage_zones(limit=limit, offset=offset, q=q, sort=sort, local=local, master=master, name=name, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZonesApi->list_object_storage_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **local** | **bool**| local or non-local zones | [optional] 
 **master** | **bool**| master or non-master zones | [optional] 
 **name** | **str**| name of zone | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**ObjectStorageZonesRecordResp**](ObjectStorageZonesRecordResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_os_zones_clock_diff**
> ObjectStorageZoneResp update_os_zones_clock_diff(zone_uuid, body)



update os zone pairs

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
api_instance = xms_client.OsZonesApi(xms_client.ApiClient(configuration))
zone_uuid = 'zone_uuid_example' # str | os zone uuid
body = xms_client.OSZonePairsUpdateReq() # OSZonePairsUpdateReq | zone pairs info

try:
    api_response = api_instance.update_os_zones_clock_diff(zone_uuid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZonesApi->update_os_zones_clock_diff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_uuid** | **str**| os zone uuid | 
 **body** | [**OSZonePairsUpdateReq**](OSZonePairsUpdateReq.md)| zone pairs info | 

### Return type

[**ObjectStorageZoneResp**](ObjectStorageZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

