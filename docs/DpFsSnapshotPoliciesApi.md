# xms_client.DpFsSnapshotPoliciesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dp_fs_snapshot_policy**](DpFsSnapshotPoliciesApi.md#create_dp_fs_snapshot_policy) | **POST** /dp-fs-snapshot-policies/ | 
[**delete_dp_fs_snapshot_policy**](DpFsSnapshotPoliciesApi.md#delete_dp_fs_snapshot_policy) | **DELETE** /dp-fs-snapshot-policies/{policy_id} | 
[**get_dp_fs_snapshot_policy**](DpFsSnapshotPoliciesApi.md#get_dp_fs_snapshot_policy) | **GET** /dp-fs-snapshot-policies/{policy_id} | 
[**list_dp_fs_snapshot_policies**](DpFsSnapshotPoliciesApi.md#list_dp_fs_snapshot_policies) | **GET** /dp-fs-snapshot-policies/ | 
[**update_dp_fs_snapshot_policy**](DpFsSnapshotPoliciesApi.md#update_dp_fs_snapshot_policy) | **PATCH** /dp-fs-snapshot-policies/{policy_id} | 


# **create_dp_fs_snapshot_policy**
> DpFSSnapshotPolicyResp create_dp_fs_snapshot_policy(body)



Create dp fs snapshot policy

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
api_instance = xms_client.DpFsSnapshotPoliciesApi(xms_client.ApiClient(configuration))
body = xms_client.DpFSSnapshotPolicyCreateReq() # DpFSSnapshotPolicyCreateReq | policy info

try:
    api_response = api_instance.create_dp_fs_snapshot_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpFsSnapshotPoliciesApi->create_dp_fs_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpFSSnapshotPolicyCreateReq**](DpFSSnapshotPolicyCreateReq.md)| policy info | 

### Return type

[**DpFSSnapshotPolicyResp**](DpFSSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_fs_snapshot_policy**
> DpFSSnapshotPolicyResp delete_dp_fs_snapshot_policy(policy_id, force=force)



Delete dp fs snapshot policy

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
api_instance = xms_client.DpFsSnapshotPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_dp_fs_snapshot_policy(policy_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpFsSnapshotPoliciesApi->delete_dp_fs_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DpFSSnapshotPolicyResp**](DpFSSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_fs_snapshot_policy**
> DpFSSnapshotPolicyResp get_dp_fs_snapshot_policy(policy_id)



Get dp fs snapshot policy

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
api_instance = xms_client.DpFsSnapshotPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_fs_snapshot_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpFsSnapshotPoliciesApi->get_dp_fs_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 

### Return type

[**DpFSSnapshotPolicyResp**](DpFSSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_fs_snapshot_policies**
> DpFSSnapshotPoliciesResp list_dp_fs_snapshot_policies(limit=limit, offset=offset, q=q, sort=sort)



List dp fs snapshot policies

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
api_instance = xms_client.DpFsSnapshotPoliciesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dp_fs_snapshot_policies(limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpFsSnapshotPoliciesApi->list_dp_fs_snapshot_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DpFSSnapshotPoliciesResp**](DpFSSnapshotPoliciesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dp_fs_snapshot_policy**
> DpFSSnapshotPolicyResp update_dp_fs_snapshot_policy(policy_id, body)



Update dp fs snapshot policy

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
api_instance = xms_client.DpFsSnapshotPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id
body = xms_client.DpFSSnapshotPolicyUpdateReq() # DpFSSnapshotPolicyUpdateReq | policy info

try:
    api_response = api_instance.update_dp_fs_snapshot_policy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpFsSnapshotPoliciesApi->update_dp_fs_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 
 **body** | [**DpFSSnapshotPolicyUpdateReq**](DpFSSnapshotPolicyUpdateReq.md)| policy info | 

### Return type

[**DpFSSnapshotPolicyResp**](DpFSSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

