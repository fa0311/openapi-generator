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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr



class Name(BaseModel):
    """
    Model for testing model name same as property name  # noqa: E501
    """
    name: StrictInt = Field(...)
    snake_case: Optional[StrictInt] = None
    var_property: Optional[StrictStr] = Field(None, alias="property")
    var_123_number: Optional[StrictInt] = Field(None, alias="123Number")
    __properties = ["name", "snake_case", "property", "123Number"]

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
    def from_json(cls, json_str: str) -> Name:
        """Create an instance of Name from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "snake_case",
                            "var_123_number",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Name:
        """Create an instance of Name from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Name.parse_obj(obj)

        _obj = Name.parse_obj({
            "name": obj.get("name"),
            "snake_case": obj.get("snake_case"),
            "var_property": obj.get("property"),
            "var_123_number": obj.get("123Number")
        })
        return _obj


