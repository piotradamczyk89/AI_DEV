# GetTemplateBasics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**preview** | **str** |  | [optional] 
**scale_factor** | **float** |  | [optional] 
**output_format** | **str** |  | [optional] 
**output_extension** | **str** |  | [optional] 
**quality** | **int** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**editor** | **str** |  | [optional] 
**properties** | [**List[ChangePlaceholder]**](ChangePlaceholder.md) |  | [optional] 
**fonts** | [**List[FontItem]**](FontItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_template_basics import GetTemplateBasics

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplateBasics from a JSON string
get_template_basics_instance = GetTemplateBasics.from_json(json)
# print the JSON string representation of the object
print(GetTemplateBasics.to_json())

# convert the object into a dict
get_template_basics_dict = get_template_basics_instance.to_dict()
# create an instance of GetTemplateBasics from a dict
get_template_basics_from_dict = GetTemplateBasics.from_dict(get_template_basics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


