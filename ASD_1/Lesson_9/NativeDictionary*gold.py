import Node, OrderedList


class NativeDictionary:
    def __init__(self):
        self.orderedListDict = OrderedList(True)

    def is_key(self, key):
        node = self.ordered_list.find((key, None))
        return node is not None

    def put(self, key, value):
        existing_node = self.orderedListDict.find((key, None))
        if existing_node is not None:
            existing_node.value = (key, value)
        else:
            self.orderedListDict.add((key, value))

    def get(self, key):
        node = self.orderedListDict.find((key, None))
        if node is not None:
            return node.value[1]
        return None

    def find_index(self, key):
        ordered_items = self.orderedListDict.get_all()
        left, right = 0, len(ordered_items) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_key = ordered_items[mid].value[0]
            if mid_key == key:
                return mid, ordered_items[mid].value[1]
            elif mid_key < key:
                left = mid + 1
            else:
                right = mid - 1
        return -1
