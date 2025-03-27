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

    def testGetAllNodes(self):
        self.assertEqual(self.empty_tree.GetAllNodes(), [])

        node2 = SimpleTreeNode(2, self.root.Root)
        node3 = SimpleTreeNode(3, self.root.Root)
        self.root.Root.Children.extend([node2, node3])
        node4 = SimpleTreeNode(4, node2)
        node2.Children.append(node4)

        all_nodes = self.root.GetAllNodes()
        values = [node.NodeValue for node in all_nodes]

        self.assertCountEqual(values, [1, 2, 3, 4])

    def testFindNodesByValue(self):
        self.assertEqual(self.empty_tree.FindNodesByValue(123), [])

        node2 = SimpleTreeNode(5, self.root.Root)
        node3 = SimpleTreeNode(3, self.root.Root)
        node4 = SimpleTreeNode(5, node2)
        self.root.Root.Children.extend([node2, node3])
        node2.Children.append(node4)

        found_nodes = self.root.FindNodesByValue(5)
        self.assertEqual(len(found_nodes), 2)
        for node in found_nodes:
            self.assertEqual(node.NodeValue, 5)

    def testMoveNode(self):
        try:
            self.empty_tree.MoveNode(SimpleTreeNode(1, None), None)
        except Exception as e:
            self.fail(f"MoveNode failed on empty tree: {e}")

        node2 = SimpleTreeNode(2, self.root.Root)
        node3 = SimpleTreeNode(3, node2)
        self.root.Root.Children.append(node2)
        node2.Children.append(node3)

        self.root.MoveNode(node3, self.root.Root)

        self.assertNotIn(node3, node2.Children)

        self.assertEqual(node3.Parent, self.root.Root)

        self.assertIn(node3, self.root.Root.Children)

    def testCount(self):
        self.assertEqual(self.empty_tree.Count(), 0)

        node2 = SimpleTreeNode(2, self.root.Root)
        node3 = SimpleTreeNode(3, node2)
        self.root.Root.Children.append(node2)
        node2.Children.append(node3)

        self.assertEqual(self.root.Count(), 3)

    def testLeafCount(self):
        self.assertEqual(self.empty_tree.LeafCount(), 0)

        node2 = SimpleTreeNode(2, self.root.Root)
        node3 = SimpleTreeNode(3, node2)
        self.root.Root.Children.append(node2)
        node2.Children.append(node3)

        self.assertEqual(self.root.LeafCount(), 1)

        node4 = SimpleTreeNode(4, self.root.Root)
        self.root.Root.Children.append(node4)

        self.assertEqual(self.root.LeafCount(), 2)


if __name__ == '__main__':
    unittest.main()
