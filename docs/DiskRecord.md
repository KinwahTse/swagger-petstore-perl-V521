# DiskRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_status** | **str** |  | [optional] 
**bytes** | **int** | size of disk | [optional] 
**cache_create** | **datetime** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**cluster** | [**ClusterNestview**](ClusterNestview.md) |  | [optional] 
**controller_id** | **str** |  | [optional] 
**create** | **datetime** |  | [optional] 
**device** | **str** |  | [optional] 
**disk_type** | **str** |  | [optional] 
**driver_type** | **str** |  | [optional] 
**enclosure_id** | **str** |  | [optional] 
**host** | [**HostNestview**](HostNestview.md) |  | [optional] 
**id** | **int** |  | [optional] 
**is_cache** | **bool** | used as cache disk, deprecated | [optional] 
**is_root** | **bool** | used as root disk, deprecated | [optional] 
**lighting_status** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**partition_num** | **int** |  | [optional] 
**partitions** | [**list[Partition]**](Partition.md) |  | [optional] 
**power_safe** | **bool** |  | [optional] 
**raid_status** | **str** |  | [optional] 
**rotation_rate** | **str** |  | [optional] 
**rotational** | **bool** |  | [optional] 
**serial** | **str** |  | [optional] 
**slot_id** | **str** |  | [optional] 
**smart_attrs** | [**list[SmartAttr]**](SmartAttr.md) |  | [optional] 
**ssd_life_left** | **int** |  | [optional] 
**ssd_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update** | **datetime** |  | [optional] 
**usage** | **str** | disk usage | [optional] 
**used** | **bool** | disk is used, deprecated | [optional] 
**wwid** | **str** |  | [optional] 
**samples** | [**list[DiskStat]**](DiskStat.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


