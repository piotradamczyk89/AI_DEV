# CreateScreenshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**request** | [**CreateScreenshotRequest**](CreateScreenshotRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_screenshot_response import CreateScreenshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScreenshotResponse from a JSON string
create_screenshot_response_instance = CreateScreenshotResponse.from_json(json)
# print the JSON string representation of the object
print(CreateScreenshotResponse.to_json())

# convert the object into a dict
create_screenshot_response_dict = create_screenshot_response_instance.to_dict()
# create an instance of CreateScreenshotResponse from a dict
create_screenshot_response_from_dict = CreateScreenshotResponse.from_dict(create_screenshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


