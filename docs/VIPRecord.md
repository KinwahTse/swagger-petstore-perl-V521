# VIPRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_status** | **str** |  | [optional] 
**create** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**ip** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**mask** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**update** | **datetime** |  | [optional] 
**vip_group** | [**VIPGroupNestview**](VIPGroupNestview.md) |  | [optional] 
**virtual_router_id** | **int** |  | [optional] 
**current_vip_instance** | [**VIPInstanceNestview**](VIPInstanceNestview.md) |  | [optional] 
**default_vip_instance** | [**VIPInstanceNestview**](VIPInstanceNestview.md) | Copy these two fields from corresponding fields of VIP to avoid JSON marshal recursion. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


