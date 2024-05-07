# FontItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_name** | **str** |  | [optional] 
**family** | **str** |  | [optional] 
**variants** | **List[str]** |  | [optional] 
**default_variant** | **str** |  | [optional] 
**subsets** | **List[str]** |  | [optional] 
**category** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.font_item import FontItem

# TODO update the JSON string below
json = "{}"
# create an instance of FontItem from a JSON string
font_item_instance = FontItem.from_json(json)
# print the JSON string representation of the object
print(FontItem.to_json())

# convert the object into a dict
font_item_dict = font_item_instance.to_dict()
# create an instance of FontItem from a dict
font_item_from_dict = FontItem.from_dict(font_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


