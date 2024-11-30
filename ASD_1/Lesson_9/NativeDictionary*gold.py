class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
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

    def clean(self, asc):
        self.__ascending = asc
        node = self.head
        while self.head is not None:
            self.head = node.next
            node.next = None
            node.prev = None
            node = self.head
        self.tail = None

    def len(self):
        result = 0
        node = self.head
        while node is not None:
            result += 1
            node = node.next
        return result

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

    def add_in_head(self, newNode):
        newNode.next = self.head
        if newNode.next is not None:
            newNode.next.prev = newNode
        newNode.prev = None
        if self.head is None:
            self.tail = newNode
        self.head = newNode

    def deleteDuplicates(self):
        node = self.head
        while node is not None and node.next is not None:
            if node.next.value == node.value:
                self.delete(node.next.value)
            else:
                node = node.next


class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = {}
        self.step = 1
        self.item_count = 0
        self.orderedListDict = OrderedList(True)

    def hash_fun(self, key):
        a = 7
        b = 11
        p = 7127
        x = 0
        for char in key:
            x += ord(char)
        return ((a * x + b) % p) % self.size

    def seek_slot(self, key):
        hash = self.hash_fun(key)
        index = hash
        current_step = self.step

        while self.slots[index] is not None:
            if self.slots[index] == key:
                return index
            index = (hash + current_step) % self.size
            current_step += self.step
            if index == hash:
                return None
        return index

    def is_key(self, key):
        node = self.ordered_list.find(key)
        return node is not None

    def put(self, key, value):
        if not self.is_key(key):
            self.ordered_list.insert(key)
        self.values[key] = value

    def get(self, key):
        if self.is_key(key):
            return self.values[key]

    def find_index(self, key):
        ordered_items = self.orderedListDict.get_all()
        left, right = 0, len(ordered_items) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_key = ordered_items[mid][0]
            if mid_key == key:
                return mid, ordered_items[mid][1]
            elif mid_key < key:
                left = mid + 1
            else:
                right = mid - 1
        return -1
