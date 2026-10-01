class AbstractNativeDictionary:
    # конструктор
    # постусловие: создан пустой словарь
    def __init__(self, capacity):
        pass

    # команды

    # предусловие: слот ключа пуст или содержит этот же ключ
    # постусловие: добавлена новая пара или обновлено значение ключа
    def put(self, key:str, value):
        raise NotImplementedError

    # предусловие: ключ имеется в словаре
    # постусловие: пара с указанным ключом удалена
    def remove(self, key):
        raise NotImplementedError

    # запросы

    # предусловие: ключ имеется в словаре
    def get(self, key):
        raise NotImplementedError

    def contains(self, key):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError

    # запросы статусов

    def get_put_status(self):
        raise NotImplementedError

    def get_remove_status(self):
        raise NotImplementedError

    def get_get_status(self):
        raise NotImplementedError


class NativeDictionary(AbstractNativeDictionary):
    PUT_STATUS_NIL = 0  # put ещё не вызывался
    PUT_STATUS_OK = 1   # значение добавлено или обновлено
    PUT_STATUS_ERR = 2  # слот занят другим ключом

    REMOVE_STATUS_NIL = 0  # remove ещё не вызывался
    REMOVE_STATUS_OK = 1   # пара удалена
    REMOVE_STATUS_ERR = 2  # ключ отсутствует

    GET_STATUS_NIL = 0  # get ещё не вызывался
    GET_STATUS_OK = 1   # значение получено
    GET_STATUS_ERR = 2  # ключ отсутствует

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Вместимость должна быть больше нуля")

        self._capacity = capacity
        self._size = 0

        self._keys = [None] * capacity
        self._values = [None] * capacity

        self._put_status = self.PUT_STATUS_NIL
        self._remove_status = self.REMOVE_STATUS_NIL
        self._get_status = self.GET_STATUS_NIL

    # команды

    def put(self, key, value):
        index = self._index(key)

        if self._keys[index] is None:
            self._keys[index] = key
            self._values[index] = value
            self._size += 1
            self._put_status = self.PUT_STATUS_OK

        elif self._keys[index] == key:
            self._values[index] = value
            self._put_status = self.PUT_STATUS_OK

        else:
            self._put_status = self.PUT_STATUS_ERR

    def remove(self, key):
        index = self._index(key)

        if self._keys[index] != key:
            self._remove_status = self.REMOVE_STATUS_ERR
            return

        self._keys[index] = None
        self._values[index] = None
        self._size -= 1
        self._remove_status = self.REMOVE_STATUS_OK

    # запросы

    def get(self, key):
        index = self._index(key)

        if self._keys[index] != key:
            self._get_status = self.GET_STATUS_ERR
            return None

        self._get_status = self.GET_STATUS_OK
        return self._values[index]

    def contains(self, key):
        index = self._index(key)
        return self._keys[index] == key

    def size(self):
        return self._size

    # запросы статусов

    def get_put_status(self):
        return self._put_status

    def get_remove_status(self):
        return self._remove_status

    def get_get_status(self):
        return self._get_status


    def _index(self, key):
        return sum(ord(char) for char in key) % self._capacity