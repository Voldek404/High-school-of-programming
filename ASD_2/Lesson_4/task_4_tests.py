import unittest

from task_4 import BST, aBST


class TestaBST(unittest.TestCase):
    def setUp(self):
        self.tree = aBST(2)

    def test_find_in_empty_tree_returns_none(self):
        self.assertIsNone(self.tree.FindKeyIndex(10))

    def test_add_key_to_empty_tree_sets_root(self):
        self.tree.AddKey(10)
        self.assertEqual(self.tree.Tree[0], 10)

    def test_add_duplicate_returns_minus_one(self):
        self.tree.AddKey(10)
        result = self.tree.AddKey(10)
        self.assertEqual(result, -1)

    def test_find_existing_key_returns_correct_index(self):
        self.tree.AddKey(10)
        self.tree.AddKey(5)
        self.tree.AddKey(15)
        self.assertEqual(self.tree.FindKeyIndex(5), 1)
        self.assertEqual(self.tree.FindKeyIndex(15), 2)

    def test_find_non_existing_key_returns_none(self):
        self.tree.AddKey(10)
        self.tree.AddKey(5)
        self.assertIsNone(self.tree.FindKeyIndex(20))

    def test_add_key_places_correctly_left_and_right(self):
        self.tree.AddKey(10)
        self.tree.AddKey(5)
        self.tree.AddKey(15)
        self.assertEqual(self.tree.Tree[1], 5)
        self.assertEqual(self.tree.Tree[2], 15)

    def test_add_key_to_full_tree_does_not_crash(self):
        keys = [10, 5, 15, 3, 7, 13, 17]
        for key in keys:
            self.tree.AddKey(key)
        self.assertNotIn(None, self.tree.Tree)
        self.assertEqual(self.tree.Tree, keys)

    def test_return_index_after_insertion(self):
        index = self.tree.AddKey(10)
        self.assertEqual(index, 0)
        index = self.tree.AddKey(5)
        self.assertEqual(index, 1)
        index = self.tree.AddKey(15)
        self.assertEqual(index, 2)


if __name__ == "__main__":
    unittest.main()
