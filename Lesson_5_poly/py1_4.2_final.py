import random


class Personel:
    def __init__(self, l: object) -> object:
        self.location = l  # Номер подстанции, где находится юнит

    def move(self):  # Перемещение юнита на новый объект
        self.location = random.randint(1, 357)
    def foo(self):
        print("Personel:")


class Ovb(Personel):  # Определение класса-наследника "Электромонтер оперативно-выездной бригады"
    def __init__(self, l):
        super().__init__(l)
    def foo(self):
        print("Ovb")

    def move(self):  # Перемещение юнита на новый объект
        self.location = random.randint(1, 357)
        print('Ovb loc = ', self.location)


class Slesar(Personel):  # Определение класса-наследника "Слесарь"
    def __init__(self, l):
        super().__init__(l)
    def foo(self):
        print("Slesar")

    def move(self):  # Перемещение юнита на новый объект
        self.location = random.randint(1, 357)
        print('Slesar  loc = ', self.location)


personels = []
for i in range(500):
    if random.randint(1, 10) <= 5:
        personels.append(Ovb(str(i)))
    else:
        personels.append(Slesar(str(i)))

for i in range(500):
    personels[i].foo()
    print(id(personels[i].foo()))
    print(type(personels[i].foo()))
# изначально функционал полиморфизма не был реализован должным образом
