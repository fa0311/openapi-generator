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


from typing import List, Optional
from pydantic import BaseModel, conlist
from petstore_api.models.file import File



class FileSchemaTestClass(BaseModel):
    """
    FileSchemaTestClass
    """
    file: Optional[File] = None
    files: Optional[conlist(File)] = None
    __properties = ["file", "files"]

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
    def from_json(cls, json_str: str) -> FileSchemaTestClass:
        """Create an instance of FileSchemaTestClass from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['files'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FileSchemaTestClass:
        """Create an instance of FileSchemaTestClass from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FileSchemaTestClass.parse_obj(obj)

        _obj = FileSchemaTestClass.parse_obj({
            "file": File.from_dict(obj.get("file")) if obj.get("file") is not None else None,
            "files": [File.from_dict(_item) for _item in obj.get("files")] if obj.get("files") is not None else None
        })
        return _obj


