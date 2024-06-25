# Рефлексия на 5.2 - набрал лишних атрибутов, судя по эталонному решению.
# По итогу нечитабельное поделие и взрыв классов (на мой неопытный взгляд). Впредь буду стремиться к более наглядным решениям


# В данном варианте максимально упростил прошлую иерархию до минимальных атрибутов с целью наглядности
class Ovb():
    def __init__(self, char, location):
        self.char = char
        self.location = location


class Slesar():
    def __init__(self, char_s, location):
        self.char_s = char_s
        self.location = location


class Personel():  # создаем класс-агрегатор, состоящий из менее крупных по масштабу классов, включаем в
    # него и атрибуты этих самых классов поменьше, через описание данных классов в конструкторе
    def __init__(self, Ovb, Slesar):
        self.Ovb = Ovb
        self.Slesar = Slesar

    def about(self):
        print('Первый класс композиции ', self.Ovb.char, 'Второй класс композиции - ', self.Slesar.char_s,
              'Расположение юнитов соответственно - ', 'Substation #', self.Ovb.location, 'Substation #',
              self.Slesar.location)


ovb = Ovb('подвижный', 357)
slesar = Slesar('стационарный', 190)
personel = Personel(ovb, slesar)
print(personel.about())


class Son():
    def __init__(self, age, name):
        self.age = age
        self.name = name


class Daughter():
    def __init__(self, age, name):
        self.age = age
        self.name = name


class Parent():  # создаем класс-агрегатор, состоящий из менее крупных по масштабу классов, включаем в
    # него и атрибуты этих самых классов поменьше, через описание данных классов в конструкторе
    def __init__(self, Son, Daughter):
        self.Son = Son
        self.Daughter = Daughter

    def aging(self, age_up):
        self.Son.age += age_up
        self.Daughter.age += age_up
        print('Son`s age = ', self.Son.age, 'Daughter`s age =', self.Daughter.age),


son = Son(15, 'Igor')
daughter = Daughter(18, 'Elena')
parent = Parent(son, daughter)
print(parent.aging(5))
