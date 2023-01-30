# xms_client.DpBlockAsyncReplicationPoliciesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dp_block_async_replication_policy**](DpBlockAsyncReplicationPoliciesApi.md#create_dp_block_async_replication_policy) | **POST** /dp-block-async-replication-policies/ | 
[**delete_dp_block_async_replication_policy**](DpBlockAsyncReplicationPoliciesApi.md#delete_dp_block_async_replication_policy) | **DELETE** /dp-block-async-replication-policies/{policy_id} | 
[**get_dp_block_async_replication_policy**](DpBlockAsyncReplicationPoliciesApi.md#get_dp_block_async_replication_policy) | **GET** /dp-block-async-replication-policies/{policy_id} | 
[**list_dp_block_async_replication_policies**](DpBlockAsyncReplicationPoliciesApi.md#list_dp_block_async_replication_policies) | **GET** /dp-block-async-replication-policies/ | 
[**update_dp_block_async_replication_policy**](DpBlockAsyncReplicationPoliciesApi.md#update_dp_block_async_replication_policy) | **PATCH** /dp-block-async-replication-policies/{policy_id} | 


# **create_dp_block_async_replication_policy**
> DpBlockAsyncReplicationPolicyResp create_dp_block_async_replication_policy(body)



Create dp block async replication policy

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
api_instance = xms_client.DpBlockAsyncReplicationPoliciesApi(xms_client.ApiClient(configuration))
body = xms_client.DpBlockAsyncReplicationPolicyCreateReq() # DpBlockAsyncReplicationPolicyCreateReq | policy info

try:
    api_response = api_instance.create_dp_block_async_replication_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPoliciesApi->create_dp_block_async_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpBlockAsyncReplicationPolicyCreateReq**](DpBlockAsyncReplicationPolicyCreateReq.md)| policy info | 

### Return type

[**DpBlockAsyncReplicationPolicyResp**](DpBlockAsyncReplicationPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_block_async_replication_policy**
> DpBlockAsyncReplicationPolicyResp delete_dp_block_async_replication_policy(policy_id, force=force)



Delete dp block async replication policy

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
api_instance = xms_client.DpBlockAsyncReplicationPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_dp_block_async_replication_policy(policy_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPoliciesApi->delete_dp_block_async_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DpBlockAsyncReplicationPolicyResp**](DpBlockAsyncReplicationPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_block_async_replication_policy**
> DpBlockAsyncReplicationPolicyResp get_dp_block_async_replication_policy(policy_id)



Get dp block async replication policy

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
api_instance = xms_client.DpBlockAsyncReplicationPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_block_async_replication_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPoliciesApi->get_dp_block_async_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 

### Return type

[**DpBlockAsyncReplicationPolicyResp**](DpBlockAsyncReplicationPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_block_async_replication_policies**
> DpBlockAsyncReplicationPoliciesResp list_dp_block_async_replication_policies(limit=limit, offset=offset, q=q, sort=sort, dp_site_id=dp_site_id, volume_id=volume_id)



List dp block async replication policies

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
api_instance = xms_client.DpBlockAsyncReplicationPoliciesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
dp_site_id = 789 # int | related site id (optional)
volume_id = 789 # int | related volume id (optional)

try:
    api_response = api_instance.list_dp_block_async_replication_policies(limit=limit, offset=offset, q=q, sort=sort, dp_site_id=dp_site_id, volume_id=volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPoliciesApi->list_dp_block_async_replication_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **dp_site_id** | **int**| related site id | [optional] 
 **volume_id** | **int**| related volume id | [optional] 

### Return type

[**DpBlockAsyncReplicationPoliciesResp**](DpBlockAsyncReplicationPoliciesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dp_block_async_replication_policy**
> DpBlockAsyncReplicationPolicyResp update_dp_block_async_replication_policy(policy_id, body)



Update dp block async replication policy

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
api_instance = xms_client.DpBlockAsyncReplicationPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id
body = xms_client.DpBlockAsyncReplicationPolicyUpdateReq() # DpBlockAsyncReplicationPolicyUpdateReq | policy info

try:
    api_response = api_instance.update_dp_block_async_replication_policy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPoliciesApi->update_dp_block_async_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 
 **body** | [**DpBlockAsyncReplicationPolicyUpdateReq**](DpBlockAsyncReplicationPolicyUpdateReq.md)| policy info | 

### Return type

[**DpBlockAsyncReplicationPolicyResp**](DpBlockAsyncReplicationPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

