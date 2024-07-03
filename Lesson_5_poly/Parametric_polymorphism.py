class Object:
    def __init__(self, content):
        self.content = content


class Digit(Object):
    def operation(self):
        return self.content / 2


class String(Object):
    def operation(self):
        return self.content * 2


def print_object_result(object):
    return object.operation()


object = Digit(2)  
print(print_object_result(object))  # Выведет «1»

object = String('2') 
print(print_object_result(object))  # Выведет «22»
