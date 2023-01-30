# xms_client.TrashResourcesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_trash_resource**](TrashResourcesApi.md#delete_trash_resource) | **DELETE** /trash-resources/{trash_resource_id} | 
[**get_trash_resource**](TrashResourcesApi.md#get_trash_resource) | **GET** /trash-resources/{trash_resource_id} | 
[**list_trash_resources**](TrashResourcesApi.md#list_trash_resources) | **GET** /trash-resources/ | 
[**restore_trash_resource**](TrashResourcesApi.md#restore_trash_resource) | **POST** /trash-resources/{trash_resource_id}:restore | 


# **delete_trash_resource**
> TrashResourceResp delete_trash_resource(trash_resource_id)



Delete trash resource

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
api_instance = xms_client.TrashResourcesApi(xms_client.ApiClient(configuration))
trash_resource_id = 789 # int | trash resource id

try:
    api_response = api_instance.delete_trash_resource(trash_resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrashResourcesApi->delete_trash_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trash_resource_id** | **int**| trash resource id | 

### Return type

[**TrashResourceResp**](TrashResourceResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trash_resource**
> TrashResourceResp get_trash_resource(trash_resource_id)



get a trash resource

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
api_instance = xms_client.TrashResourcesApi(xms_client.ApiClient(configuration))
trash_resource_id = 789 # int | trash resource id

try:
    api_response = api_instance.get_trash_resource(trash_resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrashResourcesApi->get_trash_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trash_resource_id** | **int**| trash resource id | 

### Return type

[**TrashResourceResp**](TrashResourceResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trash_resources**
> TrashResourcesResp list_trash_resources(limit=limit, offset=offset, cluster_id=cluster_id, type=type, q=q, sort=sort)



List trash resources

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
api_instance = xms_client.TrashResourcesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
type = 'type_example' # str | the type of trash resources (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_trash_resources(limit=limit, offset=offset, cluster_id=cluster_id, type=type, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrashResourcesApi->list_trash_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **type** | **str**| the type of trash resources | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**TrashResourcesResp**](TrashResourcesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_trash_resource**
> TrashResourceResp restore_trash_resource(trash_resource_id)



Restore trash resource

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
api_instance = xms_client.TrashResourcesApi(xms_client.ApiClient(configuration))
trash_resource_id = 789 # int | trash resource id

try:
    api_response = api_instance.restore_trash_resource(trash_resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrashResourcesApi->restore_trash_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trash_resource_id** | **int**| trash resource id | 

### Return type

[**TrashResourceResp**](TrashResourceResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

