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
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
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
        node = self.head
        previous = None
        while node is not None:
            if node.value == val:
                if previous is not None:
                    previous.next = node.next
                    if node.next is None:
                        self.tail = previous
                else:
                    self.head = self.head.next
                    if self.head is None:
                        self.tail = None
                current = node
                node = node.next
                current.next = None
                if not all:
                    break
                continue

            previous = node
            node = node.next

    def clean(self):
        if self.head is None:
            return
        node = self.head
        while node is not None:
            self.head = node.next
            node.next = None
            node = self.head
        self.tail = None

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
            if self.tail is None:
                self.tail = newNode
            return
        node = self.head
        while node is not None:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                if node == self.tail:
                    self.tail = newNode
                return
            node = node.next
