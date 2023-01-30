# xms_client.MetadataClustersApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_services_to_cluster**](MetadataClustersApi.md#add_metadata_services_to_cluster) | **POST** /metadata-clusters/{metadata_cluster_id}:add-metadata-services | 
[**create_metadata_cluster**](MetadataClustersApi.md#create_metadata_cluster) | **POST** /metadata-clusters/ | 
[**delete_metadata_cluster**](MetadataClustersApi.md#delete_metadata_cluster) | **DELETE** /metadata-clusters/{metadata_cluster_id} | 
[**get_metadata_cluster**](MetadataClustersApi.md#get_metadata_cluster) | **GET** /metadata-clusters/{metadata_cluster_id} | 
[**get_metadata_cluster_predictions**](MetadataClustersApi.md#get_metadata_cluster_predictions) | **GET** /metadata-clusters/{metadata_cluster_id}/predictions | 
[**get_metadata_cluster_samples**](MetadataClustersApi.md#get_metadata_cluster_samples) | **GET** /metadata-clusters/{metadata_cluster_id}/samples | 
[**list_metadata_clusters**](MetadataClustersApi.md#list_metadata_clusters) | **GET** /metadata-clusters/ | 
[**remove_metadata_services_from_cluster**](MetadataClustersApi.md#remove_metadata_services_from_cluster) | **POST** /metadata-clusters/{metadata_cluster_id}:remove-metadata-services | 
[**update_metadata_cluster**](MetadataClustersApi.md#update_metadata_cluster) | **PATCH** /metadata-clusters/{metadata_cluster_id} | 


# **add_metadata_services_to_cluster**
> MetadataClusterResp add_metadata_services_to_cluster(metadata_cluster_id, body)



Add metadata services to cluster

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
api_instance = xms_client.MetadataClustersApi(xms_client.ApiClient(configuration))
metadata_cluster_id = 789 # int | metadata cluster id
body = xms_client.MetadataClusterAddServicesReq() # MetadataClusterAddServicesReq | metadata services

try:
    api_response = api_instance.add_metadata_services_to_cluster(metadata_cluster_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataClustersApi->add_metadata_services_to_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_cluster_id** | **int**| metadata cluster id | 
 **body** | [**MetadataClusterAddServicesReq**](MetadataClusterAddServicesReq.md)| metadata services | 

### Return type

[**MetadataClusterResp**](MetadataClusterResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metadata_cluster**
> MetadataClusterResp create_metadata_cluster(body, cluster_id=cluster_id)



Create metadata cluster on specific disk

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
api_instance = xms_client.MetadataClustersApi(xms_client.ApiClient(configuration))
body = xms_client.MetadataClusterCreateReq() # MetadataClusterCreateReq | metadata cluster info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_metadata_cluster(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataClustersApi->create_metadata_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataClusterCreateReq**](MetadataClusterCreateReq.md)| metadata cluster info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**MetadataClusterResp**](MetadataClusterResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_cluster**
> MetadataClusterResp delete_metadata_cluster(metadata_cluster_id)



delete a metadata cluster

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
api_instance = xms_client.MetadataClustersApi(xms_client.ApiClient(configuration))
metadata_cluster_id = 789 # int | metadata cluster id

try:
    api_response = api_instance.delete_metadata_cluster(metadata_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataClustersApi->delete_metadata_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_cluster_id** | **int**| metadata cluster id | 

### Return type

[**MetadataClusterResp**](MetadataClusterResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_cluster**
> MetadataClusterResp get_metadata_cluster(metadata_cluster_id)



get a metadata cluster

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
api_instance = xms_client.MetadataClustersApi(xms_client.ApiClient(configuration))
metadata_cluster_id = 789 # int | metadata cluster id

try:
    api_response = api_instance.get_metadata_cluster(metadata_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataClustersApi->get_metadata_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_cluster_id** | **int**| metadata cluster id | 

### Return type

[**MetadataClusterResp**](MetadataClusterResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_cluster_predictions**
> MetadataClusterPredictionsResp get_metadata_cluster_predictions(metadata_cluster_id)



get a metadata cluster's prediction

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
api_instance = xms_client.MetadataClustersApi(xms_client.ApiClient(configuration))
metadata_cluster_id = 789 # int | metadata cluster id

try:
    api_response = api_instance.get_metadata_cluster_predictions(metadata_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataClustersApi->get_metadata_cluster_predictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_cluster_id** | **int**| metadata cluster id | 

### Return type

[**MetadataClusterPredictionsResp**](MetadataClusterPredictionsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_cluster_samples**
> MetadataClusterSamplesResp get_metadata_cluster_samples(metadata_cluster_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get samples of a metadata cluster

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
api_instance = xms_client.MetadataClustersApi(xms_client.ApiClient(configuration))
metadata_cluster_id = 789 # int | metadata cluster id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_metadata_cluster_samples(metadata_cluster_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataClustersApi->get_metadata_cluster_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_cluster_id** | **int**| metadata cluster id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**MetadataClusterSamplesResp**](MetadataClusterSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metadata_clusters**
> MetadataClustersResp list_metadata_clusters(limit=limit, offset=offset, cluster_id=cluster_id, host_id=host_id, metadata_cluster_id=metadata_cluster_id, q=q, sort=sort)



List all metadata clusters in the cluster

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
api_instance = xms_client.MetadataClustersApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
host_id = 789 # int | host id (optional)
metadata_cluster_id = 789 # int | metadata cluster id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_metadata_clusters(limit=limit, offset=offset, cluster_id=cluster_id, host_id=host_id, metadata_cluster_id=metadata_cluster_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataClustersApi->list_metadata_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **host_id** | **int**| host id | [optional] 
 **metadata_cluster_id** | **int**| metadata cluster id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**MetadataClustersResp**](MetadataClustersResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_metadata_services_from_cluster**
> MetadataClusterResp remove_metadata_services_from_cluster(metadata_cluster_id, body)



Remove metadata services from cluster

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
api_instance = xms_client.MetadataClustersApi(xms_client.ApiClient(configuration))
metadata_cluster_id = 789 # int | metadata cluster id
body = xms_client.MetadataClusterRemoveServicesReq() # MetadataClusterRemoveServicesReq | metadata services

try:
    api_response = api_instance.remove_metadata_services_from_cluster(metadata_cluster_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataClustersApi->remove_metadata_services_from_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_cluster_id** | **int**| metadata cluster id | 
 **body** | [**MetadataClusterRemoveServicesReq**](MetadataClusterRemoveServicesReq.md)| metadata services | 

### Return type

[**MetadataClusterResp**](MetadataClusterResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_cluster**
> MetadataClusterResp update_metadata_cluster(metadata_cluster_id, body)



update metadata cluster

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
api_instance = xms_client.MetadataClustersApi(xms_client.ApiClient(configuration))
metadata_cluster_id = 789 # int | metadata cluster id
body = xms_client.MetadataClusterUpdateReq() # MetadataClusterUpdateReq | metadata cluster info

try:
    api_response = api_instance.update_metadata_cluster(metadata_cluster_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataClustersApi->update_metadata_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_cluster_id** | **int**| metadata cluster id | 
 **body** | [**MetadataClusterUpdateReq**](MetadataClusterUpdateReq.md)| metadata cluster info | 

### Return type

[**MetadataClusterResp**](MetadataClusterResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

