# xms_client.DfsS3KeysApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dfs_s3_key**](DfsS3KeysApi.md#create_dfs_s3_key) | **POST** /dfs-s3-keys/ | 
[**delete_dfs_s3_key**](DfsS3KeysApi.md#delete_dfs_s3_key) | **DELETE** /dfs-s3-keys/{key_id} | 
[**get_dfs_s3_key**](DfsS3KeysApi.md#get_dfs_s3_key) | **GET** /dfs-s3-keys/{key_id} | 
[**list_dfs_s3_keys**](DfsS3KeysApi.md#list_dfs_s3_keys) | **GET** /dfs-s3-keys/ | 
[**update_dfs_s3_key**](DfsS3KeysApi.md#update_dfs_s3_key) | **PATCH** /dfs-s3-keys/{key_id} | 


# **create_dfs_s3_key**
> DfsS3KeyResp create_dfs_s3_key(body, cluster_id=cluster_id)



Create new dfs s3 key

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
api_instance = xms_client.DfsS3KeysApi(xms_client.ApiClient(configuration))
body = xms_client.DfsS3KeyCreateReq() # DfsS3KeyCreateReq | key info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_dfs_s3_key(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3KeysApi->create_dfs_s3_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsS3KeyCreateReq**](DfsS3KeyCreateReq.md)| key info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**DfsS3KeyResp**](DfsS3KeyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_s3_key**
> DfsS3KeyResp delete_dfs_s3_key(key_id)



Delete dfs s3 key

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
api_instance = xms_client.DfsS3KeysApi(xms_client.ApiClient(configuration))
key_id = 789 # int | key id

try:
    api_response = api_instance.delete_dfs_s3_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3KeysApi->delete_dfs_s3_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**| key id | 

### Return type

[**DfsS3KeyResp**](DfsS3KeyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_s3_key**
> DfsS3KeyResp get_dfs_s3_key(key_id)



get dfs s3 key

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
api_instance = xms_client.DfsS3KeysApi(xms_client.ApiClient(configuration))
key_id = 789 # int | user id

try:
    api_response = api_instance.get_dfs_s3_key(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3KeysApi->get_dfs_s3_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**| user id | 

### Return type

[**DfsS3KeyResp**](DfsS3KeyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_s3_keys**
> DfsS3KeysResp list_dfs_s3_keys(cluster_id=cluster_id, user_id=user_id, limit=limit, offset=offset)



List dfs s3 keys

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
api_instance = xms_client.DfsS3KeysApi(xms_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | cluster id (optional)
user_id = 789 # int | dfs s3 user id (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_dfs_s3_keys(cluster_id=cluster_id, user_id=user_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3KeysApi->list_dfs_s3_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| cluster id | [optional] 
 **user_id** | **int**| dfs s3 user id | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**DfsS3KeysResp**](DfsS3KeysResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_s3_key**
> DfsS3KeyResp update_dfs_s3_key(key_id, body)



Update dfs s3 key

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
api_instance = xms_client.DfsS3KeysApi(xms_client.ApiClient(configuration))
key_id = 789 # int | key id
body = xms_client.DfsS3KeyUpdateReq() # DfsS3KeyUpdateReq | key info

try:
    api_response = api_instance.update_dfs_s3_key(key_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3KeysApi->update_dfs_s3_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**| key id | 
 **body** | [**DfsS3KeyUpdateReq**](DfsS3KeyUpdateReq.md)| key info | 

### Return type

[**DfsS3KeyResp**](DfsS3KeyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

