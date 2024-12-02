class PowerSet:

    def __init__(self):
        self.slots = {}

    def size(self):
        return len(self.slots)

    def put(self, value):
        self.slots[value] = None

    def get(self, value):
        return value in self.slots

    def remove(self, value):
        if self.get(value):
            del self.slots[value]
            return True
        return False

    def intersection(self, set2):
        result = PowerSet()
        for el in set2.slots:
            if el in self.slots:
                result.put(el)
        return result

    def union(self, set2):
        result = PowerSet()

        for i in self.slots:
            if i not in result.slots:
                result.put(i)

        for i in set2.slots:
            if i not in result.slots:
                result.put(i)

        return result

    def difference(self, set2):
        result = PowerSet()

        for i in self.slots:
            if i not in set2.slots:
                result.put(i)

        return result

    def isSubSet(self, set2):
        for i in set2.slots:
            if i not in self.slots:
                return False
        return True

    def equals(self, set2):
        if len(self.slots) != len(set2.slots):
            return False
        for element in self.slots:
            if element not in set2.slots:
                return False
        return True

    def decartSet(self, set2):
        set3 = PowerSet()
        for i in self.slots:
            for j in set2.slots:
                set3.put((i, j))
        return set3

def twoPlusIntersections(main_set, sets: list[PowerSet]):
    if any(sub_set.size() == 0 for sub_set in sets):
        return PowerSet()
    intersections_result = PowerSet()
    for element in main_set:
        intersection_counter = 0
        for sub_set in sets:
            if element in sub_set:
                intersection_counter += 1
        if intersection_counter == len(sets):
            intersections_result.put(element)
    return intersections_result
