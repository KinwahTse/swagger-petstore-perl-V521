# xms_client.DfsNfsSharesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dfs_nfs_share_ac_ls**](DfsNfsSharesApi.md#add_dfs_nfs_share_ac_ls) | **POST** /dfs-nfs-shares/{dfs_nfs_share_id}:add-acls | 
[**create_dfs_nfs_share**](DfsNfsSharesApi.md#create_dfs_nfs_share) | **POST** /dfs-nfs-shares/ | 
[**delete_dfs_nfs_share**](DfsNfsSharesApi.md#delete_dfs_nfs_share) | **DELETE** /dfs-nfs-shares/{dfs_nfs_share_id} | 
[**get_dfs_nfs_share**](DfsNfsSharesApi.md#get_dfs_nfs_share) | **GET** /dfs-nfs-shares/{dfs_nfs_share_id} | 
[**list_dfs_nfs_shares**](DfsNfsSharesApi.md#list_dfs_nfs_shares) | **GET** /dfs-nfs-shares/ | 
[**remove_dfs_nfs_share_ac_ls**](DfsNfsSharesApi.md#remove_dfs_nfs_share_ac_ls) | **POST** /dfs-nfs-shares/{dfs_nfs_share_id}:remove-acls | 
[**update_dfs_nfs_share_ac_ls**](DfsNfsSharesApi.md#update_dfs_nfs_share_ac_ls) | **POST** /dfs-nfs-shares/{dfs_nfs_share_id}:update-acls | 


# **add_dfs_nfs_share_ac_ls**
> DfsNFSShareResp add_dfs_nfs_share_ac_ls(dfs_nfs_share_id, body)



Add dfs nfs shares acls

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
api_instance = xms_client.DfsNfsSharesApi(xms_client.ApiClient(configuration))
dfs_nfs_share_id = 789 # int | dfs nfs shares id
body = xms_client.DfsNFSShareAddACLsReq() # DfsNFSShareAddACLsReq | share acls info

try:
    api_response = api_instance.add_dfs_nfs_share_ac_ls(dfs_nfs_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsNfsSharesApi->add_dfs_nfs_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_nfs_share_id** | **int**| dfs nfs shares id | 
 **body** | [**DfsNFSShareAddACLsReq**](DfsNFSShareAddACLsReq.md)| share acls info | 

### Return type

[**DfsNFSShareResp**](DfsNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dfs_nfs_share**
> DfsNFSShareResp create_dfs_nfs_share(body, allow_path_create=allow_path_create)



Create dfs nfs shares

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
api_instance = xms_client.DfsNfsSharesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsNFSShareCreateReq() # DfsNFSShareCreateReq | share info
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.create_dfs_nfs_share(body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsNfsSharesApi->create_dfs_nfs_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsNFSShareCreateReq**](DfsNFSShareCreateReq.md)| share info | 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DfsNFSShareResp**](DfsNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_nfs_share**
> DfsNFSShareResp delete_dfs_nfs_share(dfs_nfs_share_id, force=force, with_directory=with_directory)



delete dfs nfs shares

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
api_instance = xms_client.DfsNfsSharesApi(xms_client.ApiClient(configuration))
dfs_nfs_share_id = 789 # int | share id
force = true # bool | force delete or not (optional)
with_directory = true # bool | also delete directory (optional)

try:
    api_response = api_instance.delete_dfs_nfs_share(dfs_nfs_share_id, force=force, with_directory=with_directory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsNfsSharesApi->delete_dfs_nfs_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_nfs_share_id** | **int**| share id | 
 **force** | **bool**| force delete or not | [optional] 
 **with_directory** | **bool**| also delete directory | [optional] 

### Return type

[**DfsNFSShareResp**](DfsNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_nfs_share**
> DfsNFSShareResp get_dfs_nfs_share(dfs_nfs_share_id)



Get dfs nfs shares

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
api_instance = xms_client.DfsNfsSharesApi(xms_client.ApiClient(configuration))
dfs_nfs_share_id = 789 # int | share id

try:
    api_response = api_instance.get_dfs_nfs_share(dfs_nfs_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsNfsSharesApi->get_dfs_nfs_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_nfs_share_id** | **int**| share id | 

### Return type

[**DfsNFSShareResp**](DfsNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_nfs_shares**
> DfsNFSSharesResp list_dfs_nfs_shares(limit=limit, offset=offset, dfs_rootfs_id=dfs_rootfs_id, path=path, dfs_gateway_group_id=dfs_gateway_group_id, q=q, sort=sort, cluster_id=cluster_id)



List dfs nfs sharess

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
api_instance = xms_client.DfsNfsSharesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
dfs_rootfs_id = 789 # int | dfs rootfs id (optional)
path = 'path_example' # str | related dfs path (optional)
dfs_gateway_group_id = 789 # int | dfs gateway group id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_dfs_nfs_shares(limit=limit, offset=offset, dfs_rootfs_id=dfs_rootfs_id, path=path, dfs_gateway_group_id=dfs_gateway_group_id, q=q, sort=sort, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsNfsSharesApi->list_dfs_nfs_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **dfs_rootfs_id** | **int**| dfs rootfs id | [optional] 
 **path** | **str**| related dfs path | [optional] 
 **dfs_gateway_group_id** | **int**| dfs gateway group id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**DfsNFSSharesResp**](DfsNFSSharesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dfs_nfs_share_ac_ls**
> DfsNFSShareResp remove_dfs_nfs_share_ac_ls(dfs_nfs_share_id, body)



remove dfs nfs shares acls

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
api_instance = xms_client.DfsNfsSharesApi(xms_client.ApiClient(configuration))
dfs_nfs_share_id = 789 # int | dfs nfs shares id
body = xms_client.DfsNFSShareRemoveACLsReq() # DfsNFSShareRemoveACLsReq | share acls info

try:
    api_response = api_instance.remove_dfs_nfs_share_ac_ls(dfs_nfs_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsNfsSharesApi->remove_dfs_nfs_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_nfs_share_id** | **int**| dfs nfs shares id | 
 **body** | [**DfsNFSShareRemoveACLsReq**](DfsNFSShareRemoveACLsReq.md)| share acls info | 

### Return type

[**DfsNFSShareResp**](DfsNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_nfs_share_ac_ls**
> DfsNFSShareResp update_dfs_nfs_share_ac_ls(dfs_nfs_share_id, body)



Update dfs nfs share acls

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
api_instance = xms_client.DfsNfsSharesApi(xms_client.ApiClient(configuration))
dfs_nfs_share_id = 789 # int | share id
body = xms_client.DfsNFSShareUpdateACLsReq() # DfsNFSShareUpdateACLsReq | share info

try:
    api_response = api_instance.update_dfs_nfs_share_ac_ls(dfs_nfs_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsNfsSharesApi->update_dfs_nfs_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_nfs_share_id** | **int**| share id | 
 **body** | [**DfsNFSShareUpdateACLsReq**](DfsNFSShareUpdateACLsReq.md)| share info | 

### Return type

[**DfsNFSShareResp**](DfsNFSShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

