# xms_client.OsdGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_osds_to_osd_group**](OsdGroupsApi.md#add_osds_to_osd_group) | **POST** /osd-groups/{group_id}:add-osds | 
[**disable_device_type_check**](OsdGroupsApi.md#disable_device_type_check) | **POST** /osd-groups/{group_id}:disable-device-type-check | 
[**enable_device_type_check**](OsdGroupsApi.md#enable_device_type_check) | **POST** /osd-groups/{group_id}:enable-device-type-check | 
[**get_osd_group**](OsdGroupsApi.md#get_osd_group) | **GET** /osd-groups/{group_id} | 
[**get_osd_group_samples**](OsdGroupsApi.md#get_osd_group_samples) | **GET** /osd-groups/{group_id}/samples | 
[**list_osd_groups**](OsdGroupsApi.md#list_osd_groups) | **GET** /osd-groups/ | 
[**remove_osds_from_osd_group**](OsdGroupsApi.md#remove_osds_from_osd_group) | **POST** /osd-groups/{group_id}:remove-osds | 
[**reweight_osd_group**](OsdGroupsApi.md#reweight_osd_group) | **POST** /osd-groups/{group_id}:reweight | 
[**set_osd_full_ratio**](OsdGroupsApi.md#set_osd_full_ratio) | **POST** /osd-groups/{group_id}:set-osd-full-ratio | 
[**set_osd_group_qos**](OsdGroupsApi.md#set_osd_group_qos) | **POST** /osd-groups/{group_id}:set-qos | 


# **add_osds_to_osd_group**
> OsdGroupResp add_osds_to_osd_group(group_id, body)



Add osds to osd grouop

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
api_instance = xms_client.OsdGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | osd group id
body = xms_client.OsdGroupOsdsUpdateReq() # OsdGroupOsdsUpdateReq | osd ids

try:
    api_response = api_instance.add_osds_to_osd_group(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdGroupsApi->add_osds_to_osd_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| osd group id | 
 **body** | [**OsdGroupOsdsUpdateReq**](OsdGroupOsdsUpdateReq.md)| osd ids | 

### Return type

[**OsdGroupResp**](OsdGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_device_type_check**
> OsdGroupResp disable_device_type_check(group_id)



Disable device type check when add osd

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
api_instance = xms_client.OsdGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | osd group id

try:
    api_response = api_instance.disable_device_type_check(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdGroupsApi->disable_device_type_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| osd group id | 

### Return type

[**OsdGroupResp**](OsdGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_device_type_check**
> OsdGroupResp enable_device_type_check(group_id)



Enable device type check when add osd

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
api_instance = xms_client.OsdGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | osd group id

try:
    api_response = api_instance.enable_device_type_check(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdGroupsApi->enable_device_type_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| osd group id | 

### Return type

[**OsdGroupResp**](OsdGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_osd_group**
> OsdGroupResp get_osd_group(group_id)



Get osd group

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
api_instance = xms_client.OsdGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | osd group id

try:
    api_response = api_instance.get_osd_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdGroupsApi->get_osd_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| osd group id | 

### Return type

[**OsdGroupResp**](OsdGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_osd_group_samples**
> OsdGroupSamplesResp get_osd_group_samples(group_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a osd group's samples

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
api_instance = xms_client.OsdGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | osd group id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_osd_group_samples(group_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdGroupsApi->get_osd_group_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| osd group id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**OsdGroupSamplesResp**](OsdGroupSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_osd_groups**
> OsdGroupsResp list_osd_groups(limit=limit, offset=offset, q=q, sort=sort)



List osd groups

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
api_instance = xms_client.OsdGroupsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_osd_groups(limit=limit, offset=offset, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdGroupsApi->list_osd_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**OsdGroupsResp**](OsdGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_osds_from_osd_group**
> OsdGroupResp remove_osds_from_osd_group(group_id, body)



Remove multiple osds from a osd group

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
api_instance = xms_client.OsdGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | osd group id
body = xms_client.OsdGroupOsdsUpdateReq() # OsdGroupOsdsUpdateReq | remove osd ids

try:
    api_response = api_instance.remove_osds_from_osd_group(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdGroupsApi->remove_osds_from_osd_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| osd group id | 
 **body** | [**OsdGroupOsdsUpdateReq**](OsdGroupOsdsUpdateReq.md)| remove osd ids | 

### Return type

[**OsdGroupResp**](OsdGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reweight_osd_group**
> OsdGroupResp reweight_osd_group(group_id)



Reweight pools of osd group

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
api_instance = xms_client.OsdGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | osd group id

try:
    api_response = api_instance.reweight_osd_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdGroupsApi->reweight_osd_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| osd group id | 

### Return type

[**OsdGroupResp**](OsdGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_osd_full_ratio**
> OsdGroupResp set_osd_full_ratio(group_id, body)



Set osd full ratio of osd group

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
api_instance = xms_client.OsdGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | osd group id
body = xms_client.SetOsdFullRatioReq() # SetOsdFullRatioReq | osds full ratio

try:
    api_response = api_instance.set_osd_full_ratio(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdGroupsApi->set_osd_full_ratio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| osd group id | 
 **body** | [**SetOsdFullRatioReq**](SetOsdFullRatioReq.md)| osds full ratio | 

### Return type

[**OsdGroupResp**](OsdGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_osd_group_qos**
> OsdGroupResp set_osd_group_qos(group_id, body)



Set osd group's qos

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
api_instance = xms_client.OsdGroupsApi(xms_client.ApiClient(configuration))
group_id = 789 # int | osd group id
body = xms_client.OsdGroupSetQosReq() # OsdGroupSetQosReq | qos info

try:
    api_response = api_instance.set_osd_group_qos(group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsdGroupsApi->set_osd_group_qos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| osd group id | 
 **body** | [**OsdGroupSetQosReq**](OsdGroupSetQosReq.md)| qos info | 

### Return type

[**OsdGroupResp**](OsdGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

