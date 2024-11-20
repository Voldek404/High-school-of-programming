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
        list_1.deleteDuplicates()
        list_2.deleteDuplicates()
        mergedList = OrderedList(asc)
        if list_1.head is None:
            return list_2
        if list_2.head is None:
            return list_1
        node_1 = list_1.head
        node_2 = list_2.head
        if asc:
            while node_1 is not None and node_2 is not None:
                if node_1.value < node_2.value:
                    mergedList.add(node_1.value)
                    node_1 = node_1.next
                else:
                    mergedList.add(node_2.value)
                    node_2 = node_2.next
            while node_1 is not None:
                mergedList.add(node_1.value)
                node_1 = node_1.next
            while node_2 is not None:
                mergedList.add(node_2.value)
                node_2 = node_2.next
        else:
            node_1 = list_1.tail
            node_2 = list_2.tail
            while node_1 is not None and node_2 is not None:
                if node_1.value > node_2.value:
                    mergedList.add_in_head(node_1.value)
                    node_1 = node_1.prev
                else:
                    mergedList.add_in_head(node_2.value)
                    node_2 = node_2.prev
            while node_1 is not None:
                mergedList.add_in_head(node_1.value)
                node_1 = node_1.prev
            while node_2 is not None:
                mergedList.add_in_head(node_2.value)
                node_2 = node_2.prev
        return mergedList

    def mostDuplicated(self):
        duplicatesCounter = {}
        node = self.head
        duplicatesCounter[node.value] = 0
        while node is not None:
            if node.value in duplicatesCounter:
                duplicatesCounter[node.value] += 1
            else:
                duplicatesCounter[node.value] = 1
            node = node.next
        return max(duplicatesCounter, key=duplicatesCounter.get)

    def isSublist(self, sublist):
        node = self.head
        subNode = sublist.head
        while node is not None:
            current = node
            while current is not None and subNode is not None and current.value == subNode.value:
                current = current.next
                subNode = subNode.next
            if subNode is None:
                return True
            subNode = sublist.head
            node = node.next
        return False

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.strip() < v2.strip():
            return -1
        if v1.strip() == v2.strip():
            return 0
        return 1


