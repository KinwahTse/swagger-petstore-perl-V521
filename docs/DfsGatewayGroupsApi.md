# xms_client.DfsGatewayGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dfs_gateways**](DfsGatewayGroupsApi.md#add_dfs_gateways) | **POST** /dfs-gateway-groups/{dfs_gateway_group_id}:add-gateways | 
[**create_dfs_gateway_group**](DfsGatewayGroupsApi.md#create_dfs_gateway_group) | **POST** /dfs-gateway-groups/ | 
[**delete_dfs_gateway_group**](DfsGatewayGroupsApi.md#delete_dfs_gateway_group) | **DELETE** /dfs-gateway-groups/{dfs_gateway_group_id} | 
[**get_dfs_gateway_group**](DfsGatewayGroupsApi.md#get_dfs_gateway_group) | **GET** /dfs-gateway-groups/{dfs_gateway_group_id} | 
[**list_dfs_gateway_groups**](DfsGatewayGroupsApi.md#list_dfs_gateway_groups) | **GET** /dfs-gateway-groups/ | 
[**rebuild_dfs_gateways**](DfsGatewayGroupsApi.md#rebuild_dfs_gateways) | **POST** /dfs-gateway-groups/{dfs_gateway_group_id}:rebuild-gateways | 
[**remove_dfs_gateways**](DfsGatewayGroupsApi.md#remove_dfs_gateways) | **POST** /dfs-gateway-groups/{dfs_gateway_group_id}:remove-gateways | 
[**update_dfs_gateway_group**](DfsGatewayGroupsApi.md#update_dfs_gateway_group) | **PATCH** /dfs-gateway-groups/{dfs_gateway_group_id} | 
[**update_dfs_gateway_group_types**](DfsGatewayGroupsApi.md#update_dfs_gateway_group_types) | **POST** /dfs-gateway-groups/{dfs_gateway_group_id}:update-types | 
[**update_dfs_gateway_group_vi_ps**](DfsGatewayGroupsApi.md#update_dfs_gateway_group_vi_ps) | **POST** /dfs-gateway-groups/{dfs_gateway_group_id}:update-vips | 


# **add_dfs_gateways**
> DfsGatewayGroupResp add_dfs_gateways(dfs_gateway_group_id, body)



add dfs gateways

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
api_instance = xms_client.DfsGatewayGroupsApi(xms_client.ApiClient(configuration))
dfs_gateway_group_id = 789 # int | gateway group id
body = xms_client.DfsGatewayGroupAddGatewaysReq() # DfsGatewayGroupAddGatewaysReq | gateways info

try:
    api_response = api_instance.add_dfs_gateways(dfs_gateway_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayGroupsApi->add_dfs_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_group_id** | **int**| gateway group id | 
 **body** | [**DfsGatewayGroupAddGatewaysReq**](DfsGatewayGroupAddGatewaysReq.md)| gateways info | 

### Return type

[**DfsGatewayGroupResp**](DfsGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dfs_gateway_group**
> DfsGatewayGroupResp create_dfs_gateway_group(body, cluster_id=cluster_id)



Create dfs gateway group

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
api_instance = xms_client.DfsGatewayGroupsApi(xms_client.ApiClient(configuration))
body = xms_client.DfsGatewayGroupCreateReq() # DfsGatewayGroupCreateReq | gateway group info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_dfs_gateway_group(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayGroupsApi->create_dfs_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsGatewayGroupCreateReq**](DfsGatewayGroupCreateReq.md)| gateway group info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**DfsGatewayGroupResp**](DfsGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_gateway_group**
> DfsGatewayGroupResp delete_dfs_gateway_group(dfs_gateway_group_id, force=force)



delete dfs gateway group

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
api_instance = xms_client.DfsGatewayGroupsApi(xms_client.ApiClient(configuration))
dfs_gateway_group_id = 789 # int | gateway group id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_dfs_gateway_group(dfs_gateway_group_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayGroupsApi->delete_dfs_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_group_id** | **int**| gateway group id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DfsGatewayGroupResp**](DfsGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_gateway_group**
> DfsGatewayGroupResp get_dfs_gateway_group(dfs_gateway_group_id)



Get dfs gateway group

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
api_instance = xms_client.DfsGatewayGroupsApi(xms_client.ApiClient(configuration))
dfs_gateway_group_id = 789 # int | gateway group id

try:
    api_response = api_instance.get_dfs_gateway_group(dfs_gateway_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayGroupsApi->get_dfs_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_group_id** | **int**| gateway group id | 

### Return type

[**DfsGatewayGroupResp**](DfsGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_gateway_groups**
> DfsGatewayGroupsResp list_dfs_gateway_groups(limit=limit, offset=offset, cluster_id=cluster_id, type=type, security=security, q=q, sort=sort)



List dfs gateway groups

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
api_instance = xms_client.DfsGatewayGroupsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
type = 'type_example' # str | type of dfs gateway group (optional)
security = 'security_example' # str | security of dfs gateway group (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dfs_gateway_groups(limit=limit, offset=offset, cluster_id=cluster_id, type=type, security=security, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayGroupsApi->list_dfs_gateway_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **type** | **str**| type of dfs gateway group | [optional] 
 **security** | **str**| security of dfs gateway group | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DfsGatewayGroupsResp**](DfsGatewayGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild_dfs_gateways**
> DfsGatewayGroupResp rebuild_dfs_gateways(dfs_gateway_group_id, body)



rebuild gateways in gateway group

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
api_instance = xms_client.DfsGatewayGroupsApi(xms_client.ApiClient(configuration))
dfs_gateway_group_id = 789 # int | gateway group id
body = xms_client.DfsGatewayGroupRebuildGatewaysReq() # DfsGatewayGroupRebuildGatewaysReq | gateways info

try:
    api_response = api_instance.rebuild_dfs_gateways(dfs_gateway_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayGroupsApi->rebuild_dfs_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_group_id** | **int**| gateway group id | 
 **body** | [**DfsGatewayGroupRebuildGatewaysReq**](DfsGatewayGroupRebuildGatewaysReq.md)| gateways info | 

### Return type

[**DfsGatewayGroupResp**](DfsGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dfs_gateways**
> DfsGatewayGroupResp remove_dfs_gateways(dfs_gateway_group_id, body, force=force)



remove gateways from gateway group

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
api_instance = xms_client.DfsGatewayGroupsApi(xms_client.ApiClient(configuration))
dfs_gateway_group_id = 789 # int | gateway group id
body = xms_client.DfsGatewayGroupRemoveGatewaysReq() # DfsGatewayGroupRemoveGatewaysReq | gateways info
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.remove_dfs_gateways(dfs_gateway_group_id, body, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayGroupsApi->remove_dfs_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_group_id** | **int**| gateway group id | 
 **body** | [**DfsGatewayGroupRemoveGatewaysReq**](DfsGatewayGroupRemoveGatewaysReq.md)| gateways info | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DfsGatewayGroupResp**](DfsGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_gateway_group**
> DfsGatewayGroupResp update_dfs_gateway_group(dfs_gateway_group_id, body)



Update dfs gateway group

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
api_instance = xms_client.DfsGatewayGroupsApi(xms_client.ApiClient(configuration))
dfs_gateway_group_id = 789 # int | gateway group id
body = xms_client.DfsGatewayGroupUpdateReq() # DfsGatewayGroupUpdateReq | gateway group info

try:
    api_response = api_instance.update_dfs_gateway_group(dfs_gateway_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayGroupsApi->update_dfs_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_group_id** | **int**| gateway group id | 
 **body** | [**DfsGatewayGroupUpdateReq**](DfsGatewayGroupUpdateReq.md)| gateway group info | 

### Return type

[**DfsGatewayGroupResp**](DfsGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_gateway_group_types**
> DfsGatewayGroupResp update_dfs_gateway_group_types(dfs_gateway_group_id, body)



Update protocal types of dfs gateway group

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
api_instance = xms_client.DfsGatewayGroupsApi(xms_client.ApiClient(configuration))
dfs_gateway_group_id = 789 # int | gateway group id
body = xms_client.DfsGatewayGroupUpdateTypesReq() # DfsGatewayGroupUpdateTypesReq | gateway group info

try:
    api_response = api_instance.update_dfs_gateway_group_types(dfs_gateway_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayGroupsApi->update_dfs_gateway_group_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_group_id** | **int**| gateway group id | 
 **body** | [**DfsGatewayGroupUpdateTypesReq**](DfsGatewayGroupUpdateTypesReq.md)| gateway group info | 

### Return type

[**DfsGatewayGroupResp**](DfsGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_gateway_group_vi_ps**
> DfsGatewayGroupResp update_dfs_gateway_group_vi_ps(dfs_gateway_group_id, body)



Update VIPs of dfs gateway group

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
api_instance = xms_client.DfsGatewayGroupsApi(xms_client.ApiClient(configuration))
dfs_gateway_group_id = 789 # int | gateway group id
body = xms_client.DfsGatewayGroupUpdateVIPsReq() # DfsGatewayGroupUpdateVIPsReq | gateway group info

try:
    api_response = api_instance.update_dfs_gateway_group_vi_ps(dfs_gateway_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsGatewayGroupsApi->update_dfs_gateway_group_vi_ps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_gateway_group_id** | **int**| gateway group id | 
 **body** | [**DfsGatewayGroupUpdateVIPsReq**](DfsGatewayGroupUpdateVIPsReq.md)| gateway group info | 

### Return type

[**DfsGatewayGroupResp**](DfsGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

