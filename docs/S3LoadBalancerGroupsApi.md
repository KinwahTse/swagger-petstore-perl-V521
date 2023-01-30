# xms_client.S3LoadBalancerGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_s3_load_balancers_to_group**](S3LoadBalancerGroupsApi.md#add_s3_load_balancers_to_group) | **PUT** /s3-load-balancer-groups/{group_id}/s3-load-balancers | 
[**create_s3_load_balancer_group**](S3LoadBalancerGroupsApi.md#create_s3_load_balancer_group) | **POST** /s3-load-balancer-groups/ | 
[**delete_s3_load_balancer_group**](S3LoadBalancerGroupsApi.md#delete_s3_load_balancer_group) | **DELETE** /s3-load-balancer-groups/{group_id} | 
[**get_s3_load_balancer_group**](S3LoadBalancerGroupsApi.md#get_s3_load_balancer_group) | **GET** /s3-load-balancer-groups/{group_id} | 
[**list_s3_load_balancer_groups**](S3LoadBalancerGroupsApi.md#list_s3_load_balancer_groups) | **GET** /s3-load-balancer-groups/ | 
[**redeploy_s3_load_balancer_group**](S3LoadBalancerGroupsApi.md#redeploy_s3_load_balancer_group) | **POST** /s3-load-balancer-groups/{group_id}:redeploy | 
[**remove_s3_load_balancers_from_group**](S3LoadBalancerGroupsApi.md#remove_s3_load_balancers_from_group) | **DELETE** /s3-load-balancer-groups/{group_id}/s3-load-balancers | 
[**update_s3_load_balancer_group**](S3LoadBalancerGroupsApi.md#update_s3_load_balancer_group) | **PATCH** /s3-load-balancer-groups/{group_id} | 


# **add_s3_load_balancers_to_group**
> S3LoadBalancerGroupResp add_s3_load_balancers_to_group(group_id, body)



add load balancers to group

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
api_instance = xms_client.S3LoadBalancerGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | group id
body = xms_client.S3LoadBalancersAddReq() # S3LoadBalancersAddReq | load balancer ids to add

try:
    api_response = api_instance.add_s3_load_balancers_to_group(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancerGroupsApi->add_s3_load_balancers_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| group id | 
 **body** | [**S3LoadBalancersAddReq**](S3LoadBalancersAddReq.md)| load balancer ids to add | 

### Return type

[**S3LoadBalancerGroupResp**](S3LoadBalancerGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_s3_load_balancer_group**
> S3LoadBalancerGroupResp create_s3_load_balancer_group(body, cluster_id=cluster_id)



Create a s3 load balancer group

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
api_instance = xms_client.S3LoadBalancerGroupsApi(xms_client.ApiClient(configuration))
body = xms_client.S3LoadBalancerGroupCreateReq() # S3LoadBalancerGroupCreateReq | s3 load balancer group info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_s3_load_balancer_group(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancerGroupsApi->create_s3_load_balancer_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3LoadBalancerGroupCreateReq**](S3LoadBalancerGroupCreateReq.md)| s3 load balancer group info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**S3LoadBalancerGroupResp**](S3LoadBalancerGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_s3_load_balancer_group**
> S3LoadBalancerGroupResp delete_s3_load_balancer_group(group_id, force=force)



Delete s3 load balancer group

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
api_instance = xms_client.S3LoadBalancerGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | s3 load balancer group id
force = true # bool | forcedly delete or not (optional)

try:
    api_response = api_instance.delete_s3_load_balancer_group(group_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancerGroupsApi->delete_s3_load_balancer_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| s3 load balancer group id | 
 **force** | **bool**| forcedly delete or not | [optional] 

### Return type

[**S3LoadBalancerGroupResp**](S3LoadBalancerGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_load_balancer_group**
> S3LoadBalancerGroupResp get_s3_load_balancer_group(group_id)



Get s3 load balancer group

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
api_instance = xms_client.S3LoadBalancerGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | s3 load balancer group id

try:
    api_response = api_instance.get_s3_load_balancer_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancerGroupsApi->get_s3_load_balancer_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| s3 load balancer group id | 

### Return type

[**S3LoadBalancerGroupResp**](S3LoadBalancerGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_s3_load_balancer_groups**
> S3LoadBalancerGroupsResp list_s3_load_balancer_groups(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id)



List s3 load balancer groups

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
api_instance = xms_client.S3LoadBalancerGroupsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_s3_load_balancer_groups(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancerGroupsApi->list_s3_load_balancer_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**S3LoadBalancerGroupsResp**](S3LoadBalancerGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_s3_load_balancer_group**
> S3LoadBalancerGroupResp redeploy_s3_load_balancer_group(group_id)



Redeploy a s3 load balancer group

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
api_instance = xms_client.S3LoadBalancerGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | s3 load balancer group id

try:
    api_response = api_instance.redeploy_s3_load_balancer_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancerGroupsApi->redeploy_s3_load_balancer_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| s3 load balancer group id | 

### Return type

[**S3LoadBalancerGroupResp**](S3LoadBalancerGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_s3_load_balancers_from_group**
> S3LoadBalancerGroupResp remove_s3_load_balancers_from_group(group_id, body, force=force)



remove load balancers from group

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
api_instance = xms_client.S3LoadBalancerGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | group id
body = xms_client.S3LoadBalancersRemoveReq() # S3LoadBalancersRemoveReq | load balancer ids to remove
force = true # bool | forcedly remove or not (optional)

try:
    api_response = api_instance.remove_s3_load_balancers_from_group(group_id, body, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancerGroupsApi->remove_s3_load_balancers_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| group id | 
 **body** | [**S3LoadBalancersRemoveReq**](S3LoadBalancersRemoveReq.md)| load balancer ids to remove | 
 **force** | **bool**| forcedly remove or not | [optional] 

### Return type

[**S3LoadBalancerGroupResp**](S3LoadBalancerGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_s3_load_balancer_group**
> S3LoadBalancerGroupResp update_s3_load_balancer_group(group_id, body)



Update a s3 load balancer group

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
api_instance = xms_client.S3LoadBalancerGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | s3 load balancer group id
body = xms_client.S3LoadBalancerGroupUpdateReq() # S3LoadBalancerGroupUpdateReq | s3 load balancer group info

try:
    api_response = api_instance.update_s3_load_balancer_group(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancerGroupsApi->update_s3_load_balancer_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| s3 load balancer group id | 
 **body** | [**S3LoadBalancerGroupUpdateReq**](S3LoadBalancerGroupUpdateReq.md)| s3 load balancer group info | 

### Return type

[**S3LoadBalancerGroupResp**](S3LoadBalancerGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

