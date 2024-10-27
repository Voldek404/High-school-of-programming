class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        list_of_nodes = []
        if not node:
            return []
        while node:
            if node.value == val:
                list_of_nodes.append(node)
            node = node.next
        return list_of_nodes

    def delete(self, val, all=False):
        node = self.head
        while node:
            if node.value == val:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                current = node
                node = node.next
                current.next = None
                current.prev = None
                if not all:
                    break
            else:
                node = node.next

    def clean(self):
        node = self.head
        while node:
            next_node = node.next
            node.next = None
            node.prev = None
            node = next_node
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.prev = self.tail
                newNode.prev.next = newNode
                newNode.next = None
                self.tail = newNode
        else:
            if afterNode.next is not None:
                afterNode.next.prev = newNode
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next = newNode
            if afterNode is self.tail:
                self.tail = newNode

    def add_in_head(self, newNode):
        node = self.head
        if node is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = node
            node.prev = newNode
            self.head = newNode

    def list_rotation(self):
        if self.head is None and self.tail is None:
            return None
        ex_list_head = self.head
        ex_list_tail = self.tail
        node = self.head
        while node:
            node_next = node.next
            node.next, node.prev = node.prev, node.next
            node = node_next
        self.tail = ex_list_head
        self.head = ex_list_tail

    def cycle_or_not(self):
        point_one = self.head
        point_two = self.head
        while point_two and point_two.next:
            if point_one == point_two:
                return True
            point_one = point_one.next
            point_two = point_two.next.next
        return False

    def sort(self):
        length = self.len()
        list2 = LinkedList2()
        for _ in range(length):
            min_node = self.head
            node = self.head
            while node:
                if node.value < min_node.value:
                    min_node = node
                node = node.next
            list2.add_in_tail(Node(min_node.value))
            self.delete(min_node)
        return list2

    def combine_lists(self, list1, list2):
        list3 = LinkedList2()
        list1.sort()
        list2.sort()
        node_1 = list1.head
        node_2 = list2.head
        while node_1 is not None and node_2 is not None:
            if node_1.value < node_2.value:
                list3.add_in_tail(Node(node_1.value))
                node_1 = node_1.next
            if node_1.value >= node_2.value:
                list3.add_in_tail(Node(node_2.value))
                node_2 = node_2.next
        while node_1 is not None:
            list3.add_in_tail(Node(node_1.value))
            node_1 = node_1.next
        while node_2 is not None:
            list3.add_in_tail(Node(node_2.value))
            node_2 = node_2.next
        return list3
