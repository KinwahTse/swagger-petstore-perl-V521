# HostCreateReqHost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_ip** | **str** | admin ip | 
**cluster_id** | **int** | cluster id | [optional] 
**description** | **str** | host description | [optional] 
**gateway_ips** | **list[str]** | gateway ips for s3 | [optional] 
**meta_device** | **str** | meta device for docker | [optional] 
**private_ip** | **str** | cluster private ip for internal data access | [optional] 
**protection_domain_id** | **int** | deprecated | [optional] 
**public_ip** | **str** | public ip for outside data access | [optional] 
**roles** | **list[str]** | host roles: admin,monitor,block_storage_gateway,file_storage_gateway,s3_gateway,nfs_gateway | [optional] 
**type** | **str** | storage server or storage client | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


