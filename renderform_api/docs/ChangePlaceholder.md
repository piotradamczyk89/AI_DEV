# ChangePlaceholder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_id** | **str** |  | [optional] 
**component_type** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**var_property** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.change_placeholder import ChangePlaceholder

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePlaceholder from a JSON string
change_placeholder_instance = ChangePlaceholder.from_json(json)
# print the JSON string representation of the object
print(ChangePlaceholder.to_json())

# convert the object into a dict
change_placeholder_dict = change_placeholder_instance.to_dict()
# create an instance of ChangePlaceholder from a dict
change_placeholder_from_dict = ChangePlaceholder.from_dict(change_placeholder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


