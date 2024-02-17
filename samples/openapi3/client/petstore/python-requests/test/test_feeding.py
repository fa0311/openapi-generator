# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from petstore_api.models.feeding import Feeding

class TestFeeding(unittest.TestCase):
    """Feeding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Feeding:
        """Test Feeding
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Feeding`
        """
        model = Feeding()
        if include_optional:
            return Feeding(
                task_name = 'cleaning',
                function_name = 'care_nourish',
                content = ''
            )
        else:
            return Feeding(
                task_name = 'cleaning',
                function_name = 'care_nourish',
                content = '',
        )
        """

    def testFeeding(self):
        """Test Feeding"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
