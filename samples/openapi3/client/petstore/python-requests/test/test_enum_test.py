# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from petstore_api.models.enum_test import EnumTest

class TestEnumTest(unittest.TestCase):
    """EnumTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnumTest:
        """Test EnumTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnumTest`
        """
        model = EnumTest()
        if include_optional:
            return EnumTest(
                enum_string = 'UPPER',
                enum_string_required = 'UPPER',
                enum_integer_default = 1,
                enum_integer = 1,
                enum_number = 1.1,
                outer_enum = 'placed',
                outer_enum_integer = 2,
                outer_enum_default_value = 'placed',
                outer_enum_integer_default_value = -1
            )
        else:
            return EnumTest(
                enum_string_required = 'UPPER',
        )
        """

    def testEnumTest(self):
        """Test EnumTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
