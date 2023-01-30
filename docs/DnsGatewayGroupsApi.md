# xms_client.DnsGatewayGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dns_gateway_to_group**](DnsGatewayGroupsApi.md#add_dns_gateway_to_group) | **POST** /dns-gateway-groups/{group_id}:add-gateway | 
[**create_dns_gateway_group**](DnsGatewayGroupsApi.md#create_dns_gateway_group) | **POST** /dns-gateway-groups/ | 
[**delete_dns_gateway_group**](DnsGatewayGroupsApi.md#delete_dns_gateway_group) | **DELETE** /dns-gateway-groups/{group_id} | 
[**get_dns_gateway_group**](DnsGatewayGroupsApi.md#get_dns_gateway_group) | **GET** /dns-gateway-groups/{group_id} | 
[**list_dns_gateway_groups**](DnsGatewayGroupsApi.md#list_dns_gateway_groups) | **GET** /dns-gateway-groups/ | 
[**redeploy_dns_gateway_group**](DnsGatewayGroupsApi.md#redeploy_dns_gateway_group) | **POST** /dns-gateway-groups/{group_id}:redeploy | 
[**remove_dns_gateway_from_group**](DnsGatewayGroupsApi.md#remove_dns_gateway_from_group) | **POST** /dns-gateway-groups/{group_id}:remove-gateway | 


# **add_dns_gateway_to_group**
> DNSGatewayGroupResp add_dns_gateway_to_group(group_id, body)



Add DNS gateways to DNS gateway group.

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
api_instance = xms_client.DnsGatewayGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | dns gateway group id
body = xms_client.DNSGatewayGroupAddGatewayReq() # DNSGatewayGroupAddGatewayReq | DNS gateway info

try:
    api_response = api_instance.add_dns_gateway_to_group(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsGatewayGroupsApi->add_dns_gateway_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| dns gateway group id | 
 **body** | [**DNSGatewayGroupAddGatewayReq**](DNSGatewayGroupAddGatewayReq.md)| DNS gateway info | 

### Return type

[**DNSGatewayGroupResp**](DNSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dns_gateway_group**
> DNSGatewayGroupResp create_dns_gateway_group(dns_gateway_group)



Create a DNS gateway group.

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
api_instance = xms_client.DnsGatewayGroupsApi(xms_client.ApiClient(configuration))
dns_gateway_group = xms_client.DNSGatewayGroupCreateReq() # DNSGatewayGroupCreateReq | DNS gateway group info

try:
    api_response = api_instance.create_dns_gateway_group(dns_gateway_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsGatewayGroupsApi->create_dns_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dns_gateway_group** | [**DNSGatewayGroupCreateReq**](DNSGatewayGroupCreateReq.md)| DNS gateway group info | 

### Return type

[**DNSGatewayGroupResp**](DNSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dns_gateway_group**
> DNSGatewayGroupResp delete_dns_gateway_group(group_id, force=force)



Delete a DNS gateway group.

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
api_instance = xms_client.DnsGatewayGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | dns gateway group id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_dns_gateway_group(group_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsGatewayGroupsApi->delete_dns_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| dns gateway group id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DNSGatewayGroupResp**](DNSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_gateway_group**
> DNSGatewayGroupResp get_dns_gateway_group(group_id)



Get a dns gateway group

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
api_instance = xms_client.DnsGatewayGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | dns gateway group id

try:
    api_response = api_instance.get_dns_gateway_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsGatewayGroupsApi->get_dns_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| dns gateway group id | 

### Return type

[**DNSGatewayGroupResp**](DNSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dns_gateway_groups**
> DNSGatewayGroupsResp list_dns_gateway_groups(limit=limit, offset=offset, cluster_id=cluster_id)



List dns gateway groups

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
api_instance = xms_client.DnsGatewayGroupsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_dns_gateway_groups(limit=limit, offset=offset, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsGatewayGroupsApi->list_dns_gateway_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**DNSGatewayGroupsResp**](DNSGatewayGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_dns_gateway_group**
> DNSGatewayGroupResp redeploy_dns_gateway_group(group_id)



Redeploy a DNS gateway group

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
api_instance = xms_client.DnsGatewayGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | dns gateway group id

try:
    api_response = api_instance.redeploy_dns_gateway_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsGatewayGroupsApi->redeploy_dns_gateway_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| dns gateway group id | 

### Return type

[**DNSGatewayGroupResp**](DNSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dns_gateway_from_group**
> DNSGatewayGroupResp remove_dns_gateway_from_group(group_id, body, force=force)



Remove DNS gateways from group.

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
api_instance = xms_client.DnsGatewayGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | dns gateway group id
body = xms_client.DNSGatewayGroupRemoveGatewayReq() # DNSGatewayGroupRemoveGatewayReq | DNS gateway info
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.remove_dns_gateway_from_group(group_id, body, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsGatewayGroupsApi->remove_dns_gateway_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| dns gateway group id | 
 **body** | [**DNSGatewayGroupRemoveGatewayReq**](DNSGatewayGroupRemoveGatewayReq.md)| DNS gateway info | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**DNSGatewayGroupResp**](DNSGatewayGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

