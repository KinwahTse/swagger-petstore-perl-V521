# xms_client.DfsDirectoriesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dfs_directories**](DfsDirectoriesApi.md#create_dfs_directories) | **POST** /dfs-directories/:create | 
[**create_dfs_directory**](DfsDirectoriesApi.md#create_dfs_directory) | **POST** /dfs-directories/:mkdir | 
[**delete_dfs_directories**](DfsDirectoriesApi.md#delete_dfs_directories) | **POST** /dfs-directories/:delete | 
[**delete_dfs_directory**](DfsDirectoriesApi.md#delete_dfs_directory) | **POST** /dfs-directories/:rmdir | 
[**directory_validator**](DfsDirectoriesApi.md#directory_validator) | **GET** /dfs-directories/directory-validator | 


# **create_dfs_directories**
> DfsDirectoriesResp create_dfs_directories(body)



Create directories in dfs rootfs

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
api_instance = xms_client.DfsDirectoriesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsDirectoriesReq() # DfsDirectoriesReq | directories info

try:
    api_response = api_instance.create_dfs_directories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsDirectoriesApi->create_dfs_directories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsDirectoriesReq**](DfsDirectoriesReq.md)| directories info | 

### Return type

[**DfsDirectoriesResp**](DfsDirectoriesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dfs_directory**
> DfsDirectoryResp create_dfs_directory(body)



Create directory in dfs rootfs

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
api_instance = xms_client.DfsDirectoriesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsDirectoryReq() # DfsDirectoryReq | directory info

try:
    api_response = api_instance.create_dfs_directory(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsDirectoriesApi->create_dfs_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsDirectoryReq**](DfsDirectoryReq.md)| directory info | 

### Return type

[**DfsDirectoryResp**](DfsDirectoryResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_directories**
> DfsDirectoriesResp delete_dfs_directories(body)



Delete directories in dfs rootfs, deprecated

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
api_instance = xms_client.DfsDirectoriesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsDirectoriesReq() # DfsDirectoriesReq | directories info

try:
    api_response = api_instance.delete_dfs_directories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsDirectoriesApi->delete_dfs_directories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsDirectoriesReq**](DfsDirectoriesReq.md)| directories info | 

### Return type

[**DfsDirectoriesResp**](DfsDirectoriesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_directory**
> DfsDirectoryResp delete_dfs_directory(body)



Delete directory in dfs rootfs

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
api_instance = xms_client.DfsDirectoriesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsDirectoryReq() # DfsDirectoryReq | directory info

try:
    api_response = api_instance.delete_dfs_directory(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsDirectoriesApi->delete_dfs_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsDirectoryReq**](DfsDirectoryReq.md)| directory info | 

### Return type

[**DfsDirectoryResp**](DfsDirectoryResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_validator**
> DfsDirectoryValidationResp directory_validator(rootfs_id, path)



validate specified directory whether exists, subdirectory contains quotas, snapshots, shares

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
api_instance = xms_client.DfsDirectoriesApi(xms_client.ApiClient(configuration))
rootfs_id = 789 # int | dfs rootfs id
path = 'path_example' # str | dfs quota path

try:
    api_response = api_instance.directory_validator(rootfs_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsDirectoriesApi->directory_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rootfs_id** | **int**| dfs rootfs id | 
 **path** | **str**| dfs quota path | 

### Return type

[**DfsDirectoryValidationResp**](DfsDirectoryValidationResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

