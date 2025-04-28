class Heap:
    def __init__(self):
        self.HeapArray = []
        self.heap_size = 0

    def Add(self, key):
        if len(self.HeapArray) == self.heap_size:
            return False

        if self.HeapArray[0] is None:
            self.HeapArray[0] = key
        self.HeapArray.append(key)
        self.SiftUp(len(self.HeapArray) - 1)

    def MakeHeap(self, a, depth):
        self.depth = depth
        self.heap_size = 2 ** (self.depth + 1) - 1
        for key in a:
            self.Add(key)
        pass

    def SiftUp(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.HeapArray[index] > self.HeapArray[parent_index]:
                self.HeapArray[index], self.HeapArray[parent_index] = (
                    self.HeapArray[parent_index],
                    self.HeapArray[index],
                )
            else:
                break
            index = parent_index

    def SiftDown(self, index):
        heap_length = len(self.HeapArray)
        while True:
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            maximum_el = index
            if (
                left_index <= heap_length - 1
                and self.HeapArray[left_index] > self.HeapArray[maximum_el]
            ):
                maximum_el = left_index
            if (
                right_index <= heap_length - 1
                and self.HeapArray[right_index] > self.HeapArray[maximum_el]
            ):
                maximum_el = right_index
            if maximum_el != index:
                self.HeapArray[maximum_el], self.HeapArray[index] = (
                    self.HeapArray[index],
                    self.HeapArray[maximum_el],
                )
                index = maximum_el
            else:
                break

    def GetMax(self):
        if len(self.HeapArray) == 0:
            return -1
        result = self.HeapArray[0]
        far_right_el = self.HeapArray[len(self.HeapArray) - 1]
        self.HeapArray[0] = far_right_el
        self.HeapArray.pop()
        self.SiftDown(0)
        return result

    def GetMaxInRange(self, left_value, right_value):
        list_of_max = []
        for el in self.HeapArray:
            if left_value <= el <= right_value:
                list_of_max.append(el)
        if not list_of_max:
            return -1
        return max(list_of_max)

    #4. * Добавьте метод поиска максимального элемента в заданном диапазон значений.
    # Для реализации алгоритма используются свойства кучи ( сверху максимальный элемент поддерева)
    # При несоответствии заданному условию отбрасывается полностью поддерево под несоответствующим значением.
    # Time/Space complexity O(log n)

    def GetInMaxRecursive(self, left_value, right_value):
        if len(self.HeapArray) == 0:
            return -1

        def GetInMaxRecursiveHelper(current_index, left_value, right_value):
            if current_index >= len(self.HeapArray):
                return -1
            current_value = self.HeapArray[current_index]

            max_value = None
            if left_value <= current_value <= right_value:
                max_value = current_value

            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2

            left_max = GetInMaxRecursiveHelper(left_child_index, left_value, right_value)
            right_max = GetInMaxRecursiveHelper(right_child_index, left_value, right_value)

            return max(max_value, left_max, right_max)

        return GetInMaxRecursiveHelper(0, left_value, right_value)


    #5.* Подумайте над эффективным алгоритмом поиска в куче элемента по заданному условию
    # (например, меньше заданного значения). Учитывайте, что классический поиск "вслепую" неэффективен;
    # используйте свойства кучи для оптимизации.
    # Фактически использован подход, использованный выше с пропуском поддеревьев
    # Time/Space complexity O(log n)

    def GetValue(self, target_value):
        if len(self.HeapArray) == 0:
            return -1

        def GetInMaxRecursiveHelper(current_index):
            if current_index >= len(self.HeapArray):
                return -1

            current_value = self.HeapArray[current_index]
            if current_value <= target_value:
                return current_value

            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2

            left_less = None
            if left_child_index < len(self.HeapArray):
                left_less = GetInMaxRecursiveHelper(left_child_index)

            right_less = None
            if right_child_index < len(self.HeapArray):
                right_less = GetInMaxRecursiveHelper(right_child_index)

            values = [v for v in [current_value, left_less, right_less] if v is not None]
            if values:
                return min(values)
            return -1

        return GetInMaxRecursiveHelper(0)

# 6. Метод объединения куч с помощью одного метода и принимаемого параметра второй кучи
    def MergeHeap(self, other_heap):
        for el in other_heap.HeapArray:
            self.Add(el)

