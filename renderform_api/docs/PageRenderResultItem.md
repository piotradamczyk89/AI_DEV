# PageRenderResultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[RenderResultItem]**](RenderResultItem.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObject**](SortObject.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.page_render_result_item import PageRenderResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of PageRenderResultItem from a JSON string
page_render_result_item_instance = PageRenderResultItem.from_json(json)
# print the JSON string representation of the object
print(PageRenderResultItem.to_json())

# convert the object into a dict
page_render_result_item_dict = page_render_result_item_instance.to_dict()
# create an instance of PageRenderResultItem from a dict
page_render_result_item_from_dict = PageRenderResultItem.from_dict(page_render_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


