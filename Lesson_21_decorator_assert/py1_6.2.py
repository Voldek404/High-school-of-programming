# Для наглядности примера устранил структуру класса с родителем, сыном и дочкой
# Декораторы из 6.1 ну никак не подходили для данного примера, в связи с чем использовались стандартные декораторы


import logging
from functools import wraps


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Вызов метода {func.__name__} с аргументами {args} и kwargs {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__}: {result}")
        return result

    return wrapper


def check_access(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.driving:
            raise ValueError("У вас нет прав на выполнение этого действия.")
        return func(self, *args, **kwargs)

    return wrapper


class personel:
    def __init__(self, l, p, d, s):
        self.location = l  # Номер подстанции, где находится юнит
        self.protection = p  # Тип защитной одежды
        self.driving = d  # Право управления ТС
        self.salary = s  # Оклад


class ovb(personel):  # Определение класса-наследника "Электромонтер оперативно-выездной бригады"
    def __init__(self, n, ss, l, p, d, s):
        super().__init__(l, p, d, s)
        self.name = n
        self.switch = ss

    @log_calls
    @check_access
    def move(self, new_point):  # Перемещение юнита на новый объект
        self.location = new_point

    @log_calls
    @check_access
    def swtch(self, new_switch):  # Переключение выключателя
        if new_switch == 1:
            self.switch = 1
        else:
            self.switch = 0


ovb_object = ovb("Вася", 0, "Москва", "Костюм", False, 25000)
ovb_object.move("Санкт-Петербург")
ovb_object.swtch(1)
