# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from petstore_api.models.self_reference_model import SelfReferenceModel

class TestSelfReferenceModel(unittest.TestCase):
    """SelfReferenceModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelfReferenceModel:
        """Test SelfReferenceModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SelfReferenceModel`
        """
        model = SelfReferenceModel()
        if include_optional:
            return SelfReferenceModel(
                size = 56,
                nested = petstore_api.models.dummy_model.Dummy-Model(
                    category = '', 
                    self_ref = petstore_api.models.self_reference_model.Self-Reference-Model(
                        size = 56, 
                        nested = petstore_api.models.dummy_model.Dummy-Model(
                            category = '', ), ), )
            )
        else:
            return SelfReferenceModel(
        )
        """

    def testSelfReferenceModel(self):
        """Test SelfReferenceModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
