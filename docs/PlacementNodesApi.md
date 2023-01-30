# xms_client.PlacementNodesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_placement_node**](PlacementNodesApi.md#create_placement_node) | **POST** /placement-nodes/ | 
[**delete_placement_node**](PlacementNodesApi.md#delete_placement_node) | **DELETE** /placement-nodes/{placement_node_id} | 
[**get_placement_node**](PlacementNodesApi.md#get_placement_node) | **GET** /placement-nodes/{placement_node_id} | 
[**get_placement_node_topology**](PlacementNodesApi.md#get_placement_node_topology) | **GET** /placement-nodes/{placement_node_id}/topology | 
[**get_topology_from_osds**](PlacementNodesApi.md#get_topology_from_osds) | **POST** /placement-nodes/:topology-from-osd | 
[**list_placement_nodes**](PlacementNodesApi.md#list_placement_nodes) | **GET** /placement-nodes/ | 
[**update_placement_node**](PlacementNodesApi.md#update_placement_node) | **PATCH** /placement-nodes/{placement_node_id} | 


# **create_placement_node**
> PlacementNodeResp create_placement_node(body)



Create placement node

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
api_instance = xms_client.PlacementNodesApi(xms_client.ApiClient(configuration))
body = xms_client.PlacementNodeCreateReq() # PlacementNodeCreateReq | placement node info

try:
    api_response = api_instance.create_placement_node(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementNodesApi->create_placement_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlacementNodeCreateReq**](PlacementNodeCreateReq.md)| placement node info | 

### Return type

[**PlacementNodeResp**](PlacementNodeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_placement_node**
> delete_placement_node(placement_node_id)



delete placement node

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
api_instance = xms_client.PlacementNodesApi(xms_client.ApiClient(configuration))
placement_node_id = 789 # int | placement node id

try:
    api_instance.delete_placement_node(placement_node_id)
except ApiException as e:
    print("Exception when calling PlacementNodesApi->delete_placement_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placement_node_id** | **int**| placement node id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_placement_node**
> PlacementNodeResp get_placement_node(placement_node_id)



Get placement node

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
api_instance = xms_client.PlacementNodesApi(xms_client.ApiClient(configuration))
placement_node_id = 789 # int | placement node id

try:
    api_response = api_instance.get_placement_node(placement_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementNodesApi->get_placement_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placement_node_id** | **int**| placement node id | 

### Return type

[**PlacementNodeResp**](PlacementNodeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_placement_node_topology**
> PlacementNodeTopologyResp get_placement_node_topology(placement_node_id, osd_type=osd_type, osd_role=osd_role, with_compound=with_compound, with_hybrid=with_hybrid)



Get subtree topology of placement node

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
api_instance = xms_client.PlacementNodesApi(xms_client.ApiClient(configuration))
placement_node_id = 789 # int | placement node id
osd_type = 'osd_type_example' # str | osd type (optional)
osd_role = 'osd_role_example' # str | osd role (optional)
with_compound = true # bool | with compound osd (optional)
with_hybrid = true # bool | with hybrid osd (optional)

try:
    api_response = api_instance.get_placement_node_topology(placement_node_id, osd_type=osd_type, osd_role=osd_role, with_compound=with_compound, with_hybrid=with_hybrid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementNodesApi->get_placement_node_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placement_node_id** | **int**| placement node id | 
 **osd_type** | **str**| osd type | [optional] 
 **osd_role** | **str**| osd role | [optional] 
 **with_compound** | **bool**| with compound osd | [optional] 
 **with_hybrid** | **bool**| with hybrid osd | [optional] 

### Return type

[**PlacementNodeTopologyResp**](PlacementNodeTopologyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_from_osds**
> PlacementNodeTopologyResp get_topology_from_osds(body)



Get topology from osds

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
api_instance = xms_client.PlacementNodesApi(xms_client.ApiClient(configuration))
body = xms_client.TopologyFromOsdReq() # TopologyFromOsdReq | osds

try:
    api_response = api_instance.get_topology_from_osds(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementNodesApi->get_topology_from_osds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TopologyFromOsdReq**](TopologyFromOsdReq.md)| osds | 

### Return type

[**PlacementNodeTopologyResp**](PlacementNodeTopologyResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_placement_nodes**
> PlacementNodesResp list_placement_nodes(limit=limit, offset=offset, type=type, parent_id=parent_id)



List placement nodes

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
api_instance = xms_client.PlacementNodesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
type = 'type_example' # str | filter placement nodes by type (optional)
parent_id = 789 # int | filter placement nodes by parent (optional)

try:
    api_response = api_instance.list_placement_nodes(limit=limit, offset=offset, type=type, parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementNodesApi->list_placement_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **type** | **str**| filter placement nodes by type | [optional] 
 **parent_id** | **int**| filter placement nodes by parent | [optional] 

### Return type

[**PlacementNodesResp**](PlacementNodesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_placement_node**
> PlacementNodeResp update_placement_node(placement_node_id, body)



update placement node

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
api_instance = xms_client.PlacementNodesApi(xms_client.ApiClient(configuration))
placement_node_id = 789 # int | the placement node id
body = xms_client.PlacementNodeUpdateReq() # PlacementNodeUpdateReq | the placement node info

try:
    api_response = api_instance.update_placement_node(placement_node_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacementNodesApi->update_placement_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **placement_node_id** | **int**| the placement node id | 
 **body** | [**PlacementNodeUpdateReq**](PlacementNodeUpdateReq.md)| the placement node info | 

### Return type

[**PlacementNodeResp**](PlacementNodeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

