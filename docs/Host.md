# Host

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_status** | **str** |  | [optional] 
**admin_ip** | **str** |  | 
**clock_diff** | **int** | clock diff in milliseconds with primary host | [optional] 
**cluster** | [**ClusterNestview**](ClusterNestview.md) |  | [optional] 
**cores** | **int** |  | [optional] 
**cpu_arch** | **str** |  | [optional] 
**cpu_model** | **str** |  | [optional] 
**create** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**disk_num** | **int** |  | [optional] 
**enclosures** | **list[object]** |  | [optional] 
**fcports** | [**list[FCPort]**](FCPort.md) | fc ports of host | [optional] 
**gateway_ips** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_master_db** | **bool** |  | [optional] 
**kvm_status** | [**HostKVMStatus**](HostKVMStatus.md) |  | [optional] 
**memory_kbyte** | **int** |  | [optional] 
**model** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**numa_nodes** | **str** |  | [optional] 
**os** | **str** |  | [optional] 
**placement_node** | [**PlacementNode**](PlacementNode.md) |  | [optional] 
**private_ip** | **str** |  | [optional] 
**protection_domain** | [**ProtectionDomainNestview**](ProtectionDomainNestview.md) | protection domain of host | [optional] 
**public_ips** | **str** |  | [optional] 
**rack** | **str** |  | [optional] 
**roles** | **str** |  | [optional] 
**root_disk** | [**DiskNestview**](DiskNestview.md) |  | [optional] 
**serial** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**up** | **bool** |  | [optional] 
**update** | **datetime** |  | [optional] 
**vendor** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


