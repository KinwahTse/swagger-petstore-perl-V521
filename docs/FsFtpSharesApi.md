# xms_client.FsFtpSharesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fsftp_share_ac_ls**](FsFtpSharesApi.md#add_fsftp_share_ac_ls) | **POST** /fs-ftp-shares/{fs_ftp_share_id}:add-acls | 
[**create_fsftp_share**](FsFtpSharesApi.md#create_fsftp_share) | **POST** /fs-ftp-shares/ | 
[**delete_fsftp_share**](FsFtpSharesApi.md#delete_fsftp_share) | **DELETE** /fs-ftp-shares/{fs_ftp_share_id} | 
[**get_fsftp_share**](FsFtpSharesApi.md#get_fsftp_share) | **GET** /fs-ftp-shares/{fs_ftp_share_id} | 
[**list_fsftp_shares**](FsFtpSharesApi.md#list_fsftp_shares) | **GET** /fs-ftp-shares/ | 
[**remove_fsftp_share_ac_ls**](FsFtpSharesApi.md#remove_fsftp_share_ac_ls) | **POST** /fs-ftp-shares/{fs_ftp_share_id}:remove-acls | 
[**update_fsftp_share_ac_ls**](FsFtpSharesApi.md#update_fsftp_share_ac_ls) | **POST** /fs-ftp-shares/{fs_ftp_share_id}:update-acls | 


# **add_fsftp_share_ac_ls**
> FSFTPShareResp add_fsftp_share_ac_ls(fs_ftp_share_id, body)



Add fs ftp share acls

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
api_instance = xms_client.FsFtpSharesApi(xms_client.ApiClient(configuration))
fs_ftp_share_id = 789 # int | fs ftp share id
body = xms_client.FSFTPShareAddACLsReq() # FSFTPShareAddACLsReq | ftp share acls info

try:
    api_response = api_instance.add_fsftp_share_ac_ls(fs_ftp_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFtpSharesApi->add_fsftp_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_ftp_share_id** | **int**| fs ftp share id | 
 **body** | [**FSFTPShareAddACLsReq**](FSFTPShareAddACLsReq.md)| ftp share acls info | 

### Return type

[**FSFTPShareResp**](FSFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fsftp_share**
> FSFTPShareResp create_fsftp_share(body)



Create fs ftp share

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
api_instance = xms_client.FsFtpSharesApi(xms_client.ApiClient(configuration))
body = xms_client.FSFTPShareCreateReq() # FSFTPShareCreateReq | share info

try:
    api_response = api_instance.create_fsftp_share(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFtpSharesApi->create_fsftp_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSFTPShareCreateReq**](FSFTPShareCreateReq.md)| share info | 

### Return type

[**FSFTPShareResp**](FSFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fsftp_share**
> FSFTPShareResp delete_fsftp_share(fs_ftp_share_id, force=force)



delete fs ftp share

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
api_instance = xms_client.FsFtpSharesApi(xms_client.ApiClient(configuration))
fs_ftp_share_id = 789 # int | share id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_fsftp_share(fs_ftp_share_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFtpSharesApi->delete_fsftp_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_ftp_share_id** | **int**| share id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**FSFTPShareResp**](FSFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fsftp_share**
> FSFTPShareResp get_fsftp_share(fs_ftp_share_id)



Get fs ftp share

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
api_instance = xms_client.FsFtpSharesApi(xms_client.ApiClient(configuration))
fs_ftp_share_id = 789 # int | share id

try:
    api_response = api_instance.get_fsftp_share(fs_ftp_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFtpSharesApi->get_fsftp_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_ftp_share_id** | **int**| share id | 

### Return type

[**FSFTPShareResp**](FSFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fsftp_shares**
> FSFTPSharesResp list_fsftp_shares(limit=limit, offset=offset, cluster_id=cluster_id, fs_folder_id=fs_folder_id, fs_gateway_group_id=fs_gateway_group_id, q=q, sort=sort)



List fs ftp shares

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
api_instance = xms_client.FsFtpSharesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
fs_folder_id = 789 # int | fs smb id (optional)
fs_gateway_group_id = 789 # int | fs gateway group id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_fsftp_shares(limit=limit, offset=offset, cluster_id=cluster_id, fs_folder_id=fs_folder_id, fs_gateway_group_id=fs_gateway_group_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFtpSharesApi->list_fsftp_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **fs_folder_id** | **int**| fs smb id | [optional] 
 **fs_gateway_group_id** | **int**| fs gateway group id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**FSFTPSharesResp**](FSFTPSharesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_fsftp_share_ac_ls**
> FSFTPShareResp remove_fsftp_share_ac_ls(fs_ftp_share_id, body)



remove fs ftp share acls

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
api_instance = xms_client.FsFtpSharesApi(xms_client.ApiClient(configuration))
fs_ftp_share_id = 789 # int | fs ftp share id
body = xms_client.FSFTPShareRemoveACLsReq() # FSFTPShareRemoveACLsReq | share acls info

try:
    api_response = api_instance.remove_fsftp_share_ac_ls(fs_ftp_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFtpSharesApi->remove_fsftp_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_ftp_share_id** | **int**| fs ftp share id | 
 **body** | [**FSFTPShareRemoveACLsReq**](FSFTPShareRemoveACLsReq.md)| share acls info | 

### Return type

[**FSFTPShareResp**](FSFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fsftp_share_ac_ls**
> FSFTPShareResp update_fsftp_share_ac_ls(fs_ftp_share_id, body)



Update fs ftp share acls

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
api_instance = xms_client.FsFtpSharesApi(xms_client.ApiClient(configuration))
fs_ftp_share_id = 789 # int | ftp share id
body = xms_client.FSFTPShareUpdateACLsReq() # FSFTPShareUpdateACLsReq | ftp share acls info

try:
    api_response = api_instance.update_fsftp_share_ac_ls(fs_ftp_share_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFtpSharesApi->update_fsftp_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_ftp_share_id** | **int**| ftp share id | 
 **body** | [**FSFTPShareUpdateACLsReq**](FSFTPShareUpdateACLsReq.md)| ftp share acls info | 

### Return type

[**FSFTPShareResp**](FSFTPShareResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

