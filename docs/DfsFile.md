# DfsFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **datetime** | access time | [optional] 
**change** | **datetime** | change time | [optional] 
**dfs_path_id** | **int** | dfs path id | [optional] 
**dfs_rootfs** | [**NestedRootfs**](NestedRootfs.md) | dfs rootfs | [optional] 
**dp_snapshot_num** | **int** | count of data protection snapshot | [optional] 
**files** | **int** | sub file count when it is a directory | [optional] 
**group** | **int** | owner group | [optional] 
**hdfs_num** | **int** | count of hdfs | [optional] 
**inode** | **int** | inode count | [optional] 
**is_bucket** | **bool** | is bucket path | [optional] 
**is_bucket_parent** | **bool** | is bucked parent path | [optional] 
**modify** | **datetime** | modify time | [optional] 
**name** | **str** | file name | [optional] 
**original_name** | **str** | original name before file moved to trash | [optional] 
**owner** | **int** | owner user | [optional] 
**parent** | **str** | parent path | [optional] 
**path** | **str** | full path | [optional] 
**quota_num** | **int** | count of quota | [optional] 
**shared** | **bool** | shared | [optional] 
**shares** | **list[str]** | share types | [optional] 
**size** | **int** | file size | [optional] 
**snapshot_num** | **int** | count of snapshot | [optional] 
**total_snapshot_num** | **int** | count of total snapshot | [optional] 
**trash** | [**DfsFileTrash**](DfsFileTrash.md) | dfs trash resource | [optional] 
**type** | **str** | file type | [optional] 
**worm** | [**DfsFileWorm**](DfsFileWorm.md) | worm info | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


