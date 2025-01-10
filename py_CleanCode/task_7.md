# Task 7. ООП и интерфейсы

##3.1. 
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

# Пример использования:

# 1. Создание квадрата с длиной стороны 4
square = Rectangle.from_side(4)
print(square)  # Rectangle(length=4, width=4)

# 2. Создание прямоугольника с длиной 6 и шириной 3
rect1 = Rectangle.from_dimensions(6, 3)
print(rect1)  # Rectangle(length=6, width=3)

# 3. Создание прямоугольника с параметрами по умолчанию
rect2 = Rectangle.from_default()
print(rect2)  # Rectangle(length=5, width=3)

# 4. Создание прямоугольника с дополнительной логикой: если длина < ширина, они меняются местами
rect3 = Rectangle.from_default(length=2, width=6)
print(rect3)  # Rectangle(length=6, width=2)

# Пример расчета площади
print(f"Area of rect1: {rect1.area()}")  # Area of rect1: 18



