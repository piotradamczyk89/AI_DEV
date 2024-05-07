# RenderResultDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**request_payload** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.render_result_details import RenderResultDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResultDetails from a JSON string
render_result_details_instance = RenderResultDetails.from_json(json)
# print the JSON string representation of the object
print(RenderResultDetails.to_json())

# convert the object into a dict
render_result_details_dict = render_result_details_instance.to_dict()
# create an instance of RenderResultDetails from a dict
render_result_details_from_dict = RenderResultDetails.from_dict(render_result_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


