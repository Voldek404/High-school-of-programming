# a program to show an example with coffee type

def americano_decorator(func):
    def wrapper():
        return 'water + ' + func()

    return wrapper


def flat_white_decorator(func):
    def wrapper():
        return func() + ' + milk'

    return wrapper


def cappuccino_decorator(func):
    def wrapper():
        return 'cream + ' + func() + ' + milk'

    return wrapper


def macciato_decorator(func):
    def wrapper():
        return 'milk foam  + ' + func()

    return wrapper


def surname_decorator(func):
    def wrapper():
        return func() + '**'


def espresso():
    assert 1 >= Coffe_type >= 5, "Type must be from 1 to 5"
    return 'espresso'


Coffe_type = int(
    input('Choose coffe type : 1 - espresso, 2 - americano, 3 - flatwhite, 4 - cappuchino, 5 - macciatto     '))
if Coffe_type == 1:
    print(espresso())
if Coffe_type == 2:
    @americano_decorator
    def espresso():
        return 'espresso'
if Coffe_type == 3:
    @flat_white_decorator
    def espresso():
        return 'espresso'
if Coffe_type == 4:
    @cappuccino_decorator
    def espresso():
        return 'espresso'
if Coffe_type == 5:
    @macciato_decorator
    def espresso():
        return 'espresso'

print(espresso())
