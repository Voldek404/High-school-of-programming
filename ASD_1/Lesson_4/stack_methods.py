class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class Dummy(Node):
    pass


class LinkedList2:
    def __init__(self):
        self.dummy = Dummy()
        self.head = self.dummy
        self.tail = self.dummy

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

    def delete_tail(self):
        if isinstance(self.dummy.prev, NodeDummy):
            return None
        self.dummy.prev.prev.next = self.dummy.prev.next
        current = self.dummy.prev
        self.dummy.prev = self.dummy.prev.prev
        current.next = None
        current.prev = None
        self.size -= 1


class Stack:
    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        return self.stack.len()

    def pop(self):
        if self.size() > 0:
            return self.stack.pop(0)
        return None

    def push(self, value):
        self.stack.add_in_tail(Node(value))

    def peek(self):
        if self.stack.len() == 0:
            return None
        return self.stack.tail.value
