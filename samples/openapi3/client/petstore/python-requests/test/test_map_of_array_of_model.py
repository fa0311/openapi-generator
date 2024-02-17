# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from petstore_api.models.map_of_array_of_model import MapOfArrayOfModel

class TestMapOfArrayOfModel(unittest.TestCase):
    """MapOfArrayOfModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MapOfArrayOfModel:
        """Test MapOfArrayOfModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MapOfArrayOfModel`
        """
        model = MapOfArrayOfModel()
        if include_optional:
            return MapOfArrayOfModel(
                shop_id_to_org_online_lip_map = {
                    'key' : [
                        petstore_api.models.tag.Tag(
                            id = 56, 
                            name = '', )
                        ]
                    }
            )
        else:
            return MapOfArrayOfModel(
        )
        """

    def testMapOfArrayOfModel(self):
        """Test MapOfArrayOfModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
