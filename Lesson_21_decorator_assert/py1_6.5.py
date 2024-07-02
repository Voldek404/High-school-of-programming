from functools import wraps


class parent:  # буквально класс - "Родитель"
    def __init__(self, w, h, a, iq):
        self.weight = w
        self.height = h
        self.age = a
        self.iq = iq

    def grow_pr(self, age):
        assert isinstance(age, int), "Value must be an integer"  # assert #5.1
        assert 0 <= age <= 150, "Age must be between 0 and 150"  # assert #5.3
        self.age = age
        self.age += age
        if age >= 1:
            self.iq += 5 * age
            assert 5 * age != 0, "IQ cannot be equal to zero"  # assert #5.5


class son(parent):  # Наследственный класс "Сын"
    def __init__(self, n, ds, rel, w, h, a, iq):
        super().__init__(w, h, a, iq)
        self.name = n
        self.doing_sport = ds
        self.relations = rel

    def pairing(self, new_stat):  # Находится ли в отношениях
        self.relations = new_stat
        assert new_stat is not None, "Data cannot be None"  # assert #5.4
        assert len(new_stat) > 0, "Data cannot be empty"  # assert #5.4

    def sport_stat(self, sport_stat_ch):  # Занимается ли спортом
        self.doing_sport = sport_stat_ch
        self.iq += 20  # Эффект от занятия спортом на айкью
        assert self.iq is not None, "Result should not be None"  # assert #5.2


class daughter(parent):  # Наследственный класс "Дочь"
    def __init__(self, n, f, pr, w, h, a, iq):
        super().__init__(w, h, a, iq)
        self.name = n
        self.surname = f
        self.old_surname = f  # Резервируем старую фамилию на случай развода
        self.pregnancy = pr

    def bride(self, new_surn, new_preg):  # Имитируем выход замуж с новой фамилией и беременностью
        assert self.surname != new_surn, "Old surname should not be equal to new on first step"  # assert #5.7
        self.surname = new_surn
        self.pregnancy += new_preg

    def divorce(self):  # Имитируем развод с возвратом старой фамилии
        self.surname = self.old_surname
        assert self.old_surname is not None, "old_surname cannot be None"
        assert 'Old surname' in self.old_surname, "Options must include 'mode" #assert #5.6.


child_1 = son('Артем', 1, 0, 60, 160, 18, 140)
child_2 = daughter('Наташа', 'Королева', 0, 60, 160, 18, 140)
child_1.pairing(1)
child_1.sport_stat(1)
print('Занялся ли спортом сын - ', child_1.doing_sport, 'Нашел ли сын девушку - ', child_1.relations,
      'Как все это сказалось на айкью - ', child_1.iq)
print(child_2.pregnancy, child_2.surname)
child_2.divorce()  # имитируем развод и девичью фамилию
print(child_2.surname)
print(child_1.grow_pr(''))  # checking 5.1 assert with string input
print(child_1.sport_stat(2))
print(child_1.grow_pr(160))  # checking 5.3 assert with string input
print(child_2.pairing(''))
print(child_2.bride("Королева", 1))
