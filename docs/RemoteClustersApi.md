# xms_client.RemoteClustersApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_remote_cluster**](RemoteClustersApi.md#create_remote_cluster) | **POST** /remote-clusters/ | 
[**delete_remote_cluster**](RemoteClustersApi.md#delete_remote_cluster) | **DELETE** /remote-clusters/{cluster_id} | 
[**get_remote_cluster**](RemoteClustersApi.md#get_remote_cluster) | **GET** /remote-clusters/{cluster_id} | 
[**list_remote_clusters**](RemoteClustersApi.md#list_remote_clusters) | **GET** /remote-clusters/ | 
[**update_remote_cluster**](RemoteClustersApi.md#update_remote_cluster) | **PATCH** /remote-clusters/{cluster_id} | 


# **create_remote_cluster**
> RemoteClusterResp create_remote_cluster(body)



Create a remote cluster

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
api_instance = xms_client.RemoteClustersApi(xms_client.ApiClient(configuration))
body = xms_client.RemoteClusterCreateReq() # RemoteClusterCreateReq | remote cluster info

try:
    api_response = api_instance.create_remote_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteClustersApi->create_remote_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteClusterCreateReq**](RemoteClusterCreateReq.md)| remote cluster info | 

### Return type

[**RemoteClusterResp**](RemoteClusterResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_remote_cluster**
> RemoteClusterResp delete_remote_cluster(cluster_id)



Delete a remote cluster

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
api_instance = xms_client.RemoteClustersApi(xms_client.ApiClient(configuration))
cluster_id = 789 # int | remote cluster id

try:
    api_response = api_instance.delete_remote_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteClustersApi->delete_remote_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| remote cluster id | 

### Return type

[**RemoteClusterResp**](RemoteClusterResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_cluster**
> RemoteClusterResp get_remote_cluster(cluster_id)



Get remote cluster

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
api_instance = xms_client.RemoteClustersApi(xms_client.ApiClient(configuration))
cluster_id = 789 # int | remote cluster id

try:
    api_response = api_instance.get_remote_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteClustersApi->get_remote_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| remote cluster id | 

### Return type

[**RemoteClusterResp**](RemoteClusterResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_remote_clusters**
> RemoteClustersResp list_remote_clusters(limit=limit, offset=offset, q=q, sort=sort, fs_id=fs_id)



List remote clusters

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
api_instance = xms_client.RemoteClustersApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
fs_id = 'fs_id_example' # str | fsid of cluster (optional)

try:
    api_response = api_instance.list_remote_clusters(limit=limit, offset=offset, q=q, sort=sort, fs_id=fs_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteClustersApi->list_remote_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **fs_id** | **str**| fsid of cluster | [optional] 

### Return type

[**RemoteClustersResp**](RemoteClustersResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_remote_cluster**
> RemoteClusterResp update_remote_cluster(cluster_id, body)



Update a remote cluster

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
api_instance = xms_client.RemoteClustersApi(xms_client.ApiClient(configuration))
cluster_id = 789 # int | remote cluster id
body = xms_client.RemoteClusterUpdateReq() # RemoteClusterUpdateReq | remote cluster info

try:
    api_response = api_instance.update_remote_cluster(cluster_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteClustersApi->update_remote_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**| remote cluster id | 
 **body** | [**RemoteClusterUpdateReq**](RemoteClusterUpdateReq.md)| remote cluster info | 

### Return type

[**RemoteClusterResp**](RemoteClusterResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

