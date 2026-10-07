class AbstractBloomFilter(ABC):
    # конструктор
    # предусловие: f_len > 0
    # постусловие: создан пустой фильтр Блума заданного размера

    def __init__(self, f_len:int):
        pass

    # команда

    # постуловие - строка добавлена в фильтр
    @abstractmethod
    def add(self, str1:str) -> None:
        pass

    # запрос
    # False - строка не добавлялась, True Positive or False Positive результат
    @abstractmethod
    def is_value(self, str1:str) -> bool:
        pass


class BloomFilter(AbstractBloomFilter):
    def __init__(self, f_len:int):
        if f_len <= 0:
            raise ValueError("Размер фильтра должен быть положительным")
        self.filter_len = f_len
        self.bit_list = 0

    def hash1(self, str1:str) -> int:
        result = 0
        for c in str1:
            code = ord(c)
            result = result * 17 + code
        return result % self.filter_len

    def hash2(self, str1:str) -> int:
        result = 0
        for c in str1:
            code = ord(c)
            result = result * 223 + code
        return result % self.filter_len

    def add(self, str1:str) -> None:
        self.bit_list |= self.hash1(str1)
        self.bit_list |= self.hash2(str1)
        return None

    def is_value(self, str1) -> bool:
        return self.bit_list & (self.hash1(str1) | self.hash2(str1)) == self.hash1(
            str1
        ) | self.hash2(str1)




