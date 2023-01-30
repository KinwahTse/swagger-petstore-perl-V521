# PoolGCPolicyReqGCPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | 
**reserve_ratio** | **int** |  | [optional] 
**scan** | **bool** |  | [optional] 
**scan_water** | **int** |  | [optional] 
**stop_decrement** | **int** |  | [optional] 
**throttle_bandwidth_base** | **int** | bandwidth &#x3D; throttle_bandwidth_base + (base_pool.water - water) * throttle_bandwidth_step | [optional] 
**throttle_bandwidth_step** | **int** |  | [optional] 
**water_level** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


