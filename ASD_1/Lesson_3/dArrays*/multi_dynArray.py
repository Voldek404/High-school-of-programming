import ctypes

class DynArray:
    def __init__(self):
        self.row_counts = 0
        self.num_cols = 0
        self.capacity_1 = 16
        self.capacity_2 = 16
        self.array = self.make_array(self.capacity_1, self.capacity_2)

    def make_array(self, new_capacity_1, new_capacity_2) -> ctypes.Array:
        array = (ctypes.py_object * new_capacity_1)()
        for i in range(new_capacity_1):
            array[i] = (ctypes.py_object * new_capacity_2)()
        return array

    def append(self, itm, row_index) -> None:
        if row_index >= self.row_counts:
            self.row_counts += 1
        if self.num_cols >= self.capacity_2:
            self.resize(self.capacity_1, self.capacity_2 * 2)
        self.array[row_index][self.num_cols] = itm
        self.num_cols += 1

    def insert(self, itm, row_index, col_index):
        if row_index < 0 or row_index >= self.row_counts or col_index < 0 or col_index > self.num_cols:
            raise IndexError('Row or column index is out of bounds')
        if self.num_cols >= self.capacity_2:
            self.resize(self.capacity_1, self.capacity_2 * 2)
        for j in range(self.num_cols, col_index, -1):
            self.array[row_index][j] = self.array[row_index][j - 1]
        self.array[row_index][col_index] = itm
        self.num_cols += 1

    def delete(self, row_index, col_index):
        if row_index < 0 or row_index >= self.row_counts or col_index < 0 or col_index >= self.num_cols:
            raise IndexError('Row or column index is out of bounds')
        for j in range(col_index, self.num_cols - 1):
            self.array[row_index][j] = self.array[row_index][j + 1]
        self.array[row_index][self.num_cols - 1] = None
        self.num_cols -= 1

    def get_row(self, row_index):
        if row_index < 0 or row_index >= self.row_counts:
            raise IndexError('Row index is out of bounds')
        return [self.array[row_index][j] for j in range(self.num_cols)]

    def resize(self, new_capacity_1, new_capacity_2):
        new_array = (ctypes.py_object * new_capacity_1)()
        for i in range(new_capacity_1):
            new_array[i] = (ctypes.py_object * new_capacity_2)()

        for i in range(self.row_counts):
            for j in range(self.num_cols):
                new_array[i][j] = self.array[i][j]
        self.array = new_array
        self.capacity_1 = new_capacity_1
        self.capacity_2 = new_capacity_2



dyn_array = DynArray()
dyn_array.append(100, 0)
print("\nПосле добавления элемента в 0-ю строку:")
print(dyn_array.get_row(0))
dyn_array.insert(200, 0, 0)
print("\nПосле вставки элемента в 0-ю строку на позицию 0:")
print(dyn_array.get_row(0))
dyn_array.delete(0, 0)
print("\nПосле удаления элемента из 0-ой строки на позицию 0:")
print(dyn_array.get_row(0))