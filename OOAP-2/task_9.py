from __future__ import annotations

import copy
import json
from typing import Any as PythonAny


class General(object):
    """Базовый класс с фундаментальными операциями над объектом."""

    def copy_from(self, source: General) -> None:
        """Глубоко копирует состояние source в существующий объект."""
        if type(self) is not type(source):
            raise TypeError("Можно копировать объекты одного класса")

        self.__dict__.clear()
        self.__dict__.update(copy.deepcopy(source.__dict__))

    def clone(self) -> General:
        """Создаёт глубокую копию объекта."""
        return copy.deepcopy(self)

    def equals(self, other: object) -> bool:
        """Сравнивает объекты вместе с их вложенными данными."""
        return type(self) is type(other) and self.__dict__ == other.__dict__

    def serialize(self) -> str:
        """Сериализует состояние объекта в JSON."""
        return json.dumps(self.__dict__, ensure_ascii=False)

    @classmethod
    def deserialize(cls, data: str) -> General:
        """Создаёт объект из JSON, не вызывая конструктор."""
        state: PythonAny = json.loads(data)

        if not isinstance(state, dict):
            raise ValueError("Ожидался JSON-объект")

        instance = cls.__new__(cls)
        instance.__dict__.update(state)
        return instance

    def print_object(self) -> None:
        """Печатает наглядное представление объекта."""
        print(self)

    def is_type(self, expected_type: type) -> bool:
        """Проверяет, является ли объект экземпляром указанного типа."""
        return isinstance(self, expected_type)

    def real_type(self) -> type:
        """Возвращает точный класс объекта."""
        return type(self)

    def __repr__(self) -> str:
        attributes = ", ".join(
            f"{name}={value!r}"
            for name, value in self.__dict__.items()
        )
        return f"{type(self).__name__}({attributes})"


class Any(General):
    pass


class Transformer(Any):
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model
        self.measurements: list[float] = []


class CurrentTransformer(Transformer):
    pass


# Демонстрация операций
original = CurrentTransformer("Электроаппарат", "ТТ-100")
original.measurements.append(5.2)

# Клонирование: вложенный список также копируется.
clone = original.clone()
clone.measurements.append(6.1)

print(original)                         # Печать объекта
print(original.equals(clone))           # False: списки различаются
print(original.is_type(Transformer))    # True
print(original.real_type().__name__)    # CurrentTransformer

# Сериализация и восстановление.
serialized = original.serialize()
restored = CurrentTransformer.deserialize(serialized)
print(original.equals(restored))        # True

# Копирование состояния в существующий объект.
target = CurrentTransformer("Другая марка", "ТТ-200")
target.copy_from(original)
print(target.equals(original))           # True
