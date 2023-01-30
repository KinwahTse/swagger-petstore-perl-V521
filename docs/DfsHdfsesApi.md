# xms_client.DfsHdfsesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dfs_hdfs_ac_ls**](DfsHdfsesApi.md#add_dfs_hdfs_ac_ls) | **POST** /dfs-hdfses/{dfs_hdfs_id}:add-acls | 
[**create_dfs_hdfs**](DfsHdfsesApi.md#create_dfs_hdfs) | **POST** /dfs-hdfses/ | 
[**delete_dfs_hdfs**](DfsHdfsesApi.md#delete_dfs_hdfs) | **DELETE** /dfs-hdfses/{dfs_hdfs_id} | 
[**get_dfs_hdfs**](DfsHdfsesApi.md#get_dfs_hdfs) | **GET** /dfs-hdfses/{dfs_hdfs_id} | 
[**list_dfs_hdfses**](DfsHdfsesApi.md#list_dfs_hdfses) | **GET** /dfs-hdfses/ | 
[**remove_dfs_hdfs_ac_ls**](DfsHdfsesApi.md#remove_dfs_hdfs_ac_ls) | **POST** /dfs-hdfses/{dfs_hdfs_id}:remove-acls | 
[**update_dfs_hdfs**](DfsHdfsesApi.md#update_dfs_hdfs) | **PATCH** /dfs-hdfses/{dfs_hdfs_id} | 
[**update_dfs_hdfs_ac_ls**](DfsHdfsesApi.md#update_dfs_hdfs_ac_ls) | **PATCH** /dfs-hdfses/{dfs_hdfs_id}:update-acls | 


# **add_dfs_hdfs_ac_ls**
> DfsHdfsResp add_dfs_hdfs_ac_ls(dfs_hdfs_id, body)



add dfs hdfs acls

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
api_instance = xms_client.DfsHdfsesApi(xms_client.ApiClient(configuration))
dfs_hdfs_id = 789 # int | hdfs id
body = xms_client.DfsHdfsAddACLsReq() # DfsHdfsAddACLsReq | dfs hdfs info

try:
    api_response = api_instance.add_dfs_hdfs_ac_ls(dfs_hdfs_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsHdfsesApi->add_dfs_hdfs_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_hdfs_id** | **int**| hdfs id | 
 **body** | [**DfsHdfsAddACLsReq**](DfsHdfsAddACLsReq.md)| dfs hdfs info | 

### Return type

[**DfsHdfsResp**](DfsHdfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dfs_hdfs**
> DfsHdfsResp create_dfs_hdfs(body, allow_path_create=allow_path_create)



Create dfs hdfs

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
api_instance = xms_client.DfsHdfsesApi(xms_client.ApiClient(configuration))
body = xms_client.DfsHdfsCreateReq() # DfsHdfsCreateReq | hdfs info
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.create_dfs_hdfs(body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsHdfsesApi->create_dfs_hdfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsHdfsCreateReq**](DfsHdfsCreateReq.md)| hdfs info | 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DfsHdfsResp**](DfsHdfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_hdfs**
> DfsHdfsResp delete_dfs_hdfs(dfs_hdfs_id, force=force)



delete dfs hdfs

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
api_instance = xms_client.DfsHdfsesApi(xms_client.ApiClient(configuration))
dfs_hdfs_id = 789 # int | dfs hdfs id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_dfs_hdfs(dfs_hdfs_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsHdfsesApi->delete_dfs_hdfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_hdfs_id** | **int**| dfs hdfs id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DfsHdfsResp**](DfsHdfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_hdfs**
> DfsHdfsResp get_dfs_hdfs(dfs_hdfs_id)



Get dfs hdfs

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
api_instance = xms_client.DfsHdfsesApi(xms_client.ApiClient(configuration))
dfs_hdfs_id = 789 # int | dfs hdfs id

try:
    api_response = api_instance.get_dfs_hdfs(dfs_hdfs_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsHdfsesApi->get_dfs_hdfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_hdfs_id** | **int**| dfs hdfs id | 

### Return type

[**DfsHdfsResp**](DfsHdfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_hdfses**
> DfsHdfsesResp list_dfs_hdfses(limit=limit, offset=offset, cluster_id=cluster_id, path=path, dfs_gateway_zone_id=dfs_gateway_zone_id, q=q, sort=sort)



List dfs hdfs

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
api_instance = xms_client.DfsHdfsesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
path = 'path_example' # str | related dfs path (optional)
dfs_gateway_zone_id = 789 # int | dfs gateway zone id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dfs_hdfses(limit=limit, offset=offset, cluster_id=cluster_id, path=path, dfs_gateway_zone_id=dfs_gateway_zone_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsHdfsesApi->list_dfs_hdfses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **path** | **str**| related dfs path | [optional] 
 **dfs_gateway_zone_id** | **int**| dfs gateway zone id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DfsHdfsesResp**](DfsHdfsesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dfs_hdfs_ac_ls**
> DfsHdfsResp remove_dfs_hdfs_ac_ls(dfs_hdfs_id, body)



remove dfs hdfs acls

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
api_instance = xms_client.DfsHdfsesApi(xms_client.ApiClient(configuration))
dfs_hdfs_id = 789 # int | dfs hdfs id
body = xms_client.DfsHdfsRemoveACLsReq() # DfsHdfsRemoveACLsReq | hdfs acls info

try:
    api_response = api_instance.remove_dfs_hdfs_ac_ls(dfs_hdfs_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsHdfsesApi->remove_dfs_hdfs_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_hdfs_id** | **int**| dfs hdfs id | 
 **body** | [**DfsHdfsRemoveACLsReq**](DfsHdfsRemoveACLsReq.md)| hdfs acls info | 

### Return type

[**DfsHdfsResp**](DfsHdfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_hdfs**
> DfsHdfsResp update_dfs_hdfs(dfs_hdfs_id, body)



Update dfs hdfs

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
api_instance = xms_client.DfsHdfsesApi(xms_client.ApiClient(configuration))
dfs_hdfs_id = 789 # int | hdfs id
body = xms_client.DfsHdfsUpdateReq() # DfsHdfsUpdateReq | dfs hdfs info

try:
    api_response = api_instance.update_dfs_hdfs(dfs_hdfs_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsHdfsesApi->update_dfs_hdfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_hdfs_id** | **int**| hdfs id | 
 **body** | [**DfsHdfsUpdateReq**](DfsHdfsUpdateReq.md)| dfs hdfs info | 

### Return type

[**DfsHdfsResp**](DfsHdfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_hdfs_ac_ls**
> DfsHdfsResp update_dfs_hdfs_ac_ls(dfs_hdfs_id, body)



Update dfs hdfs ACL

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
api_instance = xms_client.DfsHdfsesApi(xms_client.ApiClient(configuration))
dfs_hdfs_id = 789 # int | hdfs id
body = xms_client.DfsHdfsUpdateACLsReq() # DfsHdfsUpdateACLsReq | hdfs acls info

try:
    api_response = api_instance.update_dfs_hdfs_ac_ls(dfs_hdfs_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsHdfsesApi->update_dfs_hdfs_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_hdfs_id** | **int**| hdfs id | 
 **body** | [**DfsHdfsUpdateACLsReq**](DfsHdfsUpdateACLsReq.md)| hdfs acls info | 

### Return type

[**DfsHdfsResp**](DfsHdfsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

