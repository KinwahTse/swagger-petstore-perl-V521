# xms_client.FsFoldersApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fs_quota_trees**](FsFoldersApi.md#add_fs_quota_trees) | **PUT** /fs-folders/{fs_folder_id}/fs-quota-trees | 
[**create_folder**](FsFoldersApi.md#create_folder) | **POST** /fs-folders/ | 
[**delete_folder**](FsFoldersApi.md#delete_folder) | **DELETE** /fs-folders/{fs_folder_id} | 
[**get_folder**](FsFoldersApi.md#get_folder) | **GET** /fs-folders/{fs_folder_id} | 
[**get_fs_folder_samples**](FsFoldersApi.md#get_fs_folder_samples) | **GET** /fs-folders/{fs_folder_id}/samples | 
[**list_folders**](FsFoldersApi.md#list_folders) | **GET** /fs-folders/ | 
[**remove_fs_quota_trees**](FsFoldersApi.md#remove_fs_quota_trees) | **DELETE** /fs-folders/{fs_folder_id}/fs-quota-trees | 
[**roll_back_folder**](FsFoldersApi.md#roll_back_folder) | **POST** /fs-folders/{fs_folder_id}:roll-back | 
[**set_fs_snapshot_protection**](FsFoldersApi.md#set_fs_snapshot_protection) | **POST** /fs-folders/{fs_folder_id}:set-snapshot-protection | 
[**unset_fs_snapshot_protection**](FsFoldersApi.md#unset_fs_snapshot_protection) | **POST** /fs-folders/{fs_folder_id}:unset-snapshot-protection | 
[**update_folder**](FsFoldersApi.md#update_folder) | **PATCH** /fs-folders/{fs_folder_id} | 


# **add_fs_quota_trees**
> FSFolderQuotaTreesResp add_fs_quota_trees(fs_folder_id, body)



add file storage quota trees

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
fs_folder_id = 789 # int | fs folder id
body = xms_client.FSFolderAddQuotaTreesReq() # FSFolderAddQuotaTreesReq | quota trees info

try:
    api_response = api_instance.add_fs_quota_trees(fs_folder_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->add_fs_quota_trees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_folder_id** | **int**| fs folder id | 
 **body** | [**FSFolderAddQuotaTreesReq**](FSFolderAddQuotaTreesReq.md)| quota trees info | 

### Return type

[**FSFolderQuotaTreesResp**](FSFolderQuotaTreesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> FSFolderResp create_folder(body)



Create file storage folder

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
body = xms_client.FSFolderCreateReq() # FSFolderCreateReq | folder info

try:
    api_response = api_instance.create_folder(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSFolderCreateReq**](FSFolderCreateReq.md)| folder info | 

### Return type

[**FSFolderResp**](FSFolderResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> FSFolderResp delete_folder(fs_folder_id, force=force)



delete file storage folder

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
fs_folder_id = 789 # int | folder id
force = true # bool | force delete (optional)

try:
    api_response = api_instance.delete_folder(fs_folder_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_folder_id** | **int**| folder id | 
 **force** | **bool**| force delete | [optional] 

### Return type

[**FSFolderResp**](FSFolderResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> FSFolderResp get_folder(fs_folder_id)



Get file storage folder

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
fs_folder_id = 789 # int | folder id

try:
    api_response = api_instance.get_folder(fs_folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->get_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_folder_id** | **int**| folder id | 

### Return type

[**FSFolderResp**](FSFolderResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fs_folder_samples**
> FSFolderSamplesResp get_fs_folder_samples(fs_folder_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a file storage folder's samples

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
fs_folder_id = 789 # int | file storage folder id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_fs_folder_samples(fs_folder_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->get_fs_folder_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_folder_id** | **int**| file storage folder id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**FSFolderSamplesResp**](FSFolderSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_folders**
> FSFoldersResp list_folders(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, fs_user_id=fs_user_id, fs_user_group_id=fs_user_group_id, fs_gateway_group_id=fs_gateway_group_id, fs_snapshot_id=fs_snapshot_id, fs_client_id=fs_client_id, fs_client_group_id=fs_client_group_id, pool_id=pool_id)



List file storage folders

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
fs_user_id = 789 # int | file storage user id (optional)
fs_user_group_id = 789 # int | file storage user group id (optional)
fs_gateway_group_id = 789 # int | file storage gateway group id (optional)
fs_snapshot_id = 789 # int | file storage snapshot id (optional)
fs_client_id = 789 # int | file storage client id (optional)
fs_client_group_id = 789 # int | file storage client group id (optional)
pool_id = 789 # int | pool id (optional)

try:
    api_response = api_instance.list_folders(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, fs_user_id=fs_user_id, fs_user_group_id=fs_user_group_id, fs_gateway_group_id=fs_gateway_group_id, fs_snapshot_id=fs_snapshot_id, fs_client_id=fs_client_id, fs_client_group_id=fs_client_group_id, pool_id=pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->list_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **fs_user_id** | **int**| file storage user id | [optional] 
 **fs_user_group_id** | **int**| file storage user group id | [optional] 
 **fs_gateway_group_id** | **int**| file storage gateway group id | [optional] 
 **fs_snapshot_id** | **int**| file storage snapshot id | [optional] 
 **fs_client_id** | **int**| file storage client id | [optional] 
 **fs_client_group_id** | **int**| file storage client group id | [optional] 
 **pool_id** | **int**| pool id | [optional] 

### Return type

[**FSFoldersResp**](FSFoldersResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_fs_quota_trees**
> FSFolderResp remove_fs_quota_trees(fs_folder_id, body)



delete fs quota trees from fs folder

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
fs_folder_id = 789 # int | fs folder id
body = xms_client.FSFolderRemoveQuotaTreesReq() # FSFolderRemoveQuotaTreesReq | quota trees info

try:
    api_response = api_instance.remove_fs_quota_trees(fs_folder_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->remove_fs_quota_trees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_folder_id** | **int**| fs folder id | 
 **body** | [**FSFolderRemoveQuotaTreesReq**](FSFolderRemoveQuotaTreesReq.md)| quota trees info | 

### Return type

[**FSFolderResp**](FSFolderResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roll_back_folder**
> FSFolderResp roll_back_folder(fs_folder_id, body)



roll back file storage folder

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
fs_folder_id = 789 # int | folder id
body = xms_client.FSFolderRollBackReq() # FSFolderRollBackReq | folder info

try:
    api_response = api_instance.roll_back_folder(fs_folder_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->roll_back_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_folder_id** | **int**| folder id | 
 **body** | [**FSFolderRollBackReq**](FSFolderRollBackReq.md)| folder info | 

### Return type

[**FSFolderResp**](FSFolderResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_fs_snapshot_protection**
> FSFolderResp set_fs_snapshot_protection(fs_folder_id, body)



Set snapshot protection for a fs folder

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
fs_folder_id = 789 # int | fs folder id in db
body = xms_client.FSFolderSnapshotProtectionReq() # FSFolderSnapshotProtectionReq | request info

try:
    api_response = api_instance.set_fs_snapshot_protection(fs_folder_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->set_fs_snapshot_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_folder_id** | **int**| fs folder id in db | 
 **body** | [**FSFolderSnapshotProtectionReq**](FSFolderSnapshotProtectionReq.md)| request info | 

### Return type

[**FSFolderResp**](FSFolderResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_fs_snapshot_protection**
> FSFolderResp unset_fs_snapshot_protection(fs_folder_id, force=force)



Unset snapshot protection for a fs folder

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
fs_folder_id = 789 # int | fs_folder id in db
force = true # bool | force unset or not (optional)

try:
    api_response = api_instance.unset_fs_snapshot_protection(fs_folder_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->unset_fs_snapshot_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_folder_id** | **int**| fs_folder id in db | 
 **force** | **bool**| force unset or not | [optional] 

### Return type

[**FSFolderResp**](FSFolderResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> FSFolderResp update_folder(fs_folder_id, body)



Update file storage folder

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
api_instance = xms_client.FsFoldersApi(xms_client.ApiClient(configuration))
fs_folder_id = 789 # int | folder id
body = xms_client.FSFolderUpdateReq() # FSFolderUpdateReq | folder info

try:
    api_response = api_instance.update_folder(fs_folder_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFoldersApi->update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_folder_id** | **int**| folder id | 
 **body** | [**FSFolderUpdateReq**](FSFolderUpdateReq.md)| folder info | 

### Return type

[**FSFolderResp**](FSFolderResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

