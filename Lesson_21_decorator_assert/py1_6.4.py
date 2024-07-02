from functools import wraps


def invariant(predicate):
    def invariant_decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            assert predicate(self), f"Invariant condition failed {method.__name__}"
            return result

        return wrapper

    return invariant_decorator


class parent:  # буквально класс - "Родитель"
    def __init__(self, w, h, a, iq):
        self.weight = w
        self.height = h
        self.age = a
        self.iq = iq

    @invariant(lambda self: self.age >= 0)
    def grow_pr(self, age):
        self.age += age
        if age >= 1:
            self.iq += 5 * age


class son(parent):  # Наследственный класс "Сын"
    def __init__(self, n, ds, rel, w, h, a, iq):
        super().__init__(w, h, a, iq)
        self.name = n
        self.doing_sport = ds
        self.relations = rel

    def pairing(self, new_stat):  # Находится ли в отношениях
        self.relations = new_stat

    def sport_stat(self, sport_stat_ch):  # Занимается ли спортом
        self.doing_sport = sport_stat_ch
        self.iq += 20  # Эффект от занятия спортом на айкью


class daughter(parent):  # Наследственный класс "Дочь"
    def __init__(self, n, f, pr, w, h, a, iq):
        super().__init__(w, h, a, iq)
        self.name = n
        self.surname = f
        self.old_surname = f  # Резервируем старую фамилию на случай развода
        self.pregnancy = pr

    def bride(self, new_surn, new_preg):  # Имитируем выход замуж с новой фамилией и беременностью
        if self.surname != new_surn:
            self.surname = new_surn
        self.pregnancy += new_preg

    def divorce(self):  # Имитируем развод с возвратом старой фамилии
        self.surname = self.old_surname


child_1 = son('Артем', 0, 0, 60, 160, -1, 140)
child_2 = daughter('Наташа', 'Королева', 0, 60, 160, -1, 140)
child_1.pairing(1)
child_1.sport_stat(1)
child_2.bride('Петрова', 1)
print('Занялся ли спортом сын - ', child_1.doing_sport, 'Нашел ли сын девушку - ', child_1.relations,
      'Как все это сказалось на айкью - ', child_1.iq)
print(child_2.pregnancy, child_2.surname)
child_2.divorce()  # имитируем развод и девичью фамилию
print(child_2.surname)
print(child_1.grow_pr(-1))
