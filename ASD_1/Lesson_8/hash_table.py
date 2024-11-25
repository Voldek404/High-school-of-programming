class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.item_count = 0

    def hash_fun(self, value):
        a = 7
        b = 11
        p = 7127
        x = 0
        for char in value:
            x += ord(char)
        return ((a * x + b) % p) % self.size

    def seek_slot(self, value):
        if self.item_count == self.size:
            return None

        hash = self.hash_fun(value)
        index = hash
        current_step = self.step

        while self.slots[index] is not None:
            index = (hash + current_step) % self.size
            current_step += self.step
            if index == hash:
                return None

        return index

    def put(self, value):
        index_to_insert = self.seek_slot(value)
        if index_to_insert is None:
            index_to_insert = self.twoFoo(value)
        self.slots[index_to_insert] = value
        self.item_count += 1
        return index_to_insert

    def find(self, value):
        hash = self.hash_fun(value)
        index = hash
        current_step = self.step

        while self.slots[index] is not None:
            if self.slots[index] == value:
                return index
            index = (hash + current_step) % self.size
            current_step += self.step
            if index == hash:
                return None
        return None

    def resizeAndNew(self):
        if self.item_count >= self.size * 0.75:
            new_size = self.size * 2
            new_step = self.step * 2
            new_hash_table = HashTable(new_size, new_step)
            for i in range(self.size):
                if self.slots[i] is not None:
                    new_hash_table.put(self.slots[i])
            self.size = new_size
            self.step = new_step
            self.slots = new_hash_table.slots
            self.item_count = new_hash_table.item_count

    def twoFooHelper(self, index, step):
        index = (index + step) % self.size
        return index

    def twoFoo(self, value):
        step = 2
        if self.find(value) is None:
            index = self.hash_fun(value)
            while self.slots[index] is not None:
                index = self.twoFooHelper(index, step)
            self.slots[index] = value

    def addSalt(self, value):
        salt_value = int(random.random() * 256)
        salted_value = value + salt_value
        self.put(salted_value)
        return salted_value

    def ddos_with_equal_keys(self):
        keys = ['qq', 'aa', 'bb', 'cc', 'dd', 'ee','vv', 'ww','xx', 'yy', 'zz']
        for key in keys:
            self.addSalt(key)
