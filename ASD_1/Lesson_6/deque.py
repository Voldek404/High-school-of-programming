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


class Deque:
    def __init__(self):
        self.deque = LinkedList2()

    def addFront(self, item):
        self.deque.add_in_head(item)

    def addTail(self, item):
        self.deque.add_in_tail(item)

    def removeFront(self):
        if self.deque.head is not None:
            if self.deque.head.next is None:
                self.deque.head = self.deque.tail = None
            else:
                self.deque.head = self.deque.head.next
                self.deque.head.prev = None

    def removeTail(self):
        if self.deque.tail is not None:
            if self.deque.tail.prev is None:
                self.deque.head = self.deque.tail = None
            else:
                self.deque.tail = self.deque.tail.prev
                self.deque.tail.next = None

    def size(self):
        if self.deque.head is not None:
            return 0
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

