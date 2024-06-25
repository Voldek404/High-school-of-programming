import random


class Personel:
    def __init__(self, l: object) -> object:
        self.location = l  # Номер подстанции, где находится юнит

    def move(self):  # Перемещение юнита на новый объект
        self.location = random.randint(1, 357)


class Ovb(Personel):  # Определение класса-наследника "Электромонтер оперативно-выездной бригады"
    def __init__(self, l):
        super().__init__(l)

    def move(self):  # Перемещение юнита на новый объект
        self.location = random.randint(1, 357)
        print('Ovb loc = ', self.location)


class Slesar(Personel):  # Определение класса-наследника "Слесарь"
    def __init__(self, l):
        super().__init__(l)

    def move(self):  # Перемещение юнита на новый объект
        self.location = random.randint(1, 357)
        print('Slesar  loc = ', self.location)


ovb = Ovb(Personel)
slesar = Slesar(Personel)
a = []
objects = [ovb, slesar]
for i in range(500):
    rand_obj = str((random.choice(objects)).move())
    a.append(str(rand_obj))
print(a)
# в массив пишутся только None, в связи с тем, что результат метода не возвращается в переменную, однако исправно выполняется в объеме Print`a рандомайзера локации
# таким образом имеем 500 случайных значений и массив, забитый None`ами
