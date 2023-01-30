# xms_client.FsActiveDirectoriesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fs_active_directory**](FsActiveDirectoriesApi.md#create_fs_active_directory) | **POST** /fs-active-directories/ | 
[**delete_fs_active_directory**](FsActiveDirectoriesApi.md#delete_fs_active_directory) | **DELETE** /fs-active-directories/{fs_active_directory_id} | 
[**get_fs_active_directory**](FsActiveDirectoriesApi.md#get_fs_active_directory) | **GET** /fs-active-directories/{fs_active_directory_id} | 
[**list_fs_active_directories**](FsActiveDirectoriesApi.md#list_fs_active_directories) | **GET** /fs-active-directories/ | 
[**update_fs_active_directory**](FsActiveDirectoriesApi.md#update_fs_active_directory) | **PATCH** /fs-active-directories/{fs_active_directory_id} | 
[**verify_fs_active_directory**](FsActiveDirectoriesApi.md#verify_fs_active_directory) | **POST** /fs-active-directories/{fs_active_directory_id}:verify | 


# **create_fs_active_directory**
> FSActiveDirectoryResp create_fs_active_directory(body, cluster_id=cluster_id)



create file storage active directory

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
api_instance = xms_client.FsActiveDirectoriesApi(xms_client.ApiClient(configuration))
body = xms_client.FSActiveDirectoryCreateReq() # FSActiveDirectoryCreateReq | file storage active directory info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_fs_active_directory(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsActiveDirectoriesApi->create_fs_active_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSActiveDirectoryCreateReq**](FSActiveDirectoryCreateReq.md)| file storage active directory info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**FSActiveDirectoryResp**](FSActiveDirectoryResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fs_active_directory**
> FSActiveDirectoryResp delete_fs_active_directory(fs_active_directory_id)



Delete file storage active directory

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
api_instance = xms_client.FsActiveDirectoriesApi(xms_client.ApiClient(configuration))
fs_active_directory_id = 789 # int | file storage active directory id

try:
    api_response = api_instance.delete_fs_active_directory(fs_active_directory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsActiveDirectoriesApi->delete_fs_active_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_active_directory_id** | **int**| file storage active directory id | 

### Return type

[**FSActiveDirectoryResp**](FSActiveDirectoryResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fs_active_directory**
> FSActiveDirectoryResp get_fs_active_directory(fs_active_directory_id)



Get a file storage active directory

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
api_instance = xms_client.FsActiveDirectoriesApi(xms_client.ApiClient(configuration))
fs_active_directory_id = 789 # int | file storage active directory id

try:
    api_response = api_instance.get_fs_active_directory(fs_active_directory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsActiveDirectoriesApi->get_fs_active_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_active_directory_id** | **int**| file storage active directory id | 

### Return type

[**FSActiveDirectoryResp**](FSActiveDirectoryResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fs_active_directories**
> FSActiveDirectoriesResp list_fs_active_directories(limit=limit, offset=offset, cluster_id=cluster_id)



List file storage active directories

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
api_instance = xms_client.FsActiveDirectoriesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_fs_active_directories(limit=limit, offset=offset, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsActiveDirectoriesApi->list_fs_active_directories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**FSActiveDirectoriesResp**](FSActiveDirectoriesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fs_active_directory**
> FSActiveDirectoryResp update_fs_active_directory(fs_active_directory_id, body)



Update a file storage active directory

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
api_instance = xms_client.FsActiveDirectoriesApi(xms_client.ApiClient(configuration))
fs_active_directory_id = 789 # int | file storage active directory id
body = xms_client.FSActiveDirectoryUpdateReq() # FSActiveDirectoryUpdateReq | file storage active directory info

try:
    api_response = api_instance.update_fs_active_directory(fs_active_directory_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsActiveDirectoriesApi->update_fs_active_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_active_directory_id** | **int**| file storage active directory id | 
 **body** | [**FSActiveDirectoryUpdateReq**](FSActiveDirectoryUpdateReq.md)| file storage active directory info | 

### Return type

[**FSActiveDirectoryResp**](FSActiveDirectoryResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_fs_active_directory**
> FSActiveDirectoryResp verify_fs_active_directory(fs_active_directory_id)



Verify a fs active directory or user/group info

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
api_instance = xms_client.FsActiveDirectoriesApi(xms_client.ApiClient(configuration))
fs_active_directory_id = 789 # int | file storage active directory id

try:
    api_response = api_instance.verify_fs_active_directory(fs_active_directory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsActiveDirectoriesApi->verify_fs_active_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_active_directory_id** | **int**| file storage active directory id | 

### Return type

[**FSActiveDirectoryResp**](FSActiveDirectoryResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

