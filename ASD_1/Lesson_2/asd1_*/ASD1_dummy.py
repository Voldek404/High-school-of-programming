class Node:
    def __init__(self, v: Any):
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

    def add_in_tail(self, item: Any) -> None:
        self.tail.next = item
        item.prev = self.tail
        item.next = None
        self.tail = item

    def find(self, val: Any) -> Node | None:
        node = self.head
        while node is not isinstance(node, Dummy):
            if node.value == val:
                return node
            node = node.next
        return None

    def cycle_or_not(self) -> bool:
        node = self.head
        while node is not isinstance(node, Dummy):
            node = node.next
        return not (node is None)

    def find_all(self, val: Any) -> list:
        node = self.head.next
        list_of_nodes = []
        while node is not isinstance(node, Dummy):
            if node.value == val:
                list_of_nodes.append(node)
            node = node.next
        return list_of_nodes

    def delete(self, val: Any, all=False) -> None:
        node = self.head.next
        while node is not isinstance(node, Dummy):
            if node.value == val:
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                if not all:
                    break
            node = node.next

    def clean(self) -> None:
        node = self.head.next
        while node is not isinstance(node, Dummy):
            next_node = node.next
            node.next = None
            node.prev = None
            node = next_node
        self.head.next = None
        self.tail = self.dummy

    def len(self) -> int:
        node = self.head.next
        length = 0
        while node is not isinstance(node, Dummy):
            length += 1
            node = node.next
        return length

    def insert(self, afterNode: int, newNode: int):
        if afterNode is None:
            self.add_in_head(newNode)
        else:
            newNode.next = afterNode.next
            newNode.prev = afterNode
            if afterNode.next:
                afterNode.next.prev = newNode
            afterNode.next = newNode
            if afterNode is self.tail:
                self.tail = newNode

    def add_in_head(self, newNode):
        newNode.next = self.head.next
        newNode.prev = self.dummy
        if self.head.next:
            self.head.next.prev = newNode
            self.head.next = newNode
        if self.tail is self.dummy:
            self.tail = newNode
