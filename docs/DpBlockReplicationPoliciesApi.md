# xms_client.DpBlockReplicationPoliciesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dp_block_replication_policy**](DpBlockReplicationPoliciesApi.md#create_dp_block_replication_policy) | **POST** /dp-block-replication-policies/ | 
[**delete_dp_block_replication_policy**](DpBlockReplicationPoliciesApi.md#delete_dp_block_replication_policy) | **DELETE** /dp-block-replication-policies/{policy_id} | 
[**get_dp_block_replication_policy**](DpBlockReplicationPoliciesApi.md#get_dp_block_replication_policy) | **GET** /dp-block-replication-policies/{policy_id} | 
[**list_dp_block_replication_policies**](DpBlockReplicationPoliciesApi.md#list_dp_block_replication_policies) | **GET** /dp-block-replication-policies/ | 
[**update_dp_block_replication_policy**](DpBlockReplicationPoliciesApi.md#update_dp_block_replication_policy) | **PATCH** /dp-block-replication-policies/{policy_id} | 


# **create_dp_block_replication_policy**
> DpBlockReplicationPolicyResp create_dp_block_replication_policy(body)



Create dp block replication policy

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
api_instance = xms_client.DpBlockReplicationPoliciesApi(xms_client.ApiClient(configuration))
body = xms_client.DpBlockReplicationPolicyCreateReq() # DpBlockReplicationPolicyCreateReq | policy info

try:
    api_response = api_instance.create_dp_block_replication_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockReplicationPoliciesApi->create_dp_block_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpBlockReplicationPolicyCreateReq**](DpBlockReplicationPolicyCreateReq.md)| policy info | 

### Return type

[**DpBlockReplicationPolicyResp**](DpBlockReplicationPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_block_replication_policy**
> delete_dp_block_replication_policy(policy_id)



Delete dp block replication policy

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
api_instance = xms_client.DpBlockReplicationPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | policy id

try:
    api_instance.delete_dp_block_replication_policy(policy_id)
except ApiException as e:
    print("Exception when calling DpBlockReplicationPoliciesApi->delete_dp_block_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| policy id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_block_replication_policy**
> DpBlockReplicationPolicyResp get_dp_block_replication_policy(policy_id)



Get dp block replication policy

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
api_instance = xms_client.DpBlockReplicationPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_block_replication_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockReplicationPoliciesApi->get_dp_block_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 

### Return type

[**DpBlockReplicationPolicyResp**](DpBlockReplicationPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_block_replication_policies**
> DpBlockReplicationPoliciesResp list_dp_block_replication_policies(limit=limit, offset=offset, q=q, sort=sort)



List dp block replication policies

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
api_instance = xms_client.DpBlockReplicationPoliciesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dp_block_replication_policies(limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockReplicationPoliciesApi->list_dp_block_replication_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DpBlockReplicationPoliciesResp**](DpBlockReplicationPoliciesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dp_block_replication_policy**
> DpBlockReplicationPolicyResp update_dp_block_replication_policy(policy_id, body)



Update dp block replication policy

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
api_instance = xms_client.DpBlockReplicationPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id
body = xms_client.DpBlockReplicationPolicyUpdateReq() # DpBlockReplicationPolicyUpdateReq | policy info

try:
    api_response = api_instance.update_dp_block_replication_policy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockReplicationPoliciesApi->update_dp_block_replication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 
 **body** | [**DpBlockReplicationPolicyUpdateReq**](DpBlockReplicationPolicyUpdateReq.md)| policy info | 

### Return type

[**DpBlockReplicationPolicyResp**](DpBlockReplicationPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

