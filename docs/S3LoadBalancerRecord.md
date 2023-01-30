# S3LoadBalancerRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**ClusterNestview**](ClusterNestview.md) |  | [optional] 
**create** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**group** | [**S3LoadBalancerGroupNestview**](S3LoadBalancerGroupNestview.md) |  | [optional] 
**host** | [**HostNestview**](HostNestview.md) |  | [optional] 
**https_port** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**interface_name** | **str** | the interface where vip is bound, exclusive to ip | [optional] 
**ip** | **str** | the interface of ip where vip is bound, exclusive to interface_name | [optional] 
**name** | **str** |  | [optional] 
**oss_api_enabled** | **bool** |  | [optional] 
**port** | **int** |  | [optional] 
**roles** | **list[str]** |  | [optional] 
**search_https_port** | **int** |  | [optional] 
**search_port** | **int** |  | [optional] 
**ssl_certificate** | [**SSLCertificateNestview**](SSLCertificateNestview.md) |  | [optional] 
**status** | **str** |  | [optional] 
**sync_port** | **int** |  | [optional] 
**update** | **datetime** |  | [optional] 
**vip** | **str** | designated(master) vip | [optional] 
**vip_mask** | **int** | mask of vip, default: 32 | [optional] 
**vips** | **str** | current effective vips | [optional] 
**web_service_port** | **int** |  | [optional] 
**samples** | [**list[S3LoadBalancerStat]**](S3LoadBalancerStat.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


