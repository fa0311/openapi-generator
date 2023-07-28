# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class Capitalization(BaseModel):
    """
    Capitalization
    """
    small_camel: Optional[StrictStr] = Field(None, alias="smallCamel")
    capital_camel: Optional[StrictStr] = Field(None, alias="CapitalCamel")
    small_snake: Optional[StrictStr] = Field(None, alias="small_Snake")
    capital_snake: Optional[StrictStr] = Field(None, alias="Capital_Snake")
    sca_eth_flow_points: Optional[StrictStr] = Field(None, alias="SCA_ETH_Flow_Points")
    att_name: Optional[StrictStr] = Field(None, alias="ATT_NAME", description="Name of the pet ")
    additional_properties: Dict[str, Any] = {}
    __properties = ["smallCamel", "CapitalCamel", "small_Snake", "Capital_Snake", "SCA_ETH_Flow_Points", "ATT_NAME"]

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
    def from_json(cls, json_str: str) -> Capitalization:
        """Create an instance of Capitalization from a JSON string"""
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
    def from_dict(cls, obj: dict) -> Capitalization:
        """Create an instance of Capitalization from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Capitalization.parse_obj(obj)

        _obj = Capitalization.parse_obj({
            "small_camel": obj.get("smallCamel"),
            "capital_camel": obj.get("CapitalCamel"),
            "small_snake": obj.get("small_Snake"),
            "capital_snake": obj.get("Capital_Snake"),
            "sca_eth_flow_points": obj.get("SCA_ETH_Flow_Points"),
            "att_name": obj.get("ATT_NAME")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

