# xms_client.FsClientsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fs_client**](FsClientsApi.md#create_fs_client) | **POST** /fs-clients/ | 
[**delete_fs_client**](FsClientsApi.md#delete_fs_client) | **DELETE** /fs-clients/{fs_client_id} | 
[**get_fs_client**](FsClientsApi.md#get_fs_client) | **GET** /fs-clients/{fs_client_id} | 
[**list_fs_clients**](FsClientsApi.md#list_fs_clients) | **GET** /fs-clients/ | 
[**update_fs_client**](FsClientsApi.md#update_fs_client) | **PATCH** /fs-clients/{fs_client_id} | 


# **create_fs_client**
> FSClientResp create_fs_client(body, cluster_id=cluster_id)



Create file storage client

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
api_instance = xms_client.FsClientsApi(xms_client.ApiClient(configuration))
body = xms_client.FSClientCreateReq() # FSClientCreateReq | client info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_fs_client(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsClientsApi->create_fs_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSClientCreateReq**](FSClientCreateReq.md)| client info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**FSClientResp**](FSClientResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fs_client**
> delete_fs_client(fs_client_id)



delete file storage client

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
api_instance = xms_client.FsClientsApi(xms_client.ApiClient(configuration))
fs_client_id = 789 # int | client id

try:
    api_instance.delete_fs_client(fs_client_id)
except ApiException as e:
    print("Exception when calling FsClientsApi->delete_fs_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_client_id** | **int**| client id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fs_client**
> FSClientResp get_fs_client(fs_client_id)



Get file storage client

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
api_instance = xms_client.FsClientsApi(xms_client.ApiClient(configuration))
fs_client_id = 789 # int | client id

try:
    api_response = api_instance.get_fs_client(fs_client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsClientsApi->get_fs_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_client_id** | **int**| client id | 

### Return type

[**FSClientResp**](FSClientResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fs_clients**
> FSClientsResp list_fs_clients(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, fs_client_group_id=fs_client_group_id, not_fs_client_group_id=not_fs_client_group_id, not_dfs_nfs_share_id=not_dfs_nfs_share_id)



List file storage clients

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
api_instance = xms_client.FsClientsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
fs_client_group_id = 789 # int | file storage client group id (optional)
not_fs_client_group_id = 789 # int | group id the client don't belong to (optional)
not_dfs_nfs_share_id = 789 # int | id of dfs nfs share clients not in (optional)

try:
    api_response = api_instance.list_fs_clients(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, fs_client_group_id=fs_client_group_id, not_fs_client_group_id=not_fs_client_group_id, not_dfs_nfs_share_id=not_dfs_nfs_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsClientsApi->list_fs_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **fs_client_group_id** | **int**| file storage client group id | [optional] 
 **not_fs_client_group_id** | **int**| group id the client don&#39;t belong to | [optional] 
 **not_dfs_nfs_share_id** | **int**| id of dfs nfs share clients not in | [optional] 

### Return type

[**FSClientsResp**](FSClientsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fs_client**
> FSClientResp update_fs_client(fs_client_id, body)



Update file storage client

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
api_instance = xms_client.FsClientsApi(xms_client.ApiClient(configuration))
fs_client_id = 789 # int | client id
body = xms_client.FSClientUpdateReq() # FSClientUpdateReq | client info

try:
    api_response = api_instance.update_fs_client(fs_client_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsClientsApi->update_fs_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_client_id** | **int**| client id | 
 **body** | [**FSClientUpdateReq**](FSClientUpdateReq.md)| client info | 

### Return type

[**FSClientResp**](FSClientResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

