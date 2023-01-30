# xms_client.FsLdapsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fs_ldap**](FsLdapsApi.md#create_fs_ldap) | **POST** /fs-ldaps/ | 
[**delete_fs_ldap**](FsLdapsApi.md#delete_fs_ldap) | **DELETE** /fs-ldaps/{fs_ldap_id} | 
[**get_fs_ldap**](FsLdapsApi.md#get_fs_ldap) | **GET** /fs-ldaps/{fs_ldap_id} | 
[**list_fs_ldaps**](FsLdapsApi.md#list_fs_ldaps) | **GET** /fs-ldaps/ | 
[**update_fs_ldap**](FsLdapsApi.md#update_fs_ldap) | **PATCH** /fs-ldaps/{fs_ldap_id} | 
[**verify_fs_ldap**](FsLdapsApi.md#verify_fs_ldap) | **POST** /fs-ldaps/{fs_ldap_id}:verify | 


# **create_fs_ldap**
> FSLdapResp create_fs_ldap(body, cluster_id=cluster_id)



create file storage ldap

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsLdapsApi(xms_client.ApiClient(configuration))
body = xms_client.FSLdapCreateReq() # FSLdapCreateReq | file storage ldap info
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.create_fs_ldap(body, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsLdapsApi->create_fs_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FSLdapCreateReq**](FSLdapCreateReq.md)| file storage ldap info | 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**FSLdapResp**](FSLdapResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fs_ldap**
> delete_fs_ldap(fs_ldap_id)



Delete file storage ldap

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsLdapsApi(xms_client.ApiClient(configuration))
fs_ldap_id = 789 # int | file storage ldap id

try:
    api_instance.delete_fs_ldap(fs_ldap_id)
except ApiException as e:
    print("Exception when calling FsLdapsApi->delete_fs_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_ldap_id** | **int**| file storage ldap id | 

### Return type

void (empty response body)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fs_ldap**
> FSLdapResp get_fs_ldap(fs_ldap_id)



Get a file storage ldap

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsLdapsApi(xms_client.ApiClient(configuration))
fs_ldap_id = 789 # int | file storage ldap id

try:
    api_response = api_instance.get_fs_ldap(fs_ldap_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsLdapsApi->get_fs_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_ldap_id** | **int**| file storage ldap id | 

### Return type

[**FSLdapResp**](FSLdapResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fs_ldaps**
> FSLdapsResp list_fs_ldaps(limit=limit, offset=offset, cluster_id=cluster_id)



List file storage ldaps

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsLdapsApi(xms_client.ApiClient(configuration))
limit = 789 # int | paging param (optional)
offset = 789 # int | paging param (optional)
cluster_id = 'cluster_id_example' # str | cluster id (optional)

try:
    api_response = api_instance.list_fs_ldaps(limit=limit, offset=offset, cluster_id=cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsLdapsApi->list_fs_ldaps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| paging param | [optional] 
 **offset** | **int**| paging param | [optional] 
 **cluster_id** | **str**| cluster id | [optional] 

### Return type

[**FSLdapsResp**](FSLdapsResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fs_ldap**
> FSLdapResp update_fs_ldap(fs_ldap_id, body)



Update a file storage ldap

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsLdapsApi(xms_client.ApiClient(configuration))
fs_ldap_id = 789 # int | file storage ldap id
body = xms_client.FSLdapUpdateReq() # FSLdapUpdateReq | file storage ldap info

try:
    api_response = api_instance.update_fs_ldap(fs_ldap_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsLdapsApi->update_fs_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_ldap_id** | **int**| file storage ldap id | 
 **body** | [**FSLdapUpdateReq**](FSLdapUpdateReq.md)| file storage ldap info | 

### Return type

[**FSLdapResp**](FSLdapResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_fs_ldap**
> FSLdapResp verify_fs_ldap(fs_ldap_id)



Verify a file storage ldap

### Example
```python
from __future__ import print_function
import time
import xms_client
from xms_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: tokenInHeader
configuration = xms_client.Configuration()
configuration.api_key['Xms-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Xms-Auth-Token'] = 'Bearer'
# Configure API key authorization: tokenInQuery
configuration = xms_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = xms_client.FsLdapsApi(xms_client.ApiClient(configuration))
fs_ldap_id = 789 # int | file storage ldap id

try:
    api_response = api_instance.verify_fs_ldap(fs_ldap_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsLdapsApi->verify_fs_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_ldap_id** | **int**| file storage ldap id | 

### Return type

[**FSLdapResp**](FSLdapResp.md)

### Authorization

[tokenInHeader](../README.md#tokenInHeader), [tokenInQuery](../README.md#tokenInQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

