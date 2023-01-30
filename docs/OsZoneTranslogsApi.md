# xms_client.OsZoneTranslogsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_os_zone_translog**](OsZoneTranslogsApi.md#get_os_zone_translog) | **GET** /os-zone-translogs/{translog_uuid} | 
[**list_os_zone_translogs**](OsZoneTranslogsApi.md#list_os_zone_translogs) | **GET** /os-zone-translogs/ | 


# **get_os_zone_translog**
> OSZoneTranslogResp get_os_zone_translog(translog_uuid)



Get a os zone translog

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
api_instance = xms_client.OsZoneTranslogsApi(xms_client.ApiClient(configuration))
translog_uuid = 'translog_uuid_example' # str | translog uuid

try:
    api_response = api_instance.get_os_zone_translog(translog_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZoneTranslogsApi->get_os_zone_translog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translog_uuid** | **str**| translog uuid | 

### Return type

[**OSZoneTranslogResp**](OSZoneTranslogResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_zone_translogs**
> OSZoneTranslogsResp list_os_zone_translogs(limit=limit, offset=offset, epoch_uuid=epoch_uuid, cluster_id=cluster_id)



List os zone translogs

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
api_instance = xms_client.OsZoneTranslogsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
epoch_uuid = 'epoch_uuid_example' # str | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_os_zone_translogs(limit=limit, offset=offset, epoch_uuid=epoch_uuid, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZoneTranslogsApi->list_os_zone_translogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **epoch_uuid** | **str**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSZoneTranslogsResp**](OSZoneTranslogsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

