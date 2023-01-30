# xms_client.HostsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_host**](HostsApi.md#create_host) | **POST** /hosts/ | 
[**delete_host**](HostsApi.md#delete_host) | **DELETE** /hosts/{host_id} | 
[**get_host**](HostsApi.md#get_host) | **GET** /hosts/{host_id} | 
[**get_host_samples**](HostsApi.md#get_host_samples) | **GET** /hosts/{host_id}/samples | 
[**list_hosts**](HostsApi.md#list_hosts) | **GET** /hosts/ | 
[**maintain_host**](HostsApi.md#maintain_host) | **POST** /hosts/{host_id}:maintain | 
[**unmaintain_host**](HostsApi.md#unmaintain_host) | **POST** /hosts/{host_id}:unmaintain | 
[**update_host**](HostsApi.md#update_host) | **PATCH** /hosts/{host_id} | 


# **create_host**
> HostResp create_host(body)



check env and install packages

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
api_instance = xms_client.HostsApi(xms_client.ApiClient(configuration))
body = xms_client.HostCreateReq() # HostCreateReq | host info

try:
    api_response = api_instance.create_host(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->create_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostCreateReq**](HostCreateReq.md)| host info | 

### Return type

[**HostResp**](HostResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_host**
> HostResp delete_host(host_id, force=force)



delete host

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
api_instance = xms_client.HostsApi(xms_client.ApiClient(configuration))
host_id = 789 # int | host id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_host(host_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->delete_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **int**| host id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**HostResp**](HostResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host**
> HostResp get_host(host_id)



get a host info

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
api_instance = xms_client.HostsApi(xms_client.ApiClient(configuration))
host_id = 789 # int | the host id

try:
    api_response = api_instance.get_host(host_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->get_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **int**| the host id | 

### Return type

[**HostResp**](HostResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_samples**
> HostSamplesResp get_host_samples(host_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a host's samples

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
api_instance = xms_client.HostsApi(xms_client.ApiClient(configuration))
host_id = 789 # int | host id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_host_samples(host_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->get_host_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **int**| host id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**HostSamplesResp**](HostSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hosts**
> HostsResp list_hosts(limit=limit, offset=offset, protection_domain_id=protection_domain_id, cluster_id=cluster_id, hostname=hostname, type=type, role=role, fc_available=fc_available, replication_gateway_available=replication_gateway_available, fs_gateway_group_id=fs_gateway_group_id, fs_gateway_group_used=fs_gateway_group_used, q=q, sort=sort)



List hosts by fileter

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
api_instance = xms_client.HostsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
protection_domain_id = 789 # int | protection domain id (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
hostname = 'hostname_example' # str | host name (optional)
type = 'type_example' # str | if it existed, value should be xdcactive (optional)
role = 'role_example' # str | filter by host role (optional)
fc_available = true # bool | available host with fc port (optional)
replication_gateway_available = true # bool | available host for replication gateway (optional)
fs_gateway_group_id = 789 # int | file storage gateway group id (optional)
fs_gateway_group_used = true # bool | used in file storage gateway group (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_hosts(limit=limit, offset=offset, protection_domain_id=protection_domain_id, cluster_id=cluster_id, hostname=hostname, type=type, role=role, fc_available=fc_available, replication_gateway_available=replication_gateway_available, fs_gateway_group_id=fs_gateway_group_id, fs_gateway_group_used=fs_gateway_group_used, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->list_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **protection_domain_id** | **int**| protection domain id | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **hostname** | **str**| host name | [optional] 
 **type** | **str**| if it existed, value should be xdcactive | [optional] 
 **role** | **str**| filter by host role | [optional] 
 **fc_available** | **bool**| available host with fc port | [optional] 
 **replication_gateway_available** | **bool**| available host for replication gateway | [optional] 
 **fs_gateway_group_id** | **int**| file storage gateway group id | [optional] 
 **fs_gateway_group_used** | **bool**| used in file storage gateway group | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**HostsResp**](HostsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintain_host**
> HostResp maintain_host(host_id, force=force)



Put host in maintanence mode

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
api_instance = xms_client.HostsApi(xms_client.ApiClient(configuration))
host_id = 789 # int | host id
force = true # bool | force maintain (optional)

try:
    api_response = api_instance.maintain_host(host_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->maintain_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **int**| host id | 
 **force** | **bool**| force maintain | [optional] 

### Return type

[**HostResp**](HostResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmaintain_host**
> HostResp unmaintain_host(host_id)



Put host out of maintanence mode

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
api_instance = xms_client.HostsApi(xms_client.ApiClient(configuration))
host_id = 789 # int | host id

try:
    api_response = api_instance.unmaintain_host(host_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->unmaintain_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **int**| host id | 

### Return type

[**HostResp**](HostResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_host**
> HostResp update_host(host_id, body)



update host info

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
api_instance = xms_client.HostsApi(xms_client.ApiClient(configuration))
host_id = 789 # int | host id
body = xms_client.HostUpdateReq() # HostUpdateReq | host info

try:
    api_response = api_instance.update_host(host_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->update_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **int**| host id | 
 **body** | [**HostUpdateReq**](HostUpdateReq.md)| host info | 

### Return type

[**HostResp**](HostResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

