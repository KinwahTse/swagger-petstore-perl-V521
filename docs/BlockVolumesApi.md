# xms_client.BlockVolumesApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_get_block_volume_samples**](BlockVolumesApi.md#batch_get_block_volume_samples) | **GET** /block-volumes/samples | 
[**create_block_volume**](BlockVolumesApi.md#create_block_volume) | **POST** /block-volumes/ | 
[**delete_block_volume**](BlockVolumesApi.md#delete_block_volume) | **DELETE** /block-volumes/{block_volume_id} | 
[**get_block_volume**](BlockVolumesApi.md#get_block_volume) | **GET** /block-volumes/{block_volume_id} | 
[**get_block_volume_samples**](BlockVolumesApi.md#get_block_volume_samples) | **GET** /block-volumes/{block_volume_id}/samples | 
[**list_block_volumes**](BlockVolumesApi.md#list_block_volumes) | **GET** /block-volumes/ | 
[**migrate_block_volume**](BlockVolumesApi.md#migrate_block_volume) | **POST** /block-volumes/{block_volume_id}:migrate | 
[**rebuild_block_volume_replication**](BlockVolumesApi.md#rebuild_block_volume_replication) | **POST** /block-volumes/{block_volume_id}:rebuild-replication | 
[**set_async_replication_protection**](BlockVolumesApi.md#set_async_replication_protection) | **POST** /block-volumes/{block_volume_id}:set-async-replication-protection | 
[**set_backup_protection**](BlockVolumesApi.md#set_backup_protection) | **POST** /block-volumes/{block_volume_id}:set-backup-protection | 
[**set_block_volume_crc**](BlockVolumesApi.md#set_block_volume_crc) | **POST** /block-volumes/{block_volume_id}:set-crc | 
[**set_block_volume_replication**](BlockVolumesApi.md#set_block_volume_replication) | **POST** /block-volumes/{block_volume_id}:set-replication | 
[**set_snapshot_protection**](BlockVolumesApi.md#set_snapshot_protection) | **POST** /block-volumes/{block_volume_id}:set-snapshot-protection | 
[**suspend_block_volume_replication**](BlockVolumesApi.md#suspend_block_volume_replication) | **POST** /block-volumes/{block_volume_id}:suspend-replication | 
[**unset_async_replication_protection**](BlockVolumesApi.md#unset_async_replication_protection) | **POST** /block-volumes/{block_volume_id}:unset-async-replication-protection | 
[**unset_backup_protection**](BlockVolumesApi.md#unset_backup_protection) | **POST** /block-volumes/{block_volume_id}:unset-backup-protection | 
[**unset_block_volume_crc**](BlockVolumesApi.md#unset_block_volume_crc) | **POST** /block-volumes/{block_volume_id}:unset-crc | 
[**unset_block_volume_replication**](BlockVolumesApi.md#unset_block_volume_replication) | **POST** /block-volumes/{block_volume_id}:unset-replication | 
[**unset_snapshot_protection**](BlockVolumesApi.md#unset_snapshot_protection) | **POST** /block-volumes/{block_volume_id}:unset-snapshot-protection | 
[**update_block_volume**](BlockVolumesApi.md#update_block_volume) | **PATCH** /block-volumes/{block_volume_id} | 
[**update_block_volume_volume_name**](BlockVolumesApi.md#update_block_volume_volume_name) | **POST** /block-volumes/{block_volume_id}:update-volume-name | 
[**update_volume_stat**](BlockVolumesApi.md#update_volume_stat) | **POST** /block-volumes/:update-stat | 


# **batch_get_block_volume_samples**
> MultiVolumesSamplesResp batch_get_block_volume_samples()



Get samples of multiple block volumes

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))

try:
    api_response = api_instance.batch_get_block_volume_samples()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->batch_get_block_volume_samples: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MultiVolumesSamplesResp**](MultiVolumesSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_block_volume**
> VolumeResp create_block_volume(body)



Create block volume

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
body = xms_client.VolumeCreateReq() # VolumeCreateReq | volume info

try:
    api_response = api_instance.create_block_volume(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->create_block_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VolumeCreateReq**](VolumeCreateReq.md)| volume info | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_block_volume**
> VolumeResp delete_block_volume(block_volume_id, bypass_trash=bypass_trash)



Delete block volume

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | volume id
bypass_trash = true # bool | bypass trash or not (optional)

try:
    api_response = api_instance.delete_block_volume(block_volume_id, bypass_trash=bypass_trash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->delete_block_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| volume id | 
 **bypass_trash** | **bool**| bypass trash or not | [optional] 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_volume**
> VolumeResp get_block_volume(block_volume_id)



get a block volume

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | block volume id

try:
    api_response = api_instance.get_block_volume(block_volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->get_block_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| block volume id | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_volume_samples**
> VolumeSamplesResp get_block_volume_samples(block_volume_id, duration_begin=duration_begin, duration_end=duration_end, period=period)



get a block volume's Samples

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | block volume id
duration_begin = 'duration_begin_example' # str | duration begin timestamp (optional)
duration_end = 'duration_end_example' # str | duration end timestamp (optional)
period = 'period_example' # str | samples period (optional)

try:
    api_response = api_instance.get_block_volume_samples(block_volume_id, duration_begin=duration_begin, duration_end=duration_end, period=period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->get_block_volume_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| block volume id | 
 **duration_begin** | **str**| duration begin timestamp | [optional] 
 **duration_end** | **str**| duration end timestamp | [optional] 
 **period** | **str**| samples period | [optional] 

### Return type

[**VolumeSamplesResp**](VolumeSamplesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_block_volumes**
> VolumesResp list_block_volumes(limit=limit, offset=offset, pool_id=pool_id, pool_name=pool_name, cluster_id=cluster_id, block_snapshot_id=block_snapshot_id, name=name, name_prefix=name_prefix, volume_name=volume_name, uid=uid, client_group_id=client_group_id, mapping_group_id=mapping_group_id, exclude_mapping_group_id=exclude_mapping_group_id, access_path_id=access_path_id, passive=passive, recycled=recycled, status=status, with_not_used=with_not_used, q=q, sort=sort, all=all, dp_block_backup_policy_id=dp_block_backup_policy_id, dp_block_async_replication_policy_id=dp_block_async_replication_policy_id, could_have_io=could_have_io)



List block volumes

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
pool_id = 789 # int | The id of the pool volumes belong to (optional)
pool_name = 'pool_name_example' # str | The pool_name of the pool volumes belong to (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)
block_snapshot_id = 789 # int | related snapshot id (optional)
name = 'name_example' # str | name of volume (optional)
name_prefix = 'name_prefix_example' # str | name prefix of volume (optional)
volume_name = 'volume_name_example' # str | volume_name of volume (optional)
uid = 'uid_example' # str | uid of volume (optional)
client_group_id = 789 # int | related client group id (optional)
mapping_group_id = 789 # int | related mapping group id (optional)
exclude_mapping_group_id = 789 # int | exclude mapping group id, with access path id (optional)
access_path_id = 789 # int | related access path id (optional)
passive = true # bool | passive or not (optional)
recycled = true # bool | recycled or not (optional)
status = 'status_example' # str | filter with status (optional)
with_not_used = true # bool | list with not used volumes, can be used with access path id (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
all = true # bool | show all volumes (optional)
dp_block_backup_policy_id = 789 # int | show volumes of specific dp block backup policy (optional)
dp_block_async_replication_policy_id = 789 # int | show volumes of specific dp block async replication policy (optional)
could_have_io = true # bool | show volumes without volume that cannot have io (optional)

try:
    api_response = api_instance.list_block_volumes(limit=limit, offset=offset, pool_id=pool_id, pool_name=pool_name, cluster_id=cluster_id, block_snapshot_id=block_snapshot_id, name=name, name_prefix=name_prefix, volume_name=volume_name, uid=uid, client_group_id=client_group_id, mapping_group_id=mapping_group_id, exclude_mapping_group_id=exclude_mapping_group_id, access_path_id=access_path_id, passive=passive, recycled=recycled, status=status, with_not_used=with_not_used, q=q, sort=sort, all=all, dp_block_backup_policy_id=dp_block_backup_policy_id, dp_block_async_replication_policy_id=dp_block_async_replication_policy_id, could_have_io=could_have_io)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->list_block_volumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **pool_id** | **int**| The id of the pool volumes belong to | [optional] 
 **pool_name** | **str**| The pool_name of the pool volumes belong to | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 
 **block_snapshot_id** | **int**| related snapshot id | [optional] 
 **name** | **str**| name of volume | [optional] 
 **name_prefix** | **str**| name prefix of volume | [optional] 
 **volume_name** | **str**| volume_name of volume | [optional] 
 **uid** | **str**| uid of volume | [optional] 
 **client_group_id** | **int**| related client group id | [optional] 
 **mapping_group_id** | **int**| related mapping group id | [optional] 
 **exclude_mapping_group_id** | **int**| exclude mapping group id, with access path id | [optional] 
 **access_path_id** | **int**| related access path id | [optional] 
 **passive** | **bool**| passive or not | [optional] 
 **recycled** | **bool**| recycled or not | [optional] 
 **status** | **str**| filter with status | [optional] 
 **with_not_used** | **bool**| list with not used volumes, can be used with access path id | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **all** | **bool**| show all volumes | [optional] 
 **dp_block_backup_policy_id** | **int**| show volumes of specific dp block backup policy | [optional] 
 **dp_block_async_replication_policy_id** | **int**| show volumes of specific dp block async replication policy | [optional] 
 **could_have_io** | **bool**| show volumes without volume that cannot have io | [optional] 

### Return type

[**VolumesResp**](VolumesResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_block_volume**
> VolumeResp migrate_block_volume(block_volume_id, body)



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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | the block volume id
body = xms_client.VolumeMigrateReq() # VolumeMigrateReq | volume migration info

try:
    api_response = api_instance.migrate_block_volume(block_volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->migrate_block_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| the block volume id | 
 **body** | [**VolumeMigrateReq**](VolumeMigrateReq.md)| volume migration info | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild_block_volume_replication**
> VolumeResp rebuild_block_volume_replication(block_volume_id, force=force)



Rebuild block volume replication

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | block volume id
force = true # bool | force rebuild or not (optional)

try:
    api_response = api_instance.rebuild_block_volume_replication(block_volume_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->rebuild_block_volume_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| block volume id | 
 **force** | **bool**| force rebuild or not | [optional] 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_async_replication_protection**
> VolumeResp set_async_replication_protection(block_volume_id, body)



Set async replication protection for a block volume

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | the block volume id
body = xms_client.VolumeAsyncReplicationProtectionReq() # VolumeAsyncReplicationProtectionReq | request info

try:
    api_response = api_instance.set_async_replication_protection(block_volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->set_async_replication_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| the block volume id | 
 **body** | [**VolumeAsyncReplicationProtectionReq**](VolumeAsyncReplicationProtectionReq.md)| request info | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_backup_protection**
> VolumeResp set_backup_protection(block_volume_id, body)



Set backup protection for a block volume

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | the block volume id
body = xms_client.VolumeBackupProtectionReq() # VolumeBackupProtectionReq | request info

try:
    api_response = api_instance.set_backup_protection(block_volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->set_backup_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| the block volume id | 
 **body** | [**VolumeBackupProtectionReq**](VolumeBackupProtectionReq.md)| request info | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_block_volume_crc**
> VolumeResp set_block_volume_crc(block_volume_id, body)



Set block volume crc

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | block volume id
body = xms_client.VolumeCrcSetReq() # VolumeCrcSetReq | volume crc info

try:
    api_response = api_instance.set_block_volume_crc(block_volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->set_block_volume_crc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| block volume id | 
 **body** | [**VolumeCrcSetReq**](VolumeCrcSetReq.md)| volume crc info | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_block_volume_replication**
> VolumeResp set_block_volume_replication(block_volume_id, body)



Set block volume replication

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | block volume id
body = xms_client.VolumeReplicationSetReq() # VolumeReplicationSetReq | volume replication info

try:
    api_response = api_instance.set_block_volume_replication(block_volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->set_block_volume_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| block volume id | 
 **body** | [**VolumeReplicationSetReq**](VolumeReplicationSetReq.md)| volume replication info | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_snapshot_protection**
> VolumeResp set_snapshot_protection(block_volume_id, body)



Set snapshot protection for a block volume

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | the block volume id
body = xms_client.VolumeSnapshotProtectionReq() # VolumeSnapshotProtectionReq | request info

try:
    api_response = api_instance.set_snapshot_protection(block_volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->set_snapshot_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| the block volume id | 
 **body** | [**VolumeSnapshotProtectionReq**](VolumeSnapshotProtectionReq.md)| request info | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_block_volume_replication**
> VolumeResp suspend_block_volume_replication(block_volume_id)



Suspend block volume replication

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | block volume id

try:
    api_response = api_instance.suspend_block_volume_replication(block_volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->suspend_block_volume_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| block volume id | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_async_replication_protection**
> VolumeResp unset_async_replication_protection(block_volume_id, force=force, reserve_volume=reserve_volume)



Unset async replication protection for a block volume

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | the block volume id
force = true # bool | force unset or not (optional)
reserve_volume = true # bool | reserve replicated volume or not (optional)

try:
    api_response = api_instance.unset_async_replication_protection(block_volume_id, force=force, reserve_volume=reserve_volume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->unset_async_replication_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| the block volume id | 
 **force** | **bool**| force unset or not | [optional] 
 **reserve_volume** | **bool**| reserve replicated volume or not | [optional] 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_backup_protection**
> VolumeResp unset_backup_protection(block_volume_id, force=force)



Unset backup protection for a block volume

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | the block volume id
force = true # bool | force unset or not (optional)

try:
    api_response = api_instance.unset_backup_protection(block_volume_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->unset_backup_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| the block volume id | 
 **force** | **bool**| force unset or not | [optional] 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_block_volume_crc**
> VolumeResp unset_block_volume_crc(block_volume_id, body)



Unset block volume crc

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | block volume id
body = xms_client.VolumeCrcSetReq() # VolumeCrcSetReq | volume crc info

try:
    api_response = api_instance.unset_block_volume_crc(block_volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->unset_block_volume_crc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| block volume id | 
 **body** | [**VolumeCrcSetReq**](VolumeCrcSetReq.md)| volume crc info | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_block_volume_replication**
> VolumeResp unset_block_volume_replication(block_volume_id)



Unset block volume replication

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | block volume id

try:
    api_response = api_instance.unset_block_volume_replication(block_volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->unset_block_volume_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| block volume id | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_snapshot_protection**
> VolumeResp unset_snapshot_protection(block_volume_id, force=force)



Unset snapshot protection for a block volume

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | the block volume id
force = true # bool | force unset or not (optional)

try:
    api_response = api_instance.unset_snapshot_protection(block_volume_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->unset_snapshot_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| the block volume id | 
 **force** | **bool**| force unset or not | [optional] 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_block_volume**
> VolumeResp update_block_volume(block_volume_id, body)



Update block volume info

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | the block volume id
body = xms_client.VolumeUpdateReq() # VolumeUpdateReq | volume info

try:
    api_response = api_instance.update_block_volume(block_volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->update_block_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| the block volume id | 
 **body** | [**VolumeUpdateReq**](VolumeUpdateReq.md)| volume info | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_block_volume_volume_name**
> VolumeResp update_block_volume_volume_name(block_volume_id, body)



Update block volume volume_name

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | the block volume id
body = xms_client.VolumeUpdateVolumeNameReq() # VolumeUpdateVolumeNameReq | volume volume_name

try:
    api_response = api_instance.update_block_volume_volume_name(block_volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->update_block_volume_volume_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| the block volume id | 
 **body** | [**VolumeUpdateVolumeNameReq**](VolumeUpdateVolumeNameReq.md)| volume volume_name | 

### Return type

[**VolumeResp**](VolumeResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_volume_stat**
> update_volume_stat(body)



update volume stat from other cluster

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
api_instance = xms_client.BlockVolumesApi(xms_client.ApiClient(configuration))
body = xms_client.UpdateVolumeStatReq() # UpdateVolumeStatReq | volume stat

try:
    api_instance.update_volume_stat(body)
except ApiException as e:
    print("Exception when calling BlockVolumesApi->update_volume_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateVolumeStatReq**](UpdateVolumeStatReq.md)| volume stat | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

