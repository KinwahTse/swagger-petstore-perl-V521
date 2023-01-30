# xms_client.DfsS3BucketsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dfs_s3_bucket**](DfsS3BucketsApi.md#create_dfs_s3_bucket) | **POST** /dfs-s3-buckets/ | 
[**delete_dfs_s3_bucket**](DfsS3BucketsApi.md#delete_dfs_s3_bucket) | **DELETE** /dfs-s3-buckets/{bucket_id} | 
[**delete_dfs_s3_bucket_policy**](DfsS3BucketsApi.md#delete_dfs_s3_bucket_policy) | **DELETE** /dfs-s3-buckets/{bucket_id}:delete-bucket-policy | 
[**get_dfs_s3_bucket**](DfsS3BucketsApi.md#get_dfs_s3_bucket) | **GET** /dfs-s3-buckets/{bucket_id} | 
[**get_dfs_s3_bucket_samples**](DfsS3BucketsApi.md#get_dfs_s3_bucket_samples) | **GET** /dfs-s3-buckets/{bucket_id}/samples | 
[**list_dfs_s3_buckets**](DfsS3BucketsApi.md#list_dfs_s3_buckets) | **GET** /dfs-s3-buckets/ | 
[**set_dfs_s3_bucket_policy**](DfsS3BucketsApi.md#set_dfs_s3_bucket_policy) | **POST** /dfs-s3-buckets/{bucket_id}:set-bucket-policy | 
[**update_dfs_s3_bucket**](DfsS3BucketsApi.md#update_dfs_s3_bucket) | **PATCH** /dfs-s3-buckets/{bucket_id} | 


# **create_dfs_s3_bucket**
> DfsS3BucketResp create_dfs_s3_bucket(body, cluster_id=cluster_id, allow_path_create=allow_path_create)



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
api_instance = xms_client.DfsS3BucketsApi(xms_client.ApiClient(configuration))
body = xms_client.DfsS3BucketCreateReq() # DfsS3BucketCreateReq | bucket info
cluster_id = 'cluster_id_example' # str | cluster id (optional)
allow_path_create = true # bool | allow create path when not existed (optional)

try:
    api_response = api_instance.create_dfs_s3_bucket(body, cluster_id=cluster_id, allow_path_create=allow_path_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3BucketsApi->create_dfs_s3_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DfsS3BucketCreateReq**](DfsS3BucketCreateReq.md)| bucket info | 
 **cluster_id** | **str**| cluster id | [optional] 
 **allow_path_create** | **bool**| allow create path when not existed | [optional] 

### Return type

[**DfsS3BucketResp**](DfsS3BucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_s3_bucket**
> DfsS3BucketResp delete_dfs_s3_bucket(bucket_id, with_directory=with_directory)



delete dfs s3 bucket

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
api_instance = xms_client.DfsS3BucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
with_directory = true # bool | also delete directory (optional)

try:
    api_response = api_instance.delete_dfs_s3_bucket(bucket_id, with_directory=with_directory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3BucketsApi->delete_dfs_s3_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **with_directory** | **bool**| also delete directory | [optional] 

### Return type

[**DfsS3BucketResp**](DfsS3BucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dfs_s3_bucket_policy**
> DfsS3BucketResp delete_dfs_s3_bucket_policy(bucket_id)



delete dfs s3 bucket policy

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
api_instance = xms_client.DfsS3BucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id

try:
    api_response = api_instance.delete_dfs_s3_bucket_policy(bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3BucketsApi->delete_dfs_s3_bucket_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 

### Return type

[**DfsS3BucketResp**](DfsS3BucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_s3_bucket**
> DfsS3BucketResp get_dfs_s3_bucket(bucket_id)



Get dfs s3 bucket

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
api_instance = xms_client.DfsS3BucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id

try:
    api_response = api_instance.get_dfs_s3_bucket(bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3BucketsApi->get_dfs_s3_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 

### Return type

[**DfsS3BucketResp**](DfsS3BucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dfs_s3_bucket_samples**
> DfsS3BucketSamplesResp get_dfs_s3_bucket_samples(bucket_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get an dfs s3 bucket's Samples

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
api_instance = xms_client.DfsS3BucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_dfs_s3_bucket_samples(bucket_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3BucketsApi->get_dfs_s3_bucket_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**DfsS3BucketSamplesResp**](DfsS3BucketSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dfs_s3_buckets**
> DfsS3BucketsResp list_dfs_s3_buckets(cluster_id=cluster_id, limit=limit, offset=offset, name=name, owner_id=owner_id, path_id=path_id, q=q, sort=sort)



List dfs s3 buckets

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
api_instance = xms_client.DfsS3BucketsApi(xms_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | cluster id (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
name = 'name_example' # str | name of dfs s3 buckets (optional)
owner_id = 789 # int | The id of user buckets belong to (optional)
path_id = 789 # int | The id of bucket path (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)

try:
    api_response = api_instance.list_dfs_s3_buckets(cluster_id=cluster_id, limit=limit, offset=offset, name=name, owner_id=owner_id, path_id=path_id, q=q, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3BucketsApi->list_dfs_s3_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| cluster id | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **name** | **str**| name of dfs s3 buckets | [optional] 
 **owner_id** | **int**| The id of user buckets belong to | [optional] 
 **path_id** | **int**| The id of bucket path | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 

### Return type

[**DfsS3BucketsResp**](DfsS3BucketsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_dfs_s3_bucket_policy**
> DfsS3BucketResp set_dfs_s3_bucket_policy(bucket_id, body)



set dfs s3 bucket policy

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
api_instance = xms_client.DfsS3BucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.DfsS3BucketPolicySetReq() # DfsS3BucketPolicySetReq | bucket policy info

try:
    api_response = api_instance.set_dfs_s3_bucket_policy(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3BucketsApi->set_dfs_s3_bucket_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**DfsS3BucketPolicySetReq**](DfsS3BucketPolicySetReq.md)| bucket policy info | 

### Return type

[**DfsS3BucketResp**](DfsS3BucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dfs_s3_bucket**
> DfsS3BucketResp update_dfs_s3_bucket(bucket_id, body)



Update dfs s3 bucket

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
api_instance = xms_client.DfsS3BucketsApi(xms_client.ApiClient(configuration))
bucket_id = 789 # int | bucket id
body = xms_client.DfsS3BucketUpdateReq() # DfsS3BucketUpdateReq | bucket info

try:
    api_response = api_instance.update_dfs_s3_bucket(bucket_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DfsS3BucketsApi->update_dfs_s3_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | **int**| bucket id | 
 **body** | [**DfsS3BucketUpdateReq**](DfsS3BucketUpdateReq.md)| bucket info | 

### Return type

[**DfsS3BucketResp**](DfsS3BucketResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

