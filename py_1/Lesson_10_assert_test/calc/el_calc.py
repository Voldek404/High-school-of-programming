# модуль для расчета разных типов мощности

def p_power(u, i, cosfi):  # расчет активной мощности, Вт
    return u * i * cosfi


def q_power(u, i, cosfi):  # расчет реактивной мощности
    return ((u * i) ** 2 - (u * i * cosfi) ** 2) ** 0.5
