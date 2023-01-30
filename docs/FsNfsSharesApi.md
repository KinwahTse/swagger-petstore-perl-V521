# xms_client.FsNfsSharesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fsnfs_share_ac_ls**](FsNfsSharesApi.md#add_fsnfs_share_ac_ls) | **POST** /fs-nfs-shares/{fs_nfs_share_id}:add-acls | 
[**create_fsnfs_share**](FsNfsSharesApi.md#create_fsnfs_share) | **POST** /fs-nfs-shares/ | 
[**delete_fsnfs_share**](FsNfsSharesApi.md#delete_fsnfs_share) | **DELETE** /fs-nfs-shares/{fs_nfs_share_id} | 
[**get_fsnfs_share**](FsNfsSharesApi.md#get_fsnfs_share) | **GET** /fs-nfs-shares/{fs_nfs_share_id} | 
[**list_fsnfs_shares**](FsNfsSharesApi.md#list_fsnfs_shares) | **GET** /fs-nfs-shares/ | 
[**remove_fsnfs_share_ac_ls**](FsNfsSharesApi.md#remove_fsnfs_share_ac_ls) | **POST** /fs-nfs-shares/{fs_nfs_share_id}:remove-acls | 
[**update_fsnfs_share_ac_ls**](FsNfsSharesApi.md#update_fsnfs_share_ac_ls) | **POST** /fs-nfs-shares/{fs_nfs_share_id}:update-acls | 


# **add_fsnfs_share_ac_ls**
> FSNFSShareResp add_fsnfs_share_ac_ls(fs_nfs_share_id, body)



Add fs nfs shares acls

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
api_instance = xms_client.FsNfsSharesApi(xms_client.ApiClient(configuration))
fs_nfs_share_id = 789 # int | fs nfs shares id
body = xms_client.FSNFSShareAddACLsReq() # FSNFSShareAddACLsReq | share acls info

try:
    api_response = api_instance.add_fsnfs_share_ac_ls(fs_nfs_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsNfsSharesApi->add_fsnfs_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_nfs_share_id** | **int**| fs nfs shares id | 
 **body** | [**FSNFSShareAddACLsReq**](FSNFSShareAddACLsReq.md)| share acls info | 

### Return type

[**FSNFSShareResp**](FSNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fsnfs_share**
> FSNFSShareResp create_fsnfs_share(body)



Create fs nfs shares

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
api_instance = xms_client.FsNfsSharesApi(xms_client.ApiClient(configuration))
body = xms_client.FSNFSShareCreateReq() # FSNFSShareCreateReq | share info

try:
    api_response = api_instance.create_fsnfs_share(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsNfsSharesApi->create_fsnfs_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSNFSShareCreateReq**](FSNFSShareCreateReq.md)| share info | 

### Return type

[**FSNFSShareResp**](FSNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fsnfs_share**
> FSNFSShareResp delete_fsnfs_share(fs_nfs_share_id, force=force)



delete fs nfs shares

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
api_instance = xms_client.FsNfsSharesApi(xms_client.ApiClient(configuration))
fs_nfs_share_id = 789 # int | share id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_fsnfs_share(fs_nfs_share_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsNfsSharesApi->delete_fsnfs_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_nfs_share_id** | **int**| share id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**FSNFSShareResp**](FSNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fsnfs_share**
> FSNFSShareResp get_fsnfs_share(fs_nfs_share_id)



Get fs nfs shares

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
api_instance = xms_client.FsNfsSharesApi(xms_client.ApiClient(configuration))
fs_nfs_share_id = 789 # int | share id

try:
    api_response = api_instance.get_fsnfs_share(fs_nfs_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsNfsSharesApi->get_fsnfs_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_nfs_share_id** | **int**| share id | 

### Return type

[**FSNFSShareResp**](FSNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fsnfs_shares**
> FSNFSSharesResp list_fsnfs_shares(limit=limit, offset=offset, cluster_id=cluster_id, fs_folder_id=fs_folder_id, fs_gateway_group_id=fs_gateway_group_id, q=q, sort=sort)



List fs nfs sharess

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
api_instance = xms_client.FsNfsSharesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
fs_folder_id = 789 # int | fs nfs id (optional)
fs_gateway_group_id = 789 # int | file storage gateway group id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_fsnfs_shares(limit=limit, offset=offset, cluster_id=cluster_id, fs_folder_id=fs_folder_id, fs_gateway_group_id=fs_gateway_group_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsNfsSharesApi->list_fsnfs_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **fs_folder_id** | **int**| fs nfs id | [optional] 
 **fs_gateway_group_id** | **int**| file storage gateway group id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**FSNFSSharesResp**](FSNFSSharesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_fsnfs_share_ac_ls**
> FSNFSShareResp remove_fsnfs_share_ac_ls(fs_nfs_share_id, body)



remove fs nfs shares acls

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
api_instance = xms_client.FsNfsSharesApi(xms_client.ApiClient(configuration))
fs_nfs_share_id = 789 # int | fs nfs shares id
body = xms_client.FSNFSShareRemoveACLsReq() # FSNFSShareRemoveACLsReq | share acls info

try:
    api_response = api_instance.remove_fsnfs_share_ac_ls(fs_nfs_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsNfsSharesApi->remove_fsnfs_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_nfs_share_id** | **int**| fs nfs shares id | 
 **body** | [**FSNFSShareRemoveACLsReq**](FSNFSShareRemoveACLsReq.md)| share acls info | 

### Return type

[**FSNFSShareResp**](FSNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fsnfs_share_ac_ls**
> FSNFSShareResp update_fsnfs_share_ac_ls(fs_nfs_share_id, body)



Update fs nfs share acls

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
api_instance = xms_client.FsNfsSharesApi(xms_client.ApiClient(configuration))
fs_nfs_share_id = 789 # int | share id
body = xms_client.FSNFSShareUpdateACLsReq() # FSNFSShareUpdateACLsReq | share info

try:
    api_response = api_instance.update_fsnfs_share_ac_ls(fs_nfs_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsNfsSharesApi->update_fsnfs_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_nfs_share_id** | **int**| share id | 
 **body** | [**FSNFSShareUpdateACLsReq**](FSNFSShareUpdateACLsReq.md)| share info | 

### Return type

[**FSNFSShareResp**](FSNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

