# RenderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** | Template ID | 
**data** | **Dict[str, object]** | Data to be merged into the template | [optional] 
**file_name** | **str** | Name of the file to be returned | [optional] 
**webhook_url** | **str** | Webhook URL to be called when the render is done | [optional] 
**version** | **str** | Cache key to be used for caching the rendered image | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata to be passed to the webhook | [optional] 
**batch_name** | **str** | Batch name to be used for grouping renders | [optional] 

## Example

```python
from openapi_client.models.render_request import RenderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RenderRequest from a JSON string
render_request_instance = RenderRequest.from_json(json)
# print the JSON string representation of the object
print(RenderRequest.to_json())

# convert the object into a dict
render_request_dict = render_request_instance.to_dict()
# create an instance of RenderRequest from a dict
render_request_from_dict = RenderRequest.from_dict(render_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


