# xms_client.AccessPathsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_path**](AccessPathsApi.md#create_access_path) | **POST** /access-paths/ | 
[**delete_access_path**](AccessPathsApi.md#delete_access_path) | **DELETE** /access-paths/{access_path_id} | 
[**get_access_path**](AccessPathsApi.md#get_access_path) | **GET** /access-paths/{access_path_id} | 
[**list_access_paths**](AccessPathsApi.md#list_access_paths) | **GET** /access-paths/ | 
[**update_access_path**](AccessPathsApi.md#update_access_path) | **PATCH** /access-paths/{access_path_id} | 


# **create_access_path**
> AccessPathResp create_access_path(access_path, cluster_id=cluster_id)



Create an access path

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
api_instance = xms_client.AccessPathsApi(xms_client.ApiClient(configuration))
access_path = xms_client.AccessPathCreateReq() # AccessPathCreateReq | access path info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_access_path(access_path, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessPathsApi->create_access_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_path** | [**AccessPathCreateReq**](AccessPathCreateReq.md)| access path info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**AccessPathResp**](AccessPathResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_path**
> AccessPathResp delete_access_path(access_path_id)



Delete access path

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
api_instance = xms_client.AccessPathsApi(xms_client.ApiClient(configuration))
access_path_id = 789 # int | access path id

try:
    api_response = api_instance.delete_access_path(access_path_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessPathsApi->delete_access_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_path_id** | **int**| access path id | 

### Return type

[**AccessPathResp**](AccessPathResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_path**
> AccessPathResp get_access_path(access_path_id)



Get access path by id

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
api_instance = xms_client.AccessPathsApi(xms_client.ApiClient(configuration))
access_path_id = 789 # int | access path id

try:
    api_response = api_instance.get_access_path(access_path_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessPathsApi->get_access_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_path_id** | **int**| access path id | 

### Return type

[**AccessPathResp**](AccessPathResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_paths**
> AccessPathsResp list_access_paths(limit=limit, offset=offset, cluster_id=cluster_id, q=q, uid=uid, client_group_id=client_group_id, all=all)



List access paths

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
api_instance = xms_client.AccessPathsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
q = 'q_example' # str | query param of search (optional)
uid = 'uid_example' # str | access path uid (optional)
client_group_id = 789 # int | related client group id (optional)
all = true # bool | show all access targets (optional)

try:
    api_response = api_instance.list_access_paths(limit=limit, offset=offset, cluster_id=cluster_id, q=q, uid=uid, client_group_id=client_group_id, all=all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessPathsApi->list_access_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **uid** | **str**| access path uid | [optional] 
 **client_group_id** | **int**| related client group id | [optional] 
 **all** | **bool**| show all access targets | [optional] 

### Return type

[**AccessPathsResp**](AccessPathsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_path**
> AccessPathResp update_access_path(access_path_id, access_path)



update access path

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
api_instance = xms_client.AccessPathsApi(xms_client.ApiClient(configuration))
access_path_id = 789 # int | access path id
access_path = xms_client.AccessPathUpdateReq() # AccessPathUpdateReq | access path info

try:
    api_response = api_instance.update_access_path(access_path_id, access_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessPathsApi->update_access_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_path_id** | **int**| access path id | 
 **access_path** | [**AccessPathUpdateReq**](AccessPathUpdateReq.md)| access path info | 

### Return type

[**AccessPathResp**](AccessPathResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

