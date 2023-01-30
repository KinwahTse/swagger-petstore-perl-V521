# xms_client.DnsLoadBalancePoliciesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dns_load_balance_policies**](DnsLoadBalancePoliciesApi.md#list_dns_load_balance_policies) | **GET** /dns-load-balance-policies/ | 


# **list_dns_load_balance_policies**
> DNSLoadBalancePoliciesResp list_dns_load_balance_policies(limit=limit, offset=offset, resource_type=resource_type)



List dns load balance policies

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
api_instance = xms_client.DnsLoadBalancePoliciesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
resource_type = 'resource_type_example' # str | resource type (optional)

try:
    api_response = api_instance.list_dns_load_balance_policies(limit=limit, offset=offset, resource_type=resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsLoadBalancePoliciesApi->list_dns_load_balance_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **resource_type** | **str**| resource type | [optional] 

### Return type

[**DNSLoadBalancePoliciesResp**](DNSLoadBalancePoliciesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

