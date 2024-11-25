class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.item_count = 0
        self.hash_foos = [self.hash_fun, self.hash_fun1]
        self.salt = {}

    def hash_fun(self, value):
        a = 7
        b = 11
        p = 7127
        x = 0
        for char in value:
            x += ord(char)
        return ((a * x + b) % p) % self.size

    def hash_fun_1(self, value):
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
        for hash_fun in self.hash_functions:
            index = hash_fun(value)
            if self.slots[index] is None:
                self.slots[index] = value
                return

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

    def addSalt(self, value):
        salt_value = int(random.random() * 256)
        salted_value = value + salt_value
        self.put(salted_value)
        self.salts[value] = (salt_value, salted_value) 
        return salted_value

    def ddos_with_equal_keys(self):
        keys = ['qq', 'aa', 'bb', 'cc', 'dd', 'ee','vv', 'ww','xx', 'yy', 'zz']
        for key in keys:
            self.addSalt(key)
