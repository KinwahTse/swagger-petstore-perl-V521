# xms_client.OsStorageClassesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_os_storage_class**](OsStorageClassesApi.md#create_os_storage_class) | **POST** /os-storage-classes/ | 
[**delete_os_storage_class**](OsStorageClassesApi.md#delete_os_storage_class) | **DELETE** /os-storage-classes/{storage_class_id} | 
[**get_os_storage_class**](OsStorageClassesApi.md#get_os_storage_class) | **GET** /os-storage-classes/{storage_class_id} | 
[**list_os_storage_classes**](OsStorageClassesApi.md#list_os_storage_classes) | **GET** /os-storage-classes/ | 
[**update_os_storage_class**](OsStorageClassesApi.md#update_os_storage_class) | **PATCH** /os-storage-classes/{storage_class_id} | 


# **create_os_storage_class**
> OSStorageClassResp create_os_storage_class(body, cluster_id=cluster_id)



Create os storage class

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
api_instance = xms_client.OsStorageClassesApi(xms_client.ApiClient(configuration))
body = xms_client.OSStorageClassCreateReq() # OSStorageClassCreateReq | storage class info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_os_storage_class(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsStorageClassesApi->create_os_storage_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OSStorageClassCreateReq**](OSStorageClassCreateReq.md)| storage class info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSStorageClassResp**](OSStorageClassResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_os_storage_class**
> OSStorageClassResp delete_os_storage_class(storage_class_id)



Delete an os storage class

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
api_instance = xms_client.OsStorageClassesApi(xms_client.ApiClient(configuration))
storage_class_id = 789 # int | storage class id

try:
    api_response = api_instance.delete_os_storage_class(storage_class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsStorageClassesApi->delete_os_storage_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_class_id** | **int**| storage class id | 

### Return type

[**OSStorageClassResp**](OSStorageClassResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_storage_class**
> OSStorageClassResp get_os_storage_class(storage_class_id)



Get an os storage class

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
api_instance = xms_client.OsStorageClassesApi(xms_client.ApiClient(configuration))
storage_class_id = 'storage_class_id_example' # str | storage class id

try:
    api_response = api_instance.get_os_storage_class(storage_class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsStorageClassesApi->get_os_storage_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_class_id** | **str**| storage class id | 

### Return type

[**OSStorageClassResp**](OSStorageClassResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_storage_classes**
> OSStorageClassesResp list_os_storage_classes(limit=limit, offset=offset, os_policy_id=os_policy_id, cluster_id=cluster_id)



List os storage classes

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
api_instance = xms_client.OsStorageClassesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
os_policy_id = 789 # int | os policy id (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_os_storage_classes(limit=limit, offset=offset, os_policy_id=os_policy_id, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsStorageClassesApi->list_os_storage_classes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **os_policy_id** | **int**| os policy id | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSStorageClassesResp**](OSStorageClassesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_os_storage_class**
> OSStorageClassResp update_os_storage_class(storage_class_id, body)



update storage class

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
api_instance = xms_client.OsStorageClassesApi(xms_client.ApiClient(configuration))
storage_class_id = 789 # int | storage class id
body = xms_client.OSStorageClassUpdateReq() # OSStorageClassUpdateReq | storage class info

try:
    api_response = api_instance.update_os_storage_class(storage_class_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsStorageClassesApi->update_os_storage_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_class_id** | **int**| storage class id | 
 **body** | [**OSStorageClassUpdateReq**](OSStorageClassUpdateReq.md)| storage class info | 

### Return type

[**OSStorageClassResp**](OSStorageClassResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

