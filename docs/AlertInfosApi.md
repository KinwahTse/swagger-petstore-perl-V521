# xms_client.AlertInfosApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_alert_info**](AlertInfosApi.md#ack_alert_info) | **POST** /alert-infos/{alert_info_id}:ack | 
[**count_alert_infos**](AlertInfosApi.md#count_alert_infos) | **GET** /alert-infos/stats | 
[**delete_alert_info**](AlertInfosApi.md#delete_alert_info) | **DELETE** /alert-infos/{alert_info_id} | 
[**get_alert_info**](AlertInfosApi.md#get_alert_info) | **GET** /alert-infos/{alert_info_id} | 
[**get_alert_infos_report**](AlertInfosApi.md#get_alert_infos_report) | **GET** /alert-infos/report | 
[**list_alert_infos**](AlertInfosApi.md#list_alert_infos) | **GET** /alert-infos/ | 
[**resolve_alert_info**](AlertInfosApi.md#resolve_alert_info) | **POST** /alert-infos/{alert_info_id}:resolve | 


# **ack_alert_info**
> ack_alert_info(alert_info_id)



set the acked status of alert info

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
api_instance = xms_client.AlertInfosApi(xms_client.ApiClient(configuration))
alert_info_id = 789 # int | the id of alert info

try:
    api_instance.ack_alert_info(alert_info_id)
except ApiException as e:
    print("Exception when calling AlertInfosApi->ack_alert_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_info_id** | **int**| the id of alert info | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_alert_infos**
> AlertStatsResp count_alert_infos(acked=acked, resolved=resolved, resource_type=resource_type, resource_id=resource_id)



count all alert infos

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
api_instance = xms_client.AlertInfosApi(xms_client.ApiClient(configuration))
acked = true # bool | acked of alert info (optional)
resolved = true # bool | resolved or not of alert info (optional)
resource_type = 'resource_type_example' # str | resource type of alert info (optional)
resource_id = 789 # int | resource id of alert info (optional)

try:
    api_response = api_instance.count_alert_infos(acked=acked, resolved=resolved, resource_type=resource_type, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfosApi->count_alert_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acked** | **bool**| acked of alert info | [optional] 
 **resolved** | **bool**| resolved or not of alert info | [optional] 
 **resource_type** | **str**| resource type of alert info | [optional] 
 **resource_id** | **int**| resource id of alert info | [optional] 

### Return type

[**AlertStatsResp**](AlertStatsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_info**
> AlertInfoResp delete_alert_info(alert_info_id)



delete an alert info

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
api_instance = xms_client.AlertInfosApi(xms_client.ApiClient(configuration))
alert_info_id = 789 # int | the id of alert info

try:
    api_response = api_instance.delete_alert_info(alert_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfosApi->delete_alert_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_info_id** | **int**| the id of alert info | 

### Return type

[**AlertInfoResp**](AlertInfoResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_info**
> AlertInfoResp get_alert_info(alert_info_id)



get an alert info

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
api_instance = xms_client.AlertInfosApi(xms_client.ApiClient(configuration))
alert_info_id = 789 # int | alert info id

try:
    api_response = api_instance.get_alert_info(alert_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfosApi->get_alert_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_info_id** | **int**| alert info id | 

### Return type

[**AlertInfoResp**](AlertInfoResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_infos_report**
> get_alert_infos_report(level=level, resource_type=resource_type, resource_id=resource_id, create_after=create_after, acked=acked, resolved=resolved, group=group)



Get report of alert infos

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
api_instance = xms_client.AlertInfosApi(xms_client.ApiClient(configuration))
level = 'level_example' # str | level of alert info (optional)
resource_type = 'resource_type_example' # str | resource type of alert info (optional)
resource_id = 789 # int | resource id of alert info (optional)
create_after = 'create_after_example' # str | create_after timestamp of alert info (optional)
acked = true # bool | acked of alert info (optional)
resolved = true # bool | resolved or not of alert info (optional)
group = 'group_example' # str | group of alert info (optional)

try:
    api_instance.get_alert_infos_report(level=level, resource_type=resource_type, resource_id=resource_id, create_after=create_after, acked=acked, resolved=resolved, group=group)
except ApiException as e:
    print("Exception when calling AlertInfosApi->get_alert_infos_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| level of alert info | [optional] 
 **resource_type** | **str**| resource type of alert info | [optional] 
 **resource_id** | **int**| resource id of alert info | [optional] 
 **create_after** | **str**| create_after timestamp of alert info | [optional] 
 **acked** | **bool**| acked of alert info | [optional] 
 **resolved** | **bool**| resolved or not of alert info | [optional] 
 **group** | **str**| group of alert info | [optional] 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_infos**
> AlertInfosResp list_alert_infos(q_must=q_must, q=q, related_resource=related_resource, sort=sort, limit=limit, offset=offset, level=level, resource_type=resource_type, resource_id=resource_id, create_after=create_after, acked=acked, resolved=resolved, group=group)



List all alert infos

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
api_instance = xms_client.AlertInfosApi(xms_client.ApiClient(configuration))
q_must = 'q_must_example' # str | must query param of search (optional)
q = 'q_example' # str | should query param of search (optional)
related_resource = 'related_resource_example' # str | should query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
level = 'level_example' # str | level of alert info (optional)
resource_type = 'resource_type_example' # str | resource type of alert info (optional)
resource_id = 789 # int | resource id of alert info (optional)
create_after = 'create_after_example' # str | create_after timestamp of alert info (optional)
acked = true # bool | acked of alert info (optional)
resolved = true # bool | resolved or not of alert info (optional)
group = 'group_example' # str | group of alert info (optional)

try:
    api_response = api_instance.list_alert_infos(q_must=q_must, q=q, related_resource=related_resource, sort=sort, limit=limit, offset=offset, level=level, resource_type=resource_type, resource_id=resource_id, create_after=create_after, acked=acked, resolved=resolved, group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfosApi->list_alert_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q_must** | **str**| must query param of search | [optional] 
 **q** | **str**| should query param of search | [optional] 
 **related_resource** | **str**| should query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **level** | **str**| level of alert info | [optional] 
 **resource_type** | **str**| resource type of alert info | [optional] 
 **resource_id** | **int**| resource id of alert info | [optional] 
 **create_after** | **str**| create_after timestamp of alert info | [optional] 
 **acked** | **bool**| acked of alert info | [optional] 
 **resolved** | **bool**| resolved or not of alert info | [optional] 
 **group** | **str**| group of alert info | [optional] 

### Return type

[**AlertInfosResp**](AlertInfosResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_alert_info**
> resolve_alert_info(alert_info_id)



set the resolved status of alert info

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
api_instance = xms_client.AlertInfosApi(xms_client.ApiClient(configuration))
alert_info_id = 789 # int | the id of alert info

try:
    api_instance.resolve_alert_info(alert_info_id)
except ApiException as e:
    print("Exception when calling AlertInfosApi->resolve_alert_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_info_id** | **int**| the id of alert info | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

