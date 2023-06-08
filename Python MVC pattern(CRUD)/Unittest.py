# this is Unittest that figure out this program working accurately.
# Author : Dongkwan Kim

import unittest

import Cod


class MyTestCase(unittest.TestCase):
    def test_create(self):
        testCreate = Cod.CodFish('Commercail', 'latin_name', 'english_name', 'french_name', 'year', 'month', 'number_otoliths')
        self.assertEqual(testCreate.source, 'Commercail')  # add assertion here
        print("Program by Dongkwan Kim")


if __name__ == '__main__':
    unittest.main()
