# xms_client.FsNfsShareAclsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_fsnfs_share_ac_ls**](FsNfsShareAclsApi.md#list_fsnfs_share_ac_ls) | **GET** /fs-nfs-share-acls/ | 


# **list_fsnfs_share_ac_ls**
> FSNFSShareACLsResp list_fsnfs_share_ac_ls(limit=limit, offset=offset, fs_nfs_share_id=fs_nfs_share_id, cluster_id=cluster_id, q=q, sort=sort)



List fs nfs shares acls

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
api_instance = xms_client.FsNfsShareAclsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
fs_nfs_share_id = 789 # int | fs nfs shares id (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_fsnfs_share_ac_ls(limit=limit, offset=offset, fs_nfs_share_id=fs_nfs_share_id, cluster_id=cluster_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsNfsShareAclsApi->list_fsnfs_share_ac_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **fs_nfs_share_id** | **int**| fs nfs shares id | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**FSNFSShareACLsResp**](FSNFSShareACLsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

