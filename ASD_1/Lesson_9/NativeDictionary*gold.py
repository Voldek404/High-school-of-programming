class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class OrderedDictFromList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self.data = self.get_all()

    def find_index(self, key):
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_key = self.data[mid][0]
            if mid_key == key:
                return mid
            elif mid_key < key:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def getitem(self, key):
        index = self.find_index(key)
        if index == -1:
            raise KeyError(f"Key '{key}' not found.")
        return self.data[index][1]

    def setitem(self, key, value):
        node = self.head
        while node is not None:
            if node.key == key:
                node.value = value
                return
            if self.compare(node.key, key) > 0:
                self.insert_before(node, key, value)
                return
            node = node.next
        self.insert_after(self.tail, key, value)

    def delitem(self, key):
        node = self.head
        while node is not None:
            if node.key == key:  # Если нашли ключ
                self.delete_node(node)
                return
            node = node.next
        raise KeyError(f"Key '{key}' not found.")

    def compare(self, key1, key2):
        if self.__ascending:
            if key1 < key2:
                return -1
            elif key1 == key2:
                return 0
            else:
                return 1
        else:
            if key1 > key2:
                return -1
            elif key1 == key2:
                return 0
            else:
                return 1

    def add(self, value):
        node = self.head
        if self.__ascending:
            expected_compare_result = (0, 1)
        else:
            expected_compare_result = (0, -1)
        while node is not None:
            if self.compare(node.value, value) in expected_compare_result:
                if node.prev is None:
                    self.add_in_head(Node(value))
                else:
                    self.insert(node.prev, Node(value))
                return None
            if node is self.tail:
                self.insert(node, Node(value))
                return None
            node = node.next
        self.insert(None, Node(value))

    def find(self, val):
        if self.__ascending:
            stop_condition = 1
        else:
            stop_condition = -1
        node = self.head
        while node is not None and self.compare(node.value, val) != stop_condition:
            if self.compare(node.value, val) == 0:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value != val:
                node = node.next
                continue
            if node.prev is not None:
                node.prev.next = node.next
                if node.next is None:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev
            else:
                self.head = self.head.next
                if node.next is not None:
                    node.next.prev = None
                if self.head is None:
                    self.tail = None
            node.next = None
            node.prev = None
            break

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

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
