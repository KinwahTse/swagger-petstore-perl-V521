# FSFolderRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_path** | [**AccessPathNestview**](AccessPathNestview.md) |  | [optional] 
**action_status** | **str** |  | [optional] 
**actual_status** | **str** |  | [optional] 
**block_volume** | [**VolumeNestview**](VolumeNestview.md) |  | [optional] 
**block_volume_status** | **str** |  | [optional] 
**cluster** | [**ClusterNestview**](ClusterNestview.md) |  | [optional] 
**create** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**dp_fs_snapshot_policy** | [**DpFSSnapshotPolicyNestview**](DpFSSnapshotPolicyNestview.md) |  | [optional] 
**flattened** | **bool** |  | [optional] 
**formatted** | **bool** |  | [optional] 
**fs_gateway_group** | [**FSGatewayGroup**](FSGatewayGroup.md) |  | [optional] 
**fs_quota_tree_num** | **int** |  | [optional] 
**fs_snapshot** | [**FSSnapshotNestview**](FSSnapshotNestview.md) |  | [optional] 
**fs_snapshot_num** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**latest_snapshot_time** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**pool** | [**PoolNestview**](PoolNestview.md) |  | [optional] 
**progress** | **float** |  | [optional] 
**qos** | [**VolumeQosSpec**](VolumeQosSpec.md) |  | [optional] 
**qos_enabled** | **bool** |  | [optional] 
**quota_tree_share_types** | **list[str]** |  | [optional] 
**quota_tree_shared** | **bool** |  | [optional] 
**share_types** | **list[str]** |  | [optional] 
**shared** | **bool** | before version 3.2.14, these fields was calculated by wizard, but there is quota trees in new verion, calculations is too complicated, so add the fields to folder struct | [optional] 
**size** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**update** | **datetime** |  | [optional] 
**samples** | [**list[FSFolderStat]**](FSFolderStat.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


