import unittest

from flatten_array import flatten

class TestFlatten(unittest.TestCase):    
    """
    Tests flatten function
    """

    def test_flatten_nested(self):
        
        input = [[1,2,[3]],4]
        result = flatten(input)
        exptcted = [1,2,3,4]

        self.assertEqual(exptcted, result)

    def test_flatten_nested_with_empty(self):
        
        input = [[1,2,[3]],4, [],[]]
        result = flatten(input)
        exptcted = [1,2,3,4]

        self.assertEqual(exptcted, result)

    def test_flatten_nested_all_empty(self):
        
        input = [[[]],[],[]]
        result = flatten(input)
        exptcted = []

        self.assertEqual(exptcted, result)

    def test_flatten_error_no_number(self):
        
        input = [1,2, ["a", "b"], [3]]
        result = flatten(input)
        exptcted = [1,2, "a", "b",3]

        self.assertNotEqual(exptcted, result)


if __name__ == '__main__':
    unittest.main()