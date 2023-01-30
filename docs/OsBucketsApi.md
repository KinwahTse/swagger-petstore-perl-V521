# xms_client.OsBucketsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_labels**](OsBucketsApi.md#add_custom_labels) | **POST** /os-buckets/{bucket_id}:add-custom-labels | 
[**add_os_replication_paths**](OsBucketsApi.md#add_os_replication_paths) | **POST** /os-buckets/{bucket_id}:add-os-replication-paths | 
[**add_os_replication_zones**](OsBucketsApi.md#add_os_replication_zones) | **POST** /os-buckets/{bucket_id}:add-os-replication-zones | 
[**batch_get_object_storage_samples**](OsBucketsApi.md#batch_get_object_storage_samples) | **GET** /os-buckets/samples | 
[**cancel_delete_bucket**](OsBucketsApi.md#cancel_delete_bucket) | **POST** /os-buckets/{bucket_id}:cancel | 
[**create_bucket**](OsBucketsApi.md#create_bucket) | **POST** /os-buckets/ | 
[**create_object_storage_bucket_nfs_clients**](OsBucketsApi.md#create_object_storage_bucket_nfs_clients) | **POST** /os-buckets/{bucket_id}/nfs-clients | 
[**delete_bucket**](OsBucketsApi.md#delete_bucket) | **DELETE** /os-buckets/{bucket_id} | 
[**delete_object_storage_bucket_nfs_clients**](OsBucketsApi.md#delete_object_storage_bucket_nfs_clients) | **DELETE** /os-buckets/{bucket_id}/nfs-clients | 
[**delete_object_storage_lifecycle**](OsBucketsApi.md#delete_object_storage_lifecycle) | **DELETE** /os-buckets/{bucket_id}/lifecycle | 
[**get_bucket**](OsBucketsApi.md#get_bucket) | **GET** /os-buckets/{bucket_id} | 
[**get_object_storage_bucket_nfs_client**](OsBucketsApi.md#get_object_storage_bucket_nfs_client) | **GET** /os-buckets/{bucket_id}/nfs-clients/{client_id} | 
[**get_object_storage_bucket_samples**](OsBucketsApi.md#get_object_storage_bucket_samples) | **GET** /os-buckets/{bucket_id}/samples | 
[**get_os_bucket_origin_pull_samples**](OsBucketsApi.md#get_os_bucket_origin_pull_samples) | **GET** /os-buckets/{bucket_id}/origin_pull_samples | 
[**list_buckets**](OsBucketsApi.md#list_buckets) | **GET** /os-buckets/ | 
[**list_object_storage_bucket_nfs_clients**](OsBucketsApi.md#list_object_storage_bucket_nfs_clients) | **GET** /os-buckets/{bucket_id}/nfs-clients | 
[**remove_custom_labels**](OsBucketsApi.md#remove_custom_labels) | **POST** /os-buckets/{bucket_id}:remove-custom-labels | 
[**remove_os_bucket_loggings**](OsBucketsApi.md#remove_os_bucket_loggings) | **POST** /os-buckets/{bucket_id}:remove-os-bucket-loggings | 
[**remove_os_replication_paths**](OsBucketsApi.md#remove_os_replication_paths) | **POST** /os-buckets/{bucket_id}:remove-os-replication-paths | 
[**remove_os_replication_zones**](OsBucketsApi.md#remove_os_replication_zones) | **POST** /os-buckets/{bucket_id}:remove-os-replication-zones | 
[**set_access_logging**](OsBucketsApi.md#set_access_logging) | **POST** /os-buckets/{bucket_id}:set-access-logging | 
[**set_metadata_search**](OsBucketsApi.md#set_metadata_search) | **POST** /os-buckets/{bucket_id}:set-metadata-search | 
[**set_object_storage_class**](OsBucketsApi.md#set_object_storage_class) | **POST** /os-buckets/{bucket_id}:set-object-storage-class | 
[**set_object_storage_lifecycle_rules**](OsBucketsApi.md#set_object_storage_lifecycle_rules) | **PUT** /os-buckets/{bucket_id}/lifecycle | 
[**set_os_bucket_policy**](OsBucketsApi.md#set_os_bucket_policy) | **POST** /os-buckets/{bucket_id}:set-bucket-policy | 
[**suspend_access_loggings**](OsBucketsApi.md#suspend_access_loggings) | **POST** /os-buckets/{bucket_id}:suspend-access-logging | 
[**suspend_os_replication_paths**](OsBucketsApi.md#suspend_os_replication_paths) | **POST** /os-buckets/{bucket_id}:suspend-os-replication-paths | 
[**switch_owner_os_zone**](OsBucketsApi.md#switch_owner_os_zone) | **POST** /os-buckets/{bucket_id}:switch-owner-os-zone | 
[**unset_access_logging**](OsBucketsApi.md#unset_access_logging) | **POST** /os-buckets/{bucket_id}:unset-access-logging | 
[**unset_os_bucket_policy**](OsBucketsApi.md#unset_os_bucket_policy) | **POST** /os-buckets/{bucket_id}:unset-bucket-policy | 
[**unsuspend_access_logging**](OsBucketsApi.md#unsuspend_access_logging) | **POST** /os-buckets/{bucket_id}:unsuspend-access-logging | 
[**unsuspend_os_replication_paths**](OsBucketsApi.md#unsuspend_os_replication_paths) | **POST** /os-buckets/{bucket_id}:unsuspend-os-replication-paths | 
[**update_bucket**](OsBucketsApi.md#update_bucket) | **PATCH** /os-buckets/{bucket_id} | 
[**update_custom_labels**](OsBucketsApi.md#update_custom_labels) | **POST** /os-buckets/{bucket_id}:update-custom-labels | 
[**update_object_storage_bucket_nfs_client**](OsBucketsApi.md#update_object_storage_bucket_nfs_client) | **PATCH** /os-buckets/{bucket_id}/nfs-clients/{client_id} | 


# **add_custom_labels**
> ObjectStorageBucketResp add_custom_labels(bucket_id, body)



add object storage bucket custom labels

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketCustomLabelsAddReq() # OSBucketCustomLabelsAddReq | bucket custom labels info

try:
    api_response = api_instance.add_custom_labels(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->add_custom_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketCustomLabelsAddReq**](OSBucketCustomLabelsAddReq.md)| bucket custom labels info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_os_replication_paths**
> ObjectStorageBucketResp add_os_replication_paths(bucket_id, body)



add os replication paths for os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketAddReplicationPathsReq() # OSBucketAddReplicationPathsReq | replication paths info

try:
    api_response = api_instance.add_os_replication_paths(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->add_os_replication_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketAddReplicationPathsReq**](OSBucketAddReplicationPathsReq.md)| replication paths info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_os_replication_zones**
> ObjectStorageBucketResp add_os_replication_zones(bucket_id, body)



add os replication zones for os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketAddReplicationZonesReq() # OSBucketAddReplicationZonesReq | replication zones info

try:
    api_response = api_instance.add_os_replication_zones(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->add_os_replication_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketAddReplicationZonesReq**](OSBucketAddReplicationZonesReq.md)| replication zones info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_get_object_storage_samples**
> MultiObjectStorageBucketsSamplesResp batch_get_object_storage_samples(ids)



Get samples of multiple object storage buckets

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
ids = 'ids_example' # str | bucket ids

try:
    api_response = api_instance.batch_get_object_storage_samples(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->batch_get_object_storage_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| bucket ids | 

### Return type

[**MultiObjectStorageBucketsSamplesResp**](MultiObjectStorageBucketsSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_delete_bucket**
> ObjectStorageBucketResp cancel_delete_bucket(bucket_id)



cancel delete bucket task

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id

try:
    api_response = api_instance.cancel_delete_bucket(bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->cancel_delete_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bucket**
> ObjectStorageBucketResp create_bucket(body, cluster_id=cluster_id)



Create os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
body = xms_client.ObjectStorageBucketCreateReq() # ObjectStorageBucketCreateReq | bucket info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_bucket(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->create_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectStorageBucketCreateReq**](ObjectStorageBucketCreateReq.md)| bucket info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_storage_bucket_nfs_clients**
> RawObjectStorageBucketResp create_object_storage_bucket_nfs_clients(bucket_id, body)



create nfs client

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.ObjectStorageBucketNFSClientsCreateReq() # ObjectStorageBucketNFSClientsCreateReq | nfs client info

try:
    api_response = api_instance.create_object_storage_bucket_nfs_clients(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->create_object_storage_bucket_nfs_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**ObjectStorageBucketNFSClientsCreateReq**](ObjectStorageBucketNFSClientsCreateReq.md)| nfs client info | 

### Return type

[**RawObjectStorageBucketResp**](RawObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bucket**
> ObjectStorageBucketResp delete_bucket(bucket_id, force=force)



delete object storage bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
force = true # bool | force delete or not (optional)

try:
    api_response = api_instance.delete_bucket(bucket_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->delete_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **force** | **bool**| force delete or not | [optional] 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_storage_bucket_nfs_clients**
> RawObjectStorageBucketResp delete_object_storage_bucket_nfs_clients(bucket_id, body)



delete nfs clients

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.ObjectStorageBucketNFSClientsDeleteReq() # ObjectStorageBucketNFSClientsDeleteReq | nfs client info

try:
    api_response = api_instance.delete_object_storage_bucket_nfs_clients(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->delete_object_storage_bucket_nfs_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**ObjectStorageBucketNFSClientsDeleteReq**](ObjectStorageBucketNFSClientsDeleteReq.md)| nfs client info | 

### Return type

[**RawObjectStorageBucketResp**](RawObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_storage_lifecycle**
> ObjectStorageBucketResp delete_object_storage_lifecycle(bucket_id)



delete object storage lifecycle

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id

try:
    api_response = api_instance.delete_object_storage_lifecycle(bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->delete_object_storage_lifecycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bucket**
> ObjectStorageBucketResp get_bucket(bucket_id)



Get object storage bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id

try:
    api_response = api_instance.get_bucket(bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->get_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_bucket_nfs_client**
> ObjectStorageBucketNFSClientResp get_object_storage_bucket_nfs_client(bucket_id, client_id)



show nfs client

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
client_id = 789 # int | nfs client id

try:
    api_response = api_instance.get_object_storage_bucket_nfs_client(bucket_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->get_object_storage_bucket_nfs_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **client_id** | **int**| nfs client id | 

### Return type

[**ObjectStorageBucketNFSClientResp**](ObjectStorageBucketNFSClientResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_storage_bucket_samples**
> ObjectStorageBucketSamplesResp get_object_storage_bucket_samples(bucket_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get an object storage bucket's Samples

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_object_storage_bucket_samples(bucket_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->get_object_storage_bucket_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**ObjectStorageBucketSamplesResp**](ObjectStorageBucketSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_bucket_origin_pull_samples**
> OSBucketOriginPullSamplesResp get_os_bucket_origin_pull_samples(bucket_id, origin_mode=origin_mode, duration_begin=duration_begin, duration_end=duration_end, period=period)



get an os bucket's origin pull Samples

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
origin_mode = 'origin_mode_example' # str | origin mode (optional)
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_os_bucket_origin_pull_samples(bucket_id, origin_mode=origin_mode, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->get_os_bucket_origin_pull_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **origin_mode** | **str**| origin mode | [optional] 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**OSBucketOriginPullSamplesResp**](OSBucketOriginPullSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buckets**
> ObjectStorageBucketsResp list_buckets(cluster_id=cluster_id, limit=limit, offset=offset, name=name, os_policy_id=os_policy_id, os_user_id=os_user_id, replication_uuid=replication_uuid, virtual=virtual, q=q, sort=sort)



List object storage buckets

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | cluster id (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
name = 'name_example' # str | name of object storage buckets (optional)
os_policy_id = 789 # int | The id of policy object storage buckets belong to (optional)
os_user_id = 789 # int | The id of user object storage buckets belong to (optional)
replication_uuid = 'replication_uuid_example' # str | The uuid of replication os buckets belong to (optional)
virtual = true # bool | Virtual bucket or not (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_buckets(cluster_id=cluster_id, limit=limit, offset=offset, name=name, os_policy_id=os_policy_id, os_user_id=os_user_id, replication_uuid=replication_uuid, virtual=virtual, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->list_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| cluster id | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **name** | **str**| name of object storage buckets | [optional] 
 **os_policy_id** | **int**| The id of policy object storage buckets belong to | [optional] 
 **os_user_id** | **int**| The id of user object storage buckets belong to | [optional] 
 **replication_uuid** | **str**| The uuid of replication os buckets belong to | [optional] 
 **virtual** | **bool**| Virtual bucket or not | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**ObjectStorageBucketsResp**](ObjectStorageBucketsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_object_storage_bucket_nfs_clients**
> ObjectStorageBucketNFSClientsResp list_object_storage_bucket_nfs_clients(bucket_id, limit=limit, offset=offset, cluster_id=cluster_id)



List nfs clients

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_object_storage_bucket_nfs_clients(bucket_id, limit=limit, offset=offset, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->list_object_storage_bucket_nfs_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**ObjectStorageBucketNFSClientsResp**](ObjectStorageBucketNFSClientsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_custom_labels**
> ObjectStorageBucketResp remove_custom_labels(bucket_id, body)



remove object storage bucket custom labels

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | object storage bucket id
body = xms_client.OSBucketCustomLabelsRemoveReq() # OSBucketCustomLabelsRemoveReq | custom labels info

try:
    api_response = api_instance.remove_custom_labels(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->remove_custom_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| object storage bucket id | 
 **body** | [**OSBucketCustomLabelsRemoveReq**](OSBucketCustomLabelsRemoveReq.md)| custom labels info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_os_bucket_loggings**
> ObjectStorageBucketResp remove_os_bucket_loggings(bucket_id, body)



Remove os bucket loggings of os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketRemoveLoggingsReq() # OSBucketRemoveLoggingsReq | os bucket loggings info

try:
    api_response = api_instance.remove_os_bucket_loggings(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->remove_os_bucket_loggings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketRemoveLoggingsReq**](OSBucketRemoveLoggingsReq.md)| os bucket loggings info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_os_replication_paths**
> ObjectStorageBucketResp remove_os_replication_paths(bucket_id, body)



remove os replication paths for os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketRemoveReplicationPathsReq() # OSBucketRemoveReplicationPathsReq | replication paths info

try:
    api_response = api_instance.remove_os_replication_paths(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->remove_os_replication_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketRemoveReplicationPathsReq**](OSBucketRemoveReplicationPathsReq.md)| replication paths info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_os_replication_zones**
> ObjectStorageBucketResp remove_os_replication_zones(bucket_id, body, force=force)



remove os replication zones for os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketRemoveReplicationZonesReq() # OSBucketRemoveReplicationZonesReq | replication zones info
force = true # bool | force delete os replication zone even if target zone is dead (optional)

try:
    api_response = api_instance.remove_os_replication_zones(bucket_id, body, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->remove_os_replication_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketRemoveReplicationZonesReq**](OSBucketRemoveReplicationZonesReq.md)| replication zones info | 
 **force** | **bool**| force delete os replication zone even if target zone is dead | [optional] 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_access_logging**
> ObjectStorageBucketResp set_access_logging(bucket_id, body)



Set access logging of os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketSetAccessLoggingReq() # OSBucketSetAccessLoggingReq | access logging info

try:
    api_response = api_instance.set_access_logging(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->set_access_logging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketSetAccessLoggingReq**](OSBucketSetAccessLoggingReq.md)| access logging info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_metadata_search**
> ObjectStorageBucketsResp set_metadata_search(bucket_id, body)



set object storage bucket metadata search

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | object storage bucket id
body = xms_client.OSBucketMetadataSearchSetReq() # OSBucketMetadataSearchSetReq | bucket metadata search info

try:
    api_response = api_instance.set_metadata_search(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->set_metadata_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| object storage bucket id | 
 **body** | [**OSBucketMetadataSearchSetReq**](OSBucketMetadataSearchSetReq.md)| bucket metadata search info | 

### Return type

[**ObjectStorageBucketsResp**](ObjectStorageBucketsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_object_storage_class**
> ObjectStorageBucketResp set_object_storage_class(bucket_id, body)



Set bucket object match storage class

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketSetObjectStorageClassReq() # OSBucketSetObjectStorageClassReq | object storage class info

try:
    api_response = api_instance.set_object_storage_class(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->set_object_storage_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketSetObjectStorageClassReq**](OSBucketSetObjectStorageClassReq.md)| object storage class info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_object_storage_lifecycle_rules**
> ObjectStorageBucketResp set_object_storage_lifecycle_rules(bucket_id, body)



Set object storage lifecycle rules

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.ObjectStorageLifecycleSetReq() # ObjectStorageLifecycleSetReq | lifecyce rules info

try:
    api_response = api_instance.set_object_storage_lifecycle_rules(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->set_object_storage_lifecycle_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**ObjectStorageLifecycleSetReq**](ObjectStorageLifecycleSetReq.md)| lifecyce rules info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_os_bucket_policy**
> ObjectStorageBucketResp set_os_bucket_policy(bucket_id, body)



set object storage bucket policy

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketPolicySetReq() # OSBucketPolicySetReq | bucket policy info

try:
    api_response = api_instance.set_os_bucket_policy(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->set_os_bucket_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketPolicySetReq**](OSBucketPolicySetReq.md)| bucket policy info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_access_loggings**
> ObjectStorageBucketResp suspend_access_loggings(bucket_id)



suspend access logging for os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id

try:
    api_response = api_instance.suspend_access_loggings(bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->suspend_access_loggings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_os_replication_paths**
> ObjectStorageBucketResp suspend_os_replication_paths(bucket_id, body)



suspend os replication paths for os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketUpdateReplicationPathsReq() # OSBucketUpdateReplicationPathsReq | replication paths info

try:
    api_response = api_instance.suspend_os_replication_paths(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->suspend_os_replication_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketUpdateReplicationPathsReq**](OSBucketUpdateReplicationPathsReq.md)| replication paths info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_owner_os_zone**
> ObjectStorageBucketResp switch_owner_os_zone(bucket_id, body, force=force)



Switch owner zone of os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketSwitchOwnerOSZoneReq() # OSBucketSwitchOwnerOSZoneReq | new owner os zone info
force = true # bool | force to switch even if old owner zone is dead (optional)

try:
    api_response = api_instance.switch_owner_os_zone(bucket_id, body, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->switch_owner_os_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketSwitchOwnerOSZoneReq**](OSBucketSwitchOwnerOSZoneReq.md)| new owner os zone info | 
 **force** | **bool**| force to switch even if old owner zone is dead | [optional] 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_access_logging**
> ObjectStorageBucketResp unset_access_logging(bucket_id)



Unset access logging of os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id

try:
    api_response = api_instance.unset_access_logging(bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->unset_access_logging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_os_bucket_policy**
> ObjectStorageBucketResp unset_os_bucket_policy(bucket_id)



unset object storage bucket policy

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id

try:
    api_response = api_instance.unset_os_bucket_policy(bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->unset_os_bucket_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsuspend_access_logging**
> ObjectStorageBucketResp unsuspend_access_logging(bucket_id)



unsuspend access logging for os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id

try:
    api_response = api_instance.unsuspend_access_logging(bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->unsuspend_access_logging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsuspend_os_replication_paths**
> ObjectStorageBucketResp unsuspend_os_replication_paths(bucket_id, body)



unsuspend os replication paths for os bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.OSBucketUpdateReplicationPathsReq() # OSBucketUpdateReplicationPathsReq | replication paths info

try:
    api_response = api_instance.unsuspend_os_replication_paths(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->unsuspend_os_replication_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**OSBucketUpdateReplicationPathsReq**](OSBucketUpdateReplicationPathsReq.md)| replication paths info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bucket**
> ObjectStorageBucketResp update_bucket(bucket_id, body)



Update object storage bucket

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.ObjectStorageBucketUpdateReq() # ObjectStorageBucketUpdateReq | bucket info

try:
    api_response = api_instance.update_bucket(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->update_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**ObjectStorageBucketUpdateReq**](ObjectStorageBucketUpdateReq.md)| bucket info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_labels**
> ObjectStorageBucketResp update_custom_labels(bucket_id, body)



update object storage bucket custom labels

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | object storage bucket id
body = xms_client.OSBucketCustomLabelsUpdateReq() # OSBucketCustomLabelsUpdateReq | custom labels info

try:
    api_response = api_instance.update_custom_labels(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->update_custom_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| object storage bucket id | 
 **body** | [**OSBucketCustomLabelsUpdateReq**](OSBucketCustomLabelsUpdateReq.md)| custom labels info | 

### Return type

[**ObjectStorageBucketResp**](ObjectStorageBucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_storage_bucket_nfs_client**
> ObjectStorageBucketNFSClientResp update_object_storage_bucket_nfs_client(bucket_id, client_id, body)



update nfs client

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
api_instance = xms_client.OsBucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
client_id = 789 # int | nfs client id
body = xms_client.ObjectStorageBucketNFSClientUpdateReq() # ObjectStorageBucketNFSClientUpdateReq | nfs client info

try:
    api_response = api_instance.update_object_storage_bucket_nfs_client(bucket_id, client_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsBucketsApi->update_object_storage_bucket_nfs_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **client_id** | **int**| nfs client id | 
 **body** | [**ObjectStorageBucketNFSClientUpdateReq**](ObjectStorageBucketNFSClientUpdateReq.md)| nfs client info | 

### Return type

[**ObjectStorageBucketNFSClientResp**](ObjectStorageBucketNFSClientResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

