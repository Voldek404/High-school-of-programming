
class HashTable(Generic[T]):
    NIL = 0
    OK = 1
    ERR = 2

    # Конструктор: создана пустая таблица с максимальным размером max_size > 0.
    def __init__(self, max_size: int):
        if max_size <= 0:
            raise ValueError("max_size должен быть положительным")
        self._max_size = max_size

    # Команда: добавить значение. Повторное добавление не изменяет таблицу.
    # Постусловие: значение добавлено (OK) либо свободного места нет (ERR).
    @abstractmethod
    def put(self, value: T) -> None:
        pass

    # Команда: удалить значение.
    # Постусловие: значение удалено (OK) либо отсутствует (ERR).
    @abstractmethod
    def remove(self, value: T) -> None:
        pass

    # Запросы.
    @abstractmethod
    def contains(self, value: T) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    # Запросы статусов последних соответствующих команд.
    @abstractmethod
    def get_put_status(self) -> int:
        pass

    @abstractmethod
    def get_remove_status(self) -> int:
        pass


class HashTableImpl(HashTable[T]):
    # Реализация последовательными пробами; удалённые слоты отмечаются отдельно.
    _EMPTY = 0
    _OCCUPIED = 1
    _DELETED = 2

    def __init__(self, max_size: int):
        super().__init__(max_size)
        self._slots: list[T | None] = [None] * max_size
        self._states = [self._EMPTY] * max_size
        self._count = 0
        self._put_status = self.NIL
        self._remove_status = self.NIL

    def _find_index(self, value: T) -> int:
        start = hash(value) % self._max_size
        for offset in range(self._max_size):
            index = (start + offset) % self._max_size
            if self._states[index] == self._EMPTY:
                return -1
            if (self._states[index] == self._OCCUPIED
                    and self._slots[index] == value):
                return index
        return -1

    def put(self, value: T) -> None:
        start = hash(value) % self._max_size
        first_deleted = -1
        for offset in range(self._max_size):
            index = (start + offset) % self._max_size
            state = self._states[index]
            if state == self._OCCUPIED:
                if self._slots[index] == value:
                    self._put_status = self.OK
                    return
            elif state == self._DELETED:
                if first_deleted == -1:
                    first_deleted = index
            else:
                self._insert(first_deleted if first_deleted != -1 else index, value)
                return

        if first_deleted != -1:
            self._insert(first_deleted, value)
        else:
            self._put_status = self.ERR

    def _insert(self, index: int, value: T) -> None:
        self._slots[index] = value
        self._states[index] = self._OCCUPIED
        self._count += 1
        self._put_status = self.OK

    def remove(self, value: T) -> None:
        index = self._find_index(value)
        if index == -1:
            self._remove_status = self.ERR
            return
        self._slots[index] = None
        self._states[index] = self._DELETED
        self._count -= 1
        self._remove_status = self.OK

    def contains(self, value: T) -> bool:
        return self._find_index(value) != -1

    def size(self) -> int:
        return self._count

    def get_put_status(self) -> int:
        return self._put_status

    def get_remove_status(self) -> int:
        return self._remove_status
