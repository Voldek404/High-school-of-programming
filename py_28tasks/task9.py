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
