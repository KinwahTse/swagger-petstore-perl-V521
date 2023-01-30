# xms_client.DfsFtpSharesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dfs_ftp_share_ac_ls**](DfsFtpSharesApi.md#add_dfs_ftp_share_ac_ls) | **POST** /dfs-ftp-shares/{dfs_ftp_share_id}:add-acls | 
[**create_dfs_ftp_share**](DfsFtpSharesApi.md#create_dfs_ftp_share) | **POST** /dfs-ftp-shares/ | 
[**delete_dfs_ftp_share**](DfsFtpSharesApi.md#delete_dfs_ftp_share) | **DELETE** /dfs-ftp-shares/{dfs_ftp_share_id} | 
[**get_dfs_ftp_share**](DfsFtpSharesApi.md#get_dfs_ftp_share) | **GET** /dfs-ftp-shares/{dfs_ftp_share_id} | 
[**list_dfs_ftp_shares**](DfsFtpSharesApi.md#list_dfs_ftp_shares) | **GET** /dfs-ftp-shares/ | 
[**remove_dfs_ftp_share_ac_ls**](DfsFtpSharesApi.md#remove_dfs_ftp_share_ac_ls) | **POST** /dfs-ftp-shares/{dfs_ftp_share_id}:remove-acls | 
[**update_dfs_ftp_share_ac_ls**](DfsFtpSharesApi.md#update_dfs_ftp_share_ac_ls) | **POST** /dfs-ftp-shares/{dfs_ftp_share_id}:update-acls | 


# **add_dfs_ftp_share_ac_ls**
> DfsFTPShareResp add_dfs_ftp_share_ac_ls(dfs_ftp_share_id, body)



Add dfs ftp share acls

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
api_instance = xms_client.DfsFtpSharesApi(xms_client.ApiClient(configuration))
dfs_ftp_share_id = 789 # int | dfs ftp share id
body = xms_client.DfsFTPShareAddACLsReq() # DfsFTPShareAddACLsReq | ftp share acls info

try:
    api_response = api_instance.add_dfs_ftp_share_ac_ls(dfs_ftp_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFtpSharesApi->add_dfs_ftp_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_ftp_share_id** | **int**| dfs ftp share id | 
 **body** | [**DfsFTPShareAddACLsReq**](DfsFTPShareAddACLsReq.md)| ftp share acls info | 

### Return type

[**DfsFTPShareResp**](DfsFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dfs_ftp_share**
> DfsFTPShareResp create_dfs_ftp_share(body, allow_path_create=allow_path_create)



Create dfs ftp share

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
api_instance = xms_client.DfsFtpSharesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsFTPShareCreateReq() # DfsFTPShareCreateReq | share info
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.create_dfs_ftp_share(body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFtpSharesApi->create_dfs_ftp_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsFTPShareCreateReq**](DfsFTPShareCreateReq.md)| share info | 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DfsFTPShareResp**](DfsFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_ftp_share**
> DfsFTPShareResp delete_dfs_ftp_share(dfs_ftp_share_id, force=force, with_directory=with_directory)



delete dfs ftp share

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
api_instance = xms_client.DfsFtpSharesApi(xms_client.ApiClient(configuration))
dfs_ftp_share_id = 789 # int | share id
force = true # bool | force delete or not (optional)
with_directory = true # bool | also delete directory (optional)

try:
    api_response = api_instance.delete_dfs_ftp_share(dfs_ftp_share_id, force=force, with_directory=with_directory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFtpSharesApi->delete_dfs_ftp_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_ftp_share_id** | **int**| share id | 
 **force** | **bool**| force delete or not | [optional] 
 **with_directory** | **bool**| also delete directory | [optional] 

### Return type

[**DfsFTPShareResp**](DfsFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_ftp_share**
> DfsFTPShareResp get_dfs_ftp_share(dfs_ftp_share_id)



Get dfs ftp share

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
api_instance = xms_client.DfsFtpSharesApi(xms_client.ApiClient(configuration))
dfs_ftp_share_id = 789 # int | share id

try:
    api_response = api_instance.get_dfs_ftp_share(dfs_ftp_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFtpSharesApi->get_dfs_ftp_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_ftp_share_id** | **int**| share id | 

### Return type

[**DfsFTPShareResp**](DfsFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_ftp_shares**
> DfsFTPSharesResp list_dfs_ftp_shares(limit=limit, offset=offset, cluster_id=cluster_id, dfs_rootfs_id=dfs_rootfs_id, path=path, dfs_gateway_group_id=dfs_gateway_group_id, q=q, sort=sort)



List dfs ftp shares

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
api_instance = xms_client.DfsFtpSharesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
dfs_rootfs_id = 789 # int | dfs rootfs id (optional)
path = 'path_example' # str | related dfs path (optional)
dfs_gateway_group_id = 789 # int | dfs gateway group id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dfs_ftp_shares(limit=limit, offset=offset, cluster_id=cluster_id, dfs_rootfs_id=dfs_rootfs_id, path=path, dfs_gateway_group_id=dfs_gateway_group_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFtpSharesApi->list_dfs_ftp_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **dfs_rootfs_id** | **int**| dfs rootfs id | [optional] 
 **path** | **str**| related dfs path | [optional] 
 **dfs_gateway_group_id** | **int**| dfs gateway group id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DfsFTPSharesResp**](DfsFTPSharesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dfs_ftp_share_ac_ls**
> DfsFTPShareResp remove_dfs_ftp_share_ac_ls(dfs_ftp_share_id, body)



remove dfs ftp share acls

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
api_instance = xms_client.DfsFtpSharesApi(xms_client.ApiClient(configuration))
dfs_ftp_share_id = 789 # int | dfs ftp share id
body = xms_client.DfsFTPShareRemoveACLsReq() # DfsFTPShareRemoveACLsReq | share acls info

try:
    api_response = api_instance.remove_dfs_ftp_share_ac_ls(dfs_ftp_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFtpSharesApi->remove_dfs_ftp_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_ftp_share_id** | **int**| dfs ftp share id | 
 **body** | [**DfsFTPShareRemoveACLsReq**](DfsFTPShareRemoveACLsReq.md)| share acls info | 

### Return type

[**DfsFTPShareResp**](DfsFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_ftp_share_ac_ls**
> DfsFTPShareResp update_dfs_ftp_share_ac_ls(dfs_ftp_share_id, body)



Update dfs ftp share acls

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
api_instance = xms_client.DfsFtpSharesApi(xms_client.ApiClient(configuration))
dfs_ftp_share_id = 789 # int | ftp share id
body = xms_client.DfsFTPShareUpdateACLsReq() # DfsFTPShareUpdateACLsReq | ftp share acls info

try:
    api_response = api_instance.update_dfs_ftp_share_ac_ls(dfs_ftp_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsFtpSharesApi->update_dfs_ftp_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_ftp_share_id** | **int**| ftp share id | 
 **body** | [**DfsFTPShareUpdateACLsReq**](DfsFTPShareUpdateACLsReq.md)| ftp share acls info | 

### Return type

[**DfsFTPShareResp**](DfsFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

