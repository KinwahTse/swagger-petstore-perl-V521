# xms_client.OsRemotePoliciesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_os_remote_policy**](OsRemotePoliciesApi.md#get_os_remote_policy) | **GET** /os-remote-policies/{policy_uuid} | 
[**list_os_remote_policies**](OsRemotePoliciesApi.md#list_os_remote_policies) | **GET** /os-remote-policies/ | 


# **get_os_remote_policy**
> OSRemotePolicyResp get_os_remote_policy(policy_uuid)



Get a os remote policy

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
api_instance = xms_client.OsRemotePoliciesApi(xms_client.ApiClient(configuration))
policy_uuid = 'policy_uuid_example' # str | policy uuid

try:
    api_response = api_instance.get_os_remote_policy(policy_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsRemotePoliciesApi->get_os_remote_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| policy uuid | 

### Return type

[**OSRemotePolicyResp**](OSRemotePolicyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_remote_policies**
> OSRemotePoliciesResp list_os_remote_policies(limit=limit, offset=offset, marker=marker, zone_uuid=zone_uuid, cluster_id=cluster_id)



List os remote policies

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
api_instance = xms_client.OsRemotePoliciesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
marker = 'marker_example' # str | paging param (optional)
zone_uuid = 'zone_uuid_example' # str | zone uuid (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_os_remote_policies(limit=limit, offset=offset, marker=marker, zone_uuid=zone_uuid, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsRemotePoliciesApi->list_os_remote_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **marker** | **str**| paging param | [optional] 
 **zone_uuid** | **str**| zone uuid | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSRemotePoliciesResp**](OSRemotePoliciesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

