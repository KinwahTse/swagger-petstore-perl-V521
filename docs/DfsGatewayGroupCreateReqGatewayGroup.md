# DfsGatewayGroupCreateReqGatewayGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description of gateway group | [optional] 
**dfs_gateways** | [**list[DfsGatewayReq]**](DfsGatewayReq.md) | dfs gateways list | 
**dfs_vip_gateways** | **list[str]** | VIPGateways contains all the gateways of VIP network | [optional] 
**dfs_vips** | **list[str]** | VIPs of gateway group | 
**encoding** | **str** | ftp encoding format, default is utf8 | [optional] 
**name** | **str** | name of gateway group | 
**nfs_versions** | **list[str]** | nfs versions of nfs supported | [optional] 
**securities** | **list[str]** | smb security type | [optional] 
**smb1_enabled** | **bool** | smb version 1.0 enabled | [optional] 
**smb_ports** | **list[int]** | smb ports | [optional] 
**types** | **list[str]** | types of supported (smb, nfs, ftp) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


