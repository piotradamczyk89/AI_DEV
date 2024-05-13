# openapi-client
Swagger documentation for RenderForm API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5d659ea_2024-04-19_14-21-33
- Package version: 1.0.0
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = openapi_client.FontsAPIApi(api_client)

    try:
        api_response = api_instance.get_all_fonts()
        print("The response of FontsAPIApi->get_all_fonts:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FontsAPIApi->get_all_fonts: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.renderform.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FontsAPIApi* | [**get_all_fonts**](docs/FontsAPIApi.md#get_all_fonts) | **GET** /api/v1/fonts | 
*RenderAPIApi* | [**render_v2**](docs/RenderAPIApi.md#render_v2) | **POST** /api/v2/render | 
*RenderResultsAPIApi* | [**delete_content**](docs/RenderResultsAPIApi.md#delete_content) | **DELETE** /api/v2/results/{identifier} | 
*RenderResultsAPIApi* | [**get_render_result**](docs/RenderResultsAPIApi.md#get_render_result) | **GET** /api/v2/results/{identifier} | 
*RenderResultsAPIApi* | [**get_render_results**](docs/RenderResultsAPIApi.md#get_render_results) | **GET** /api/v2/results | 
*ScreenshotsAPIApi* | [**create_screenshot**](docs/ScreenshotsAPIApi.md#create_screenshot) | **POST** /api/v1/screenshots | 
*TemplatesAPIApi* | [**get_my_template**](docs/TemplatesAPIApi.md#get_my_template) | **GET** /api/v2/my-templates/{templateId} | 
*TemplatesAPIApi* | [**get_my_templates**](docs/TemplatesAPIApi.md#get_my_templates) | **GET** /api/v2/my-templates | 


## Documentation For Models

 - [ApiError](docs/ApiError.md)
 - [ChangePlaceholder](docs/ChangePlaceholder.md)
 - [CreateScreenshotRequest](docs/CreateScreenshotRequest.md)
 - [CreateScreenshotResponse](docs/CreateScreenshotResponse.md)
 - [FontItem](docs/FontItem.md)
 - [GetTemplateBasics](docs/GetTemplateBasics.md)
 - [MyTemplateEntryV2](docs/MyTemplateEntryV2.md)
 - [PageRenderResultItem](docs/PageRenderResultItem.md)
 - [PageableObject](docs/PageableObject.md)
 - [RenderRequest](docs/RenderRequest.md)
 - [RenderResponse](docs/RenderResponse.md)
 - [RenderResultDetails](docs/RenderResultDetails.md)
 - [RenderResultItem](docs/RenderResultItem.md)
 - [SortObject](docs/SortObject.md)
 - [SwaggerPageable](docs/SwaggerPageable.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="apiKey"></a>
### apiKey

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author

contact@renderform.io

