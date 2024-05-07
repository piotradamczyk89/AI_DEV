# MyTemplateEntryV2


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
**is_shared** | **bool** |  | [optional] 
**is_live_preview_shared** | **bool** |  | [optional] 
**is_email_notification** | **bool** |  | [optional] 
**email_notification** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**editor** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.my_template_entry_v2 import MyTemplateEntryV2

# TODO update the JSON string below
json = "{}"
# create an instance of MyTemplateEntryV2 from a JSON string
my_template_entry_v2_instance = MyTemplateEntryV2.from_json(json)
# print the JSON string representation of the object
print(MyTemplateEntryV2.to_json())

# convert the object into a dict
my_template_entry_v2_dict = my_template_entry_v2_instance.to_dict()
# create an instance of MyTemplateEntryV2 from a dict
my_template_entry_v2_from_dict = MyTemplateEntryV2.from_dict(my_template_entry_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


