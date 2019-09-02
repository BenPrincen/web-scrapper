import unittest
import sys
import os

sys.path.insert(1, os.path.join(os.getcwd(), "libs"))
import product as p

class TestProductLib(unittest.TestCase):

    def testConstructors(self):
        product = p.Product(100, 'graphics card', '10/10/2019')
        self.assertEqual(product.getLastPrice(), 100)
        self.assertEqual(product.getTitle(), 'graphics card')
        self.assertEqual(product.getLastUpdated(), '10/10/2019')