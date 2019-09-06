import unittest
import sys
import os

sys.path.insert(1, os.path.join(os.getcwd(), "apps"))
import web_scraper as wb

class TestWebScrapperMethods(unittest.TestCase):

    def testFindTrackedProducts(self):
        product_list = wb.trackedProductList()
        self.assertEqual(len(product_list), 1)
        self.assertEqual(product_list[0], 'N82E16834235015')

    def testLastLine(self):
        product_list = wb.trackedProductList()
        csv_file = wb.getCSVPath(product_list[0])
        with open(csv_file, 'r') as f:
            self.assertTrue(wb.shouldUpdatePrice(f))

    def testExtractLineInfo(self):
        line = 'S258FG,129.99,12/2/2019'
        line_info = wb.extractInfoFromLine(line)
        self.assertEqual(line_info[0], 'S258FG')
        self.assertEqual(line_info[1], '129.99')
        self.assertEqual(line_info[2], '12/2/2019')


if __name__ == '__main__':
    unittest.main()