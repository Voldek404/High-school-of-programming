import unittest

from task_3 import BST, BSTFind, BSTNode


class BSTSearchMethods(unittest.TestCase):
    def setUp(self):
        self.tree = BST(None)
        self.tree.AddKeyValue(10, "A")
        self.tree.AddKeyValue(5, "B")
        self.tree.AddKeyValue(15, "C")
        self.tree.AddKeyValue(2, "D")
        self.tree.AddKeyValue(7, "E")
        self.tree.AddKeyValue(12, "F")
        self.tree.AddKeyValue(17, "G")

    def testDFS(self):
        result = self.tree.DeepAllNodes(0)
        self.assertEqual(result, (2, 5, 7, 10, 12, 15, 17))

        result = self.tree.DeepAllNodes(1)
        self.assertEqual(result, (10, 5, 2, 7, 15, 12, 17))

        result = self.tree.DeepAllNodes(2)
        self.assertEqual(result, (2, 7, 5, 12, 17, 15, 10))

    def testsBFS(self):
        result = self.tree.WideAllNodes()
        self.assertEqual(result, (10, 5, 15, 2, 7, 12, 17))


if __name__ == "__main__":
    unittest.main()
