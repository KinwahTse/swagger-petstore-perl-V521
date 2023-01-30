# xms_client.OsSamplesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_os_samples**](OsSamplesApi.md#get_os_samples) | **GET** /os-samples/ | 
[**get_os_samples_by_bucket_name**](OsSamplesApi.md#get_os_samples_by_bucket_name) | **GET** /os-samples/{user_name}/{bucket_name} | 
[**get_os_samples_by_user_name**](OsSamplesApi.md#get_os_samples_by_user_name) | **GET** /os-samples/{user_name} | 


# **get_os_samples**
> OSSampleResp get_os_samples(time=time, cluster_id=cluster_id)



Get os samples

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
api_instance = xms_client.OsSamplesApi(xms_client.ApiClient(configuration))
time = 'time_example' # str | query time(url encode RFC3339) (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.get_os_samples(time=time, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSamplesApi->get_os_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time** | **str**| query time(url encode RFC3339) | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSSampleResp**](OSSampleResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_samples_by_bucket_name**
> OSSampleResp get_os_samples_by_bucket_name(user_name, bucket_name, time=time, cluster_id=cluster_id)



get os samples by os bucket name

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
api_instance = xms_client.OsSamplesApi(xms_client.ApiClient(configuration))
user_name = 'user_name_example' # str | os user name
bucket_name = 'bucket_name_example' # str | os bucket name
time = 'time_example' # str | query time(url encode RFC3339) (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.get_os_samples_by_bucket_name(user_name, bucket_name, time=time, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSamplesApi->get_os_samples_by_bucket_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| os user name | 
 **bucket_name** | **str**| os bucket name | 
 **time** | **str**| query time(url encode RFC3339) | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSSampleResp**](OSSampleResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_samples_by_user_name**
> OSSampleResp get_os_samples_by_user_name(user_name, time=time, cluster_id=cluster_id)



Get os samples by user name

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
api_instance = xms_client.OsSamplesApi(xms_client.ApiClient(configuration))
user_name = 'user_name_example' # str | os user name
time = 'time_example' # str | query time(url encode RFC3339) (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.get_os_samples_by_user_name(user_name, time=time, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsSamplesApi->get_os_samples_by_user_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| os user name | 
 **time** | **str**| query time(url encode RFC3339) | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSSampleResp**](OSSampleResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

