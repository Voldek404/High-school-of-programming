import unittest
from task_5 import GenerateBBSTArray

class TestGenerateBBSTArray(unittest.TestCase):
    def test_full_tree_size_7(self):
        # 2^3 - 1 = 7 элементов
        input_array = [1, 2, 3, 4, 5, 6, 7]
        expected = [4, 2, 6, 1, 3, 5, 7]
        self.assertEqual(GenerateBBSTArray(input_array), expected)

    def test_full_tree_size_15(self):
        # 2^4 - 1 = 15 элементов
        input_array = list(range(1, 16))
        expected = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        self.assertEqual(GenerateBBSTArray(input_array), expected)

    def test_full_tree_size_3(self):
        # 2^2 - 1 = 3 элементов
        input_array = [1, 2, 3]
        expected = [2, 1, 3]
        self.assertEqual(GenerateBBSTArray(input_array), expected)

    def test_empty_array(self):
        self.assertEqual(GenerateBBSTArray([]), [])

    def test_single_element(self):
        self.assertEqual(GenerateBBSTArray([42]), [42])

if __name__ == '__main__':
    unittest.main()
