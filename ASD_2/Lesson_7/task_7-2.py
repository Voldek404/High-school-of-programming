class Heap:
    def __init__(self):
        self.HeapArray = []

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
        self.SiftDown(0)
        return result
