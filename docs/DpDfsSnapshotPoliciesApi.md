# xms_client.DpDfsSnapshotPoliciesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dp_dfs_snapshot_policy**](DpDfsSnapshotPoliciesApi.md#create_dp_dfs_snapshot_policy) | **POST** /dp-dfs-snapshot-policies/ | 
[**delete_dp_dfs_snapshot_policy**](DpDfsSnapshotPoliciesApi.md#delete_dp_dfs_snapshot_policy) | **DELETE** /dp-dfs-snapshot-policies/{policy_id} | 
[**get_dp_dfs_snapshot_policy**](DpDfsSnapshotPoliciesApi.md#get_dp_dfs_snapshot_policy) | **GET** /dp-dfs-snapshot-policies/{policy_id} | 
[**list_dp_dfs_snapshot_policies**](DpDfsSnapshotPoliciesApi.md#list_dp_dfs_snapshot_policies) | **GET** /dp-dfs-snapshot-policies/ | 
[**update_dp_dfs_snapshot_policy**](DpDfsSnapshotPoliciesApi.md#update_dp_dfs_snapshot_policy) | **PATCH** /dp-dfs-snapshot-policies/{policy_id} | 


# **create_dp_dfs_snapshot_policy**
> DpDfsSnapshotPolicyResp create_dp_dfs_snapshot_policy(body)



Create dp dfs snapshot policy

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
api_instance = xms_client.DpDfsSnapshotPoliciesApi(xms_client.ApiClient(configuration))
body = xms_client.DpDfsSnapshotPolicyCreateReq() # DpDfsSnapshotPolicyCreateReq | dp dfs snapshot policy info

try:
    api_response = api_instance.create_dp_dfs_snapshot_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotPoliciesApi->create_dp_dfs_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpDfsSnapshotPolicyCreateReq**](DpDfsSnapshotPolicyCreateReq.md)| dp dfs snapshot policy info | 

### Return type

[**DpDfsSnapshotPolicyResp**](DpDfsSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_dfs_snapshot_policy**
> DpDfsSnapshotPolicyResp delete_dp_dfs_snapshot_policy(policy_id, force=force)



Delete a dp dfs snapshot policy

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
api_instance = xms_client.DpDfsSnapshotPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | dp dfs snapshot policy id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_dp_dfs_snapshot_policy(policy_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotPoliciesApi->delete_dp_dfs_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| dp dfs snapshot policy id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DpDfsSnapshotPolicyResp**](DpDfsSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_dfs_snapshot_policy**
> DpDfsSnapshotPolicyResp get_dp_dfs_snapshot_policy(policy_id)



get dp dfs snapshot policy

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
api_instance = xms_client.DpDfsSnapshotPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | the dp dfs snapshot policy id

try:
    api_response = api_instance.get_dp_dfs_snapshot_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotPoliciesApi->get_dp_dfs_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| the dp dfs snapshot policy id | 

### Return type

[**DpDfsSnapshotPolicyResp**](DpDfsSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_dfs_snapshot_policies**
> DpDfsSnapshotPoliciesResp list_dp_dfs_snapshot_policies(limit=limit, offset=offset, q=q, sort=sort, dfs_path_name=dfs_path_name)



List dp dfs snapshot policies

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
api_instance = xms_client.DpDfsSnapshotPoliciesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
dfs_path_name = 'dfs_path_name_example' # str | show dp dfs snapshot policies of specific dfs path (optional)

try:
    api_response = api_instance.list_dp_dfs_snapshot_policies(limit=limit, offset=offset, q=q, sort=sort, dfs_path_name=dfs_path_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotPoliciesApi->list_dp_dfs_snapshot_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **dfs_path_name** | **str**| show dp dfs snapshot policies of specific dfs path | [optional] 

### Return type

[**DpDfsSnapshotPoliciesResp**](DpDfsSnapshotPoliciesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dp_dfs_snapshot_policy**
> DpDfsSnapshotPolicyResp update_dp_dfs_snapshot_policy(policy_id, body)



Update dp dfs snapshot policy

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
api_instance = xms_client.DpDfsSnapshotPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | dp dfs snapshot policy id
body = xms_client.DpDfsSnapshotPolicyUpdateReq() # DpDfsSnapshotPolicyUpdateReq | dp dfs snapshot policy update info

try:
    api_response = api_instance.update_dp_dfs_snapshot_policy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpDfsSnapshotPoliciesApi->update_dp_dfs_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| dp dfs snapshot policy id | 
 **body** | [**DpDfsSnapshotPolicyUpdateReq**](DpDfsSnapshotPolicyUpdateReq.md)| dp dfs snapshot policy update info | 

### Return type

[**DpDfsSnapshotPolicyResp**](DpDfsSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

