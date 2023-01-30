# xms_client.TargetsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_target_gateway_i_ps**](TargetsApi.md#add_target_gateway_i_ps) | **POST** /targets/{target_id}:add-gateway-ips | 
[**create_target**](TargetsApi.md#create_target) | **POST** /targets/ | 
[**delete_target**](TargetsApi.md#delete_target) | **DELETE** /targets/{target_id} | 
[**list_targets**](TargetsApi.md#list_targets) | **GET** /targets/ | 


# **add_target_gateway_i_ps**
> TargetResp add_target_gateway_i_ps(target_id, body)



Add gateway ips to target

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
api_instance = xms_client.TargetsApi(xms_client.ApiClient(configuration))
target_id = 789 # int | target id
body = xms_client.TargetAddGatewayIPsReq() # TargetAddGatewayIPsReq | gateway ips info

try:
    api_response = api_instance.add_target_gateway_i_ps(target_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->add_target_gateway_i_ps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **int**| target id | 
 **body** | [**TargetAddGatewayIPsReq**](TargetAddGatewayIPsReq.md)| gateway ips info | 

### Return type

[**TargetResp**](TargetResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_target**
> TargetResp create_target(target)



Create target

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
api_instance = xms_client.TargetsApi(xms_client.ApiClient(configuration))
target = xms_client.TargetCreateReq() # TargetCreateReq | target info

try:
    api_response = api_instance.create_target(target)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->create_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | [**TargetCreateReq**](TargetCreateReq.md)| target info | 

### Return type

[**TargetResp**](TargetResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_target**
> TargetResp delete_target(target_id, force=force)



delete target

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
api_instance = xms_client.TargetsApi(xms_client.ApiClient(configuration))
target_id = 789 # int | target id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_target(target_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->delete_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **int**| target id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**TargetResp**](TargetResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_targets**
> TargetsResp list_targets(limit=limit, offset=offset, cluster_id=cluster_id, host_id=host_id, access_path_id=access_path_id, q=q, sort=sort)



List all targets in the cluster

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
api_instance = xms_client.TargetsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
host_id = 789 # int | host id (optional)
access_path_id = 789 # int | access path id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_targets(limit=limit, offset=offset, cluster_id=cluster_id, host_id=host_id, access_path_id=access_path_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->list_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **host_id** | **int**| host id | [optional] 
 **access_path_id** | **int**| access path id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**TargetsResp**](TargetsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

