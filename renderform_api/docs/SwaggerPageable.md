# SwaggerPageable

Pageable parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Page size | [optional] 
**page** | **int** | Page number | [optional] 

## Example

```python
from openapi_client.models.swagger_pageable import SwaggerPageable

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerPageable from a JSON string
swagger_pageable_instance = SwaggerPageable.from_json(json)
# print the JSON string representation of the object
print(SwaggerPageable.to_json())

# convert the object into a dict
swagger_pageable_dict = swagger_pageable_instance.to_dict()
# create an instance of SwaggerPageable from a dict
swagger_pageable_from_dict = SwaggerPageable.from_dict(swagger_pageable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


