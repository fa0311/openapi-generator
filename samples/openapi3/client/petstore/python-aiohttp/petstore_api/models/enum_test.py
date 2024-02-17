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

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from petstore_api.models.outer_enum import OuterEnum
from petstore_api.models.outer_enum_default_value import OuterEnumDefaultValue
from petstore_api.models.outer_enum_integer import OuterEnumInteger
from petstore_api.models.outer_enum_integer_default_value import OuterEnumIntegerDefaultValue
from typing import Optional, Set
from typing_extensions import Self



class EnumTest(BaseModel):
    """
    EnumTest
    """ # noqa: E501
    enum_string: Optional[StrictStr] = None
    enum_string_required: StrictStr
    enum_integer_default: Optional[StrictInt] = 5
    enum_integer: Optional[StrictInt] = None
    enum_number: Optional[float] = None
    outer_enum: Optional[OuterEnum] = Field(default=None, alias="outerEnum")
    outer_enum_integer: Optional[OuterEnumInteger] = Field(default=None, alias="outerEnumInteger")
    outer_enum_default_value: Optional[OuterEnumDefaultValue] = Field(default=None, alias="outerEnumDefaultValue")
    outer_enum_integer_default_value: Optional[OuterEnumIntegerDefaultValue] = Field(default=None, alias="outerEnumIntegerDefaultValue")
    __properties: ClassVar[List[str]] = ["enum_string", "enum_string_required", "enum_integer_default", "enum_integer", "enum_number", "outerEnum", "outerEnumInteger", "outerEnumDefaultValue", "outerEnumIntegerDefaultValue"]

    @field_validator('enum_string')
    def enum_string_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UPPER', 'lower', '']):
            raise ValueError("must be one of enum values ('UPPER', 'lower', '')")
        return value

    @field_validator('enum_string_required')
    def enum_string_required_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['UPPER', 'lower', '']):
            raise ValueError("must be one of enum values ('UPPER', 'lower', '')")
        return value

    @field_validator('enum_integer_default')
    def enum_integer_default_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([1, 5, 14]):
            raise ValueError("must be one of enum values (1, 5, 14)")
        return value

    @field_validator('enum_integer')
    def enum_integer_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([1, -1]):
            raise ValueError("must be one of enum values (1, -1)")
        return value

    @field_validator('enum_number')
    def enum_number_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([1.1, -1.2]):
            raise ValueError("must be one of enum values (1.1, -1.2)")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EnumTest from a JSON string"""
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
        # set to None if outer_enum (nullable) is None
        # and model_fields_set contains the field
        if self.outer_enum is None and "outer_enum" in self.model_fields_set:
            _dict['outerEnum'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnumTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enum_string": obj.get("enum_string"),
            "enum_string_required": obj.get("enum_string_required"),
            "enum_integer_default": obj.get("enum_integer_default") if obj.get("enum_integer_default") is not None else 5,
            "enum_integer": obj.get("enum_integer"),
            "enum_number": obj.get("enum_number"),
            "outerEnum": obj.get("outerEnum"),
            "outerEnumInteger": obj.get("outerEnumInteger"),
            "outerEnumDefaultValue": obj.get("outerEnumDefaultValue"),
            "outerEnumIntegerDefaultValue": obj.get("outerEnumIntegerDefaultValue")
        })
        return _obj


