# xms_client.NetworkDiagnosesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_diagnosis**](NetworkDiagnosesApi.md#create_network_diagnosis) | **POST** /network-diagnoses/ | 
[**delete_network_diagnosis**](NetworkDiagnosesApi.md#delete_network_diagnosis) | **DELETE** /network-diagnoses/{network_diagnosis_id} | 
[**get_network_diagnosis**](NetworkDiagnosesApi.md#get_network_diagnosis) | **GET** /network-diagnoses/{network_diagnosis_id} | 
[**list_network_diagnoses**](NetworkDiagnosesApi.md#list_network_diagnoses) | **GET** /network-diagnoses/ | 
[**stop_network_diagnosis**](NetworkDiagnosesApi.md#stop_network_diagnosis) | **POST** /network-diagnoses/{network_diagnosis_id}:stop | 


# **create_network_diagnosis**
> NetworkDiagnosisResp create_network_diagnosis(body)



Create network diagnosis

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
api_instance = xms_client.NetworkDiagnosesApi(xms_client.ApiClient(configuration))
body = xms_client.NetworkDiagnosisCreateReq() # NetworkDiagnosisCreateReq | network diagnosis info

try:
    api_response = api_instance.create_network_diagnosis(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiagnosesApi->create_network_diagnosis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkDiagnosisCreateReq**](NetworkDiagnosisCreateReq.md)| network diagnosis info | 

### Return type

[**NetworkDiagnosisResp**](NetworkDiagnosisResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_diagnosis**
> delete_network_diagnosis(network_diagnosis_id)



delete network diagnosis

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
api_instance = xms_client.NetworkDiagnosesApi(xms_client.ApiClient(configuration))
network_diagnosis_id = 789 # int | network diagnosis id

try:
    api_instance.delete_network_diagnosis(network_diagnosis_id)
except ApiException as e:
    print("Exception when calling NetworkDiagnosesApi->delete_network_diagnosis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_diagnosis_id** | **int**| network diagnosis id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_diagnosis**
> NetworkDiagnosisResp get_network_diagnosis(network_diagnosis_id)



Get network diagnosis

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
api_instance = xms_client.NetworkDiagnosesApi(xms_client.ApiClient(configuration))
network_diagnosis_id = 789 # int | network diagnosis id

try:
    api_response = api_instance.get_network_diagnosis(network_diagnosis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiagnosesApi->get_network_diagnosis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_diagnosis_id** | **int**| network diagnosis id | 

### Return type

[**NetworkDiagnosisResp**](NetworkDiagnosisResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_diagnoses**
> NetworkDiagnosesResp list_network_diagnoses(limit=limit, offset=offset)



List network diagnoses

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
api_instance = xms_client.NetworkDiagnosesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_network_diagnoses(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiagnosesApi->list_network_diagnoses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**NetworkDiagnosesResp**](NetworkDiagnosesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_network_diagnosis**
> NetworkDiagnosisResp stop_network_diagnosis(network_diagnosis_id)



stop network diagnosis

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
api_instance = xms_client.NetworkDiagnosesApi(xms_client.ApiClient(configuration))
network_diagnosis_id = 789 # int | network diagnosis id

try:
    api_response = api_instance.stop_network_diagnosis(network_diagnosis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkDiagnosesApi->stop_network_diagnosis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_diagnosis_id** | **int**| network diagnosis id | 

### Return type

[**NetworkDiagnosisResp**](NetworkDiagnosisResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

