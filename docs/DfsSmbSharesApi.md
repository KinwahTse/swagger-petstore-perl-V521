# xms_client.DfsSmbSharesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dfs_smb_share_ac_ls**](DfsSmbSharesApi.md#add_dfs_smb_share_ac_ls) | **POST** /dfs-smb-shares/{dfs_smb_share_id}:add-acls | 
[**create_dfs_smb_share**](DfsSmbSharesApi.md#create_dfs_smb_share) | **POST** /dfs-smb-shares/ | 
[**delete_dfs_smb_share**](DfsSmbSharesApi.md#delete_dfs_smb_share) | **DELETE** /dfs-smb-shares/{dfs_smb_share_id} | 
[**get_dfs_smb_share**](DfsSmbSharesApi.md#get_dfs_smb_share) | **GET** /dfs-smb-shares/{dfs_smb_share_id} | 
[**list_dfs_smb_shares**](DfsSmbSharesApi.md#list_dfs_smb_shares) | **GET** /dfs-smb-shares/ | 
[**remove_dfs_smb_share_ac_ls**](DfsSmbSharesApi.md#remove_dfs_smb_share_ac_ls) | **POST** /dfs-smb-shares/{dfs_smb_share_id}:remove-acls | 
[**update_dfs_smb_share**](DfsSmbSharesApi.md#update_dfs_smb_share) | **PATCH** /dfs-smb-shares/{dfs_smb_share_id} | 
[**update_dfs_smb_share_ac_ls**](DfsSmbSharesApi.md#update_dfs_smb_share_ac_ls) | **POST** /dfs-smb-shares/{dfs_smb_share_id}:update-acls | 


# **add_dfs_smb_share_ac_ls**
> DfsSMBShareResp add_dfs_smb_share_ac_ls(dfs_smb_share_id, body)



Add dfs smb share acls

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
api_instance = xms_client.DfsSmbSharesApi(xms_client.ApiClient(configuration))
dfs_smb_share_id = 789 # int | dfs smb share id
body = xms_client.DfsSMBShareAddACLsReq() # DfsSMBShareAddACLsReq | share acls info

try:
    api_response = api_instance.add_dfs_smb_share_ac_ls(dfs_smb_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSmbSharesApi->add_dfs_smb_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_smb_share_id** | **int**| dfs smb share id | 
 **body** | [**DfsSMBShareAddACLsReq**](DfsSMBShareAddACLsReq.md)| share acls info | 

### Return type

[**DfsSMBShareResp**](DfsSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dfs_smb_share**
> DfsSMBShareResp create_dfs_smb_share(body, allow_path_create=allow_path_create)



Create dfs smb share

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
api_instance = xms_client.DfsSmbSharesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsSMBShareCreateReq() # DfsSMBShareCreateReq | share info
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.create_dfs_smb_share(body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSmbSharesApi->create_dfs_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsSMBShareCreateReq**](DfsSMBShareCreateReq.md)| share info | 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DfsSMBShareResp**](DfsSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_smb_share**
> DfsSMBShareResp delete_dfs_smb_share(dfs_smb_share_id, force=force, with_directory=with_directory)



delete dfs smb share

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
api_instance = xms_client.DfsSmbSharesApi(xms_client.ApiClient(configuration))
dfs_smb_share_id = 789 # int | share id
force = true # bool | force delete or not (optional)
with_directory = true # bool | also delete directory (optional)

try:
    api_response = api_instance.delete_dfs_smb_share(dfs_smb_share_id, force=force, with_directory=with_directory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSmbSharesApi->delete_dfs_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_smb_share_id** | **int**| share id | 
 **force** | **bool**| force delete or not | [optional] 
 **with_directory** | **bool**| also delete directory | [optional] 

### Return type

[**DfsSMBShareResp**](DfsSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_smb_share**
> DfsSMBShareResp get_dfs_smb_share(dfs_smb_share_id)



Get dfs smb share

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
api_instance = xms_client.DfsSmbSharesApi(xms_client.ApiClient(configuration))
dfs_smb_share_id = 789 # int | share id

try:
    api_response = api_instance.get_dfs_smb_share(dfs_smb_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSmbSharesApi->get_dfs_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_smb_share_id** | **int**| share id | 

### Return type

[**DfsSMBShareResp**](DfsSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_smb_shares**
> DfsSMBSharesResp list_dfs_smb_shares(limit=limit, offset=offset, cluster_id=cluster_id, dfs_rootfs_id=dfs_rootfs_id, dfs_gateway_group_id=dfs_gateway_group_id, q=q, path=path, sort=sort)



List dfs smb shares

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
api_instance = xms_client.DfsSmbSharesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
dfs_rootfs_id = 789 # int | dfs rootfs id (optional)
dfs_gateway_group_id = 789 # int | dfs gateway group id (optional)
q = 'q_example' # str | query param of search (optional)
path = 'path_example' # str | related dfs path (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dfs_smb_shares(limit=limit, offset=offset, cluster_id=cluster_id, dfs_rootfs_id=dfs_rootfs_id, dfs_gateway_group_id=dfs_gateway_group_id, q=q, path=path, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSmbSharesApi->list_dfs_smb_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **dfs_rootfs_id** | **int**| dfs rootfs id | [optional] 
 **dfs_gateway_group_id** | **int**| dfs gateway group id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **path** | **str**| related dfs path | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DfsSMBSharesResp**](DfsSMBSharesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dfs_smb_share_ac_ls**
> DfsSMBShareResp remove_dfs_smb_share_ac_ls(dfs_smb_share_id, body)



remove dfs smb share acls

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
api_instance = xms_client.DfsSmbSharesApi(xms_client.ApiClient(configuration))
dfs_smb_share_id = 789 # int | dfs smb share id
body = xms_client.DfsSMBShareRemoveACLsReq() # DfsSMBShareRemoveACLsReq | share acls info

try:
    api_response = api_instance.remove_dfs_smb_share_ac_ls(dfs_smb_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSmbSharesApi->remove_dfs_smb_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_smb_share_id** | **int**| dfs smb share id | 
 **body** | [**DfsSMBShareRemoveACLsReq**](DfsSMBShareRemoveACLsReq.md)| share acls info | 

### Return type

[**DfsSMBShareResp**](DfsSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_smb_share**
> DfsSMBShareResp update_dfs_smb_share(dfs_smb_share_id, body)



Update dfs smb share

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
api_instance = xms_client.DfsSmbSharesApi(xms_client.ApiClient(configuration))
dfs_smb_share_id = 789 # int | share id
body = xms_client.DfsSMBShareUpdateReq() # DfsSMBShareUpdateReq | share info

try:
    api_response = api_instance.update_dfs_smb_share(dfs_smb_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSmbSharesApi->update_dfs_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_smb_share_id** | **int**| share id | 
 **body** | [**DfsSMBShareUpdateReq**](DfsSMBShareUpdateReq.md)| share info | 

### Return type

[**DfsSMBShareResp**](DfsSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_smb_share_ac_ls**
> DfsSMBShareResp update_dfs_smb_share_ac_ls(dfs_smb_share_id, body)



Update dfs smb share ACL

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
api_instance = xms_client.DfsSmbSharesApi(xms_client.ApiClient(configuration))
dfs_smb_share_id = 789 # int | share id
body = xms_client.DfsSMBShareUpdateACLsReq() # DfsSMBShareUpdateACLsReq | share acls info

try:
    api_response = api_instance.update_dfs_smb_share_ac_ls(dfs_smb_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsSmbSharesApi->update_dfs_smb_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_smb_share_id** | **int**| share id | 
 **body** | [**DfsSMBShareUpdateACLsReq**](DfsSMBShareUpdateACLsReq.md)| share acls info | 

### Return type

[**DfsSMBShareResp**](DfsSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

