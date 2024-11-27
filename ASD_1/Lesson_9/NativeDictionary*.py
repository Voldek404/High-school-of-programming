class BitStringDictionary:
    def __init__(self, size, key_length):
        self.size = size
        self.key_length = key_length
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        hash_value = 0
        for bit in key:
            hash_value = (hash_value << 1) | int(bit)
        return hash_value % self.size

    def seek_slot(self, key):
        hash_value = self.hash_fun(key)
        start_index = hash_value
        index = hash_value
        while self.slots[index] is not None and self.slots[index] != key:
            index = (index + 1) % self.size
            if index == start_index:
                return None
        return index

    def add(self, key, value):
        index = self.seek_slot(key)
        if index is None:
            raise Exception("Таблица переполнена")
        self.slots[index] = key
        self.values[index] = value

    def remove(self, key):
        index = self.seek_slot(key)
        if index is None or self.slots[index] is None:
            raise KeyError("Ключ не найден")
        self.slots[index] = None
        self.values[index] = None

    def get(self, key):
        index = self.seek_slot(key)
        if index is None or self.slots[index] is None:
            return None
        return self.values[index]

    def __str__(self):
        return str([(self.slots[i], self.values[i]) for i in range(self.size) if self.slots[i] is not None])
