# xms_client.DnsZonesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dns_zone**](DnsZonesApi.md#get_dns_zone) | **GET** /dns-zones/{zone_id} | 
[**list_dns_zones**](DnsZonesApi.md#list_dns_zones) | **GET** /dns-zones/ | 
[**update_dns_zone**](DnsZonesApi.md#update_dns_zone) | **PATCH** /dns-zones/{zone_id} | 


# **get_dns_zone**
> DNSZoneResp get_dns_zone(zone_id)



Get a dns zone

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
api_instance = xms_client.DnsZonesApi(xms_client.ApiClient(configuration))
zone_id = 789 # int | dns zone id

try:
    api_response = api_instance.get_dns_zone(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsZonesApi->get_dns_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| dns zone id | 

### Return type

[**DNSZoneResp**](DNSZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dns_zones**
> DNSZonesResp list_dns_zones(limit=limit, offset=offset, dns_gateway_group_id=dns_gateway_group_id)



List dns zones

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
api_instance = xms_client.DnsZonesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
dns_gateway_group_id = 789 # int | dns gateway group id (optional)

try:
    api_response = api_instance.list_dns_zones(limit=limit, offset=offset, dns_gateway_group_id=dns_gateway_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsZonesApi->list_dns_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **dns_gateway_group_id** | **int**| dns gateway group id | [optional] 

### Return type

[**DNSZonesResp**](DNSZonesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dns_zone**
> DNSZoneResp update_dns_zone(zone_id, dns_zone)



Update a dns zone

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
api_instance = xms_client.DnsZonesApi(xms_client.ApiClient(configuration))
zone_id = 789 # int | dns zone id
dns_zone = xms_client.DNSZoneUpdateReq() # DNSZoneUpdateReq | DNS zone info

try:
    api_response = api_instance.update_dns_zone(zone_id, dns_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsZonesApi->update_dns_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| dns zone id | 
 **dns_zone** | [**DNSZoneUpdateReq**](DNSZoneUpdateReq.md)| DNS zone info | 

### Return type

[**DNSZoneResp**](DNSZoneResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

