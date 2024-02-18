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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from petstore_api.models.category import Category



class SpecialName(BaseModel):
    """
    SpecialName
    """
    var_property: Optional[StrictInt] = Field(None, alias="property")
    var_async: Optional[Category] = Field(None, alias="async")
    var_schema: Optional[StrictStr] = Field(None, alias="schema", description="pet status in the store")
    __properties = ["property", "async", "schema"]

    @validator('var_schema')
    def var_schema_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('available', 'pending', 'sold'):
            raise ValueError("must be one of enum values ('available', 'pending', 'sold')")
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
    def from_json(cls, json_str: str) -> SpecialName:
        """Create an instance of SpecialName from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_async
        if self.var_async:
            _dict['async'] = self.var_async.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpecialName:
        """Create an instance of SpecialName from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpecialName.parse_obj(obj)

        _obj = SpecialName.parse_obj({
            "var_property": obj.get("property"),
            "var_async": Category.from_dict(obj.get("async")) if obj.get("async") is not None else None,
            "var_schema": obj.get("schema")
        })
        return _obj


