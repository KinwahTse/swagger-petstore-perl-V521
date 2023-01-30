# xms_client.DpBlockSnapshotPoliciesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dp_block_snapshot_policy**](DpBlockSnapshotPoliciesApi.md#create_dp_block_snapshot_policy) | **POST** /dp-block-snapshot-policies/ | 
[**delete_dp_block_snapshot_policy**](DpBlockSnapshotPoliciesApi.md#delete_dp_block_snapshot_policy) | **DELETE** /dp-block-snapshot-policies/{policy_id} | 
[**get_dp_block_snapshot_policy**](DpBlockSnapshotPoliciesApi.md#get_dp_block_snapshot_policy) | **GET** /dp-block-snapshot-policies/{policy_id} | 
[**list_dp_block_snapshot_policies**](DpBlockSnapshotPoliciesApi.md#list_dp_block_snapshot_policies) | **GET** /dp-block-snapshot-policies/ | 
[**update_dp_block_snapshot_policy**](DpBlockSnapshotPoliciesApi.md#update_dp_block_snapshot_policy) | **PATCH** /dp-block-snapshot-policies/{policy_id} | 


# **create_dp_block_snapshot_policy**
> DpBlockSnapshotPolicyResp create_dp_block_snapshot_policy(body)



Create dp block snapshot policy

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
api_instance = xms_client.DpBlockSnapshotPoliciesApi(xms_client.ApiClient(configuration))
body = xms_client.DpBlockSnapshotPolicyCreateReq() # DpBlockSnapshotPolicyCreateReq | policy info

try:
    api_response = api_instance.create_dp_block_snapshot_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockSnapshotPoliciesApi->create_dp_block_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpBlockSnapshotPolicyCreateReq**](DpBlockSnapshotPolicyCreateReq.md)| policy info | 

### Return type

[**DpBlockSnapshotPolicyResp**](DpBlockSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_block_snapshot_policy**
> DpBlockSnapshotPolicyResp delete_dp_block_snapshot_policy(policy_id, force=force)



Delete dp block snapshot policy

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
api_instance = xms_client.DpBlockSnapshotPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_dp_block_snapshot_policy(policy_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockSnapshotPoliciesApi->delete_dp_block_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DpBlockSnapshotPolicyResp**](DpBlockSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_block_snapshot_policy**
> DpBlockSnapshotPolicyResp get_dp_block_snapshot_policy(policy_id)



Get dp block snapshot policy

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
api_instance = xms_client.DpBlockSnapshotPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_block_snapshot_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockSnapshotPoliciesApi->get_dp_block_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 

### Return type

[**DpBlockSnapshotPolicyResp**](DpBlockSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_block_snapshot_policies**
> DpBlockSnapshotPoliciesResp list_dp_block_snapshot_policies(limit=limit, offset=offset, q=q, sort=sort)



List dp block snapshot policies

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
api_instance = xms_client.DpBlockSnapshotPoliciesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dp_block_snapshot_policies(limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockSnapshotPoliciesApi->list_dp_block_snapshot_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DpBlockSnapshotPoliciesResp**](DpBlockSnapshotPoliciesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dp_block_snapshot_policy**
> DpBlockSnapshotPolicyResp update_dp_block_snapshot_policy(policy_id, body)



Update dp block snapshot policy

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
api_instance = xms_client.DpBlockSnapshotPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id
body = xms_client.DpBlockSnapshotPolicyUpdateReq() # DpBlockSnapshotPolicyUpdateReq | policy info

try:
    api_response = api_instance.update_dp_block_snapshot_policy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockSnapshotPoliciesApi->update_dp_block_snapshot_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 
 **body** | [**DpBlockSnapshotPolicyUpdateReq**](DpBlockSnapshotPolicyUpdateReq.md)| policy info | 

### Return type

[**DpBlockSnapshotPolicyResp**](DpBlockSnapshotPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

