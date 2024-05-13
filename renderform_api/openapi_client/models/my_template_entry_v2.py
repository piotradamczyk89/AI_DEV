# coding: utf-8

"""
    RenderForm API

    Swagger documentation for RenderForm API

    The version of the OpenAPI document: 5d659ea_2024-04-19_14-21-33
    Contact: contact@renderform.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class MyTemplateEntryV2(BaseModel):
    """
    MyTemplateEntryV2
    """ # noqa: E501
    identifier: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    preview: Optional[StrictStr] = None
    scale_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="scaleFactor")
    output_format: Optional[StrictStr] = Field(default=None, alias="outputFormat")
    output_extension: Optional[StrictStr] = Field(default=None, alias="outputExtension")
    quality: Optional[StrictInt] = None
    is_shared: Optional[StrictBool] = Field(default=None, alias="isShared")
    is_live_preview_shared: Optional[StrictBool] = Field(default=None, alias="isLivePreviewShared")
    is_email_notification: Optional[StrictBool] = Field(default=None, alias="isEmailNotification")
    email_notification: Optional[StrictStr] = Field(default=None, alias="emailNotification")
    width: Optional[StrictInt] = None
    height: Optional[StrictInt] = None
    created_by: Optional[StrictStr] = Field(default=None, alias="createdBy")
    editor: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["identifier", "name", "preview", "scaleFactor", "outputFormat", "outputExtension", "quality", "isShared", "isLivePreviewShared", "isEmailNotification", "emailNotification", "width", "height", "createdBy", "editor"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MyTemplateEntryV2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MyTemplateEntryV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identifier": obj.get("identifier"),
            "name": obj.get("name"),
            "preview": obj.get("preview"),
            "scaleFactor": obj.get("scaleFactor"),
            "outputFormat": obj.get("outputFormat"),
            "outputExtension": obj.get("outputExtension"),
            "quality": obj.get("quality"),
            "isShared": obj.get("isShared"),
            "isLivePreviewShared": obj.get("isLivePreviewShared"),
            "isEmailNotification": obj.get("isEmailNotification"),
            "emailNotification": obj.get("emailNotification"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "createdBy": obj.get("createdBy"),
            "editor": obj.get("editor")
        })
        return _obj

