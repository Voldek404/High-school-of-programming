import unittest
from list_sort.my_sort import list_sort


class sort_tests(unittest.TestCase):
    def test_sort(self):
        # Use the sort function on one list and compare the result with the sorted version of the other list
        self.assertEqual(list_sort([43, 21, 54, 76, 87, 32, 54, 12, 43, 65]),
                         sorted([43, 21, 54, 76, 87, 32, 54, 12, 43, 65]))

    def test_sort_floating(self):
        # Test with floating point
        self.assertEqual(list_sort([4.3, 2.1, 5.4, 7.6, 8.7, 3.2, 5.4, 1.2, 4.3, 6.5]),
                         sorted([4.3, 2.1, 5.4, 7.6, 8.7, 3.2, 5.4, 1.2, 4.3, 6.5]))

    def test_sort_small(self):
        # Test with small nums
        self.assertEqual(list_sort([0, 0, 0, 7.6, 1, 0, 0, 0, 0, 0]),
                         sorted([0, 0, 0, 7.6, 1, 0, 0, 0, 0, 0]))

    def test_ascending(self): #test ascending order
         lst = list_sort([43, 21, 54, 76, 87, 32, 54, 12, 43, 65])
         self.assertTrue(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


if __name__ == '__main__':
    unittest.main()
