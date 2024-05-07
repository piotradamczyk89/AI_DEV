# openapi_client.ScreenshotsAPIApi

All URIs are relative to *https://api.renderform.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_screenshot**](ScreenshotsAPIApi.md#create_screenshot) | **POST** /api/v1/screenshots | 


# **create_screenshot**
> CreateScreenshotResponse create_screenshot(x_api_key, create_screenshot_request)



### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.create_screenshot_request import CreateScreenshotRequest
from openapi_client.models.create_screenshot_response import CreateScreenshotResponse
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
    api_instance = openapi_client.ScreenshotsAPIApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    create_screenshot_request = openapi_client.CreateScreenshotRequest() # CreateScreenshotRequest | 

    try:
        api_response = api_instance.create_screenshot(x_api_key, create_screenshot_request)
        print("The response of ScreenshotsAPIApi->create_screenshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScreenshotsAPIApi->create_screenshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **create_screenshot_request** | [**CreateScreenshotRequest**](CreateScreenshotRequest.md)|  | 

### Return type

[**CreateScreenshotResponse**](CreateScreenshotResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

