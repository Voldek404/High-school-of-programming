# Task 7. ООП и интерфейсы

## 3.1. 

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Статический метод для создания квадрата (один параметр)
    @staticmethod
    def from_side(side):
        return Rectangle(side, side)

    # Статический метод для создания прямоугольника (два параметра)
    @staticmethod
    def from_dimensions(length, width):
        return Rectangle(length, width)

    # Статический метод с параметрами по умолчанию и дополнительной логикой
    @staticmethod
    def from_default(length=5, width=3):
        # Логика: если длина меньше ширины, меняем их местами
        if length < width:
            length, width = width, length
        return Rectangle(length, width)

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"

## 3.2. Ранее абстрактные классы не использовал. Пример с Гугла

from abc import ABC, abstractmethod

# Абстрактный класс (интерфейс)
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass  # Метод должен быть реализован в дочернем классе

    @abstractmethod
    def area(self):
        pass  # Метод должен быть реализован в дочернем классе

# Реализация интерфейса
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return f"Drawing a circle with radius {self.radius}"

    def area(self):
        return 3.14 * self.radius ** 2




