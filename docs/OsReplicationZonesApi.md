# xms_client.OsReplicationZonesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_os_replication_zone**](OsReplicationZonesApi.md#create_os_replication_zone) | **POST** /os-replication-zones/ | 
[**delete_os_replication_zone**](OsReplicationZonesApi.md#delete_os_replication_zone) | **DELETE** /os-replication-zones/{zone_uuid} | 
[**get_os_replication_zone**](OsReplicationZonesApi.md#get_os_replication_zone) | **GET** /os-replication-zones/{zone_uuid} | 
[**get_os_replication_zone_samples**](OsReplicationZonesApi.md#get_os_replication_zone_samples) | **GET** /os-replication-zones/{zone_uuid}/samples | 
[**list_os_replication_zones**](OsReplicationZonesApi.md#list_os_replication_zones) | **GET** /os-replication-zones/ | 
[**update_os_replication_zone**](OsReplicationZonesApi.md#update_os_replication_zone) | **PATCH** /os-replication-zones/{zone_uuid} | 


# **create_os_replication_zone**
> OSReplicationZoneResp create_os_replication_zone(body, cluster_id=cluster_id)



Create a os replication zone

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
api_instance = xms_client.OsReplicationZonesApi(xms_client.ApiClient(configuration))
body = xms_client.OSReplicationZoneCreateReq() # OSReplicationZoneCreateReq | os replication zone info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_os_replication_zone(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsReplicationZonesApi->create_os_replication_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OSReplicationZoneCreateReq**](OSReplicationZoneCreateReq.md)| os replication zone info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSReplicationZoneResp**](OSReplicationZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_os_replication_zone**
> OSReplicationZoneResp delete_os_replication_zone(zone_uuid)



Delete a os replication zone

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
api_instance = xms_client.OsReplicationZonesApi(xms_client.ApiClient(configuration))
zone_uuid = 'zone_uuid_example' # str | os replication zone uuid

try:
    api_response = api_instance.delete_os_replication_zone(zone_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsReplicationZonesApi->delete_os_replication_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_uuid** | **str**| os replication zone uuid | 

### Return type

[**OSReplicationZoneResp**](OSReplicationZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_replication_zone**
> OSReplicationZoneRecordResp get_os_replication_zone(zone_uuid)



Get a os replication zone

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
api_instance = xms_client.OsReplicationZonesApi(xms_client.ApiClient(configuration))
zone_uuid = 'zone_uuid_example' # str | os replication zone uuid

try:
    api_response = api_instance.get_os_replication_zone(zone_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsReplicationZonesApi->get_os_replication_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_uuid** | **str**| os replication zone uuid | 

### Return type

[**OSReplicationZoneRecordResp**](OSReplicationZoneRecordResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_replication_zone_samples**
> OSReplicationZoneSamplesResp get_os_replication_zone_samples(zone_uuid, duration_begin=duration_begin, duration_end=duration_end, period=period)



get an os replication zone's samples

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
api_instance = xms_client.OsReplicationZonesApi(xms_client.ApiClient(configuration))
zone_uuid = 'zone_uuid_example' # str | os replication zone uuid
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_os_replication_zone_samples(zone_uuid, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsReplicationZonesApi->get_os_replication_zone_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_uuid** | **str**| os replication zone uuid | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**OSReplicationZoneSamplesResp**](OSReplicationZoneSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_replication_zones**
> OSReplicationZoneRecordsResp list_os_replication_zones(limit=limit, offset=offset, marker=marker, replication_uuid=replication_uuid, os_zone_uuid=os_zone_uuid, cluster_id=cluster_id)



List os replication zones

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
api_instance = xms_client.OsReplicationZonesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
marker = 'marker_example' # str | paging param (optional)
replication_uuid = 'replication_uuid_example' # str | os replication uuid (optional)
os_zone_uuid = 'os_zone_uuid_example' # str | os zone uuid (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_os_replication_zones(limit=limit, offset=offset, marker=marker, replication_uuid=replication_uuid, os_zone_uuid=os_zone_uuid, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsReplicationZonesApi->list_os_replication_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **marker** | **str**| paging param | [optional] 
 **replication_uuid** | **str**| os replication uuid | [optional] 
 **os_zone_uuid** | **str**| os zone uuid | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSReplicationZoneRecordsResp**](OSReplicationZoneRecordsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_os_replication_zone**
> OSReplicationZoneResp update_os_replication_zone(zone_uuid)



Update an os replication zone

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
api_instance = xms_client.OsReplicationZonesApi(xms_client.ApiClient(configuration))
zone_uuid = 'zone_uuid_example' # str | os replication zone uuid

try:
    api_response = api_instance.update_os_replication_zone(zone_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsReplicationZonesApi->update_os_replication_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_uuid** | **str**| os replication zone uuid | 

### Return type

[**OSReplicationZoneResp**](OSReplicationZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

