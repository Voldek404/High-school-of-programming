class Object:
    def __init__(self, content):
        self.content = content


class Digit(Object):
    pass


class String(Object):
    pass


def print_object_result(object):
    return object.content * 2


object = Digit(2)  # Создаём объект дочернего класса
print(print_object_result(object))  # Выведет «4»

object = String('2')  # Создаём ещё один объект дочернего класса
print(print_object_result(object))  # Выведет «22»
