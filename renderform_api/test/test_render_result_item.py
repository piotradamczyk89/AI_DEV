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

from openapi_client.models.render_result_item import RenderResultItem

class TestRenderResultItem(unittest.TestCase):
    """RenderResultItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenderResultItem:
        """Test RenderResultItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenderResultItem`
        """
        model = RenderResultItem()
        if include_optional:
            return RenderResultItem(
                identifier = '',
                href = '',
                width = 56,
                height = 56,
                template_name = '',
                file_name = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return RenderResultItem(
        )
        """

    def testRenderResultItem(self):
        """Test RenderResultItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
