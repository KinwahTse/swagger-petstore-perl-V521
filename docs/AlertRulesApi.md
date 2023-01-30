# xms_client.AlertRulesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_rule_resource_blacklist**](AlertRulesApi.md#create_alert_rule_resource_blacklist) | **POST** /alert-rules/{rule_id}/blacklist | 
[**delete_alert_rule**](AlertRulesApi.md#delete_alert_rule) | **DELETE** /alert-rules/{rule_id} | 
[**delete_alert_rule_resource_blacklist**](AlertRulesApi.md#delete_alert_rule_resource_blacklist) | **DELETE** /alert-rules/{rule_id}/blacklist | 
[**get_alert_rule**](AlertRulesApi.md#get_alert_rule) | **GET** /alert-rules/{rule_id} | 
[**get_alert_rule_schema**](AlertRulesApi.md#get_alert_rule_schema) | **GET** /alert-rules/schema | 
[**list_alert_rule_resource_blacklist**](AlertRulesApi.md#list_alert_rule_resource_blacklist) | **GET** /alert-rules/{rule_id}/blacklist | 
[**list_alert_rules**](AlertRulesApi.md#list_alert_rules) | **GET** /alert-rules/ | 
[**update_alert_rule**](AlertRulesApi.md#update_alert_rule) | **PATCH** /alert-rules/{rule_id} | 


# **create_alert_rule_resource_blacklist**
> AlertRuleResourceBlacklistResp create_alert_rule_resource_blacklist(rule_id, body)



create resource blacklist of alert rule

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
api_instance = xms_client.AlertRulesApi(xms_client.ApiClient(configuration))
rule_id = 789 # int | the id of alert rule
body = xms_client.UpdateAlertRuleResourceBlacklistReq() # UpdateAlertRuleResourceBlacklistReq | resource blacklist

try:
    api_response = api_instance.create_alert_rule_resource_blacklist(rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRulesApi->create_alert_rule_resource_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| the id of alert rule | 
 **body** | [**UpdateAlertRuleResourceBlacklistReq**](UpdateAlertRuleResourceBlacklistReq.md)| resource blacklist | 

### Return type

[**AlertRuleResourceBlacklistResp**](AlertRuleResourceBlacklistResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_rule**
> delete_alert_rule(rule_id)



delete alert rule

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
api_instance = xms_client.AlertRulesApi(xms_client.ApiClient(configuration))
rule_id = 789 # int | the id of alert rule

try:
    api_instance.delete_alert_rule(rule_id)
except ApiException as e:
    print("Exception when calling AlertRulesApi->delete_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| the id of alert rule | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_rule_resource_blacklist**
> delete_alert_rule_resource_blacklist(rule_id, body)



delete resource blacklist of alert rule

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
api_instance = xms_client.AlertRulesApi(xms_client.ApiClient(configuration))
rule_id = 789 # int | the id of alert rule
body = xms_client.UpdateAlertRuleResourceBlacklistReq() # UpdateAlertRuleResourceBlacklistReq | resource blacklist

try:
    api_instance.delete_alert_rule_resource_blacklist(rule_id, body)
except ApiException as e:
    print("Exception when calling AlertRulesApi->delete_alert_rule_resource_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| the id of alert rule | 
 **body** | [**UpdateAlertRuleResourceBlacklistReq**](UpdateAlertRuleResourceBlacklistReq.md)| resource blacklist | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rule**
> AlertRuleResp get_alert_rule(rule_id)



get alert rule

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
api_instance = xms_client.AlertRulesApi(xms_client.ApiClient(configuration))
rule_id = 789 # int | the id of alert rule

try:
    api_response = api_instance.get_alert_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRulesApi->get_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| the id of alert rule | 

### Return type

[**AlertRuleResp**](AlertRuleResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rule_schema**
> AlertRuleSchemaResp get_alert_rule_schema()



get alert rule schema

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
api_instance = xms_client.AlertRulesApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.get_alert_rule_schema()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRulesApi->get_alert_rule_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertRuleSchemaResp**](AlertRuleSchemaResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_rule_resource_blacklist**
> AlertRuleResourceBlacklistResp list_alert_rule_resource_blacklist(rule_id, blacklist, limit=limit, offset=offset)



List all blacklist of alert rule

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
api_instance = xms_client.AlertRulesApi(xms_client.ApiClient(configuration))
rule_id = 789 # int | the id of alert rule
blacklist = 'blacklist_example' # str | filter resource in blacklist or not
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_alert_rule_resource_blacklist(rule_id, blacklist, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRulesApi->list_alert_rule_resource_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| the id of alert rule | 
 **blacklist** | **str**| filter resource in blacklist or not | 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**AlertRuleResourceBlacklistResp**](AlertRuleResourceBlacklistResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_rules**
> AlertRulesResp list_alert_rules(limit=limit, offset=offset, alert_group_id=alert_group_id, resource_type=resource_type, group_name=group_name, level=level, enabled=enabled, q=q, sort=sort)



List all alert rules

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
api_instance = xms_client.AlertRulesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
alert_group_id = 789 # int | alert group id (optional)
resource_type = 'resource_type_example' # str | resource type of alert rule (optional)
group_name = 'group_name_example' # str | group name of alert rule (optional)
level = 'level_example' # str | level of alert rule (optional)
enabled = true # bool | enabled or not (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_alert_rules(limit=limit, offset=offset, alert_group_id=alert_group_id, resource_type=resource_type, group_name=group_name, level=level, enabled=enabled, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRulesApi->list_alert_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **alert_group_id** | **int**| alert group id | [optional] 
 **resource_type** | **str**| resource type of alert rule | [optional] 
 **group_name** | **str**| group name of alert rule | [optional] 
 **level** | **str**| level of alert rule | [optional] 
 **enabled** | **bool**| enabled or not | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**AlertRulesResp**](AlertRulesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_rule**
> AlertRuleResp update_alert_rule(rule_id, body)



set alert rule

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
api_instance = xms_client.AlertRulesApi(xms_client.ApiClient(configuration))
rule_id = 789 # int | the id of alert rule
body = xms_client.AlertRuleUpdateReq() # AlertRuleUpdateReq | alert rule

try:
    api_response = api_instance.update_alert_rule(rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRulesApi->update_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| the id of alert rule | 
 **body** | [**AlertRuleUpdateReq**](AlertRuleUpdateReq.md)| alert rule | 

### Return type

[**AlertRuleResp**](AlertRuleResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

