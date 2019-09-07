from libs import scraper_utils as scraper
import unittest
import os


class TestWebScrapperMethods(unittest.TestCase):

    def testFindTrackedProducts(self):
        product_list = scraper.trackedProductList()
        self.assertEqual(len(product_list), 7)

    def testLastLine(self):
        product_list = scraper.trackedProductList()
        csv_file = scraper.getCSVPath(product_list[0])
        with open(csv_file, 'r') as f:
            self.assertFalse(scraper.shouldUpdatePrice(f, 443.65))

    def testExtractLineInfo(self):
        line = 'S258FG,129.99,12/2/2019'
        line_info = scraper.extractInfoFromLine(line)
        self.assertEqual(line_info[0], 'S258FG')
        self.assertEqual(line_info[1], '129.99')
        self.assertEqual(line_info[2], '12/2/2019')


if __name__ == '__main__':
    unittest.main()
