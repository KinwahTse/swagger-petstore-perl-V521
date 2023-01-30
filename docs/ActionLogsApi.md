# xms_client.ActionLogsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_log**](ActionLogsApi.md#get_action_log) | **GET** /action-logs/{action_log_id} | 
[**list_action_logs**](ActionLogsApi.md#list_action_logs) | **GET** /action-logs/ | 


# **get_action_log**
> ActionLogResp get_action_log(action_log_id)



get a action log

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
api_instance = xms_client.ActionLogsApi(xms_client.ApiClient(configuration))
action_log_id = 789 # int | action log id

try:
    api_response = api_instance.get_action_log(action_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionLogsApi->get_action_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_log_id** | **int**| action log id | 

### Return type

[**ActionLogResp**](ActionLogResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_action_logs**
> ActionLogsResp list_action_logs(limit=limit, offset=offset, resource_type=resource_type, status=status, user_id=user_id, create_begin=create_begin, create_end=create_end, q=q, related_resource=related_resource, sort=sort)



List action logs

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
api_instance = xms_client.ActionLogsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
resource_type = 'resource_type_example' # str | resource type of action logs (optional)
status = 'status_example' # str | status of action logs (optional)
user_id = 789 # int | user id of action logs (optional)
create_begin = 'create_begin_example' # str | create begin timestamp (optional)
create_end = 'create_end_example' # str | create end timestamp (optional)
q = 'q_example' # str | query param of search (optional)
related_resource = 'related_resource_example' # str | related resource info of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_action_logs(limit=limit, offset=offset, resource_type=resource_type, status=status, user_id=user_id, create_begin=create_begin, create_end=create_end, q=q, related_resource=related_resource, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionLogsApi->list_action_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **resource_type** | **str**| resource type of action logs | [optional] 
 **status** | **str**| status of action logs | [optional] 
 **user_id** | **int**| user id of action logs | [optional] 
 **create_begin** | **str**| create begin timestamp | [optional] 
 **create_end** | **str**| create end timestamp | [optional] 
 **q** | **str**| query param of search | [optional] 
 **related_resource** | **str**| related resource info of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**ActionLogsResp**](ActionLogsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

