# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class Category(BaseModel):
    """
    Category
    """
    id: Optional[StrictInt] = None
    name: StrictStr = Field(...)
    additional_properties: Dict[str, Any] = {}

    """Pydantic configuration"""
    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Category:
        """Create an instance of Category from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Category:
        """Create an instance of Category from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Category.model_validate(obj)

        _obj = Category.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name") if obj.get("name") is not None else 'default-name'
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in ["id", "name"]:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


