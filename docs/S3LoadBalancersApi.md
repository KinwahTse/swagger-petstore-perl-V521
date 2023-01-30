# xms_client.S3LoadBalancersApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_get_s3_load_balancer_samples**](S3LoadBalancersApi.md#batch_get_s3_load_balancer_samples) | **GET** /s3-load-balancers/samples | 
[**get_s3_load_balancer**](S3LoadBalancersApi.md#get_s3_load_balancer) | **GET** /s3-load-balancers/{load_balancer_id} | 
[**get_s3_load_balancer_samples**](S3LoadBalancersApi.md#get_s3_load_balancer_samples) | **GET** /s3-load-balancers/{s3_load_balancer_id}/samples | 
[**list_s3_load_balancers**](S3LoadBalancersApi.md#list_s3_load_balancers) | **GET** /s3-load-balancers/ | 


# **batch_get_s3_load_balancer_samples**
> MultiS3LoadBalancersSamplesResp batch_get_s3_load_balancer_samples()



Get samples of multiple s3 load balancers

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
api_instance = xms_client.S3LoadBalancersApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.batch_get_s3_load_balancer_samples()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancersApi->batch_get_s3_load_balancer_samples: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MultiS3LoadBalancersSamplesResp**](MultiS3LoadBalancersSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_load_balancer**
> S3LoadBalancerResp get_s3_load_balancer(load_balancer_id)



Get s3 load balancer

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
api_instance = xms_client.S3LoadBalancersApi(xms_client.ApiClient(configuration))
load_balancer_id = 789 # int | s3 load balancer id

try:
    api_response = api_instance.get_s3_load_balancer(load_balancer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancersApi->get_s3_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_balancer_id** | **int**| s3 load balancer id | 

### Return type

[**S3LoadBalancerResp**](S3LoadBalancerResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_load_balancer_samples**
> S3LoadBalancerSamplesResp get_s3_load_balancer_samples(s3_load_balancer_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a s3 load balancer's samples

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
api_instance = xms_client.S3LoadBalancersApi(xms_client.ApiClient(configuration))
s3_load_balancer_id = 789 # int | s3 load balancer id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_s3_load_balancer_samples(s3_load_balancer_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancersApi->get_s3_load_balancer_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_load_balancer_id** | **int**| s3 load balancer id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**S3LoadBalancerSamplesResp**](S3LoadBalancerSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_s3_load_balancers**
> S3LoadBalancersResp list_s3_load_balancers(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, group_id=group_id)



List s3 load balancers

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
api_instance = xms_client.S3LoadBalancersApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
group_id = 789 # int | s3 load balancer group id (optional)

try:
    api_response = api_instance.list_s3_load_balancers(limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S3LoadBalancersApi->list_s3_load_balancers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **group_id** | **int**| s3 load balancer group id | [optional] 

### Return type

[**S3LoadBalancersResp**](S3LoadBalancersResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

