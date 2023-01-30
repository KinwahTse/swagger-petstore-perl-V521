# xms_client.CloudInstancesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cloud_instance**](CloudInstancesApi.md#get_cloud_instance) | **GET** /cloud-instances/{cloud_instance_id} | 
[**get_cloud_instance_samples**](CloudInstancesApi.md#get_cloud_instance_samples) | **GET** /cloud-instances/{cloud_instance_id}/samples | 
[**list_cloud_instances**](CloudInstancesApi.md#list_cloud_instances) | **GET** /cloud-instances/ | 


# **get_cloud_instance**
> CloudInstanceResp get_cloud_instance(cloud_instance_id)



Get a cloud instance

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
api_instance = xms_client.CloudInstancesApi(xms_client.ApiClient(configuration))
cloud_instance_id = 789 # int | cloud instance id

try:
    api_response = api_instance.get_cloud_instance(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudInstancesApi->get_cloud_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **int**| cloud instance id | 

### Return type

[**CloudInstanceResp**](CloudInstanceResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_instance_samples**
> CloudInstanceSamplesResp get_cloud_instance_samples(cloud_instance_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a cloud instance's Samples

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
api_instance = xms_client.CloudInstancesApi(xms_client.ApiClient(configuration))
cloud_instance_id = 789 # int | cloud instance id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_cloud_instance_samples(cloud_instance_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudInstancesApi->get_cloud_instance_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **int**| cloud instance id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**CloudInstanceSamplesResp**](CloudInstanceSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_instances**
> CloudInstancesResp list_cloud_instances(limit=limit, offset=offset, cloud_platform_id=cloud_platform_id, cloud_platform_type=cloud_platform_type, cloud_platform_name=cloud_platform_name)



List cloud instances

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
api_instance = xms_client.CloudInstancesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cloud_platform_id = 789 # int | cloud platform id (optional)
cloud_platform_type = 'cloud_platform_type_example' # str | cloud platform type (optional)
cloud_platform_name = 'cloud_platform_name_example' # str | cloud platform name (optional)

try:
    api_response = api_instance.list_cloud_instances(limit=limit, offset=offset, cloud_platform_id=cloud_platform_id, cloud_platform_type=cloud_platform_type, cloud_platform_name=cloud_platform_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudInstancesApi->list_cloud_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cloud_platform_id** | **int**| cloud platform id | [optional] 
 **cloud_platform_type** | **str**| cloud platform type | [optional] 
 **cloud_platform_name** | **str**| cloud platform name | [optional] 

### Return type

[**CloudInstancesResp**](CloudInstancesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

