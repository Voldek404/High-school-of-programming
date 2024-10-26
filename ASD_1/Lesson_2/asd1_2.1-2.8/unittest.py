import unittest

from ASD_1_linkedlist import LinkedList2, Node


class TestLinkedList2(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList2()

    def test_add_in_tail(self):
        node1 = Node(1)
        node2 = Node(2)
        self.linked_list.add_in_tail(node1)
        self.linked_list.add_in_tail(node2)
        self.assertEqual(self.linked_list.head.value, 1)
        self.assertEqual(self.linked_list.tail.value, 2)
        self.assertEqual(self.linked_list.head.next.value, 2)

    def test_find(self):
        node1 = Node(1)
        node2 = Node(2)
        self.linked_list.add_in_tail(node1)
        self.linked_list.add_in_tail(node2)
        found_node = self.linked_list.find(2)
        self.assertEqual(found_node.value, 2)
        self.assertIsNone(self.linked_list.find(3))

    def test_find_all(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(1)
        self.linked_list.add_in_tail(node1)
        self.linked_list.add_in_tail(node2)
        self.linked_list.add_in_tail(node3)
        found_nodes = self.linked_list.find_all(1)
        self.assertEqual(len(found_nodes), 2)

    def test_delete(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        self.linked_list.add_in_tail(node1)
        self.linked_list.add_in_tail(node2)
        self.linked_list.add_in_tail(node3)

        self.linked_list.delete(2)
        self.assertEqual(self.linked_list.length(), 2)
        self.assertIsNone(self.linked_list.find(2))

        self.linked_list.delete(1)
        self.assertEqual(self.linked_list.head.value, 3)

        self.linked_list.delete(3)
        self.assertIsNone(self.linked_list.head)

    def test_clean(self):
        node1 = Node(1)
        node2 = Node(2)
        self.linked_list.add_in_tail(node1)
        self.linked_list.add_in_tail(node2)
        self.linked_list.clean()
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

    def test_len(self):
        node1 = Node(1)
        node2 = Node(2)
        self.linked_list.add_in_tail(node1)
        self.linked_list.add_in_tail(node2)
        self.assertEqual(self.linked_list.length(), 2)
        self.linked_list.delete(1)
        self.assertEqual(self.linked_list.length(), 1)

    def test_insert(self):
        node1 = Node(0)
        node2 = Node(0)
        node3 = Node(0)
        self.linked_list.add_in_tail(node1)
        self.linked_list.add_in_tail(node3)

        self.linked_list.insert(node1, node2)
        self.assertEqual(self.linked_list.head.next.value, 2)
        self.assertEqual(self.linked_list.tail.value, 3)

        self.linked_list.insert(None, Node(0))  # Insert at the head
        self.assertEqual(self.linked_list.head.value, 0)


if __name__ == "__main__":
    unittest.main()
