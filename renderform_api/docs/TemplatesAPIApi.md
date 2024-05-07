# openapi_client.TemplatesAPIApi

All URIs are relative to *https://api.renderform.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_template**](TemplatesAPIApi.md#get_my_template) | **GET** /api/v2/my-templates/{templateId} | 
[**get_my_templates**](TemplatesAPIApi.md#get_my_templates) | **GET** /api/v2/my-templates | 


# **get_my_template**
> GetTemplateBasics get_my_template(template_id)



### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.get_template_basics import GetTemplateBasics
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.renderform.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.renderform.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TemplatesAPIApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        api_response = api_instance.get_my_template(template_id)
        print("The response of TemplatesAPIApi->get_my_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesAPIApi->get_my_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**GetTemplateBasics**](GetTemplateBasics.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**418** | I&#39;m a teapot |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_templates**
> List[MyTemplateEntryV2] get_my_templates(pageable, name=name)



### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.my_template_entry_v2 import MyTemplateEntryV2
from openapi_client.models.swagger_pageable import SwaggerPageable
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.renderform.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.renderform.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TemplatesAPIApi(api_client)
    pageable = openapi_client.SwaggerPageable() # SwaggerPageable | Pagination
    name = 'name_example' # str | Filter by template name (optional)

    try:
        api_response = api_instance.get_my_templates(pageable, name=name)
        print("The response of TemplatesAPIApi->get_my_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesAPIApi->get_my_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | [**SwaggerPageable**](.md)| Pagination | 
 **name** | **str**| Filter by template name | [optional] 

### Return type

[**List[MyTemplateEntryV2]**](MyTemplateEntryV2.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**418** | I&#39;m a teapot |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

