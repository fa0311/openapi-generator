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
from pydantic import BaseModel, Field, StrictInt, constr, validator

class NullableProperty(BaseModel):
    """
    NullableProperty
    """
    id: StrictInt = Field(...)
    name: Optional[constr(strict=True)] = Field(...)
    __properties = ["id", "name"]

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[A-Z].*", value):
            raise ValueError(r"must validate the regular expression /^[A-Z].*/")
        return value

    """Pydantic configuration"""
    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> NullableProperty:
        """Create an instance of NullableProperty from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NullableProperty:
        """Create an instance of NullableProperty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NullableProperty.parse_obj(obj)

        _obj = NullableProperty.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj


