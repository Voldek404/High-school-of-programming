

class PowerSet(HashTable[T]):
    # конструктор
    # предусловие: max_size > 0
    # постусловие: создано пустое множество с максимальным
    # количеством элементов max_size
    def __init__(self, max_size: int):
        super().__init__(max_size)

    # Команды put(), remove(), запросы contains(), size()
    # и запросы статусов наследуются от HashTable.

    # запросы
    # Все операции сохраняют исходные множества и их статусы.

    # Возвращает новое множество общих элементов текущего множества и other.
    def intersection(self, other: PowerSet[T]) -> PowerSet[T]:
        pass

    # Возвращает новое множество всех элементов обоих множеств без повторений.
    # Максимальный размер результата равен сумме максимальных размеров исходных.
    def union(self, other: PowerSet[T]) -> PowerSet[T]:
        pass

    # Возвращает новое множество элементов текущего множества,
    # которые отсутствуют в other.
    # Максимальный размер результата равен максимальному размеру текущего.
    def difference(self, other: PowerSet[T]) -> PowerSet[T]:
        pass

    # Проверяет, является ли other подмножеством текущего множества.
    def is_subset(self, other: PowerSet[T]) -> bool:
        pass


class PowerSetImpl(HashTableImpl[T], PowerSet[T]):

    def intersection(self, other: PowerSet[T]) -> PowerSetImpl[T]:
        result = PowerSetImpl[T](self._max_size)
        for index, state in enumerate(self._states):
            if state == self._OCCUPIED:
                value = self._slots[index]
                if other.contains(value):
                    result.put(value)
        return result

    def union(self, other: PowerSet[T]) -> PowerSetImpl[T]:
        result = PowerSetImpl[T](self._max_size + other._max_size)
        for index, state in enumerate(self._states):
            if state == self._OCCUPIED:
                result.put(self._slots[index])
        for index, state in enumerate(other._states):
            if state == other._OCCUPIED:
                result.put(other._slots[index])
        return result

    def difference(self, other: PowerSet[T]) -> PowerSetImpl[T]:
        result = PowerSetImpl[T](self._max_size)
        for index, state in enumerate(self._states):
            if state == self._OCCUPIED:
                value = self._slots[index]
                if not other.contains(value):
                    result.put(value)
        return result

    def is_subset(self, other: PowerSet[T]) -> bool:
        for index, state in enumerate(other._states):
            if state == other._OCCUPIED:
                if not self.contains(other._slots[index]):
                    return False
        return True
