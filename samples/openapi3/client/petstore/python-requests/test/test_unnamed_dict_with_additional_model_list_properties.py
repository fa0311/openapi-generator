# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from petstore_api.models.unnamed_dict_with_additional_model_list_properties import UnnamedDictWithAdditionalModelListProperties

class TestUnnamedDictWithAdditionalModelListProperties(unittest.TestCase):
    """UnnamedDictWithAdditionalModelListProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnnamedDictWithAdditionalModelListProperties:
        """Test UnnamedDictWithAdditionalModelListProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnnamedDictWithAdditionalModelListProperties`
        """
        model = UnnamedDictWithAdditionalModelListProperties()
        if include_optional:
            return UnnamedDictWithAdditionalModelListProperties(
                dict_property = {
                    'key' : [
                        petstore_api.models.creature_info.CreatureInfo(
                            name = '', )
                        ]
                    }
            )
        else:
            return UnnamedDictWithAdditionalModelListProperties(
        )
        """

    def testUnnamedDictWithAdditionalModelListProperties(self):
        """Test UnnamedDictWithAdditionalModelListProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
