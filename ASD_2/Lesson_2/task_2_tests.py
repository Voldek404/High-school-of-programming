import unittest

from task_2 import BSTNode, BSTFind, BST


class BSTMethods(unittest.TestCase):
    def setUp(self):
        self.tree = BST(None)
        self.tree.AddKeyValue(10, "Root")
        self.tree.AddKeyValue(5, "Left")
        self.tree.AddKeyValue(15, "Right")
        self.tree.AddKeyValue(2, "Left Left")
        self.tree.AddKeyValue(7, "Left Right")
        self.tree.AddKeyValue(12, "Right Left")
        self.tree.AddKeyValue(17, "Right Right")

    def testFindNodeByKey(self):
        result = self.tree.FindNodeByKey(7)
        self.assertTrue(result.NodeHasKey)
        self.assertEqual(result.Node.NodeKey, 7)

        result = self.tree.FindNodeByKey(20)
        self.assertFalse(result.NodeHasKey)

    def testAddKeyValue(self):
        self.assertFalse(self.tree.AddKeyValue(6, "New Node"))
        self.assertTrue(self.tree.AddKeyValue(7, "Duplicate"))

    def testFinMinMax(self):
        min_node = self.tree.FinMinMax(self.tree.Root, False)
        max_node = self.tree.FinMinMax(self.tree.Root, True)
        self.assertEqual(min_node.NodeKey, 2)
        self.assertEqual(max_node.NodeKey, 17)

    def testDeleteNodeByKey(self):
        self.assertTrue(self.tree.DeleteNodeByKey(7))
        result = self.tree.FindNodeByKey(7)
        self.assertFalse(result.NodeHasKey)

        self.assertFalse(self.tree.DeleteNodeByKey(20))

    def testCount(self):
        self.assertEqual(self.tree.Count(), 7)
        self.tree.DeleteNodeByKey(5)
        self.assertEqual(self.tree.Count(), 6)


if __name__ == "__main__":
    unittest.main()
