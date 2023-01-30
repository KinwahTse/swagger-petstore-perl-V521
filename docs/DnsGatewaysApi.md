# xms_client.DnsGatewaysApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dns_gateway**](DnsGatewaysApi.md#get_dns_gateway) | **GET** /dns-gateways/{gateway_id} | 
[**list_dns_gateways**](DnsGatewaysApi.md#list_dns_gateways) | **GET** /dns-gateways/ | 


# **get_dns_gateway**
> DNSGatewayResp get_dns_gateway(gateway_id)



Get a dns gateway

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
api_instance = xms_client.DnsGatewaysApi(xms_client.ApiClient(configuration))
gateway_id = 789 # int | dns gateway id

try:
    api_response = api_instance.get_dns_gateway(gateway_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsGatewaysApi->get_dns_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| dns gateway id | 

### Return type

[**DNSGatewayResp**](DNSGatewayResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dns_gateways**
> DNSGatewaysResp list_dns_gateways(limit=limit, offset=offset, dns_gateway_group_id=dns_gateway_group_id)



List dns gateway

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
api_instance = xms_client.DnsGatewaysApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
dns_gateway_group_id = 789 # int | dns_gateway_group id (optional)

try:
    api_response = api_instance.list_dns_gateways(limit=limit, offset=offset, dns_gateway_group_id=dns_gateway_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsGatewaysApi->list_dns_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **dns_gateway_group_id** | **int**| dns_gateway_group id | [optional] 

### Return type

[**DNSGatewaysResp**](DNSGatewaysResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

