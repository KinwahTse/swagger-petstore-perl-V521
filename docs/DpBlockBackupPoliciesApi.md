# xms_client.DpBlockBackupPoliciesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dp_block_backup_policy**](DpBlockBackupPoliciesApi.md#create_dp_block_backup_policy) | **POST** /dp-block-backup-policies/ | 
[**delete_dp_block_backup_policy**](DpBlockBackupPoliciesApi.md#delete_dp_block_backup_policy) | **DELETE** /dp-block-backup-policies/{policy_id} | 
[**get_dp_block_backup_policy**](DpBlockBackupPoliciesApi.md#get_dp_block_backup_policy) | **GET** /dp-block-backup-policies/{policy_id} | 
[**list_dp_block_backup_policies**](DpBlockBackupPoliciesApi.md#list_dp_block_backup_policies) | **GET** /dp-block-backup-policies/ | 
[**update_dp_block_backup_policy**](DpBlockBackupPoliciesApi.md#update_dp_block_backup_policy) | **PATCH** /dp-block-backup-policies/{policy_id} | 


# **create_dp_block_backup_policy**
> DpBlockBackupPolicyResp create_dp_block_backup_policy(body)



Create dp block backup policy

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
api_instance = xms_client.DpBlockBackupPoliciesApi(xms_client.ApiClient(configuration))
body = xms_client.DpBlockBackupPolicyCreateReq() # DpBlockBackupPolicyCreateReq | policy info

try:
    api_response = api_instance.create_dp_block_backup_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockBackupPoliciesApi->create_dp_block_backup_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpBlockBackupPolicyCreateReq**](DpBlockBackupPolicyCreateReq.md)| policy info | 

### Return type

[**DpBlockBackupPolicyResp**](DpBlockBackupPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_block_backup_policy**
> DpBlockBackupPolicyResp delete_dp_block_backup_policy(policy_id, force=force)



Delete dp block backup policy

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
api_instance = xms_client.DpBlockBackupPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_dp_block_backup_policy(policy_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockBackupPoliciesApi->delete_dp_block_backup_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DpBlockBackupPolicyResp**](DpBlockBackupPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_block_backup_policy**
> DpBlockBackupPolicyResp get_dp_block_backup_policy(policy_id)



Get dp block backup policy

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
api_instance = xms_client.DpBlockBackupPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_block_backup_policy(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockBackupPoliciesApi->get_dp_block_backup_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 

### Return type

[**DpBlockBackupPolicyResp**](DpBlockBackupPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_block_backup_policies**
> DpBlockBackupPoliciesResp list_dp_block_backup_policies(limit=limit, offset=offset, q=q, sort=sort, block_volume_id=block_volume_id, dp_site_id=dp_site_id)



List dp block backup policies

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
api_instance = xms_client.DpBlockBackupPoliciesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
block_volume_id = 789 # int | show dp block backup policies of specific block volume (optional)
dp_site_id = 789 # int | related site id (optional)

try:
    api_response = api_instance.list_dp_block_backup_policies(limit=limit, offset=offset, q=q, sort=sort, block_volume_id=block_volume_id, dp_site_id=dp_site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockBackupPoliciesApi->list_dp_block_backup_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **block_volume_id** | **int**| show dp block backup policies of specific block volume | [optional] 
 **dp_site_id** | **int**| related site id | [optional] 

### Return type

[**DpBlockBackupPoliciesResp**](DpBlockBackupPoliciesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dp_block_backup_policy**
> DpBlockBackupPolicyResp update_dp_block_backup_policy(policy_id, body)



Update dp block backup policy

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
api_instance = xms_client.DpBlockBackupPoliciesApi(xms_client.ApiClient(configuration))
policy_id = 789 # int | resource id
body = xms_client.DpBlockBackupPolicyUpdateReq() # DpBlockBackupPolicyUpdateReq | policy info

try:
    api_response = api_instance.update_dp_block_backup_policy(policy_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockBackupPoliciesApi->update_dp_block_backup_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| resource id | 
 **body** | [**DpBlockBackupPolicyUpdateReq**](DpBlockBackupPolicyUpdateReq.md)| policy info | 

### Return type

[**DpBlockBackupPolicyResp**](DpBlockBackupPolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

