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
import importlib

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from petstore_api.models.deprecated_object import DeprecatedObject
from typing import Optional, Set
from typing_extensions import Self

class ObjectWithDeprecatedFields(BaseModel):
    """
    ObjectWithDeprecatedFields
    """ # noqa: E501
    uuid: Optional[StrictStr] = None
    id: Optional[float] = None
    deprecated_ref: Optional[DeprecatedObject] = Field(default=None, alias="deprecatedRef")
    bars: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["uuid", "id", "deprecatedRef", "bars"]

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
        """Create an instance of ObjectWithDeprecatedFields from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of deprecated_ref
        if self.deprecated_ref:
            _dict['deprecatedRef'] = self.deprecated_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectWithDeprecatedFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "id": obj.get("id"),
            "deprecatedRef": DeprecatedObject.from_dict(obj["deprecatedRef"]) if obj.get("deprecatedRef") is not None else None,
            "bars": obj.get("bars")
        })
        return _obj


