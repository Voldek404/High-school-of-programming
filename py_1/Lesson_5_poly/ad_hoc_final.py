class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав-гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу-мяу!"

animal = Animal()  # Создаём объект базового класса
dog = Dog()  # Создаём объект дочернего класса
cat = Cat()  # Создаём ещё один объект дочернего класса

for animal in [dog, cat]: #цикл для неявного вызова метода
    print(animal.speak())
