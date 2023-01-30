# FSGatewayGroupCreateReqGatewayGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description of gateway group | [optional] 
**encoding** | **str** | ftp encoding format, default is utf8 | [optional] 
**fs_gateways** | [**list[FSGatewayReq]**](FSGatewayReq.md) | file storage gateways list | 
**name** | **str** | name of gateway group | 
**nfs_versions** | **list[str]** | nfs versions of nfs supported | [optional] 
**security** | **str** | smb security type | [optional] 
**smb1_enabled** | **bool** | smb version 1.0 enabled | [optional] 
**smb_ports** | **list[int]** | smb ports | [optional] 
**types** | **list[str]** | types of supported (smb, nfs, ftp) | 
**vip** | **str** | virtual ip of gateway group | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


