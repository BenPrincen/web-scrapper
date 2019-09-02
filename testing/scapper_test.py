import unittest
import sys
import os

sys.path.insert(1, os.path.join(os.getcwd(), "apps"))
import web_scrapper as wb

class TestWebScrapperMethods(unittest.TestCase):

    def testFindTrackedProducts(self):
        product_list = wb.trackedProductList()
        self.assertEqual(len(product_list), 1)
        self.assertEqual(product_list[0], 'N82E16834235015')


if __name__ == '__main__':
    unittest.main()