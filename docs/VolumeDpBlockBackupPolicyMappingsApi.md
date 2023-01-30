# xms_client.VolumeDpBlockBackupPolicyMappingsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_volume_dp_block_backup_policy_mappings**](VolumeDpBlockBackupPolicyMappingsApi.md#list_volume_dp_block_backup_policy_mappings) | **GET** /volume-dp-block-backup-policy-mappings/ | 


# **list_volume_dp_block_backup_policy_mappings**
> VolumeDpBlockBackupPolicyMappingsResp list_volume_dp_block_backup_policy_mappings(block_volume_id=block_volume_id, dp_block_backup_policy_id=dp_block_backup_policy_id)



List volume dp block backup policy mapping

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
api_instance = xms_client.VolumeDpBlockBackupPolicyMappingsApi(xms_client.ApiClient(configuration))
block_volume_id = 789 # int | show mappings of specific block volume (optional)
dp_block_backup_policy_id = 789 # int | show mappings of specific block volume (optional)

try:
    api_response = api_instance.list_volume_dp_block_backup_policy_mappings(block_volume_id=block_volume_id, dp_block_backup_policy_id=dp_block_backup_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeDpBlockBackupPolicyMappingsApi->list_volume_dp_block_backup_policy_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_volume_id** | **int**| show mappings of specific block volume | [optional] 
 **dp_block_backup_policy_id** | **int**| show mappings of specific block volume | [optional] 

### Return type

[**VolumeDpBlockBackupPolicyMappingsResp**](VolumeDpBlockBackupPolicyMappingsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

