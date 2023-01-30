# xms_client.AlertInfoGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_alert_info_group**](AlertInfoGroupsApi.md#ack_alert_info_group) | **POST** /alert-info-groups/{alert_info_group_id}:ack | 
[**count_alert_info_groups**](AlertInfoGroupsApi.md#count_alert_info_groups) | **GET** /alert-info-groups/stats | 
[**delete_alert_info_group**](AlertInfoGroupsApi.md#delete_alert_info_group) | **DELETE** /alert-info-groups/{alert_info_group_id} | 
[**get_alert_info_group**](AlertInfoGroupsApi.md#get_alert_info_group) | **GET** /alert-info-groups/{group_id} | 
[**get_alert_info_groups_report**](AlertInfoGroupsApi.md#get_alert_info_groups_report) | **GET** /alert-info-groups/report | 
[**list_alert_info_groups**](AlertInfoGroupsApi.md#list_alert_info_groups) | **GET** /alert-info-groups/ | 
[**resolve_alert_info_group**](AlertInfoGroupsApi.md#resolve_alert_info_group) | **POST** /alert-info-groups/{alert_info_group_id}:resolve | 


# **ack_alert_info_group**
> AlertInfoGroupResp ack_alert_info_group(alert_info_group_id)



set the acked status of alert info group

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
api_instance = xms_client.AlertInfoGroupsApi(xms_client.ApiClient(configuration))
alert_info_group_id = 789 # int | the id of alert info group

try:
    api_response = api_instance.ack_alert_info_group(alert_info_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfoGroupsApi->ack_alert_info_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_info_group_id** | **int**| the id of alert info group | 

### Return type

[**AlertInfoGroupResp**](AlertInfoGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_alert_info_groups**
> AlertStatsResp count_alert_info_groups(acked=acked, resolved=resolved, resource_type=resource_type, resource_id=resource_id, start_time=start_time, end_time=end_time)



count alert info groups with conditions

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
api_instance = xms_client.AlertInfoGroupsApi(xms_client.ApiClient(configuration))
acked = true # bool | acked of the most recently alert info in group (optional)
resolved = true # bool | resolved or not of the most recently alert info in group (optional)
resource_type = 'resource_type_example' # str | resource type of alert info group (optional)
resource_id = 789 # int | resource id of alert info group (optional)
start_time = 'start_time_example' # str | start time of create of alert info group (optional)
end_time = 'end_time_example' # str | end time of create of alert info group (optional)

try:
    api_response = api_instance.count_alert_info_groups(acked=acked, resolved=resolved, resource_type=resource_type, resource_id=resource_id, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfoGroupsApi->count_alert_info_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acked** | **bool**| acked of the most recently alert info in group | [optional] 
 **resolved** | **bool**| resolved or not of the most recently alert info in group | [optional] 
 **resource_type** | **str**| resource type of alert info group | [optional] 
 **resource_id** | **int**| resource id of alert info group | [optional] 
 **start_time** | **str**| start time of create of alert info group | [optional] 
 **end_time** | **str**| end time of create of alert info group | [optional] 

### Return type

[**AlertStatsResp**](AlertStatsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_info_group**
> AlertInfoGroupResp delete_alert_info_group(alert_info_group_id)



delete an alert info group

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
api_instance = xms_client.AlertInfoGroupsApi(xms_client.ApiClient(configuration))
alert_info_group_id = 789 # int | the id of alert info group

try:
    api_response = api_instance.delete_alert_info_group(alert_info_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfoGroupsApi->delete_alert_info_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_info_group_id** | **int**| the id of alert info group | 

### Return type

[**AlertInfoGroupResp**](AlertInfoGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_info_group**
> AlertInfoGroupResp get_alert_info_group(group_id)



get alert info group

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
api_instance = xms_client.AlertInfoGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | the id of alert info group

try:
    api_response = api_instance.get_alert_info_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfoGroupsApi->get_alert_info_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| the id of alert info group | 

### Return type

[**AlertInfoGroupResp**](AlertInfoGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_info_groups_report**
> get_alert_info_groups_report(level=level, resource_type=resource_type, create_after=create_after, acked=acked, resolved=resolved, group=group)



Get report of alert info groups

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
api_instance = xms_client.AlertInfoGroupsApi(xms_client.ApiClient(configuration))
level = 'level_example' # str | level of alert info group (optional)
resource_type = 'resource_type_example' # str | resource type of alert info group (optional)
create_after = 'create_after_example' # str | create_after timestamp of alert info group (optional)
acked = true # bool | acked of alert info (optional)
resolved = true # bool | resolved or not of alert info (optional)
group = 'group_example' # str | group of alert info (optional)

try:
    api_instance.get_alert_info_groups_report(level=level, resource_type=resource_type, create_after=create_after, acked=acked, resolved=resolved, group=group)
except ApiException as e:
    print("Exception when calling AlertInfoGroupsApi->get_alert_info_groups_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| level of alert info group | [optional] 
 **resource_type** | **str**| resource type of alert info group | [optional] 
 **create_after** | **str**| create_after timestamp of alert info group | [optional] 
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

# **list_alert_info_groups**
> AlertInfoGroupsResp list_alert_info_groups(q_must=q_must, q=q, related_resource=related_resource, sort=sort, limit=limit, offset=offset, level=level, resource_type=resource_type, resource_id=resource_id, create_after=create_after, create_before=create_before, acked=acked, resolved=resolved, group=group)



List all alert info groups

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
api_instance = xms_client.AlertInfoGroupsApi(xms_client.ApiClient(configuration))
q_must = 'q_must_example' # str | must query param of search (optional)
q = 'q_example' # str | should query param of search (optional)
related_resource = 'related_resource_example' # str | should query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
level = 'level_example' # str | level of alert info group (optional)
resource_type = 'resource_type_example' # str | resource type of alert info group (optional)
resource_id = 789 # int | resource id of alert info group (optional)
create_after = 'create_after_example' # str | create_after start time of alert info group (optional)
create_before = 'create_before_example' # str | create_before end time of alert info group (optional)
acked = true # bool | acked of alert info (optional)
resolved = true # bool | resolved or not of alert info (optional)
group = 'group_example' # str | group of alert info (optional)

try:
    api_response = api_instance.list_alert_info_groups(q_must=q_must, q=q, related_resource=related_resource, sort=sort, limit=limit, offset=offset, level=level, resource_type=resource_type, resource_id=resource_id, create_after=create_after, create_before=create_before, acked=acked, resolved=resolved, group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfoGroupsApi->list_alert_info_groups: %s\n" % e)
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
 **level** | **str**| level of alert info group | [optional] 
 **resource_type** | **str**| resource type of alert info group | [optional] 
 **resource_id** | **int**| resource id of alert info group | [optional] 
 **create_after** | **str**| create_after start time of alert info group | [optional] 
 **create_before** | **str**| create_before end time of alert info group | [optional] 
 **acked** | **bool**| acked of alert info | [optional] 
 **resolved** | **bool**| resolved or not of alert info | [optional] 
 **group** | **str**| group of alert info | [optional] 

### Return type

[**AlertInfoGroupsResp**](AlertInfoGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_alert_info_group**
> AlertInfoGroupResp resolve_alert_info_group(alert_info_group_id)



set the resolved status of alert info group

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
api_instance = xms_client.AlertInfoGroupsApi(xms_client.ApiClient(configuration))
alert_info_group_id = 789 # int | the id of alert info group

try:
    api_response = api_instance.resolve_alert_info_group(alert_info_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertInfoGroupsApi->resolve_alert_info_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_info_group_id** | **int**| the id of alert info group | 

### Return type

[**AlertInfoGroupResp**](AlertInfoGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

