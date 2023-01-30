# xms_client.BlockVolumeGroupsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_block_volume_group**](BlockVolumeGroupsApi.md#create_block_volume_group) | **POST** /block-volume-groups/ | 
[**delete_block_volume_group**](BlockVolumeGroupsApi.md#delete_block_volume_group) | **DELETE** /block-volume-groups/{block_volume_group_id} | 
[**get_block_volume_group**](BlockVolumeGroupsApi.md#get_block_volume_group) | **GET** /block-volume-groups/{block_volume_group_id} | 
[**list_block_volume_groups**](BlockVolumeGroupsApi.md#list_block_volume_groups) | **GET** /block-volume-groups/ | 
[**rollback_volume_group**](BlockVolumeGroupsApi.md#rollback_volume_group) | **POST** /block-volume-groups/{block_volume_group_id}:rollback | 
[**set_volume_group_snapshot_replication_protection**](BlockVolumeGroupsApi.md#set_volume_group_snapshot_replication_protection) | **POST** /block-volume-groups/{block_volume_group_id}:set-snapshot-replication-protection | 
[**unset_volume_group_snapshot_replication_protection**](BlockVolumeGroupsApi.md#unset_volume_group_snapshot_replication_protection) | **POST** /block-volume-groups/{block_volume_group_id}:unset-snapshot-replication-protection | 
[**update_block_volume_group**](BlockVolumeGroupsApi.md#update_block_volume_group) | **PATCH** /block-volume-groups/{block_volume_group_id} | 


# **create_block_volume_group**
> VolumeGroupResp create_block_volume_group(body, cluster_id=cluster_id)



Create block volume group

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
api_instance = xms_client.BlockVolumeGroupsApi(xms_client.ApiClient(configuration))
body = xms_client.VolumeGroupCreateReq() # VolumeGroupCreateReq | volume group info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_block_volume_group(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupsApi->create_block_volume_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VolumeGroupCreateReq**](VolumeGroupCreateReq.md)| volume group info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**VolumeGroupResp**](VolumeGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_block_volume_group**
> VolumeGroupResp delete_block_volume_group(block_volume_group_id)



Delete a block volume group

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
api_instance = xms_client.BlockVolumeGroupsApi(xms_client.ApiClient(configuration))
block_volume_group_id = 789 # int | block volume group id

try:
    api_response = api_instance.delete_block_volume_group(block_volume_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupsApi->delete_block_volume_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_group_id** | **int**| block volume group id | 

### Return type

[**VolumeGroupResp**](VolumeGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_volume_group**
> VolumeGroupResp get_block_volume_group(block_volume_group_id)



get a block volume group

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
api_instance = xms_client.BlockVolumeGroupsApi(xms_client.ApiClient(configuration))
block_volume_group_id = 789 # int | block volume group id

try:
    api_response = api_instance.get_block_volume_group(block_volume_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupsApi->get_block_volume_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_group_id** | **int**| block volume group id | 

### Return type

[**VolumeGroupResp**](VolumeGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_block_volume_groups**
> VolumeGroupsResp list_block_volume_groups(cluster_id=cluster_id, passive=passive, name=name, limit=limit, offset=offset, q=q, sort=sort, dp_volume_group_snapshot_replication_policy_id=dp_volume_group_snapshot_replication_policy_id)



List block volume groups

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
api_instance = xms_client.BlockVolumeGroupsApi(xms_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | cluster id (optional)
passive = true # bool | passive or not (optional)
name = 'name_example' # str | name of volume group (optional)
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
q = 'q_example' # str | query param of search (optional)
sort = 'sort_example' # str | sort param of search (optional)
dp_volume_group_snapshot_replication_policy_id = 789 # int | show volume groups of specific dp block async replication policy (optional)

try:
    api_response = api_instance.list_block_volume_groups(cluster_id=cluster_id, passive=passive, name=name, limit=limit, offset=offset, q=q, sort=sort, dp_volume_group_snapshot_replication_policy_id=dp_volume_group_snapshot_replication_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupsApi->list_block_volume_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| cluster id | [optional] 
 **passive** | **bool**| passive or not | [optional] 
 **name** | **str**| name of volume group | [optional] 
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **q** | **str**| query param of search | [optional] 
 **sort** | **str**| sort param of search | [optional] 
 **dp_volume_group_snapshot_replication_policy_id** | **int**| show volume groups of specific dp block async replication policy | [optional] 

### Return type

[**VolumeGroupsResp**](VolumeGroupsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_volume_group**
> VolumeGroupResp rollback_volume_group(block_volume_group_id, body)



Rollback volume group

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
api_instance = xms_client.BlockVolumeGroupsApi(xms_client.ApiClient(configuration))
block_volume_group_id = 789 # int | block volume group id
body = xms_client.VolumeGroupRollbackReq() # VolumeGroupRollbackReq | rollback info

try:
    api_response = api_instance.rollback_volume_group(block_volume_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupsApi->rollback_volume_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_group_id** | **int**| block volume group id | 
 **body** | [**VolumeGroupRollbackReq**](VolumeGroupRollbackReq.md)| rollback info | 

### Return type

[**VolumeGroupResp**](VolumeGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_volume_group_snapshot_replication_protection**
> VolumeGroupResp set_volume_group_snapshot_replication_protection(block_volume_group_id, body)



Set snapshot replication protection for a volume group

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
api_instance = xms_client.BlockVolumeGroupsApi(xms_client.ApiClient(configuration))
block_volume_group_id = 789 # int | the block volume group id
body = xms_client.VolumeGroupSnapshotReplicationProtectionReq() # VolumeGroupSnapshotReplicationProtectionReq | request info

try:
    api_response = api_instance.set_volume_group_snapshot_replication_protection(block_volume_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupsApi->set_volume_group_snapshot_replication_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_group_id** | **int**| the block volume group id | 
 **body** | [**VolumeGroupSnapshotReplicationProtectionReq**](VolumeGroupSnapshotReplicationProtectionReq.md)| request info | 

### Return type

[**VolumeGroupResp**](VolumeGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_volume_group_snapshot_replication_protection**
> VolumeGroupResp unset_volume_group_snapshot_replication_protection(block_volume_group_id, force=force, reserve_volume_group=reserve_volume_group)



Unset volume group snapshot replication protection for a volume group

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
api_instance = xms_client.BlockVolumeGroupsApi(xms_client.ApiClient(configuration))
block_volume_group_id = 789 # int | the volume group id
force = true # bool | force unset or not (optional)
reserve_volume_group = true # bool | reserve replicated volume group or not (optional)

try:
    api_response = api_instance.unset_volume_group_snapshot_replication_protection(block_volume_group_id, force=force, reserve_volume_group=reserve_volume_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupsApi->unset_volume_group_snapshot_replication_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_group_id** | **int**| the volume group id | 
 **force** | **bool**| force unset or not | [optional] 
 **reserve_volume_group** | **bool**| reserve replicated volume group or not | [optional] 

### Return type

[**VolumeGroupResp**](VolumeGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_block_volume_group**
> VolumeGroupResp update_block_volume_group(block_volume_group_id, body)



Update block volume group

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
api_instance = xms_client.BlockVolumeGroupsApi(xms_client.ApiClient(configuration))
block_volume_group_id = 789 # int | block volume group id
body = xms_client.VolumeGroupUpdateReq() # VolumeGroupUpdateReq | volume group info

try:
    api_response = api_instance.update_block_volume_group(block_volume_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockVolumeGroupsApi->update_block_volume_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_group_id** | **int**| block volume group id | 
 **body** | [**VolumeGroupUpdateReq**](VolumeGroupUpdateReq.md)| volume group info | 

### Return type

[**VolumeGroupResp**](VolumeGroupResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

