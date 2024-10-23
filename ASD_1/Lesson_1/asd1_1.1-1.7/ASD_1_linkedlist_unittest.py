import unittest

from ASD_1_linkedlist import LinkedList, Node


class TestLinkedListMethods(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_insert(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        self.list.insert(None, node1)
        self.assertEqual(self.list.head, node1)
        self.list.insert(node1, node2)
        self.assertEqual(self.list.head.next, node2)
        self.list.insert(node2, node3)
        self.assertEqual(self.list.head.next.next, node3)

    def test_find_all(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(1)

        self.list.insert(None, node1)
        self.list.insert(node1, node2)
        self.list.insert(node2, node3)

        self.assertEqual(self.list.find_all(1), [node1, node3])
        self.assertEqual(self.list.find_all(2), [node2 ])
        self.assertEqual(self.list.find_all(3), [])

    def test_delete(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(1)
        node4 = Node(3)

        self.list.insert(None, node1)
        self.list.insert(node1, node2)
        self.list.insert(node2, node3)
        self.list.insert(node3, node4)

        self.list.delete(1)
        self.assertEqual(self.list.head.value, 2)
        self.assertEqual(self.list.head.next.value, 1)

        self.list.delete(1, all=True)
        self.assertEqual(self.list.head.next.value, 3)

    def test_clean(self):
        node1 = Node(1)
        node2 = Node(2)
        self.list.insert(node1, node2)

        self.list.clean()
        self.assertEqual(self.list.head, None)

    def test_len(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        self.assertEqual(self.list.len(), 0)

        self.list.insert(None, node1)
        self.list.insert(node1, node2)
        self.list.insert(node2, node3)

        self.assertEqual(self.list.len(), 3)


if __name__ == '__main__':
    unittest.main()
