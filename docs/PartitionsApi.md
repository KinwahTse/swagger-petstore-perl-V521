# xms_client.PartitionsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_partition**](PartitionsApi.md#get_partition) | **GET** /partitions/{partition_id} | 
[**list_partitions**](PartitionsApi.md#list_partitions) | **GET** /partitions/ | 


# **get_partition**
> PartitionResp get_partition(partition_id)



Get a partition info

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
api_instance = xms_client.PartitionsApi(xms_client.ApiClient(configuration))
partition_id = 'partition_id_example' # str | partition id

try:
    api_response = api_instance.get_partition(partition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionsApi->get_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_id** | **str**| partition id | 

### Return type

[**PartitionResp**](PartitionResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_partitions**
> PartitionsResp list_partitions(limit=limit, offset=offset, q=q, sort=sort, host_id=host_id, type=type, disk_id=disk_id)



List partitions

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
api_instance = xms_client.PartitionsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
host_id = 789 # int | host id (optional)
type = 'type_example' # str | partition type (optional)
disk_id = 789 # int | disk id (optional)

try:
    api_response = api_instance.list_partitions(limit=limit, offset=offset, q=q, sort=sort, host_id=host_id, type=type, disk_id=disk_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartitionsApi->list_partitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **host_id** | **int**| host id | [optional] 
 **type** | **str**| partition type | [optional] 
 **disk_id** | **int**| disk id | [optional] 

### Return type

[**PartitionsResp**](PartitionsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

