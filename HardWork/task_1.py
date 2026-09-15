# Задание Уменьшение цикломатической сложности

# Задача 1. 9/28 задач
# Исходный код. Количество инструкций 33, сложность 11. Complexity Level: Moderate
import math


def TheRabbitsFoot(s, encode):
    if encode:
        s = s.replace(' ', '')
        N = len(s)
        down_board, upper_board = math.floor(N ** 0.5), math.ceil(N ** 0.5)
        while down_board * upper_board < N:
            down_board += 1
        if len(s) < down_board * upper_board:
            s = s + ' ' * (down_board * upper_board - N)
        matrix = [[] for _ in range(down_board)]
        for i in range(down_board * upper_board):
            matrix[i // upper_board].append(s[i])
        s_new = ''
        for i in range(down_board):
            for j in range(upper_board):
                s_new += matrix[j][i]
            s_new += ' '
        s_new = s_new.replace('  ', ' ')
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
                    return ''.join(symbols)
                symbols.append(symbol)
            index += 1

# Код после рефакторинга в соответствие с СИ. Количество инструкций 33, сложность 7. Complexity Level: Low

import math


def encodeTrue(s):
    s = s.replace(' ', '')
    N = len(s)
    upper_board = math.ceil(N ** 0.5)
    down_board = math.ceil(N / upper_board)
    s = s + ' ' * (down_board * upper_board - N)
    matrix = [[] for _ in range(down_board)]
    for i in range(down_board * upper_board):
        matrix[i // upper_board].append(s[i])
    s_new = ''
    for i in range(down_board):
        for j in range(upper_board):
            s_new += matrix[j][i]
        s_new += ' '
    s_new = s_new.replace('  ', ' ')
    s_new = s_new.rstrip()
    return s_new


def encodeFalse(s):
    s_new = s.split()
    symbols = []
    for index in range(len(min(s_new, key=len))):
        for i in s_new:
            symbol = i[index]
            symbols.append(symbol)

    return ''.join(symbols)


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


# Задача 2 . 7/28 задач
# Исходный код. Количество инструкций 64, сложность 22. Complexity Level: Moderate

def WordSearch(length, input_string, subs):
    search_list = []
    splitted_string = input_string.split()
    while splitted_string != []:
        if len(splitted_string[0]) == length and len(splitted_string) == 1 :
            search_list.append(splitted_string[0])
            splitted_string.pop(0)
            break
        if len(splitted_string[0]) == length:
            search_list.append(splitted_string[0])
            splitted_string.pop(0)
        elif len(splitted_string) == 1 and len(splitted_string[0]) < length:
            search_list.append(splitted_string[0] + ' ' * (
                    length - len(splitted_string[0])))
            splitted_string.pop(0)
            break
        elif len(splitted_string) == 1 and len(splitted_string[0]) > length:
            search_list.append(splitted_string[0][:length ])
            splitted_string[0] = splitted_string[0][length:]
            search_list.append(splitted_string[0][:length - 1] + ' ' * (
                    length - len(splitted_string[0])))
            break
        elif len(splitted_string[0] + splitted_string[1]) < length:
            search_list.append(splitted_string[0] + ' ' + splitted_string[1] + ' ' * (
                    length - len(splitted_string[0] + splitted_string[1] + ' ')))
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif len(splitted_string[0]) < length and len(splitted_string[0] + splitted_string[1]) > length:
            search_list.append(splitted_string[0] + ' ' * (
                    length - len(splitted_string[0])))
            splitted_string.pop(0)
        elif len(splitted_string[0] + splitted_string[1]) == length:
            search_list.append(splitted_string[0])
            splitted_string.pop(0)
        elif len(splitted_string) > 2 and len(splitted_string[0] + ' ' + splitted_string[1] + ' ' + splitted_string[2]) == length:
            search_list.append(splitted_string[0] + ' ' + splitted_string[1] + ' ' + splitted_string[2])
            splitted_string.pop(0)
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif len(splitted_string) > 2 and len(splitted_string[0] + ' ' + splitted_string[1] + ' ' + splitted_string[2]) < length:
            search_list.append(splitted_string[0] + ' ' + splitted_string[1] + ' ' + splitted_string[2] + ' ' * (
                    length - len(splitted_string[0]) - len(splitted_string[1] - len(splitted_string[2]))))
            splitted_string.pop(0)
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif len(splitted_string[0]) > length:
            search_list.append(splitted_string[0][:length ])
            splitted_string[0] = splitted_string[0][length:]
        elif len(splitted_string[0] + splitted_string[1]) < length:
            search_list.append(splitted_string[0] + ' ' + splitted_string[1] + ' ' * (
                    length - len(splitted_string[0] + splitted_string[1] + ' ')))
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif len(splitted_string[0]) < length:
            search_list.append(splitted_string[0] + ' ' * (
                    length - len(splitted_string[0])))
            splitted_string.pop(0)
    result_array = []
    for rows in search_list:
        if subs in rows.split():
            result_array.append(1)
        else:
            result_array.append(0)
    return result_array