# xms_client.DfsTiersApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dfs_tier_pools**](DfsTiersApi.md#add_dfs_tier_pools) | **POST** /dfs-tiers/{dfs_tier_id}:add-pools | 
[**get_dfs_tier**](DfsTiersApi.md#get_dfs_tier) | **GET** /dfs-tiers/{dfs_tier_id} | 
[**list_dfs_tiers**](DfsTiersApi.md#list_dfs_tiers) | **GET** /dfs-tiers/ | 
[**remove_dfs_tier_pools**](DfsTiersApi.md#remove_dfs_tier_pools) | **POST** /dfs-tiers/{dfs_tier_id}:remove-pools | 


# **add_dfs_tier_pools**
> DfsTierResp add_dfs_tier_pools(dfs_tier_id, body)



add dfs tier pools

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
api_instance = xms_client.DfsTiersApi(xms_client.ApiClient(configuration))
dfs_tier_id = 789 # int | dfs tier id
body = xms_client.DfsTierAddPoolReq() # DfsTierAddPoolReq | pools info

try:
    api_response = api_instance.add_dfs_tier_pools(dfs_tier_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTiersApi->add_dfs_tier_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_tier_id** | **int**| dfs tier id | 
 **body** | [**DfsTierAddPoolReq**](DfsTierAddPoolReq.md)| pools info | 

### Return type

[**DfsTierResp**](DfsTierResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_tier**
> DfsTierResp get_dfs_tier(dfs_tier_id)



Get dfs tier

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
api_instance = xms_client.DfsTiersApi(xms_client.ApiClient(configuration))
dfs_tier_id = 789 # int | dfs tier id

try:
    api_response = api_instance.get_dfs_tier(dfs_tier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTiersApi->get_dfs_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_tier_id** | **int**| dfs tier id | 

### Return type

[**DfsTierResp**](DfsTierResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_tiers**
> DfsTiersResp list_dfs_tiers(limit=limit, offset=offset, cluster_id=cluster_id, dfs_rootfs_id=dfs_rootfs_id, q=q, sort=sort)



List dfs tiers

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
api_instance = xms_client.DfsTiersApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
dfs_rootfs_id = 789 # int | dfs rootfs id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dfs_tiers(limit=limit, offset=offset, cluster_id=cluster_id, dfs_rootfs_id=dfs_rootfs_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTiersApi->list_dfs_tiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **dfs_rootfs_id** | **int**| dfs rootfs id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DfsTiersResp**](DfsTiersResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dfs_tier_pools**
> DfsTierResp remove_dfs_tier_pools(dfs_tier_id, body)



remove dfs tier pools

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
api_instance = xms_client.DfsTiersApi(xms_client.ApiClient(configuration))
dfs_tier_id = 789 # int | dfs tier id
body = xms_client.DfsTierRemovePoolReq() # DfsTierRemovePoolReq | pools info

try:
    api_response = api_instance.remove_dfs_tier_pools(dfs_tier_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsTiersApi->remove_dfs_tier_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dfs_tier_id** | **int**| dfs tier id | 
 **body** | [**DfsTierRemovePoolReq**](DfsTierRemovePoolReq.md)| pools info | 

### Return type

[**DfsTierResp**](DfsTierResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

