# xms_client.DfsQuotasApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dfs_quota**](DfsQuotasApi.md#create_dfs_quota) | **POST** /dfs-quotas/ | 
[**delete_dfs_quota**](DfsQuotasApi.md#delete_dfs_quota) | **DELETE** /dfs-quotas/{dfs_quota_id} | 
[**dfs_quota_overview**](DfsQuotasApi.md#dfs_quota_overview) | **GET** /dfs-quotas/overview | 
[**get_dfs_quota**](DfsQuotasApi.md#get_dfs_quota) | **GET** /dfs-quotas/{dfs_quota_id} | 
[**get_dfs_quota_predictions**](DfsQuotasApi.md#get_dfs_quota_predictions) | **GET** /dfs-quotas/{dfs_quota_id}/predictions | 
[**get_dfs_quota_samples**](DfsQuotasApi.md#get_dfs_quota_samples) | **GET** /dfs-quotas/{dfs_quota_id}/samples | 
[**list_dfs_quotas**](DfsQuotasApi.md#list_dfs_quotas) | **GET** /dfs-quotas/ | 
[**path_validator**](DfsQuotasApi.md#path_validator) | **GET** /dfs-quotas/path-validator | 
[**update_dfs_quota**](DfsQuotasApi.md#update_dfs_quota) | **PATCH** /dfs-quotas/{dfs_quota_id} | 


# **create_dfs_quota**
> DfsQuotaResp create_dfs_quota(body, allow_path_create=allow_path_create)



Create dfs quota

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
api_instance = xms_client.DfsQuotasApi(xms_client.ApiClient(configuration))
body = xms_client.DfsQuotaCreateReq() # DfsQuotaCreateReq | quota info
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.create_dfs_quota(body, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsQuotasApi->create_dfs_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsQuotaCreateReq**](DfsQuotaCreateReq.md)| quota info | 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DfsQuotaResp**](DfsQuotaResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_quota**
> DfsQuotaResp delete_dfs_quota(dfs_quota_id)



delete dfs quota

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
api_instance = xms_client.DfsQuotasApi(xms_client.ApiClient(configuration))
dfs_quota_id = 789 # int | dfs quota id

try:
    api_response = api_instance.delete_dfs_quota(dfs_quota_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsQuotasApi->delete_dfs_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_quota_id** | **int**| dfs quota id | 

### Return type

[**DfsQuotaResp**](DfsQuotaResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dfs_quota_overview**
> DfsQuotaOverviewResp dfs_quota_overview()



dfs quota overview about type and status

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
api_instance = xms_client.DfsQuotasApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.dfs_quota_overview()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsQuotasApi->dfs_quota_overview: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DfsQuotaOverviewResp**](DfsQuotaOverviewResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_quota**
> DfsQuotaResp get_dfs_quota(dfs_quota_id)



Get dfs quota

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
api_instance = xms_client.DfsQuotasApi(xms_client.ApiClient(configuration))
dfs_quota_id = 789 # int | dfs quota id

try:
    api_response = api_instance.get_dfs_quota(dfs_quota_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsQuotasApi->get_dfs_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_quota_id** | **int**| dfs quota id | 

### Return type

[**DfsQuotaResp**](DfsQuotaResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_quota_predictions**
> DfsQuotaPredictionsResp get_dfs_quota_predictions(dfs_quota_id)



get a quota's prediction

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
api_instance = xms_client.DfsQuotasApi(xms_client.ApiClient(configuration))
dfs_quota_id = 789 # int | dfs quota id

try:
    api_response = api_instance.get_dfs_quota_predictions(dfs_quota_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsQuotasApi->get_dfs_quota_predictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_quota_id** | **int**| dfs quota id | 

### Return type

[**DfsQuotaPredictionsResp**](DfsQuotaPredictionsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_quota_samples**
> DfsQuotaSamplesResp get_dfs_quota_samples(dfs_quota_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a dfs quota's samples

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
api_instance = xms_client.DfsQuotasApi(xms_client.ApiClient(configuration))
dfs_quota_id = 789 # int | dfs quota id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_dfs_quota_samples(dfs_quota_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsQuotasApi->get_dfs_quota_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_quota_id** | **int**| dfs quota id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**DfsQuotaSamplesResp**](DfsQuotaSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_quotas**
> DfsQuotasResp list_dfs_quotas(path=path, type=type, domain_user_name=domain_user_name, domain_user_group_name=domain_user_group_name, limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id)



List dfs quotas

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
api_instance = xms_client.DfsQuotasApi(xms_client.ApiClient(configuration))
path = 'path_example' # str | dfs quota path (optional)
type = 'type_example' # str | dfs quota type (optional)
domain_user_name = 'domain_user_name_example' # str | dfs quota domain user name (optional)
domain_user_group_name = 'domain_user_group_name_example' # str | dfs quota domain user group name (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_dfs_quotas(path=path, type=type, domain_user_name=domain_user_name, domain_user_group_name=domain_user_group_name, limit=limit, offset=offset, q=q, sort=sort, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsQuotasApi->list_dfs_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| dfs quota path | [optional] 
 **type** | **str**| dfs quota type | [optional] 
 **domain_user_name** | **str**| dfs quota domain user name | [optional] 
 **domain_user_group_name** | **str**| dfs quota domain user group name | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**DfsQuotasResp**](DfsQuotasResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_validator**
> DfsQuotaPathValidateResp path_validator(dfs_rootfs_id, path)



validate a path for dfs quota

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
api_instance = xms_client.DfsQuotasApi(xms_client.ApiClient(configuration))
dfs_rootfs_id = 789 # int | dfs rootfs id
path = 'path_example' # str | dfs quota path

try:
    api_response = api_instance.path_validator(dfs_rootfs_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsQuotasApi->path_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_rootfs_id** | **int**| dfs rootfs id | 
 **path** | **str**| dfs quota path | 

### Return type

[**DfsQuotaPathValidateResp**](DfsQuotaPathValidateResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_quota**
> DfsQuotaResp update_dfs_quota(dfs_quota_id, body)



Update dfs quota

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
api_instance = xms_client.DfsQuotasApi(xms_client.ApiClient(configuration))
dfs_quota_id = 789 # int | quota id
body = xms_client.DfsQuotaUpdateReq() # DfsQuotaUpdateReq | dfs quota info

try:
    api_response = api_instance.update_dfs_quota(dfs_quota_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsQuotasApi->update_dfs_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_quota_id** | **int**| quota id | 
 **body** | [**DfsQuotaUpdateReq**](DfsQuotaUpdateReq.md)| dfs quota info | 

### Return type

[**DfsQuotaResp**](DfsQuotaResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

