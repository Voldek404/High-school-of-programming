class BloomFilterWithCounter:

    def __init__(self, f_len, numberOfHashFoos, counter_size):
        self.filter_len = f_len
        self.counter_size = counter_size
        self.numberOfHashFoos = numberOfHashFoos
        self.bit_array = []
        for i in range(self.filter_len):
            count = bitarray(self.counter_size)
            count.setall(0)
            self.bit_array.append(count)

    def hash(self, str1, salt):
        result = 0
        for c in str1:
            code = ord(c)
            result = result * 17 + code
        return (result + salt) % self.filter_len

    def add(self, str1):
        for i in range(self.numberOfHashFoos):
            salt = i
            index = self.hash(str1, salt)
            bit_array = self.bit_array[index]
            current_value = 0
            for bit in bit_array:
                current_value = (current_value << 1) | bit
            new_value = current_value + 1
            new_bit_array = []
            for j in range(len(bit_array)):
                new_bit_array.append((new_value >> (len(bit_array) - j - 1)) & 1)
            self.bit_array[index] = new_bit_array

    def check(self, str1):
        for i in range(self.numberOfHashFoos):
            salt = i
            index = self.hash(str1, salt)
            bit_array = self.bit_array[index]
            current_value = 0
            for bit in bit_array:
                current_value = (current_value << 1) | bit
            new_value = current_value + 1
            if current_value == 0:
                return False
        return True

    def remove(self, str1):
        if (self.check(str1)):
            for i in range(self.numberOfHashFoos):
                salt = i
                index = self.hash(str1, salt)
                bit_array = self.bit_array[index]
                current_value = 0
                for bit in bit_array:
                    current_value = (current_value << 1) | bit
                if current_value > 0:
                    new_value = current_value - 1
                    new_bit_array = []
                    for j in range(len(bit_array)):
                        new_bit_array.append((new_value >> (len(bit_array) - j - 1)) & 1)
                    self.bit_array[index] = new_bit_array

