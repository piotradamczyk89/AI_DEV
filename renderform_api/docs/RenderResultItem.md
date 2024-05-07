# RenderResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**template_name** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.render_result_item import RenderResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResultItem from a JSON string
render_result_item_instance = RenderResultItem.from_json(json)
# print the JSON string representation of the object
print(RenderResultItem.to_json())

# convert the object into a dict
render_result_item_dict = render_result_item_instance.to_dict()
# create an instance of RenderResultItem from a dict
render_result_item_from_dict = RenderResultItem.from_dict(render_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


