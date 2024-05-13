# coding: utf-8

"""
    RenderForm API

    Swagger documentation for RenderForm API

    The version of the OpenAPI document: 5d659ea_2024-04-19_14-21-33
    Contact: contact@renderform.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.change_placeholder import ChangePlaceholder

class TestChangePlaceholder(unittest.TestCase):
    """ChangePlaceholder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChangePlaceholder:
        """Test ChangePlaceholder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChangePlaceholder`
        """
        model = ChangePlaceholder()
        if include_optional:
            return ChangePlaceholder(
                component_id = '',
                component_type = 'RECTANGLE',
                type = '',
                key = '',
                var_property = '',
                default_value = ''
            )
        else:
            return ChangePlaceholder(
        )
        """

    def testChangePlaceholder(self):
        """Test ChangePlaceholder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()