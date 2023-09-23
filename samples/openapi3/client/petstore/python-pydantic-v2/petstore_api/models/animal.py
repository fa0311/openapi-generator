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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictStr

class Animal(BaseModel):
    """
    Animal
    """
    class_name: StrictStr = Field(..., alias="className")
    color: Optional[StrictStr] = 'red'
    additional_properties: Dict[str, Any] = {}

    """Pydantic configuration"""
    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
    }

    # JSON field name that stores the object type

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj['className']
        discriminator_value_class_map = {
            'Cat': 'Cat','Dog': 'Dog'
        }

        if discriminator_value:
            return discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union(Cat, Dog):
        """Create an instance of Animal from a JSON string"""
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
    def from_dict(cls, obj: dict) -> Union(Cat, Dog):
        """Create an instance of Animal from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        discriminator_value_class_map = {
            'Cat': 'Cat','Dog': 'Dog'
        }
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("Animal failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + 'className' +
                             ", mapping: " + json.dumps(discriminator_value_class_map))

from petstore_api.models.cat import Cat
from petstore_api.models.dog import Dog
try:
    Animal.model_rebuild()
except Exception:
    pass

