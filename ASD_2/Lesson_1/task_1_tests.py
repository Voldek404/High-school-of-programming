import unittest

from task_1 import SimpleTreeNode, SimpleTree


class SimpleTreeMethods(unittest.TestCase):

    def setUp(self):
        self.root = SimpleTree(SimpleTreeNode(1, None))
        self.empty_tree = SimpleTree(None)

    def testAddChild(self):
        tree_node_1 = SimpleTreeNode(2, self.root.Root)
        self.root.Root.Children.append(tree_node_1)

        tree_node_2 = SimpleTreeNode(3, self.root.Root)
        self.root.Root.Children.append(tree_node_2)

        tree_node_3 = SimpleTreeNode(4, tree_node_2)
        tree_node_2.Children.append(tree_node_3)

        test_node_1 = SimpleTreeNode(12, None)
        test_node_2 = SimpleTreeNode(13, None)

        self.root.AddChild(tree_node_3, test_node_1)
        self.root.AddChild(tree_node_2, test_node_2)

        test_node_3 = SimpleTreeNode(14, None)
        self.empty_tree.AddChild(None, test_node_3)

        self.assertIn(test_node_1, tree_node_3.Children)
        self.assertIn(test_node_2, tree_node_2.Children)

        self.assertEqual(test_node_1.Parent, tree_node_3)
        self.assertEqual(test_node_2.Parent, tree_node_2)

        

    def testDeleteNode(self):

    def testGetAllNodes(self):

    def testFindNodesByValue(self):

    def testMoveNode(self):

    def testCount(self):

    def testLeafCount(self):



if __name__ == '__main__':
    unittest.main()
