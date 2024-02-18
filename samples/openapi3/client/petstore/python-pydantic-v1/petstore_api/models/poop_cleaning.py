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


from typing import Any, Dict
from pydantic import BaseModel, Field, StrictStr, validator



class PoopCleaning(BaseModel):
    """
    PoopCleaning
    """
    task_name: StrictStr = Field(...)
    function_name: StrictStr = Field(...)
    content: StrictStr = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["task_name", "function_name", "content"]

    @validator('task_name')
    def task_name_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('cleaning'):
            raise ValueError("must be one of enum values ('cleaning')")
        return value

    @validator('function_name')
    def function_name_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('care'):
            raise ValueError("must be one of enum values ('care')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PoopCleaning:
        """Create an instance of PoopCleaning from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
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
    def from_dict(cls, obj: dict) -> PoopCleaning:
        """Create an instance of PoopCleaning from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PoopCleaning.parse_obj(obj)

        _obj = PoopCleaning.parse_obj({
            "task_name": obj.get("task_name"),
            "function_name": obj.get("function_name"),
            "content": obj.get("content")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


