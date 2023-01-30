# xms_client.VipGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vip_group**](VipGroupsApi.md#create_vip_group) | **POST** /vip-groups/ | 
[**delete_vip_group**](VipGroupsApi.md#delete_vip_group) | **DELETE** /vip-groups/{vip_group_id} | 
[**get_vip_group**](VipGroupsApi.md#get_vip_group) | **GET** /vip-groups/{vip_group_id} | 
[**list_vip_groups**](VipGroupsApi.md#list_vip_groups) | **GET** /vip-groups/ | 
[**redeploy_vip_group**](VipGroupsApi.md#redeploy_vip_group) | **POST** /vip-groups/{vip_group_id}:redeploy | 
[**update_vip_group**](VipGroupsApi.md#update_vip_group) | **PATCH** /vip-groups/{vip_group_id} | 


# **create_vip_group**
> VIPGroupResp create_vip_group(vip_group)



Create a vip group

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
api_instance = xms_client.VipGroupsApi(xms_client.ApiClient(configuration))
vip_group = xms_client.VIPGroupCreateReq() # VIPGroupCreateReq | vip group info

try:
    api_response = api_instance.create_vip_group(vip_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VipGroupsApi->create_vip_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vip_group** | [**VIPGroupCreateReq**](VIPGroupCreateReq.md)| vip group info | 

### Return type

[**VIPGroupResp**](VIPGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vip_group**
> VIPGroupResp delete_vip_group(vip_group_id)



Delete a vip group

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
api_instance = xms_client.VipGroupsApi(xms_client.ApiClient(configuration))
vip_group_id = 789 # int | vip group id

try:
    api_response = api_instance.delete_vip_group(vip_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VipGroupsApi->delete_vip_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vip_group_id** | **int**| vip group id | 

### Return type

[**VIPGroupResp**](VIPGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vip_group**
> VIPGroupResp get_vip_group(vip_group_id)



Get a vip group

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
api_instance = xms_client.VipGroupsApi(xms_client.ApiClient(configuration))
vip_group_id = 789 # int | vip group id

try:
    api_response = api_instance.get_vip_group(vip_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VipGroupsApi->get_vip_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vip_group_id** | **int**| vip group id | 

### Return type

[**VIPGroupResp**](VIPGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vip_groups**
> VIPGroupResps list_vip_groups(limit=limit, offset=offset, resource_type=resource_type, resource_id=resource_id)



List vip groups

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
api_instance = xms_client.VipGroupsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
resource_type = 'resource_type_example' # str | resource type (optional)
resource_id = 789 # int | resource id (optional)

try:
    api_response = api_instance.list_vip_groups(limit=limit, offset=offset, resource_type=resource_type, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VipGroupsApi->list_vip_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **resource_type** | **str**| resource type | [optional] 
 **resource_id** | **int**| resource id | [optional] 

### Return type

[**VIPGroupResps**](VIPGroupResps.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_vip_group**
> VIPGroupResp redeploy_vip_group(vip_group_id)



Redeploy a vip group

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
api_instance = xms_client.VipGroupsApi(xms_client.ApiClient(configuration))
vip_group_id = 789 # int | vip group id

try:
    api_response = api_instance.redeploy_vip_group(vip_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VipGroupsApi->redeploy_vip_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vip_group_id** | **int**| vip group id | 

### Return type

[**VIPGroupResp**](VIPGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vip_group**
> VIPGroupResp update_vip_group(vip_group_id, vip_group)



Update a vip group

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
api_instance = xms_client.VipGroupsApi(xms_client.ApiClient(configuration))
vip_group_id = 789 # int | vip group id
vip_group = xms_client.VIPGroupUpdateReq() # VIPGroupUpdateReq | vip group info

try:
    api_response = api_instance.update_vip_group(vip_group_id, vip_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VipGroupsApi->update_vip_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vip_group_id** | **int**| vip group id | 
 **vip_group** | [**VIPGroupUpdateReq**](VIPGroupUpdateReq.md)| vip group info | 

### Return type

[**VIPGroupResp**](VIPGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

