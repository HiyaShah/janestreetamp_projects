import unittest
from number_op import *

class NumTests (unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_two_num(2,3),5)


if __name__ == "__main__":
    unittest.main()