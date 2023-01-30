# xms_client.OsOriginPullRulesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_os_origin_pull_rule**](OsOriginPullRulesApi.md#create_os_origin_pull_rule) | **POST** /os-origin-pull-rules/ | 
[**delete_os_origin_pull_rule**](OsOriginPullRulesApi.md#delete_os_origin_pull_rule) | **DELETE** /os-origin-pull-rules/{rule_id} | 
[**get_os_origin_pull_rule**](OsOriginPullRulesApi.md#get_os_origin_pull_rule) | **GET** /os-origin-pull-rules/{rule_id} | 
[**list_os_origin_pull_rules**](OsOriginPullRulesApi.md#list_os_origin_pull_rules) | **GET** /os-origin-pull-rules/ | 
[**update_os_origin_pull_rule**](OsOriginPullRulesApi.md#update_os_origin_pull_rule) | **PATCH** /os-origin-pull-rules/{rule_id} | 


# **create_os_origin_pull_rule**
> OSOriginPullRuleResp create_os_origin_pull_rule(body, cluster_id=cluster_id)



Create os origin pull rule

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
api_instance = xms_client.OsOriginPullRulesApi(xms_client.ApiClient(configuration))
body = xms_client.OSOriginPullRuleCreateReq() # OSOriginPullRuleCreateReq | origin pull rule info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_os_origin_pull_rule(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsOriginPullRulesApi->create_os_origin_pull_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OSOriginPullRuleCreateReq**](OSOriginPullRuleCreateReq.md)| origin pull rule info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**OSOriginPullRuleResp**](OSOriginPullRuleResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_os_origin_pull_rule**
> OSOriginPullRuleResp delete_os_origin_pull_rule(rule_id)



Delete an os origin pull rule

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
api_instance = xms_client.OsOriginPullRulesApi(xms_client.ApiClient(configuration))
rule_id = 789 # int | origin pull rule id

try:
    api_response = api_instance.delete_os_origin_pull_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsOriginPullRulesApi->delete_os_origin_pull_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| origin pull rule id | 

### Return type

[**OSOriginPullRuleResp**](OSOriginPullRuleResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_origin_pull_rule**
> OSOriginPullRuleResp get_os_origin_pull_rule(rule_id)



Get an os origin pull rule

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
api_instance = xms_client.OsOriginPullRulesApi(xms_client.ApiClient(configuration))
rule_id = 789 # int | rule id

try:
    api_response = api_instance.get_os_origin_pull_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsOriginPullRulesApi->get_os_origin_pull_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| rule id | 

### Return type

[**OSOriginPullRuleResp**](OSOriginPullRuleResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_os_origin_pull_rules**
> OSOriginPullRulesResp list_os_origin_pull_rules(cluster_id=cluster_id, limit=limit, offset=offset, bucket_id=bucket_id, s3_lb_group_id=s3_lb_group_id)



List os origin pull rules

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
api_instance = xms_client.OsOriginPullRulesApi(xms_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | cluster id (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
bucket_id = 789 # int | bucket id (optional)
s3_lb_group_id = 789 # int | s3 lb group id (optional)

try:
    api_response = api_instance.list_os_origin_pull_rules(cluster_id=cluster_id, limit=limit, offset=offset, bucket_id=bucket_id, s3_lb_group_id=s3_lb_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsOriginPullRulesApi->list_os_origin_pull_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| cluster id | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **bucket_id** | **int**| bucket id | [optional] 
 **s3_lb_group_id** | **int**| s3 lb group id | [optional] 

### Return type

[**OSOriginPullRulesResp**](OSOriginPullRulesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_os_origin_pull_rule**
> OSOriginPullRuleResp update_os_origin_pull_rule(rule_id, body)



update os origin pull rule

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
api_instance = xms_client.OsOriginPullRulesApi(xms_client.ApiClient(configuration))
rule_id = 789 # int | origin pull rule id
body = xms_client.OSOriginPullRuleUpdateReq() # OSOriginPullRuleUpdateReq | origin pull rule info

try:
    api_response = api_instance.update_os_origin_pull_rule(rule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsOriginPullRulesApi->update_os_origin_pull_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**| origin pull rule id | 
 **body** | [**OSOriginPullRuleUpdateReq**](OSOriginPullRuleUpdateReq.md)| origin pull rule info | 

### Return type

[**OSOriginPullRuleResp**](OSOriginPullRuleResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

