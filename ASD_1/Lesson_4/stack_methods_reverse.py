class Node:
    def init(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def init(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            self.tail = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
            self.tail = item

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            newNode.prev = None

    def len(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def delete_head(self):
        if self.head is None:
            return None
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_value

    def delete_tail(self):
        if self.tail is None:
            return None
        removed_value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value


class Stack:
    def init(self):
        self.stack = LinkedList2()

    def size(self):
        return self.stack.len()

    def pop(self):
        return self.stack.delete_head()

    def push(self, value):
        self.stack.add_in_head(Node(value))

    def peek(self):
        if self.stack.head is not None:
            return self.stack.head.value
        return None
