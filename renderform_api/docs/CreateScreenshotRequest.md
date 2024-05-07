# CreateScreenshotRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wait_time** | **int** | Wait time in milliseconds before capturing the screenshot | [optional] 
**url** | **str** | URL to capture | 
**width** | **int** | Width of the screenshot in pixels | 
**height** | **int** | Height of the screenshot in pixels | 

## Example

```python
from openapi_client.models.create_screenshot_request import CreateScreenshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScreenshotRequest from a JSON string
create_screenshot_request_instance = CreateScreenshotRequest.from_json(json)
# print the JSON string representation of the object
print(CreateScreenshotRequest.to_json())

# convert the object into a dict
create_screenshot_request_dict = create_screenshot_request_instance.to_dict()
# create an instance of CreateScreenshotRequest from a dict
create_screenshot_request_from_dict = CreateScreenshotRequest.from_dict(create_screenshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


