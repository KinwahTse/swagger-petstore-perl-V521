# ObjectStorageBucketStat

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_obj_category** | [**OSBucketUsageCategory**](OSBucketUsageCategory.md) |  | [optional] 
**get_obj_category** | [**OSBucketUsageCategory**](OSBucketUsageCategory.md) |  | [optional] 
**list_bucket_category** | [**OSBucketUsageCategory**](OSBucketUsageCategory.md) |  | [optional] 
**objects** | **int** |  | [optional] 
**post_obj_category** | [**OSBucketUsageCategory**](OSBucketUsageCategory.md) |  | [optional] 
**put_obj_category** | [**OSBucketUsageCategory**](OSBucketUsageCategory.md) |  | [optional] 
**used_capacity_bytes** | **dict(str, int)** |  | [optional] 
**allocated_objects** | **int** |  | [optional] 
**allocated_size** | **int** |  | [optional] 
**cache_allocated_objects** | **int** |  | [optional] 
**cache_allocated_size** | **int** |  | [optional] 
**create** | **datetime** |  | [optional] 
**del_ops_pm** | **float** |  | [optional] 
**down_latency_us** | **float** |  | [optional] 
**external_allocated_objects** | **int** |  | [optional] 
**external_allocated_size** | **int** |  | [optional] 
**latency_down** | **int** |  | [optional] 
**latency_up** | **int** |  | [optional] 
**list_ops_pm** | **float** |  | [optional] 
**local_allocated_objects** | **int** |  | [optional] 
**local_allocated_size** | **int** |  | [optional] 
**num_down** | **int** |  | [optional] 
**num_up** | **int** |  | [optional] 
**rx_bandwidth_kbyte** | **float** |  | [optional] 
**rx_ops_pm** | **float** |  | [optional] 
**storage_classes** | [**dict(str, OSStorageClassStat)**](OSStorageClassStat.md) |  | [optional] 
**total_del_ops** | **int** |  | [optional] 
**total_del_success_ops** | **int** |  | [optional] 
**total_rx_bytes** | **int** |  | [optional] 
**total_rx_ops** | **int** |  | [optional] 
**total_rx_success_ops** | **int** |  | [optional] 
**total_tx_bytes** | **int** |  | [optional] 
**total_tx_ops** | **int** |  | [optional] 
**total_tx_success_ops** | **int** |  | [optional] 
**tx_bandwidth_kbyte** | **float** |  | [optional] 
**tx_ops_pm** | **float** |  | [optional] 
**up_latency_us** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


