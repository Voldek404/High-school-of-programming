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
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
        else:
            node = self.head
            while node is not None:
                if node == afterNode:
                    newNode.next = node.next
                    newNode.prev = node
                    if node.next is not None:
                        node.next.prev = newNode
                    else:
                        self.tail = newNode
                    node.next = newNode
                    return
                node = node.next



    def add_in_head(self, newNode):
        node = self.head
        if node is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = node
            node.prev = newNode
            self.head = newNode
