# xms_client.MappingGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_volumes**](MappingGroupsApi.md#add_volumes) | **POST** /mapping-groups/{mapping_group_id}/block-volumes | 
[**create_mapping_group**](MappingGroupsApi.md#create_mapping_group) | **POST** /mapping-groups/ | 
[**delete_mapping_group**](MappingGroupsApi.md#delete_mapping_group) | **DELETE** /mapping-groups/{mapping_group_id} | 
[**get_mapping_group**](MappingGroupsApi.md#get_mapping_group) | **GET** /mapping-groups/{mapping_group_id} | 
[**list_mapping_groups**](MappingGroupsApi.md#list_mapping_groups) | **GET** /mapping-groups/ | 
[**remove_volumes**](MappingGroupsApi.md#remove_volumes) | **DELETE** /mapping-groups/{mapping_group_id}/block-volumes | 
[**update_mapping_group**](MappingGroupsApi.md#update_mapping_group) | **PATCH** /mapping-groups/{mapping_group_id} | 
[**update_mapping_group_client_group**](MappingGroupsApi.md#update_mapping_group_client_group) | **PATCH** /mapping-groups/{mapping_group_id}/client-group | 


# **add_volumes**
> MappingGroupResp add_volumes(mapping_group_id, block_volume_ids)



add volumes to mapping group

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
api_instance = xms_client.MappingGroupsApi(xms_client.ApiClient(configuration))
mapping_group_id = 789 # int | mapping group id
block_volume_ids = xms_client.MappingGroupAddVolumesReq() # MappingGroupAddVolumesReq | block volume ids

try:
    api_response = api_instance.add_volumes(mapping_group_id, block_volume_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingGroupsApi->add_volumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_group_id** | **int**| mapping group id | 
 **block_volume_ids** | [**MappingGroupAddVolumesReq**](MappingGroupAddVolumesReq.md)| block volume ids | 

### Return type

[**MappingGroupResp**](MappingGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mapping_group**
> MappingGroupResp create_mapping_group(mapping_group)



create a mapping group in access path

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
api_instance = xms_client.MappingGroupsApi(xms_client.ApiClient(configuration))
mapping_group = xms_client.MappingGroupCreateReq() # MappingGroupCreateReq | mapping info

try:
    api_response = api_instance.create_mapping_group(mapping_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingGroupsApi->create_mapping_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_group** | [**MappingGroupCreateReq**](MappingGroupCreateReq.md)| mapping info | 

### Return type

[**MappingGroupResp**](MappingGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mapping_group**
> MappingGroupResp delete_mapping_group(mapping_group_id, force=force)



Delete mapping group

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
api_instance = xms_client.MappingGroupsApi(xms_client.ApiClient(configuration))
mapping_group_id = 789 # int | mapping group id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_mapping_group(mapping_group_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingGroupsApi->delete_mapping_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_group_id** | **int**| mapping group id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**MappingGroupResp**](MappingGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping_group**
> MappingGroupResp get_mapping_group(mapping_group_id)



Get mapping group by id

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
api_instance = xms_client.MappingGroupsApi(xms_client.ApiClient(configuration))
mapping_group_id = 789 # int | mapping group id

try:
    api_response = api_instance.get_mapping_group(mapping_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingGroupsApi->get_mapping_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_group_id** | **int**| mapping group id | 

### Return type

[**MappingGroupResp**](MappingGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mapping_groups**
> MappingGroupsResp list_mapping_groups(limit=limit, offset=offset, access_path_id=access_path_id, client_group_id=client_group_id)



List mapping groups

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
api_instance = xms_client.MappingGroupsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
access_path_id = 789 # int | access path id (optional)
client_group_id = 789 # int | client group id (optional)

try:
    api_response = api_instance.list_mapping_groups(limit=limit, offset=offset, access_path_id=access_path_id, client_group_id=client_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingGroupsApi->list_mapping_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **access_path_id** | **int**| access path id | [optional] 
 **client_group_id** | **int**| client group id | [optional] 

### Return type

[**MappingGroupsResp**](MappingGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_volumes**
> MappingGroupResp remove_volumes(mapping_group_id, block_volume_ids, force=force)



remove volumes from mapping group

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
api_instance = xms_client.MappingGroupsApi(xms_client.ApiClient(configuration))
mapping_group_id = 789 # int | mapping group id
block_volume_ids = xms_client.MappingGroupRemoveVolumesReq() # MappingGroupRemoveVolumesReq | block volume ids
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.remove_volumes(mapping_group_id, block_volume_ids, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingGroupsApi->remove_volumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_group_id** | **int**| mapping group id | 
 **block_volume_ids** | [**MappingGroupRemoveVolumesReq**](MappingGroupRemoveVolumesReq.md)| block volume ids | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**MappingGroupResp**](MappingGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mapping_group**
> MappingGroupResp update_mapping_group(mapping_group_id, mapping_group)



update mapping group

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
api_instance = xms_client.MappingGroupsApi(xms_client.ApiClient(configuration))
mapping_group_id = 789 # int | mapping group id
mapping_group = xms_client.MappingGroupUpdateReq() # MappingGroupUpdateReq | mapping info

try:
    api_response = api_instance.update_mapping_group(mapping_group_id, mapping_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingGroupsApi->update_mapping_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_group_id** | **int**| mapping group id | 
 **mapping_group** | [**MappingGroupUpdateReq**](MappingGroupUpdateReq.md)| mapping info | 

### Return type

[**MappingGroupResp**](MappingGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mapping_group_client_group**
> MappingGroupResp update_mapping_group_client_group(mapping_group_id, client_group_id)



update client group in mapping group

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
api_instance = xms_client.MappingGroupsApi(xms_client.ApiClient(configuration))
mapping_group_id = 789 # int | mapping group id
client_group_id = xms_client.MappingGroupUpdateClientGroupReq() # MappingGroupUpdateClientGroupReq | client group id

try:
    api_response = api_instance.update_mapping_group_client_group(mapping_group_id, client_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingGroupsApi->update_mapping_group_client_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_group_id** | **int**| mapping group id | 
 **client_group_id** | [**MappingGroupUpdateClientGroupReq**](MappingGroupUpdateClientGroupReq.md)| client group id | 

### Return type

[**MappingGroupResp**](MappingGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

