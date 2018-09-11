import unittest
import product_dimension_builder


class TestProductDimensionBuilder(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    """ simple test to make sure we are connecting through alchemy"""
    def test_connect_exists(self):
        con, meta = product_dimension_builder.connect('Gene','Gene', 'MyCompany')
        self.assertIsNotNone(con, 'Connection test passed')
        self.assertIsNotNone(meta, 'metadata passed')


if __name__ == '__main__':
    unittest.main()