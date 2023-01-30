# xms_client.DpSitesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dp_site**](DpSitesApi.md#create_dp_site) | **POST** /dp-sites/ | 
[**delete_dp_site**](DpSitesApi.md#delete_dp_site) | **DELETE** /dp-sites/{site_id} | 
[**get_backup_block_snapshots**](DpSitesApi.md#get_backup_block_snapshots) | **GET** /dp-sites/{site_id}/backup-block-snapshots | 
[**get_backup_block_volumes**](DpSitesApi.md#get_backup_block_volumes) | **GET** /dp-sites/{site_id}/backup-block-volumes | 
[**get_backup_clusters**](DpSitesApi.md#get_backup_clusters) | **GET** /dp-sites/{site_id}/backup-clusters | 
[**get_dp_site**](DpSitesApi.md#get_dp_site) | **GET** /dp-sites/{site_id} | 
[**list_dp_sites**](DpSitesApi.md#list_dp_sites) | **GET** /dp-sites/ | 
[**update_dp_site**](DpSitesApi.md#update_dp_site) | **PATCH** /dp-sites/{site_id} | 


# **create_dp_site**
> DpSiteResp create_dp_site(body)



Create a data protection site

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
api_instance = xms_client.DpSitesApi(xms_client.ApiClient(configuration))
body = xms_client.DpSiteCreateReq() # DpSiteCreateReq | dp site info

try:
    api_response = api_instance.create_dp_site(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpSitesApi->create_dp_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DpSiteCreateReq**](DpSiteCreateReq.md)| dp site info | 

### Return type

[**DpSiteResp**](DpSiteResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dp_site**
> delete_dp_site(site_id)



Delete data protection site

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
api_instance = xms_client.DpSitesApi(xms_client.ApiClient(configuration))
site_id = 789 # int | dp site id

try:
    api_instance.delete_dp_site(site_id)
except ApiException as e:
    print("Exception when calling DpSitesApi->delete_dp_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| dp site id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_block_snapshots**
> DpBackupBlockSnapshotsResp get_backup_block_snapshots(site_id, dp_gateway_id, cluster_fs_id, block_volume_name, after=after)



List snapshots of a volume stored on a dp site

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
api_instance = xms_client.DpSitesApi(xms_client.ApiClient(configuration))
site_id = 789 # int | dp site id
dp_gateway_id = 789 # int | the dp gateway to execute the query
cluster_fs_id = 'cluster_fs_id_example' # str | cluster fs id
block_volume_name = 'block_volume_name_example' # str | block volume name
after = 'after_example' # str | continuation token (optional)

try:
    api_response = api_instance.get_backup_block_snapshots(site_id, dp_gateway_id, cluster_fs_id, block_volume_name, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpSitesApi->get_backup_block_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| dp site id | 
 **dp_gateway_id** | **int**| the dp gateway to execute the query | 
 **cluster_fs_id** | **str**| cluster fs id | 
 **block_volume_name** | **str**| block volume name | 
 **after** | **str**| continuation token | [optional] 

### Return type

[**DpBackupBlockSnapshotsResp**](DpBackupBlockSnapshotsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_block_volumes**
> DpBackupBlockVolumesResp get_backup_block_volumes(site_id, dp_gateway_id, cluster_fs_id, after=after)



List volumes of a cluster stored on a dp site

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
api_instance = xms_client.DpSitesApi(xms_client.ApiClient(configuration))
site_id = 789 # int | dp site id
dp_gateway_id = 789 # int | the dp gateway to execute the query
cluster_fs_id = 'cluster_fs_id_example' # str | cluster fs id
after = 'after_example' # str | continuation token (optional)

try:
    api_response = api_instance.get_backup_block_volumes(site_id, dp_gateway_id, cluster_fs_id, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpSitesApi->get_backup_block_volumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| dp site id | 
 **dp_gateway_id** | **int**| the dp gateway to execute the query | 
 **cluster_fs_id** | **str**| cluster fs id | 
 **after** | **str**| continuation token | [optional] 

### Return type

[**DpBackupBlockVolumesResp**](DpBackupBlockVolumesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_clusters**
> DpBackupClustersResp get_backup_clusters(site_id, dp_gateway_id)



List clusters stored on a dp site

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
api_instance = xms_client.DpSitesApi(xms_client.ApiClient(configuration))
site_id = 789 # int | dp site id
dp_gateway_id = 789 # int | the dp gateway to execute the query

try:
    api_response = api_instance.get_backup_clusters(site_id, dp_gateway_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpSitesApi->get_backup_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| dp site id | 
 **dp_gateway_id** | **int**| the dp gateway to execute the query | 

### Return type

[**DpBackupClustersResp**](DpBackupClustersResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dp_site**
> DpSiteResp get_dp_site(site_id)



Get data protection site

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
api_instance = xms_client.DpSitesApi(xms_client.ApiClient(configuration))
site_id = 789 # int | protection site id

try:
    api_response = api_instance.get_dp_site(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpSitesApi->get_dp_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| protection site id | 

### Return type

[**DpSiteResp**](DpSiteResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dp_sites**
> DpSitesResp list_dp_sites(limit=limit, offset=offset, q=q, sort=sort, protection_type=protection_type)



List data protection sites

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
api_instance = xms_client.DpSitesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
protection_type = 'protection_type_example' # str | protection type (optional)

try:
    api_response = api_instance.list_dp_sites(limit=limit, offset=offset, q=q, sort=sort, protection_type=protection_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpSitesApi->list_dp_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **protection_type** | **str**| protection type | [optional] 

### Return type

[**DpSitesResp**](DpSitesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dp_site**
> DpSiteResp update_dp_site(site_id, body)



Update a data protection site

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
api_instance = xms_client.DpSitesApi(xms_client.ApiClient(configuration))
site_id = 789 # int | dp site id
body = xms_client.DpSiteUpdateReq() # DpSiteUpdateReq | dp site info

try:
    api_response = api_instance.update_dp_site(site_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DpSitesApi->update_dp_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| dp site id | 
 **body** | [**DpSiteUpdateReq**](DpSiteUpdateReq.md)| dp site info | 

### Return type

[**DpSiteResp**](DpSiteResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

