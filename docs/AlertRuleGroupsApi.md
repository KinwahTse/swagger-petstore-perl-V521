# xms_client.AlertRuleGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_rule_group_detail**](AlertRuleGroupsApi.md#get_alert_rule_group_detail) | **GET** /alert-rule-groups/{id}/detail | 
[**list_alert_rule_groups**](AlertRuleGroupsApi.md#list_alert_rule_groups) | **GET** /alert-rule-groups/ | 
[**update_alert_rule_group_detail**](AlertRuleGroupsApi.md#update_alert_rule_group_detail) | **PATCH** /alert-rule-groups/{id}/detail | 


# **get_alert_rule_group_detail**
> AlertRuleGroupDetailResp get_alert_rule_group_detail(id)



Get alert rule group detail

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
api_instance = xms_client.AlertRuleGroupsApi(xms_client.ApiClient(configuration))
id = 789 # int | alert rule group id

try:
    api_response = api_instance.get_alert_rule_group_detail(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRuleGroupsApi->get_alert_rule_group_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| alert rule group id | 

### Return type

[**AlertRuleGroupDetailResp**](AlertRuleGroupDetailResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_rule_groups**
> AlertRuleGroupsResp list_alert_rule_groups(limit=limit, offset=offset, resource_type=resource_type, name=name, level=level, enabled=enabled)



List alert rule groups

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
api_instance = xms_client.AlertRuleGroupsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
resource_type = 'resource_type_example' # str | resource type of alert rule group (optional)
name = 'name_example' # str | name of alert rule group (optional)
level = 'level_example' # str | level of alert rule group (optional)
enabled = true # bool | enabled or not (optional)

try:
    api_response = api_instance.list_alert_rule_groups(limit=limit, offset=offset, resource_type=resource_type, name=name, level=level, enabled=enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRuleGroupsApi->list_alert_rule_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **resource_type** | **str**| resource type of alert rule group | [optional] 
 **name** | **str**| name of alert rule group | [optional] 
 **level** | **str**| level of alert rule group | [optional] 
 **enabled** | **bool**| enabled or not | [optional] 

### Return type

[**AlertRuleGroupsResp**](AlertRuleGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_rule_group_detail**
> AlertRuleGroupDetailResp update_alert_rule_group_detail(id, body, restore=restore)



set alert rule group

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
api_instance = xms_client.AlertRuleGroupsApi(xms_client.ApiClient(configuration))
id = 789 # int | alert rule group id
body = xms_client.AlertRuleGroupDetailUpdateReq() # AlertRuleGroupDetailUpdateReq | alert rule group detail
restore = true # bool | restore default setup (optional)

try:
    api_response = api_instance.update_alert_rule_group_detail(id, body, restore=restore)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertRuleGroupsApi->update_alert_rule_group_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| alert rule group id | 
 **body** | [**AlertRuleGroupDetailUpdateReq**](AlertRuleGroupDetailUpdateReq.md)| alert rule group detail | 
 **restore** | **bool**| restore default setup | [optional] 

### Return type

[**AlertRuleGroupDetailResp**](AlertRuleGroupDetailResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

