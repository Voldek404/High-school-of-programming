class BitSet:
    def __init__(self, size):
        self.size = size
        self.bitset = bytearray(self.size)

    def artificial_muscle_fibers_helper(self, number, repeated_array):
        byte_index = number // 8
        bit_index = number % 8
        if byte_index >= 8192:
            raise ValueError("Число выходит за пределы буфера")
        if self.bitset[byte_index] & (1 << bit_index):
            repeated_array.append(number)
            return False
        else:
            self.bitset[byte_index] |= (1 << bit_index)
            return True

    def artificial_muscle_fibers(self, numbers):
        repeated_array = []
        for index, number in enumerate(numbers):
            self.artificial_muscle_fibers_helper(number, repeated_array)
        return len(repeated_array)


bitset = BitSet(32000)
numbers = [1, 2, 32000, 15, 2, 32000]
repeated_numbers = bitset.artificial_muscle_fibers(numbers)
