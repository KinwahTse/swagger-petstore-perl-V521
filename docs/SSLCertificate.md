# SSLCertificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | **datetime** | created time of certificate | [optional] 
**description** | **str** | certificate description | [optional] 
**enabled** | **bool** | enabled or not | [optional] 
**force_https** | **bool** | redirect http request to https | [optional] 
**id** | **int** | certificate id | [optional] 
**issuer** | **object** | issuer info | [optional] 
**name** | **str** | certificate name | [optional] 
**not_after** | **datetime** | validity is not after the time | [optional] 
**not_before** | **datetime** | validity is not before the time | [optional] 
**permitted_dns_domains** | **list[object]** | permitted dns domains | [optional] 
**public_key_algorithm** | **str** | public key algorithm | [optional] 
**raw_certificate** | **str** | public certificate | [optional] 
**signature_algorithm** | **str** | signature algorithm | [optional] 
**status** | **str** |  | [optional] 
**subject** | **object** | subject info | [optional] 
**type** | **str** | applied type: admin, s3, dfs_s3 | [optional] 
**update** | **datetime** | updated time of certificate | [optional] 
**version** | **int** | certificate version | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


