import unittest
from LinkedList_star_task import LinkedList, Node

class TestSumLinkedLists(unittest.TestCase):

    def create_linked_list(self, values):
        linked_list = LinkedList()
        for value in values:
            linked_list.add_in_tail(Node(value))
        return linked_list

    def linked_list_to_list(self, linked_list):
        result = []
        node = linked_list.head
        while node is not None:
            result.append(node.value)
            node = node.next
        return result

    def test_equal_length_lists(self):
        list_1 = self.create_linked_list([1, 2, 3])
        list_2 = self.create_linked_list([4, 5, 6])
        expected_result = [5, 7, 9]

        result_list = sum_return(list_1, list_2)
        result = self.linked_list_to_list(result_list)

        self.assertEqual(result, expected_result)

    def test_different_length_lists(self):
        list_1 = self.create_linked_list([1, 2, 3])
        list_2 = self.create_linked_list([4, 5])

        result_list = sum_return(list_1, list_2)

        self.assertIsNone(result_list)

    def test_empty_lists(self):
        list_1 = self.create_linked_list([])
        list_2 = self.create_linked_list([])
        expected_result = []

        result_list = sum_return(list_1, list_2)
        result = self.linked_list_to_list(result_list)

        self.assertEqual(result, expected_result)

    def test_one_empty_list(self):
        list_1 = self.create_linked_list([1, 2, 3])
        list_2 = self.create_linked_list([])

        result_list = sum_return(list_1, list_2)

        self.assertIsNone(result_list)


if __name__ == '__main__':
    unittest.main()