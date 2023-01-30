# ObjectStorageBucketCreateReqBucket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_user_permission** | **str** | permission setting of all users | [optional] 
**auth_user_permission** | **str** | permission setting of authenticated users | [optional] 
**delete_archive_storage_class** | **str** | delete archive storage class | [optional] 
**description** | **str** | bucket description | [optional] 
**external_quota_max_objects** | **int** | max number of external storage objects | [optional] 
**external_quota_max_size** | **int** | max size of external storage objects | [optional] 
**flag** | [**BucketFlag**](BucketFlag.md) | bucket options | [optional] 
**local_quota_max_objects** | **int** | max number of local storage objects | [optional] 
**local_quota_max_size** | **int** | max size of local storage objects | [optional] 
**log_delivery_permission** | **str** | permission setting of log delivery group | [optional] 
**name** | **str** | bucket name | 
**object_cover** | [**OSBucketObjectCoverConf**](OSBucketObjectCoverConf.md) |  | [optional] 
**object_storage_class** | [**OSBucketObjectStorageClass**](OSBucketObjectStorageClass.md) | bucket object storage class | [optional] 
**owner_id** | **int** | bucket owner | 
**owner_permission** | **str** | permission setting of owner | [optional] 
**policy_id** | **int** | storage policy | 
**quota_max_objects** | **int** | max number of objects | [optional] 
**quota_max_size** | **int** | max size of all objects | [optional] 
**restore_days** | **int** | restore expiration days | [optional] 
**specification_objects** | **int** | specification objects | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


