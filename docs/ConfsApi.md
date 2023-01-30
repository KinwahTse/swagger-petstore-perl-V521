# xms_client.ConfsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_conf_item**](ConfsApi.md#delete_conf_item) | **DELETE** /confs/{type}/{key} | 
[**get_conf_item**](ConfsApi.md#get_conf_item) | **GET** /confs/{type}/{key} | 
[**list_conf_items**](ConfsApi.md#list_conf_items) | **GET** /confs/{type} | 
[**list_conf_items_query**](ConfsApi.md#list_conf_items_query) | **GET** /confs/ | 
[**set_conf_item**](ConfsApi.md#set_conf_item) | **PUT** /confs/ | 
[**set_conf_items**](ConfsApi.md#set_conf_items) | **PUT** /confs/{type} | 


# **delete_conf_item**
> delete_conf_item(type, key)



delete conf item

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
api_instance = xms_client.ConfsApi(xms_client.ApiClient(configuration))
type = 'type_example' # str | filter the type of conf item
key = 'key_example' # str | filter the key of conf item

try:
    api_instance.delete_conf_item(type, key)
except ApiException as e:
    print("Exception when calling ConfsApi->delete_conf_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| filter the type of conf item | 
 **key** | **str**| filter the key of conf item | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conf_item**
> ConfItemResp get_conf_item(type, key, cluster_id=cluster_id)



get conf item

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
api_instance = xms_client.ConfsApi(xms_client.ApiClient(configuration))
type = 'type_example' # str | filter the type of conf
key = 'key_example' # str | filter the key of conf item
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.get_conf_item(type, key, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfsApi->get_conf_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| filter the type of conf | 
 **key** | **str**| filter the key of conf item | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**ConfItemResp**](ConfItemResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conf_items**
> ConfItemsResp list_conf_items(type, limit=limit, offset=offset)



List conf items

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
api_instance = xms_client.ConfsApi(xms_client.ApiClient(configuration))
type = 'type_example' # str | filter the type of conf
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)

try:
    api_response = api_instance.list_conf_items(type, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfsApi->list_conf_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| filter the type of conf | 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 

### Return type

[**ConfItemsResp**](ConfItemsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conf_items_query**
> ConfItemsResp list_conf_items_query(limit=limit, offset=offset, type=type, key=key)



List conf items with query

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
api_instance = xms_client.ConfsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
type = 'type_example' # str | filter the type of conf (optional)
key = 'key_example' # str | filter the key of conf (optional)

try:
    api_response = api_instance.list_conf_items_query(limit=limit, offset=offset, type=type, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfsApi->list_conf_items_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **type** | **str**| filter the type of conf | [optional] 
 **key** | **str**| filter the key of conf | [optional] 

### Return type

[**ConfItemsResp**](ConfItemsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_conf_item**
> ConfItem set_conf_item(body, cluster_id=cluster_id)



set conf item

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
api_instance = xms_client.ConfsApi(xms_client.ApiClient(configuration))
body = xms_client.ConfItemSetReq() # ConfItemSetReq | conf item
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.set_conf_item(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfsApi->set_conf_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfItemSetReq**](ConfItemSetReq.md)| conf item | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**ConfItem**](ConfItem.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_conf_items**
> set_conf_items(type, body, cluster_id=cluster_id)



set conf items

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
api_instance = xms_client.ConfsApi(xms_client.ApiClient(configuration))
type = 'type_example' # str | filter the type of conf
body = xms_client.ConfItemsSetReq() # ConfItemsSetReq | conf items
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_instance.set_conf_items(type, body, cluster_id=cluster_id)
except ApiException as e:
    print("Exception when calling ConfsApi->set_conf_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| filter the type of conf | 
 **body** | [**ConfItemsSetReq**](ConfItemsSetReq.md)| conf items | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

