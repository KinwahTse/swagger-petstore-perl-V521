# xms_client.DfsWormsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dfs_worm**](DfsWormsApi.md#create_dfs_worm) | **POST** /dfs-worms/ | 
[**delete_dfs_worm**](DfsWormsApi.md#delete_dfs_worm) | **DELETE** /dfs-worms/{dfs_worm_id} | 
[**get_dfs_worm**](DfsWormsApi.md#get_dfs_worm) | **GET** /dfs-worms/{dfs_worm_id} | 
[**list_dfs_worms**](DfsWormsApi.md#list_dfs_worms) | **GET** /dfs-worms/ | 
[**update_dfs_worm**](DfsWormsApi.md#update_dfs_worm) | **PATCH** /dfs-worms/{dfs_worm_id} | 


# **create_dfs_worm**
> DfsWormResp create_dfs_worm(body, allow_path_create=allow_path_create)



Create dfs worm

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
api_instance = xms_client.DfsWormsApi(xms_client.ApiClient(configuration))
body = xms_client.DfsWormCreateReq() # DfsWormCreateReq | worm info
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.create_dfs_worm(body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsWormsApi->create_dfs_worm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsWormCreateReq**](DfsWormCreateReq.md)| worm info | 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DfsWormResp**](DfsWormResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_worm**
> DfsWormResp delete_dfs_worm(dfs_worm_id)



delete dfs worm

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
api_instance = xms_client.DfsWormsApi(xms_client.ApiClient(configuration))
dfs_worm_id = 789 # int | worm id

try:
    api_response = api_instance.delete_dfs_worm(dfs_worm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsWormsApi->delete_dfs_worm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_worm_id** | **int**| worm id | 

### Return type

[**DfsWormResp**](DfsWormResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_worm**
> DfsWormResp get_dfs_worm(dfs_worm_id)



get dfs worm

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
api_instance = xms_client.DfsWormsApi(xms_client.ApiClient(configuration))
dfs_worm_id = 789 # int | the dfs worm id

try:
    api_response = api_instance.get_dfs_worm(dfs_worm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsWormsApi->get_dfs_worm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_worm_id** | **int**| the dfs worm id | 

### Return type

[**DfsWormResp**](DfsWormResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_worms**
> DfsWormsResp list_dfs_worms(cluster_id=cluster_id, dfs_path_id=dfs_path_id, path=path, limit=limit, offset=offset, q=q, sort=sort)



List dfs worms

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
api_instance = xms_client.DfsWormsApi(xms_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | cluster id (optional)
dfs_path_id = 789 # int | related dfs path id (optional)
path = 'path_example' # str | related dfs path (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dfs_worms(cluster_id=cluster_id, dfs_path_id=dfs_path_id, path=path, limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsWormsApi->list_dfs_worms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| cluster id | [optional] 
 **dfs_path_id** | **int**| related dfs path id | [optional] 
 **path** | **str**| related dfs path | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DfsWormsResp**](DfsWormsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_worm**
> DfsWormResp update_dfs_worm(dfs_worm_id, body)



Update dfs worm

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
api_instance = xms_client.DfsWormsApi(xms_client.ApiClient(configuration))
dfs_worm_id = 789 # int | dfs worm id
body = xms_client.DfsWormUpdateReq() # DfsWormUpdateReq | dfs worm info

try:
    api_response = api_instance.update_dfs_worm(dfs_worm_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsWormsApi->update_dfs_worm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_worm_id** | **int**| dfs worm id | 
 **body** | [**DfsWormUpdateReq**](DfsWormUpdateReq.md)| dfs worm info | 

### Return type

[**DfsWormResp**](DfsWormResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

