# xms_client.OsReplicationPathsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_os_replication_path**](OsReplicationPathsApi.md#get_os_replication_path) | **GET** /os-replication-paths/{path_uuid} | 
[**list_os_replication_paths**](OsReplicationPathsApi.md#list_os_replication_paths) | **GET** /os-replication-paths/ | 


# **get_os_replication_path**
> OSReplicationPathResp get_os_replication_path(path_uuid)



Get a os replication path

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
api_instance = xms_client.OsReplicationPathsApi(xms_client.ApiClient(configuration))
path_uuid = 'path_uuid_example' # str | replication path uuid

try:
    api_response = api_instance.get_os_replication_path(path_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsReplicationPathsApi->get_os_replication_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_uuid** | **str**| replication path uuid | 

### Return type

[**OSReplicationPathResp**](OSReplicationPathResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_replication_paths**
> OSReplicationPathsResp list_os_replication_paths(limit=limit, offset=offset, marker=marker, replication_uuid=replication_uuid, allow_unknown_zone=allow_unknown_zone, cluster_id=cluster_id)



List os replication paths

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
api_instance = xms_client.OsReplicationPathsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
marker = 'marker_example' # str | paging param (optional)
replication_uuid = 'replication_uuid_example' # str | os replication uuid (optional)
allow_unknown_zone = true # bool | allow has nil zone result(default true) (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_os_replication_paths(limit=limit, offset=offset, marker=marker, replication_uuid=replication_uuid, allow_unknown_zone=allow_unknown_zone, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsReplicationPathsApi->list_os_replication_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **marker** | **str**| paging param | [optional] 
 **replication_uuid** | **str**| os replication uuid | [optional] 
 **allow_unknown_zone** | **bool**| allow has nil zone result(default true) | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSReplicationPathsResp**](OSReplicationPathsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

