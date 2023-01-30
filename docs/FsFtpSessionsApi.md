# xms_client.FsFtpSessionsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_fsftp_sessions**](FsFtpSessionsApi.md#list_fsftp_sessions) | **GET** /fs-ftp-sessions/ | 


# **list_fsftp_sessions**
> FSFTPSessionsResp list_fsftp_sessions(limit=limit, offset=offset, cluster_id=cluster_id, fs_ftp_share_id=fs_ftp_share_id, q=q, sort=sort)



List fs ftp sessions

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
api_instance = xms_client.FsFtpSessionsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
fs_ftp_share_id = 789 # int | fs ftp share id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_fsftp_sessions(limit=limit, offset=offset, cluster_id=cluster_id, fs_ftp_share_id=fs_ftp_share_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsFtpSessionsApi->list_fsftp_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **fs_ftp_share_id** | **int**| fs ftp share id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**FSFTPSessionsResp**](FSFTPSessionsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

