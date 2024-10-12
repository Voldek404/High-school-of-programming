class BitSet:
    def __init__(self, size):
        self.size = size
        self.bitset = bytearray(self.size)

    def add(self, number):

        byte_index = number // 8
        bit_index = number % 8
        if byte_index >= self.size:
            raise ValueError("Число выходит за пределы буфера")

        # Проверяем, если бит уже установлен
        if self.bitset[byte_index] & (1 << bit_index):
            return False  # Число повторяется
        else:
            # Устанавливаем бит
            self.bitset[byte_index] |= (1 << bit_index)
            return True  # Новое число

bitset = BitSet(32000)

numbers = [1, 2, 32000, 15, 2, 32000]  # Пример чисел, где 2 и 32000 повторяются

for num in numbers:
    if not bitset.add(num):
        print(f"Число {num} повторяется.")
