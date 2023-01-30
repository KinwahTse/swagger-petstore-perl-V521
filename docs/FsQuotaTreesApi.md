# xms_client.FsQuotaTreesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quota_tree**](FsQuotaTreesApi.md#get_quota_tree) | **GET** /fs-quota-trees/{fs_quota_tree_id} | 
[**list_quota_trees**](FsQuotaTreesApi.md#list_quota_trees) | **GET** /fs-quota-trees/ | 
[**update_quota_tree**](FsQuotaTreesApi.md#update_quota_tree) | **PATCH** /fs-quota-trees/{fs_quota_tree_id} | 


# **get_quota_tree**
> FSQuotaTreeResp get_quota_tree(fs_quota_tree_id)



Get file storage quota tree

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
api_instance = xms_client.FsQuotaTreesApi(xms_client.ApiClient(configuration))
fs_quota_tree_id = 789 # int | quota tree id

try:
    api_response = api_instance.get_quota_tree(fs_quota_tree_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsQuotaTreesApi->get_quota_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_quota_tree_id** | **int**| quota tree id | 

### Return type

[**FSQuotaTreeResp**](FSQuotaTreeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quota_trees**
> FSQuotaTreesResp list_quota_trees(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, fs_folder_id=fs_folder_id)



List file storage quota trees

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
api_instance = xms_client.FsQuotaTreesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
fs_folder_id = 789 # int | file storage folder id (optional)

try:
    api_response = api_instance.list_quota_trees(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, fs_folder_id=fs_folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsQuotaTreesApi->list_quota_trees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **fs_folder_id** | **int**| file storage folder id | [optional] 

### Return type

[**FSQuotaTreesResp**](FSQuotaTreesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quota_tree**
> FSQuotaTreeResp update_quota_tree(fs_quota_tree_id, body)



Update file storage quota tree

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
api_instance = xms_client.FsQuotaTreesApi(xms_client.ApiClient(configuration))
fs_quota_tree_id = 789 # int | quota tree id
body = xms_client.FSQuotaTreeUpdateReq() # FSQuotaTreeUpdateReq | quota tree info

try:
    api_response = api_instance.update_quota_tree(fs_quota_tree_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsQuotaTreesApi->update_quota_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_quota_tree_id** | **int**| quota tree id | 
 **body** | [**FSQuotaTreeUpdateReq**](FSQuotaTreeUpdateReq.md)| quota tree info | 

### Return type

[**FSQuotaTreeResp**](FSQuotaTreeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

