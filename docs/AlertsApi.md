# xms_client.AlertsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_alerts**](AlertsApi.md#count_alerts) | **GET** /alerts/stats | 
[**delete_alert**](AlertsApi.md#delete_alert) | **DELETE** /alerts/{alert_id} | 
[**delete_alerts**](AlertsApi.md#delete_alerts) | **DELETE** /alerts/ | 
[**do_alert**](AlertsApi.md#do_alert) | **PUT** /alerts/{alert_id} | 
[**do_alerts**](AlertsApi.md#do_alerts) | **PATCH** /alerts/ | 
[**get_alert**](AlertsApi.md#get_alert) | **GET** /alerts/{alert_id} | 
[**list_alerts**](AlertsApi.md#list_alerts) | **GET** /alerts/ | 
[**resolve_alert**](AlertsApi.md#resolve_alert) | **POST** /alerts/{alert_id}:resolve | 
[**resolve_alerts**](AlertsApi.md#resolve_alerts) | **POST** /alerts/:resolve | 


# **count_alerts**
> AlertStatsResp count_alerts(acked=acked, resolved=resolved, resource_type=resource_type, resource_id=resource_id)



count all alert

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
api_instance = xms_client.AlertsApi(xms_client.ApiClient(configuration))
acked = true # bool | acked of alert (optional)
resolved = true # bool | resolved or not of alert (optional)
resource_type = 'resource_type_example' # str | resource type of alert (optional)
resource_id = 789 # int | resource id of alert (optional)

try:
    api_response = api_instance.count_alerts(acked=acked, resolved=resolved, resource_type=resource_type, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->count_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acked** | **bool**| acked of alert | [optional] 
 **resolved** | **bool**| resolved or not of alert | [optional] 
 **resource_type** | **str**| resource type of alert | [optional] 
 **resource_id** | **int**| resource id of alert | [optional] 

### Return type

[**AlertStatsResp**](AlertStatsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert**
> delete_alert(alert_id)



Delete alert

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
api_instance = xms_client.AlertsApi(xms_client.ApiClient(configuration))
alert_id = 789 # int | alert id

try:
    api_instance.delete_alert(alert_id)
except ApiException as e:
    print("Exception when calling AlertsApi->delete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| alert id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alerts**
> delete_alerts(before=before)



delete alerts

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
api_instance = xms_client.AlertsApi(xms_client.ApiClient(configuration))
before = 'before_example' # str | create time of last alert (optional)

try:
    api_instance.delete_alerts(before=before)
except ApiException as e:
    print("Exception when calling AlertsApi->delete_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **str**| create time of last alert | [optional] 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_alert**
> AlertResp do_alert(alert_id, alert)



set the ack status of alert

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
api_instance = xms_client.AlertsApi(xms_client.ApiClient(configuration))
alert_id = 789 # int | the id of alert
alert = xms_client.AlertActionReq() # AlertActionReq | the alert action info

try:
    api_response = api_instance.do_alert(alert_id, alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->do_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| the id of alert | 
 **alert** | [**AlertActionReq**](AlertActionReq.md)| the alert action info | 

### Return type

[**AlertResp**](AlertResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_alerts**
> do_alerts(alert)



set the ack status of alerts

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
api_instance = xms_client.AlertsApi(xms_client.ApiClient(configuration))
alert = xms_client.AlertsActionReq() # AlertsActionReq | the alerts action info

try:
    api_instance.do_alerts(alert)
except ApiException as e:
    print("Exception when calling AlertsApi->do_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**AlertsActionReq**](AlertsActionReq.md)| the alerts action info | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> AlertResp get_alert(alert_id)



get a alert

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
api_instance = xms_client.AlertsApi(xms_client.ApiClient(configuration))
alert_id = 789 # int | alert id

try:
    api_response = api_instance.get_alert(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| alert id | 

### Return type

[**AlertResp**](AlertResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alerts**
> AlertsResp list_alerts(limit=limit, offset=offset, resource_type=resource_type, resource_id=resource_id, alert_type=alert_type, acked=acked, resolved=resolved, resolve_type=resolve_type, level=level, duration_begin=duration_begin, duration_end=duration_end, duration_limit=duration_limit, duration_offset=duration_offset, q=q, related_resource=related_resource, sort=sort)



List all alerts

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
api_instance = xms_client.AlertsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
resource_type = 'resource_type_example' # str | resource type of alert (optional)
resource_id = 789 # int | resource id of alert (optional)
alert_type = 'alert_type_example' # str | type of alert (optional)
acked = true # bool | acked of alert (optional)
resolved = true # bool | resolved or not of alert (optional)
resolve_type = 'resolve_type_example' # str | resolve type of alert (optional)
level = 'level_example' # str | level of alert (optional)
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
duration_limit = 789 # int | duration limit param (optional)
duration_offset = 789 # int | duration offset param (optional)
q = 'q_example' # str | query param of search (optional)
related_resource = 'related_resource_example' # str | related resource info of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_alerts(limit=limit, offset=offset, resource_type=resource_type, resource_id=resource_id, alert_type=alert_type, acked=acked, resolved=resolved, resolve_type=resolve_type, level=level, duration_begin=duration_begin, duration_end=duration_end, duration_limit=duration_limit, duration_offset=duration_offset, q=q, related_resource=related_resource, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->list_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **resource_type** | **str**| resource type of alert | [optional] 
 **resource_id** | **int**| resource id of alert | [optional] 
 **alert_type** | **str**| type of alert | [optional] 
 **acked** | **bool**| acked of alert | [optional] 
 **resolved** | **bool**| resolved or not of alert | [optional] 
 **resolve_type** | **str**| resolve type of alert | [optional] 
 **level** | **str**| level of alert | [optional] 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **duration_limit** | **int**| duration limit param | [optional] 
 **duration_offset** | **int**| duration offset param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **related_resource** | **str**| related resource info of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**AlertsResp**](AlertsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_alert**
> AlertResp resolve_alert(alert_id)



set the resolved status of alert

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
api_instance = xms_client.AlertsApi(xms_client.ApiClient(configuration))
alert_id = 789 # int | the id of alert

try:
    api_response = api_instance.resolve_alert(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->resolve_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**| the id of alert | 

### Return type

[**AlertResp**](AlertResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_alerts**
> resolve_alerts(alert)



resolve alerts of specific group or resource type

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
api_instance = xms_client.AlertsApi(xms_client.ApiClient(configuration))
alert = xms_client.AlertsResolveReq() # AlertsResolveReq | the alerts resolve info

try:
    api_instance.resolve_alerts(alert)
except ApiException as e:
    print("Exception when calling AlertsApi->resolve_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**AlertsResolveReq**](AlertsResolveReq.md)| the alerts resolve info | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

