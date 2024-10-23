class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        if self.head is None:
            return []
        values_list = []
        node = self.head
        while node is not None:
            if node.value == val:
                values_list.append(node)
            node = node.next
        return values_list

    def delete(self, val, all=False):
        while self.head is not None and self.head.value == val:
            self.head = self.head.next
            if not all:
                return
        node = self.head
        while node is not None and node.next is not None:
            if node.next.value == val:
                node.next = node.next.next
                if not all:
                    return
                else:
                    continue
            else:
                node = node.next

    def clean(self):
        if self.head is None:
            return
        node = self.head
        while node is not None:
            next_node = node.next
            node.next = None
            node = node.next
        node = None

    def len(self):
        if self.head is None:
            return 0
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return
        node = self.head
        while node is not None:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                return
            node = node.next
