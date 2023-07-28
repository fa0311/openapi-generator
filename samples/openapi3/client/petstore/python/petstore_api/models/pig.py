# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from petstore_api.models.basque_pig import BasquePig
from petstore_api.models.danish_pig import DanishPig
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

PIG_ONE_OF_SCHEMAS = ["BasquePig", "DanishPig"]

class Pig(BaseModel):
    """
    Pig
    """
    # data type: BasquePig
    oneof_schema_1_validator: Optional[BasquePig] = None
    # data type: DanishPig
    oneof_schema_2_validator: Optional[DanishPig] = None
    if TYPE_CHECKING:
        actual_instance: Union[BasquePig, DanishPig]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(PIG_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = Pig.construct()
        error_messages = []
        match = 0
        # validate data type: BasquePig
        if not isinstance(v, BasquePig):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BasquePig`")
        else:
            match += 1
        # validate data type: DanishPig
        if not isinstance(v, DanishPig):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DanishPig`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in Pig with oneOf schemas: BasquePig, DanishPig. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in Pig with oneOf schemas: BasquePig, DanishPig. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Pig:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Pig:
        """Returns the object represented by the json string"""
        instance = Pig.construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("className")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `className` in the input.")

        # check if data type is `BasquePig`
        if _data_type == "BasquePig":
            instance.actual_instance = BasquePig.from_json(json_str)
            return instance

        # check if data type is `DanishPig`
        if _data_type == "DanishPig":
            instance.actual_instance = DanishPig.from_json(json_str)
            return instance

        # deserialize data into BasquePig
        try:
            instance.actual_instance = BasquePig.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DanishPig
        try:
            instance.actual_instance = DanishPig.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Pig with oneOf schemas: BasquePig, DanishPig. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Pig with oneOf schemas: BasquePig, DanishPig. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

