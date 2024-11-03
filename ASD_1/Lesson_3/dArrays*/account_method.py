import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.bank_account = 4
        self.array = self.make_array(self.capacity + self.bank_account)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count + self.bank_account >= self.capacity:
            self.capacity = self.capacity * 2
            self.resize(self.capacity)
            self.bank_account = int(self.capacity * 0.25)
        self.array[self.count] = itm
        self.count += 1
        if self.bank_account > 0:
            self.bank_account -= 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if self.count + self.bank_account >= self.capacity:
            self.capacity = self.capacity * 2
            self.resize(self.capacity)
            self.bank_account = int(self.capacity * 0.25)
        for j in range(self.count, i, -1):
            self.array[j] = self.array[j - 1]
        self.array[i] = itm
        self.count += 1
        if self.bank_account > 0:
            self.bank_account -= 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]
        self.array[self.count - 1] = None
        self.count -= 1
        if self.count < self.capacity // 4:
            new_capacity = max(self.capacity // 2, 16)
            self.resize(new_capacity)
            self.capacity = new_capacity
            self.bank_account = int(self.capacity * 0.25)
