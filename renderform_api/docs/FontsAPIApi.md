# openapi_client.FontsAPIApi

All URIs are relative to *https://api.renderform.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_fonts**](FontsAPIApi.md#get_all_fonts) | **GET** /api/v1/fonts | 


# **get_all_fonts**
> List[FontItem] get_all_fonts()



Returns all fonts available in the system for the current user.  'source' field can be 'GOOGLE' or 'CUSTOM' (for custom fonts uploaded by the user)  'family' field is the name of the font  'variants' field is a list of all variants available for the font  

### Example

* Api Key Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.font_item import FontItem
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
    api_instance = openapi_client.FontsAPIApi(api_client)

    try:
        api_response = api_instance.get_all_fonts()
        print("The response of FontsAPIApi->get_all_fonts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FontsAPIApi->get_all_fonts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FontItem]**](FontItem.md)

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

