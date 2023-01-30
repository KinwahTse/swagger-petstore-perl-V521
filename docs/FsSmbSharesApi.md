# xms_client.FsSmbSharesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fssmb_share_ac_ls**](FsSmbSharesApi.md#add_fssmb_share_ac_ls) | **POST** /fs-smb-shares/{fs_smb_share_id}:add-acls | 
[**create_fssmb_share**](FsSmbSharesApi.md#create_fssmb_share) | **POST** /fs-smb-shares/ | 
[**delete_fssmb_share**](FsSmbSharesApi.md#delete_fssmb_share) | **DELETE** /fs-smb-shares/{fs_smb_share_id} | 
[**get_fssmb_share**](FsSmbSharesApi.md#get_fssmb_share) | **GET** /fs-smb-shares/{fs_smb_share_id} | 
[**list_fssmb_shares**](FsSmbSharesApi.md#list_fssmb_shares) | **GET** /fs-smb-shares/ | 
[**remove_fssmb_share_ac_ls**](FsSmbSharesApi.md#remove_fssmb_share_ac_ls) | **POST** /fs-smb-shares/{fs_smb_share_id}:remove-acls | 
[**update_fssmb_share**](FsSmbSharesApi.md#update_fssmb_share) | **PATCH** /fs-smb-shares/{fs_smb_share_id} | 
[**update_fssmb_share_ac_ls**](FsSmbSharesApi.md#update_fssmb_share_ac_ls) | **POST** /fs-smb-shares/{fs_smb_share_id}:update-acls | 


# **add_fssmb_share_ac_ls**
> FSSMBShareResp add_fssmb_share_ac_ls(fs_smb_share_id, body)



Add fs smb share acls

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
api_instance = xms_client.FsSmbSharesApi(xms_client.ApiClient(configuration))
fs_smb_share_id = 789 # int | fs smb share id
body = xms_client.FSSMBShareAddACLsReq() # FSSMBShareAddACLsReq | share acls info

try:
    api_response = api_instance.add_fssmb_share_ac_ls(fs_smb_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSmbSharesApi->add_fssmb_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_smb_share_id** | **int**| fs smb share id | 
 **body** | [**FSSMBShareAddACLsReq**](FSSMBShareAddACLsReq.md)| share acls info | 

### Return type

[**FSSMBShareResp**](FSSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fssmb_share**
> FSSMBShareResp create_fssmb_share(body)



Create fs smb share

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
api_instance = xms_client.FsSmbSharesApi(xms_client.ApiClient(configuration))
body = xms_client.FSSMBShareCreateReq() # FSSMBShareCreateReq | share info

try:
    api_response = api_instance.create_fssmb_share(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSmbSharesApi->create_fssmb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSSMBShareCreateReq**](FSSMBShareCreateReq.md)| share info | 

### Return type

[**FSSMBShareResp**](FSSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fssmb_share**
> FSSMBShareResp delete_fssmb_share(fs_smb_share_id, force=force)



delete fs smb share

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
api_instance = xms_client.FsSmbSharesApi(xms_client.ApiClient(configuration))
fs_smb_share_id = 789 # int | share id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_fssmb_share(fs_smb_share_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSmbSharesApi->delete_fssmb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_smb_share_id** | **int**| share id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**FSSMBShareResp**](FSSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fssmb_share**
> FSSMBShareResp get_fssmb_share(fs_smb_share_id)



Get fs smb share

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
api_instance = xms_client.FsSmbSharesApi(xms_client.ApiClient(configuration))
fs_smb_share_id = 789 # int | share id

try:
    api_response = api_instance.get_fssmb_share(fs_smb_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSmbSharesApi->get_fssmb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_smb_share_id** | **int**| share id | 

### Return type

[**FSSMBShareResp**](FSSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fssmb_shares**
> FSSMBSharesResp list_fssmb_shares(limit=limit, offset=offset, cluster_id=cluster_id, fs_folder_id=fs_folder_id, fs_gateway_group_id=fs_gateway_group_id, q=q, sort=sort)



List fs smb shares

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
api_instance = xms_client.FsSmbSharesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
fs_folder_id = 789 # int | fs folder id (optional)
fs_gateway_group_id = 789 # int | fs gateway group id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_fssmb_shares(limit=limit, offset=offset, cluster_id=cluster_id, fs_folder_id=fs_folder_id, fs_gateway_group_id=fs_gateway_group_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSmbSharesApi->list_fssmb_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **fs_folder_id** | **int**| fs folder id | [optional] 
 **fs_gateway_group_id** | **int**| fs gateway group id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**FSSMBSharesResp**](FSSMBSharesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_fssmb_share_ac_ls**
> FSSMBShareResp remove_fssmb_share_ac_ls(fs_smb_share_id, body)



remove fs smb share acls

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
api_instance = xms_client.FsSmbSharesApi(xms_client.ApiClient(configuration))
fs_smb_share_id = 789 # int | fs smb share id
body = xms_client.FSSMBShareRemoveACLsReq() # FSSMBShareRemoveACLsReq | share acls info

try:
    api_response = api_instance.remove_fssmb_share_ac_ls(fs_smb_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSmbSharesApi->remove_fssmb_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_smb_share_id** | **int**| fs smb share id | 
 **body** | [**FSSMBShareRemoveACLsReq**](FSSMBShareRemoveACLsReq.md)| share acls info | 

### Return type

[**FSSMBShareResp**](FSSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fssmb_share**
> FSSMBShareResp update_fssmb_share(fs_smb_share_id, body)



Update fs smb share

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
api_instance = xms_client.FsSmbSharesApi(xms_client.ApiClient(configuration))
fs_smb_share_id = 789 # int | share id
body = xms_client.FSSMBShareUpdateReq() # FSSMBShareUpdateReq | share info

try:
    api_response = api_instance.update_fssmb_share(fs_smb_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSmbSharesApi->update_fssmb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_smb_share_id** | **int**| share id | 
 **body** | [**FSSMBShareUpdateReq**](FSSMBShareUpdateReq.md)| share info | 

### Return type

[**FSSMBShareResp**](FSSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fssmb_share_ac_ls**
> FSSMBShareResp update_fssmb_share_ac_ls(fs_smb_share_id, body)



Update fs smb share ACL

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
api_instance = xms_client.FsSmbSharesApi(xms_client.ApiClient(configuration))
fs_smb_share_id = 789 # int | share id
body = xms_client.FSSMBShareUpdateACLsReq() # FSSMBShareUpdateACLsReq | share acls info

try:
    api_response = api_instance.update_fssmb_share_ac_ls(fs_smb_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsSmbSharesApi->update_fssmb_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_smb_share_id** | **int**| share id | 
 **body** | [**FSSMBShareUpdateACLsReq**](FSSMBShareUpdateACLsReq.md)| share acls info | 

### Return type

[**FSSMBShareResp**](FSSMBShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

