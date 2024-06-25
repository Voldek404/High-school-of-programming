# Программа для расчета электротехническиъ величин с помощью подключаемых модулей
from calc import el_calc  # импорт модуля целиков
from calc.el_calc import q_power  # импорт конкретного метода из модуля
from calc.power_calc import power_calc as pc
import calc.power_calc

u = int(input('Введите значение фазного напряжения, В -- '))
i = int(input('Введите значение нагрузки, А  -- '))
cosfi = float(input('Введите значение косинуса фи, от 0 до 1 включительно - '))
a = False
while a == False:
    if cosfi >= 0 and cosfi <= 1:
        a = True
        continue
    else:
        print('Введенное значение косинуса фи недопустимо, повторите ввод')
        cosfi = float(input('Введите значение косинуса фи, от 0 до 1 включительно - '))
print('Величина активной мощности, Вт - ', el_calc.p_power(u, i, cosfi))
print('Величина полной мощности, Вар - ', pc.s_power(u, i))
print('Величина реактивной мощности, Вар - ', el_calc.q_power(u, i, cosfi))
print('Величина сопротивления, Ом - ', pc.res(u, i))
