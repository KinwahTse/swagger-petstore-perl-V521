# xms_client.OsExternalStorageClassesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_storage_class**](OsExternalStorageClassesApi.md#create_external_storage_class) | **POST** /os-external-storage-classes/ | 
[**delete_os_external_storage_class**](OsExternalStorageClassesApi.md#delete_os_external_storage_class) | **DELETE** /os-external-storage-classes/{external_storage_class_id} | 
[**get_os_external_storage_class**](OsExternalStorageClassesApi.md#get_os_external_storage_class) | **GET** /os-external-storage-classes/{external_storage_class_id} | 
[**list_os_external_storage_classes**](OsExternalStorageClassesApi.md#list_os_external_storage_classes) | **GET** /os-external-storage-classes/ | 
[**update_os_external_storage_class**](OsExternalStorageClassesApi.md#update_os_external_storage_class) | **PATCH** /os-external-storage-classes/{external_storage_class_id} | 


# **create_external_storage_class**
> OSExternalStorageClassResp create_external_storage_class(body, cluster_id=cluster_id)



Create os external storage class

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
api_instance = xms_client.OsExternalStorageClassesApi(xms_client.ApiClient(configuration))
body = xms_client.OSExternalStorageClassCreateReq() # OSExternalStorageClassCreateReq | external storage class info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_external_storage_class(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsExternalStorageClassesApi->create_external_storage_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OSExternalStorageClassCreateReq**](OSExternalStorageClassCreateReq.md)| external storage class info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSExternalStorageClassResp**](OSExternalStorageClassResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_os_external_storage_class**
> OSExternalStorageClassResp delete_os_external_storage_class(external_storage_class_id)



Delete an os external storage class

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
api_instance = xms_client.OsExternalStorageClassesApi(xms_client.ApiClient(configuration))
external_storage_class_id = 789 # int | external storage class id

try:
    api_response = api_instance.delete_os_external_storage_class(external_storage_class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsExternalStorageClassesApi->delete_os_external_storage_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_storage_class_id** | **int**| external storage class id | 

### Return type

[**OSExternalStorageClassResp**](OSExternalStorageClassResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_external_storage_class**
> OSExternalStorageClassResp get_os_external_storage_class(external_storage_class_id)



Get a os external storage class

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
api_instance = xms_client.OsExternalStorageClassesApi(xms_client.ApiClient(configuration))
external_storage_class_id = 789 # int | external storage class id

try:
    api_response = api_instance.get_os_external_storage_class(external_storage_class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsExternalStorageClassesApi->get_os_external_storage_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_storage_class_id** | **int**| external storage class id | 

### Return type

[**OSExternalStorageClassResp**](OSExternalStorageClassResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_external_storage_classes**
> OSExternalStorageClassesResp list_os_external_storage_classes(limit=limit, offset=offset, os_policy_id=os_policy_id, general_status=general_status, cluster_id=cluster_id)



List os external storage classes

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
api_instance = xms_client.OsExternalStorageClassesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
os_policy_id = 789 # int | os policy id (optional)
general_status = true # bool | query records with active or error status (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_os_external_storage_classes(limit=limit, offset=offset, os_policy_id=os_policy_id, general_status=general_status, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsExternalStorageClassesApi->list_os_external_storage_classes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **os_policy_id** | **int**| os policy id | [optional] 
 **general_status** | **bool**| query records with active or error status | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSExternalStorageClassesResp**](OSExternalStorageClassesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_os_external_storage_class**
> OSExternalStorageClassResp update_os_external_storage_class(external_storage_class_id, body)



update os external storage class

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
api_instance = xms_client.OsExternalStorageClassesApi(xms_client.ApiClient(configuration))
external_storage_class_id = 789 # int | external storage class id
body = xms_client.OSExternalStorageClassUpdateReq() # OSExternalStorageClassUpdateReq | external storage class info

try:
    api_response = api_instance.update_os_external_storage_class(external_storage_class_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsExternalStorageClassesApi->update_os_external_storage_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_storage_class_id** | **int**| external storage class id | 
 **body** | [**OSExternalStorageClassUpdateReq**](OSExternalStorageClassUpdateReq.md)| external storage class info | 

### Return type

[**OSExternalStorageClassResp**](OSExternalStorageClassResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

