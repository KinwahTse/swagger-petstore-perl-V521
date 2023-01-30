# VolumeCreateReqVolume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_snapshot_id** | **int** | id of related block volume snapshot | [optional] 
**crc_check** | **bool** | crc check or not | [optional] 
**description** | **str** | description of volume | [optional] 
**flattened** | **bool** | flatten or not flatten | [optional] 
**format** | **int** | volume format: { 128 | 129 (advanced) }, default 128 | [optional] 
**name** | **str** | name of volume | 
**performance_priority** | **int** | performance priority: { 0 | 1 }, default 0 | [optional] 
**pool_id** | **int** | id of pool belonged to | 
**qos** | [**VolumeQosSpec**](VolumeQosSpec.md) | qos of volume | [optional] 
**qos_enabled** | **bool** | enable or disable the qos | [optional] 
**remote_cluster_fs_id** | **str** | replication remote cluster fsid | [optional] 
**replication_pool** | **str** | replication peer pool | [optional] 
**replication_pool_id** | **int** | replication peer pool id | [optional] 
**replication_pool_name** | **str** | replication peer pool name | [optional] 
**replication_version** | **int** | replication version | [optional] 
**replication_volume** | **str** | replication peer volume | [optional] 
**replication_volume_id** | **int** | replication peer volume id | [optional] 
**replication_volume_name** | **str** | replication peer volume name | [optional] 
**size** | **int** | size of volume | [optional] 
**sn** | **str** | volume sn, used when creating replication volume | [optional] 
**snapshot_replication_pool** | **str** | snapshot replication peer pool | [optional] 
**snapshot_replication_pool_id** | **int** | snapshot replication peer pool id | [optional] 
**snapshot_replication_volume** | **str** | snapshot replication peer volume | [optional] 
**snapshot_replication_volume_id** | **int** | snapshot replication peer volume id | [optional] 
**uid** | **str** | UID of volume | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


