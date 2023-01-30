# S3LoadBalancerGroupCreateReqGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | group description | [optional] 
**https_port** | **int** | group access https port | [optional] 
**name** | **str** | group name | 
**oss_api_enabled** | **bool** |  | [optional] 
**port** | **int** | group access http port | [optional] 
**roles** | **list[str]** | group roles | [optional] 
**s3_load_balancers** | [**list[S3LoadBalancerGroupCreateReqGroupLoadBalancersElt]**](S3LoadBalancerGroupCreateReqGroupLoadBalancersElt.md) | s3 load balancers | 
**search_https_port** | **int** | group search https port | [optional] 
**search_port** | **int** | group search http port | [optional] 
**sync_port** | **int** | group sync http port | [optional] 
**web_service_config** | [**S3LbGroupWebServiceConfig**](S3LbGroupWebServiceConfig.md) | web service config | [optional] 
**web_service_port** | **int** | group web service http port | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


