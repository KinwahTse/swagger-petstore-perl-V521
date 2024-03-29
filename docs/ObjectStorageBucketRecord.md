# ObjectStorageBucketRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_status** | **str** |  | [optional] 
**all_user_permission** | **str** |  | [optional] 
**auth_user_permission** | **str** |  | [optional] 
**bucket_policy** | **str** |  | [optional] 
**cluster** | [**ClusterNestview**](ClusterNestview.md) |  | [optional] 
**create** | **datetime** |  | [optional] 
**delete_archive_storage_class** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**external_quota_max_objects** | **int** |  | [optional] 
**external_quota_max_size** | **int** |  | [optional] 
**flag** | [**BucketFlag**](BucketFlag.md) |  | [optional] 
**id** | **int** |  | [optional] 
**lifecycle** | [**ObjectStorageLifecycle**](ObjectStorageLifecycle.md) |  | [optional] 
**local_quota_max_objects** | **int** |  | [optional] 
**local_quota_max_size** | **int** |  | [optional] 
**log_delivery_permission** | **str** |  | [optional] 
**logging_enabled** | **bool** |  | [optional] 
**logging_grants** | [**list[OSBucketLoggingGrant]**](OSBucketLoggingGrant.md) |  | [optional] 
**logging_owner** | [**ObjectStorageUserNestview**](ObjectStorageUserNestview.md) |  | [optional] 
**logging_prefix** | **str** |  | [optional] 
**logging_suspended** | **bool** |  | [optional] 
**logging_target_bucket** | [**ObjectStorageBucketNestview**](ObjectStorageBucketNestview.md) |  | [optional] 
**metadata_search_enabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**nfs_client_num** | **int** |  | [optional] 
**object_cover** | [**OSBucketObjectCoverConf**](OSBucketObjectCoverConf.md) |  | [optional] 
**object_storage_class** | [**OSBucketObjectStorageClass**](OSBucketObjectStorageClass.md) |  | [optional] 
**os_replication_path_num** | **int** |  | [optional] 
**os_replication_zone_num** | **int** |  | [optional] 
**os_zone** | [**ObjectStorageZoneNestview**](ObjectStorageZoneNestview.md) |  | [optional] 
**os_zone_uuid** | **str** |  | [optional] 
**owner** | [**ObjectStorageUserNestview**](ObjectStorageUserNestview.md) |  | [optional] 
**owner_permission** | **str** |  | [optional] 
**policy** | [**ObjectStoragePolicyNestview**](ObjectStoragePolicyNestview.md) |  | [optional] 
**policy_enabled** | **bool** |  | [optional] 
**qos** | [**OSBucketQos**](OSBucketQos.md) |  | [optional] 
**quota_max_objects** | **int** |  | [optional] 
**quota_max_size** | **int** |  | [optional] 
**remote_cluster** | [**RemoteClusterNestview**](RemoteClusterNestview.md) |  | [optional] 
**replication_uuid** | **str** | NOTE: Use name of bucket as replication uuid for simplicity | [optional] 
**restore_days** | **int** |  | [optional] 
**shards** | **int** |  | [optional] 
**specification_objects** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**update** | **datetime** |  | [optional] 
**virtual** | **bool** |  | [optional] 
**samples** | [**list[ObjectStorageBucketStat]**](ObjectStorageBucketStat.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


