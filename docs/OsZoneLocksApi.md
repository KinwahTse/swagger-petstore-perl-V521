# xms_client.OsZoneLocksApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_os_zone_lock**](OsZoneLocksApi.md#create_os_zone_lock) | **POST** /os-zone-locks/ | 
[**delete_os_zone_lock**](OsZoneLocksApi.md#delete_os_zone_lock) | **DELETE** /os-zone-locks/{lock_uuid} | 
[**get_os_zone_lock**](OsZoneLocksApi.md#get_os_zone_lock) | **GET** /os-zone-locks/{lock_uuid} | 
[**list_os_zone_locks**](OsZoneLocksApi.md#list_os_zone_locks) | **GET** /os-zone-locks/ | 
[**refresh_os_zone_lock**](OsZoneLocksApi.md#refresh_os_zone_lock) | **POST** /os-zone-locks/{lock_uuid}:refresh | 


# **create_os_zone_lock**
> OSZoneLockResp create_os_zone_lock(body, cluster_id=cluster_id)



Create a os zone lock.

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
api_instance = xms_client.OsZoneLocksApi(xms_client.ApiClient(configuration))
body = xms_client.OSZoneLockCreateReq() # OSZoneLockCreateReq | os zone lock info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_os_zone_lock(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZoneLocksApi->create_os_zone_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OSZoneLockCreateReq**](OSZoneLockCreateReq.md)| os zone lock info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSZoneLockResp**](OSZoneLockResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_os_zone_lock**
> delete_os_zone_lock(lock_uuid)



Delete a os zone lock.

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
api_instance = xms_client.OsZoneLocksApi(xms_client.ApiClient(configuration))
lock_uuid = 'lock_uuid_example' # str | os zone lock uuid

try:
    api_instance.delete_os_zone_lock(lock_uuid)
except ApiException as e:
    print("Exception when calling OsZoneLocksApi->delete_os_zone_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_uuid** | **str**| os zone lock uuid | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_zone_lock**
> OSZoneLockResp get_os_zone_lock(lock_uuid)



Get a os zone lock.

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
api_instance = xms_client.OsZoneLocksApi(xms_client.ApiClient(configuration))
lock_uuid = 'lock_uuid_example' # str | os zone lock uuid

try:
    api_response = api_instance.get_os_zone_lock(lock_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZoneLocksApi->get_os_zone_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_uuid** | **str**| os zone lock uuid | 

### Return type

[**OSZoneLockResp**](OSZoneLockResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_zone_locks**
> OSZoneLocksResp list_os_zone_locks(limit=limit, offset=offset, all=all, cluster_id=cluster_id)



List os zone locks.

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
api_instance = xms_client.OsZoneLocksApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
all = true # bool | show all zone locks (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_os_zone_locks(limit=limit, offset=offset, all=all, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZoneLocksApi->list_os_zone_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **all** | **bool**| show all zone locks | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSZoneLocksResp**](OSZoneLocksResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_os_zone_lock**
> OSZoneLockResp refresh_os_zone_lock(lock_uuid)



Refresh a os zone lock.

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
api_instance = xms_client.OsZoneLocksApi(xms_client.ApiClient(configuration))
lock_uuid = 'lock_uuid_example' # str | os zone lock uuid

try:
    api_response = api_instance.refresh_os_zone_lock(lock_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsZoneLocksApi->refresh_os_zone_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock_uuid** | **str**| os zone lock uuid | 

### Return type

[**OSZoneLockResp**](OSZoneLockResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

