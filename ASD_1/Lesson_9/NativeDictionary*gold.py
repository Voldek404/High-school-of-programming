class Node:
    def __init__(self, value):
        self.value = value
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

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node.value)
            node = node.next
        return r

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


class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = 1
        self.item_count = 0

    def hash_fun(self, key):
        a = 7
        b = 11
        p = 7127
        x = 0
        for char in key:
            x += ord(char)
        return ((a * x + b) % p) % self.size

    def get(self, key):
        supposed_index = self.seek_slot(key)
        if supposed_index is None:
            return None
        if self.slots[supposed_index] is None:
            return None
        return self.values[supposed_index]

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

    def nativeDictOnSortedList(self):
        raw_list = OrderedList(True)
        for key in self.slots:
            if key is not None:
                raw_list.add(key)
        keys_list = raw_list.get_all()
        key_value_pairs = [(key, self.values[i]) for i, key in enumerate(self.slots) if key is not None]
        return sorted(key_value_pairs, key = lambda pair: keys_list .index[pair[0]])
