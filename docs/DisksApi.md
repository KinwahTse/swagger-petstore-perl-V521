# xms_client.DisksApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_partitions**](DisksApi.md#create_partitions) | **PUT** /disks/{disk_id}/partitions | 
[**delete_partitions**](DisksApi.md#delete_partitions) | **DELETE** /disks/{disk_id}/partitions | 
[**get_disk**](DisksApi.md#get_disk) | **GET** /disks/{disk_id} | 
[**get_disk_samples**](DisksApi.md#get_disk_samples) | **GET** /disks/{disk_id}/samples | 
[**list_disks**](DisksApi.md#list_disks) | **GET** /disks/ | 
[**update_disk**](DisksApi.md#update_disk) | **PATCH** /disks/{disk_id} | 


# **create_partitions**
> DiskResp create_partitions(disk_id, body, num=num)



create cache partitions for disk

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
api_instance = xms_client.DisksApi(xms_client.ApiClient(configuration))
disk_id = 789 # int | disk id
body = xms_client.PartitionsCreateReq() # PartitionsCreateReq | partitions info
num = 789 # int | num of cache partitions to create (optional)

try:
    api_response = api_instance.create_partitions(disk_id, body, num=num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->create_partitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk_id** | **int**| disk id | 
 **body** | [**PartitionsCreateReq**](PartitionsCreateReq.md)| partitions info | 
 **num** | **int**| num of cache partitions to create | [optional] 

### Return type

[**DiskResp**](DiskResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_partitions**
> DiskResp delete_partitions(disk_id)



delete cache partitions of disk

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
api_instance = xms_client.DisksApi(xms_client.ApiClient(configuration))
disk_id = 789 # int | disk id

try:
    api_response = api_instance.delete_partitions(disk_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->delete_partitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk_id** | **int**| disk id | 

### Return type

[**DiskResp**](DiskResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk**
> DiskResp get_disk(disk_id)



Get a disk

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
api_instance = xms_client.DisksApi(xms_client.ApiClient(configuration))
disk_id = 789 # int | disk id

try:
    api_response = api_instance.get_disk(disk_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->get_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk_id** | **int**| disk id | 

### Return type

[**DiskResp**](DiskResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk_samples**
> DiskSamplesResp get_disk_samples(disk_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a disk's samples

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
api_instance = xms_client.DisksApi(xms_client.ApiClient(configuration))
disk_id = 789 # int | disk id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_disk_samples(disk_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->get_disk_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk_id** | **int**| disk id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**DiskSamplesResp**](DiskSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_disks**
> DisksResp list_disks(limit=limit, offset=offset, host_id=host_id, cluster_id=cluster_id, is_cache=is_cache, disk_type=disk_type, usage=usage, used=used, q=q, sort=sort, device=device, status=status, ids=ids, order_by=order_by)



List all pyhsical disks in the system

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
api_instance = xms_client.DisksApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
host_id = 789 # int | host id (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
is_cache = true # bool | filter cache disk, deprecated, use `usage=partition` instead (optional)
disk_type = 'disk_type_example' # str | filter disk type (optional)
usage = 'usage_example' # str | filter disk usage (optional)
used = true # bool | filter used (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
device = 'device_example' # str | device name of disk (optional)
status = 'status_example' # str | disk status (optional)
ids = 'ids_example' # str | disk comma seperate ids (optional)
order_by = 'order_by_example' # str | sort param without search, split with comma, e.g. -host.name (optional)

try:
    api_response = api_instance.list_disks(limit=limit, offset=offset, host_id=host_id, cluster_id=cluster_id, is_cache=is_cache, disk_type=disk_type, usage=usage, used=used, q=q, sort=sort, device=device, status=status, ids=ids, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->list_disks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **host_id** | **int**| host id | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **is_cache** | **bool**| filter cache disk, deprecated, use &#x60;usage&#x3D;partition&#x60; instead | [optional] 
 **disk_type** | **str**| filter disk type | [optional] 
 **usage** | **str**| filter disk usage | [optional] 
 **used** | **bool**| filter used | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **device** | **str**| device name of disk | [optional] 
 **status** | **str**| disk status | [optional] 
 **ids** | **str**| disk comma seperate ids | [optional] 
 **order_by** | **str**| sort param without search, split with comma, e.g. -host.name | [optional] 

### Return type

[**DisksResp**](DisksResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_disk**
> DiskResp update_disk(disk_id, disk)



update disk info

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
api_instance = xms_client.DisksApi(xms_client.ApiClient(configuration))
disk_id = 789 # int | disk id
disk = xms_client.DiskUpdateReq() # DiskUpdateReq | disk info

try:
    api_response = api_instance.update_disk(disk_id, disk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisksApi->update_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk_id** | **int**| disk id | 
 **disk** | [**DiskUpdateReq**](DiskUpdateReq.md)| disk info | 

### Return type

[**DiskResp**](DiskResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

