# xms_client.DpBlockAsyncReplicationPairsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**async_failover_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#async_failover_dp_block_async_replication_pair) | **POST** /dp-block-async-replication-pairs/{pair_id}:async-failover | 
[**create_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#create_dp_block_async_replication_pair) | **POST** /dp-block-async-replication-pairs/ | 
[**delete_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#delete_dp_block_async_replication_pair) | **DELETE** /dp-block-async-replication-pairs/{pair_id} | 
[**failback_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#failback_dp_block_async_replication_pair) | **POST** /dp-block-async-replication-pairs/{pair_id}:failback | 
[**get_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#get_dp_block_async_replication_pair) | **GET** /dp-block-async-replication-pairs/{pair_id} | 
[**list_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#list_dp_block_async_replication_pair) | **GET** /dp-block-async-replication-pairs/ | 
[**pause_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#pause_dp_block_async_replication_pair) | **POST** /dp-block-async-replication-pairs/{pair_id}:pause | 
[**resume_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#resume_dp_block_async_replication_pair) | **POST** /dp-block-async-replication-pairs/{pair_id}:resume | 
[**rollback_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#rollback_dp_block_async_replication_pair) | **POST** /dp-block-async-replication-pairs/{pair_id}:rollback | 
[**sync_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#sync_dp_block_async_replication_pair) | **POST** /dp-block-async-replication-pairs/{pair_id}:sync | 
[**sync_failover_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#sync_failover_dp_block_async_replication_pair) | **POST** /dp-block-async-replication-pairs/{pair_id}:sync-failover | 
[**update_dp_block_async_replication_pair**](DpBlockAsyncReplicationPairsApi.md#update_dp_block_async_replication_pair) | **PATCH** /dp-block-async-replication-pairs/{pair_id} | 


# **async_failover_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp async_failover_dp_block_async_replication_pair(pair_id)



switch the roles of the pair

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.async_failover_dp_block_async_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->async_failover_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp create_dp_block_async_replication_pair(body)



Create dp block async replication pair

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
body = xms_client.DpBlockAsyncReplicationPairCreateReq() # DpBlockAsyncReplicationPairCreateReq | pair info

try:
    api_response = api_instance.create_dp_block_async_replication_pair(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->create_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpBlockAsyncReplicationPairCreateReq**](DpBlockAsyncReplicationPairCreateReq.md)| pair info | 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp delete_dp_block_async_replication_pair(pair_id, reserve_volume=reserve_volume)



Delete dp block async replication pair

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id
reserve_volume = true # bool | reserve replicated volume or not (optional)

try:
    api_response = api_instance.delete_dp_block_async_replication_pair(pair_id, reserve_volume=reserve_volume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->delete_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 
 **reserve_volume** | **bool**| reserve replicated volume or not | [optional] 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **failback_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp failback_dp_block_async_replication_pair(pair_id)



switch the roles of the pair to synced

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.failback_dp_block_async_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->failback_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp get_dp_block_async_replication_pair(pair_id)



Get dp block async replication pair

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.get_dp_block_async_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->get_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairsResp list_dp_block_async_replication_pair(block_volume_id=block_volume_id, dp_block_async_replication_policy_id=dp_block_async_replication_policy_id)



List dp block async replication pairs

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | show volume snapshot replication pairs of specific block volume (optional)
dp_block_async_replication_policy_id = 789 # int | show volume snapshot replication pairs of specific block async replication policy (optional)

try:
    api_response = api_instance.list_dp_block_async_replication_pair(block_volume_id=block_volume_id, dp_block_async_replication_policy_id=dp_block_async_replication_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->list_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| show volume snapshot replication pairs of specific block volume | [optional] 
 **dp_block_async_replication_policy_id** | **int**| show volume snapshot replication pairs of specific block async replication policy | [optional] 

### Return type

[**DpBlockAsyncReplicationPairsResp**](DpBlockAsyncReplicationPairsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp pause_dp_block_async_replication_pair(pair_id)



pause periodic sync

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.pause_dp_block_async_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->pause_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp resume_dp_block_async_replication_pair(pair_id)



resume periodic sync

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.resume_dp_block_async_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->resume_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp rollback_dp_block_async_replication_pair(pair_id)



rollback volume snapshot pair to previous snapshot

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.rollback_dp_block_async_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->rollback_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp sync_dp_block_async_replication_pair(pair_id)



sync pair

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.sync_dp_block_async_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->sync_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_failover_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp sync_failover_dp_block_async_replication_pair(pair_id)



switch the roles of the pair

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id

try:
    api_response = api_instance.sync_failover_dp_block_async_replication_pair(pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->sync_failover_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dp_block_async_replication_pair**
> DpBlockAsyncReplicationPairResp update_dp_block_async_replication_pair(pair_id, body)



Update dp block async replication pair

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
api_instance = xms_client.DpBlockAsyncReplicationPairsApi(xms_client.ApiClient(configuration))
pair_id = 789 # int | resource id
body = xms_client.DpBlockAsyncReplicationPairUpdateReq() # DpBlockAsyncReplicationPairUpdateReq | pair info

try:
    api_response = api_instance.update_dp_block_async_replication_pair(pair_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpBlockAsyncReplicationPairsApi->update_dp_block_async_replication_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair_id** | **int**| resource id | 
 **body** | [**DpBlockAsyncReplicationPairUpdateReq**](DpBlockAsyncReplicationPairUpdateReq.md)| pair info | 

### Return type

[**DpBlockAsyncReplicationPairResp**](DpBlockAsyncReplicationPairResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

