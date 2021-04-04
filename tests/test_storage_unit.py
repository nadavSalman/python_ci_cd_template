import sys
import os
import unittest

from storage.storage_units import false_function



class TestStorageUnit(unittest.TestCase):

    def test_storage_item(self):
        self.assertEqual(True, false_function())






if __name__ == '__main__':
    unittest.main()



