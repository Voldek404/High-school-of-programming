# Задание Уменьшение цикломатической сложности

# Задача 1. 9/28 задач
# Исходный код. Количество инструкций 33, сложность 11. Complexity Level: Moderate
import math


def TheRabbitsFoot(s, encode):
    if encode:
        s = s.replace(" ", "")
        N = len(s)
        down_board, upper_board = math.floor(N**0.5), math.ceil(N**0.5)
        while down_board * upper_board < N:
            down_board += 1
        if len(s) < down_board * upper_board:
            s = s + " " * (down_board * upper_board - N)
        matrix = [[] for _ in range(down_board)]
        for i in range(down_board * upper_board):
            matrix[i // upper_board].append(s[i])
        s_new = ""
        for i in range(down_board):
            for j in range(upper_board):
                s_new += matrix[j][i]
            s_new += " "
        s_new = s_new.replace("  ", " ")
        s_new = s_new.rstrip()
        return s_new
    else:
        s_new = s.split()
        symbols = []
        index = 0
        while True:
            for i in s_new:
                try:
                    symbol = i[index]
                except IndexError:
                    return "".join(symbols)
                symbols.append(symbol)
            index += 1


# Код после рефакторинга в соответствие с СИ. Количество инструкций 33, сложность 7. Complexity Level: Low

import math


def encodeTrue(s):
    s = s.replace(" ", "")
    N = len(s)
    upper_board = math.ceil(N**0.5)
    down_board = math.ceil(N / upper_board)
    s = s + " " * (down_board * upper_board - N)
    matrix = [[] for _ in range(down_board)]
    for i in range(down_board * upper_board):
        matrix[i // upper_board].append(s[i])
    s_new = ""
    for i in range(down_board):
        for j in range(upper_board):
            s_new += matrix[j][i]
        s_new += " "
    s_new = s_new.replace("  ", " ")
    s_new = s_new.rstrip()
    return s_new


def encodeFalse(s):
    s_new = s.split()
    symbols = []
    for index in range(len(min(s_new, key=len))):
        for i in s_new:
            symbol = i[index]
            symbols.append(symbol)

    return "".join(symbols)


def TheRabbitsFoot(s, encode):
    operations = {
        True: encodeTrue,
        False: encodeFalse,
    }
    operation = operations[encode]

    return operation(s)


# Выполненные по 1 заданию мероприятия:
# - разделение одной функции на три с реализацией табличной логики в главной функции RabbitFoot
# - устранение избыточной конструкции else, поскольку ветка if encode завершается return; выбор между кодированием и декодированием затем реализован с помощью таблицы соответствий.
# - устранения цикла while путем приведения вычисления down_board, upper_board в одно действие с выполнением условия непревышения N
# - устранение дополнительной проверки if на необходимость добить паддингами клетки, то есть у нас действие по добавке паддингов всегда выполняется корректно
# - остальные вложенности устранить не получилось в связи со спецификой алгоритма
# - ИТОГО - устранение ветвлений и табличная логика


# Задача 2 . 7/28 задач
# Исходный код. Количество инструкций 64, сложность 22. Complexity Level: Moderate


def WordSearch(length, input_string, subs):
    search_list = []
    splitted_string = input_string.split()
    while splitted_string != []:
        if len(splitted_string[0]) == length and len(splitted_string) == 1:
            search_list.append(splitted_string[0])
            splitted_string.pop(0)
            break
        if len(splitted_string[0]) == length:
            search_list.append(splitted_string[0])
            splitted_string.pop(0)
        elif len(splitted_string) == 1 and len(splitted_string[0]) < length:
            search_list.append(
                splitted_string[0] + " " * (length - len(splitted_string[0]))
            )
            splitted_string.pop(0)
            break
        elif len(splitted_string) == 1 and len(splitted_string[0]) > length:
            search_list.append(splitted_string[0][:length])
            splitted_string[0] = splitted_string[0][length:]
            search_list.append(
                splitted_string[0][: length - 1]
                + " " * (length - len(splitted_string[0]))
            )
            break
        elif len(splitted_string[0] + splitted_string[1]) < length:
            search_list.append(
                splitted_string[0]
                + " "
                + splitted_string[1]
                + " " * (length - len(splitted_string[0] + splitted_string[1] + " "))
            )
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif (
            len(splitted_string[0]) < length
            and len(splitted_string[0] + splitted_string[1]) > length
        ):
            search_list.append(
                splitted_string[0] + " " * (length - len(splitted_string[0]))
            )
            splitted_string.pop(0)
        elif len(splitted_string[0] + splitted_string[1]) == length:
            search_list.append(splitted_string[0])
            splitted_string.pop(0)
        elif (
            len(splitted_string) > 2
            and len(
                splitted_string[0] + " " + splitted_string[1] + " " + splitted_string[2]
            )
            == length
        ):
            search_list.append(
                splitted_string[0] + " " + splitted_string[1] + " " + splitted_string[2]
            )
            splitted_string.pop(0)
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif (
            len(splitted_string) > 2
            and len(
                splitted_string[0] + " " + splitted_string[1] + " " + splitted_string[2]
            )
            < length
        ):
            search_list.append(
                splitted_string[0]
                + " "
                + splitted_string[1]
                + " "
                + splitted_string[2]
                + " "
                * (
                    length
                    - len(splitted_string[0])
                    - len(splitted_string[1] - len(splitted_string[2]))
                )
            )
            splitted_string.pop(0)
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif len(splitted_string[0]) > length:
            search_list.append(splitted_string[0][:length])
            splitted_string[0] = splitted_string[0][length:]
        elif len(splitted_string[0] + splitted_string[1]) < length:
            search_list.append(
                splitted_string[0]
                + " "
                + splitted_string[1]
                + " " * (length - len(splitted_string[0] + splitted_string[1] + " "))
            )
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif len(splitted_string[0]) < length:
            search_list.append(
                splitted_string[0] + " " * (length - len(splitted_string[0]))
            )
            splitted_string.pop(0)
    result_array = []
    for rows in search_list:
        if subs in rows.split():
            result_array.append(1)
        else:
            result_array.append(0)
    return result_array


# Код после рефакторинга в соответствие с СИ. Количество инструкций 29, сложность 9. Complexity Level: Low

def WordSearch(length, input_string, subs):
    search_list = []
    splitted_string = input_string.split()
    temp_string = ""

    for i in range(len(splitted_string)):

        if len(splitted_string[i]) > length:
            if temp_string:
                temp_string += " " * (length - len(temp_string))
                search_list.append(temp_string)
                temp_string = ""

            while len(splitted_string[i]) > length:
                search_list.append(splitted_string[i][:length])
                splitted_string[i] = splitted_string[i][length:]

            temp_string = splitted_string[i]

        elif len(temp_string + " " + splitted_string[i]) <= length:
            if temp_string:
                temp_string += " "
            temp_string += splitted_string[i]

        else:
            temp_string += " " * (length - len(temp_string))
            search_list.append(temp_string)
            temp_string = splitted_string[i]

    if temp_string:
        temp_string += " " * (length - len(temp_string))
        search_list.append(temp_string)

    result_array = []

    for rows in search_list:
        result_array.append(int(subs in rows.split()))

    return result_array




# Выполненные по 2 заданию мероприятия:
# - изменение алгоритма формирования строк;
# - устранение избыточных операций типа pop();
# - удаление дублированных условий и сокращение количества ветвлений;
# - объединение нескольких проверок длины строк в общую логику обработки текущего слова;
# - устранение специальных случаев для обработки первого, второго и третьего элементов списка;
# - упрощение проверки наличия искомой подстроки за счёт преобразования результата логического выражения в целое число. - отличная практика, впервые до такой фичи додумался
# - ИТОГО - устранение ветвлений и табличная логика + изменение алгоритма



# Задача 3 . 7/28 задач
# Исходный код. Количество инструкций 63, сложность 21. Complexity Level: High

def write_birds_count(number):
    units = {1: 'одна', 2: 'две', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    units_exclusion = {1: 'один', 2: 'два'}
    teens = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
             16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    tens = {20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
            80: 'восемьдесят', 90: 'девяносто'}
    hundreds = {100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста', 500: 'пятьсот', 600: 'шестьсот',
                700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот'}
    bird_forms = ['сорока', 'сороки', 'сорок']

    thousands_forms = ['тысяча', 'тысячи', 'тысяч']
    millions_forms = ['миллион', 'миллиона', 'миллионов']
    billions_forms = ['миллиард', 'миллиарда', 'миллиардов']

    if number < 0 or number > 10 ** 9 or isinstance(number, float):
        return "Invariant Value"

    def get_form(n, forms):
        if 11 <= n % 100 <= 19:
            return forms[2]
        last_digit = n % 10
        if last_digit == 1:
            return forms[0]
        elif 2 <= last_digit <= 4:
            return forms[1]
        else:
            return forms[2]

    def number_to_words(n, is_thousand=False, is_million=False):
        if n == 0:
            return ''
        elif n < 10:
            if is_thousand and n in units:
                return units[n]
            elif is_million and n in units_exclusion:
                return units_exclusion[n]
            return units[n]
        elif n < 20:
            return teens[n]
        elif n < 100:
            return tens[n // 10 * 10] + (f' {units[n % 10]}' if n % 10 != 0 else '')
        elif n < 1000:
            if n in hundreds:
                return hundreds[n]
            return hundreds[n // 100 * 100] + (
                f' {number_to_words(n % 100, is_thousand, is_million)}' if n % 100 != 0 else '')

    result = []

    chunks = [
        (10 ** 9, billions_forms),
        (10 ** 6, millions_forms, True),
        (10 ** 3, thousands_forms)
    ]

    for divisor, forms, *rest in chunks:
        chunk = number // divisor
        if chunk > 0:
            is_thousand = (divisor == 10 ** 3)
            is_million = (divisor == 10 ** 6)
            result.append(f'{number_to_words(chunk, is_thousand, is_million)} {get_form(chunk, forms)}')
        number %= divisor

    if number > 0:
        result.append(number_to_words(number))

    if len(result) == 0:
        result.append('Ноль')

    bird_form = get_form(number, bird_forms)
    result.append(bird_form)

    return ' '.join(result).capitalize() + '.'


# Код после рефакторинга в соответствие с СИ. Количество инструкций 94, сложность 13. Complexity Level: Moderate
#- выделение различающегося поведения для разных разрядов чисел в отдельные классы с использованием полиморфизма;
#- устранение флагов is_thousand и is_million и связанных с ними условных ветвлений;
#- замена цепочки условий выбора формы числительного табличной логикой;
#- перенос специфической логики формирования "один/два" для миллионов и миллиардов в соответствующие классы;
#- устранение избыточных elif после операторов return;
#- упрощение формирования числительных для десятков и сотен за счёт объединения общей логики;
#- использование общего интерфейса get_units() для различных разрядов вместо явной проверки их типа;
#- ИТОГО — устранение ветвлений, табличная логика и полиморфизм + упрощение алгоритма формирования числительных.


# Итоговый отчет
# Для себя отметил, как легко избавиться от лишний else, насколько важно обращать внимание на наличие раннего return.
# Для абсолютного большинства ветвлений есть вполне себе рабочие способы их убрать, а не просто записать тернарным оператором в одну строку
# Полиморфизм имеет смысл использовать для управления состояниями - то есть куда реже, чем остальные приемы, рассмотренные в СИ
# Ну а самая рабочая тема - пересмотр, собственно, алгоритма
