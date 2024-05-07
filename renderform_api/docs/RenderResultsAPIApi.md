# openapi_client.RenderResultsAPIApi

All URIs are relative to *https://api.renderform.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_content**](RenderResultsAPIApi.md#delete_content) | **DELETE** /api/v2/results/{identifier} | 
[**get_render_result**](RenderResultsAPIApi.md#get_render_result) | **GET** /api/v2/results/{identifier} | 
[**get_render_results**](RenderResultsAPIApi.md#get_render_results) | **GET** /api/v2/results | 


# **delete_content**
> delete_content(identifier)



### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
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
    api_instance = openapi_client.RenderResultsAPIApi(api_client)
    identifier = 'identifier_example' # str | 

    try:
        api_instance.delete_content(identifier)
    except Exception as e:
        print("Exception when calling RenderResultsAPIApi->delete_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 

### Return type

void (empty response body)

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

# **get_render_result**
> RenderResultDetails get_render_result(identifier)



### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.render_result_details import RenderResultDetails
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
    api_instance = openapi_client.RenderResultsAPIApi(api_client)
    identifier = 'identifier_example' # str | 

    try:
        api_response = api_instance.get_render_result(identifier)
        print("The response of RenderResultsAPIApi->get_render_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenderResultsAPIApi->get_render_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 

### Return type

[**RenderResultDetails**](RenderResultDetails.md)

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

# **get_render_results**
> PageRenderResultItem get_render_results(pageable, template=template, batch=batch)



### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.page_render_result_item import PageRenderResultItem
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
    api_instance = openapi_client.RenderResultsAPIApi(api_client)
    pageable = openapi_client.SwaggerPageable() # SwaggerPageable | Pagination
    template = 'template_example' # str | Template identifier (optional)
    batch = 'batch_example' # str | Batch identifier for the render request (optional)

    try:
        api_response = api_instance.get_render_results(pageable, template=template, batch=batch)
        print("The response of RenderResultsAPIApi->get_render_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenderResultsAPIApi->get_render_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageable** | [**SwaggerPageable**](.md)| Pagination | 
 **template** | **str**| Template identifier | [optional] 
 **batch** | **str**| Batch identifier for the render request | [optional] 

### Return type

[**PageRenderResultItem**](PageRenderResultItem.md)

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

