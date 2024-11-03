class DynamicMultiArray:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.size = self.calculate_size(dimensions)
        self.array = [0] * self.size

    def calculate_size(self, dimensions):
        size = 1
        for dim in dimensions:
            size *= dim
        return size

    def get_flat_index(self, indices):
        if len(indices) != len(self.dimensions):
            raise IndexError("Количество индексов не совпадает с размерностями массива.")
        flat_index = 0
        for i in range(len(indices)):
            flat_index *= self.dimensions[i]
            flat_index += indices[i]
        return flat_index

    def set_value(self, indices, value):
        flat_index = self.get_flat_index(indices)
        self.array[flat_index] = value

    def get_value(self, indices):
        flat_index = self.get_flat_index(indices)
        return self.array[flat_index]

    def insert(self, indices, value):
        flat_index = self.get_flat_index(indices)
        self.size += 1
        self.array.append(0)
        for i in range(self.size - 1, flat_index, -1):
            self.array[i] = self.array[i - 1]
        self.array[flat_index] = value
        if indices[-1] == self.dimensions[-1] - 1:
            self.dimensions[-1] += 1

    def display(self):
        print(self.array)
