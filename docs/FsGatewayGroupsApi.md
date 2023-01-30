# xms_client.FsGatewayGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fs_gateways**](FsGatewayGroupsApi.md#add_fs_gateways) | **POST** /fs-gateway-groups/{fs_gateway_group_id}:add-gateways | 
[**create_fs_gateway_group**](FsGatewayGroupsApi.md#create_fs_gateway_group) | **POST** /fs-gateway-groups/ | 
[**delete_fs_gateway_group**](FsGatewayGroupsApi.md#delete_fs_gateway_group) | **DELETE** /fs-gateway-groups/{fs_gateway_group_id} | 
[**get_fs_gateway_group**](FsGatewayGroupsApi.md#get_fs_gateway_group) | **GET** /fs-gateway-groups/{fs_gateway_group_id} | 
[**list_fs_gateway_groups**](FsGatewayGroupsApi.md#list_fs_gateway_groups) | **GET** /fs-gateway-groups/ | 
[**remove_fs_gateways**](FsGatewayGroupsApi.md#remove_fs_gateways) | **POST** /fs-gateway-groups/{fs_gateway_group_id}:remove-gateways | 
[**update_fs_gateway_group**](FsGatewayGroupsApi.md#update_fs_gateway_group) | **PATCH** /fs-gateway-groups/{fs_gateway_group_id} | 


# **add_fs_gateways**
> FSGatewayGroupResp add_fs_gateways(fs_gateway_group_id, body)



add file storage gateways

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
api_instance = xms_client.FsGatewayGroupsApi(xms_client.ApiClient(configuration))
fs_gateway_group_id = 789 # int | gateway group id
body = xms_client.FSGatewayGroupAddGatewaysReq() # FSGatewayGroupAddGatewaysReq | gateways info

try:
    api_response = api_instance.add_fs_gateways(fs_gateway_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsGatewayGroupsApi->add_fs_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_gateway_group_id** | **int**| gateway group id | 
 **body** | [**FSGatewayGroupAddGatewaysReq**](FSGatewayGroupAddGatewaysReq.md)| gateways info | 

### Return type

[**FSGatewayGroupResp**](FSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fs_gateway_group**
> FSGatewayGroupResp create_fs_gateway_group(body, cluster_id=cluster_id)



Create file storage gateway group

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
api_instance = xms_client.FsGatewayGroupsApi(xms_client.ApiClient(configuration))
body = xms_client.FSGatewayGroupCreateReq() # FSGatewayGroupCreateReq | gateway group info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_fs_gateway_group(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsGatewayGroupsApi->create_fs_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSGatewayGroupCreateReq**](FSGatewayGroupCreateReq.md)| gateway group info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**FSGatewayGroupResp**](FSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fs_gateway_group**
> FSGatewayGroupResp delete_fs_gateway_group(fs_gateway_group_id, force=force)



delete file storage gateway group

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
api_instance = xms_client.FsGatewayGroupsApi(xms_client.ApiClient(configuration))
fs_gateway_group_id = 789 # int | gateway group id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_fs_gateway_group(fs_gateway_group_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsGatewayGroupsApi->delete_fs_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_gateway_group_id** | **int**| gateway group id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**FSGatewayGroupResp**](FSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fs_gateway_group**
> FSGatewayGroupResp get_fs_gateway_group(fs_gateway_group_id)



Get file storage gateway group

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
api_instance = xms_client.FsGatewayGroupsApi(xms_client.ApiClient(configuration))
fs_gateway_group_id = 789 # int | gateway group id

try:
    api_response = api_instance.get_fs_gateway_group(fs_gateway_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsGatewayGroupsApi->get_fs_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_gateway_group_id** | **int**| gateway group id | 

### Return type

[**FSGatewayGroupResp**](FSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fs_gateway_groups**
> FSGatewayGroupsResp list_fs_gateway_groups(limit=limit, offset=offset, cluster_id=cluster_id, type=type, security=security, q=q, sort=sort)



List file storage gateway groups

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
api_instance = xms_client.FsGatewayGroupsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
type = 'type_example' # str | type of file storage gateway group (optional)
security = 'security_example' # str | security of file storage gateway group (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_fs_gateway_groups(limit=limit, offset=offset, cluster_id=cluster_id, type=type, security=security, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsGatewayGroupsApi->list_fs_gateway_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **type** | **str**| type of file storage gateway group | [optional] 
 **security** | **str**| security of file storage gateway group | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**FSGatewayGroupsResp**](FSGatewayGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_fs_gateways**
> FSGatewayGroupResp remove_fs_gateways(fs_gateway_group_id, body, force=force)



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
api_instance = xms_client.FsGatewayGroupsApi(xms_client.ApiClient(configuration))
fs_gateway_group_id = 789 # int | gateway group id
body = xms_client.FSGatewayGroupRemoveGatewaysReq() # FSGatewayGroupRemoveGatewaysReq | gateways info
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.remove_fs_gateways(fs_gateway_group_id, body, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsGatewayGroupsApi->remove_fs_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_gateway_group_id** | **int**| gateway group id | 
 **body** | [**FSGatewayGroupRemoveGatewaysReq**](FSGatewayGroupRemoveGatewaysReq.md)| gateways info | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**FSGatewayGroupResp**](FSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fs_gateway_group**
> FSGatewayGroupResp update_fs_gateway_group(fs_gateway_group_id, body)



Update file storage gateway group

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
api_instance = xms_client.FsGatewayGroupsApi(xms_client.ApiClient(configuration))
fs_gateway_group_id = 789 # int | gateway group id
body = xms_client.FSGatewayGroupUpdateReq() # FSGatewayGroupUpdateReq | gateway group info

try:
    api_response = api_instance.update_fs_gateway_group(fs_gateway_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsGatewayGroupsApi->update_fs_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_gateway_group_id** | **int**| gateway group id | 
 **body** | [**FSGatewayGroupUpdateReq**](FSGatewayGroupUpdateReq.md)| gateway group info | 

### Return type

[**FSGatewayGroupResp**](FSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

