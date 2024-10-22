class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setUp(self):
        self.list = LinkedList()

    def len(self):
        if self.head is None:
            return 0
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count


def sum_return( list_1, list_2):
    node_1 = list_1.head
    node_2 = list_2.head
    list_3 = LinkedList()
    prev_node = None
    if list_1.len() == list_2.len():
        while node_1 is not None and node_2 is not None:
            new_node = Node(node_1.value + node_2.value)
            if list_3.head is None:
                list_3.head = new_node
            else:
                prev_node.next = new_node
            prev_node = new_node
            node_1 = node_1.next
            node_2 = node_2.next
        return list_3
    else:
        return None
