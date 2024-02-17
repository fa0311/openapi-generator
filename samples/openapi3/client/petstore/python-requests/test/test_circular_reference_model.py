# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from petstore_api.models.circular_reference_model import CircularReferenceModel

class TestCircularReferenceModel(unittest.TestCase):
    """CircularReferenceModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CircularReferenceModel:
        """Test CircularReferenceModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CircularReferenceModel`
        """
        model = CircularReferenceModel()
        if include_optional:
            return CircularReferenceModel(
                size = 56,
                nested = petstore_api.models.first_ref.FirstRef(
                    category = '', 
                    self_ref = petstore_api.models.second_ref.SecondRef(
                        category = '', 
                        circular_ref = petstore_api.models.circular_reference_model.Circular-Reference-Model(
                            size = 56, 
                            nested = petstore_api.models.first_ref.FirstRef(
                                category = '', ), ), ), )
            )
        else:
            return CircularReferenceModel(
        )
        """

    def testCircularReferenceModel(self):
        """Test CircularReferenceModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
