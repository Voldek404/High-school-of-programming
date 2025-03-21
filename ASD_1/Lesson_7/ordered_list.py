class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [0] * self.size

    def add(self, value):
        index = hash(value) % self.size
        if self.table[index] == 0:
            self.table[index] = 1
        else:
            self.table[index] += 1

    def find(self, value):
        index = hash(value) % self.size
        return self.table[index] > 0

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

    def mergeTwoLists(self, list_1, list_2, asc=True):
        mergedList = OrderedList(asc)
        if list_1.head is None:
            return list_2
        if list_2.head is None:
            return list_1
        node_1 = list_1.head if asc else list_1.tail
        node_2 = list_2.head if asc else list_2.tail
        add_method = mergedList.add if asc else mergedList.add_in_head
        while node_1 is not None and node_2 is not None:
            if (node_1.value <= node_2.value if asc else node_1.value >= node_2.value):
                add_method(node_1.value)
                node_1 = node_1.next if asc else node_1.prev
            else:
                add_method(node_2.value)
                node_2 = node_2.next if asc else node_2.prev
        while node_1 is not None:
            add_method(node_1.value)
            node_1 = node_1.next if asc else node_1.prev
        while node_2 is not None:
            add_method(node_2.value)
            node_2 = node_2.next if asc else node_2.prev
        return mergedList

    def mostDuplicated(self):
        duplicatesCounter = {}
        node = self.head
        while node is not None:
            value = node.value
            count = duplicatesCounter.get(value, 0) + 1
            duplicatesCounter[value] = count
            node = node.next
        return max(duplicatesCounter, key=duplicatesCounter.get)

    def isSublist(self, sublist):
        node = self.head
        subNode = sublist.head
        index = 0
        while node is not None:
            if node.value == subNode.value:
                node = node.next
                subNode = subNode.next
                index += 1
                if index == sublist.len():
                    return True
            elif node.value != subNode.value:
                subNode = sublist.head
                index = 0
                node = node.next
            print(index)
        return False


    def findIndex(self, val):
        node = self.head
        elements = []
        while node is not None:
            elements.append(node.value)
            node = node.next
        left, right = 0, len(elements) - 1
        while left <= right:
            mid = (left + right) // 2
            if elements[mid] == val:
                return mid
            elif self.compare(elements[mid], val) < 0:
                left = mid + 1
            else:
                right = mid - 1
        return -1

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.strip() < v2.strip():
            return -1
        if v1.strip() == v2.strip():
            return 0
        return 1






