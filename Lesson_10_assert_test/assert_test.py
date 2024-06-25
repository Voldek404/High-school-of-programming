# Программа для расчета электротехническиъ величин с помощью подключаемых модулей
from calc import el_calc  # импорт модуля целиков
from calc.el_calc import q_power  # импорт конкретного метода из модуля
from calc.power_calc import power_calc as pc
import calc.power_calc
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")
u = int(input('Введите значение фазного напряжения, В -- '))
assert u >= 0  # устанавливаем параметр, сигнализирующий о невозможности принятия отрицательного значения напряжения
i = int(input('Введите значение нагрузки, А  -- '))
cosfi = float(input('Введите значение косинуса фи, от 0 до 1 включительно - '))
assert cosfi >= 0 and cosfi <= 1  # устанавливаем параметр, ограничивающий значение вводимого косинуса фи
print('Величина активной мощности, Вт - ', el_calc.p_power(u, i, cosfi))
print('Величина полной мощности, Вар - ', pc.s_power(u, i))
print('Величина реактивной мощности, Вар - ', el_calc.q_power(u, i, cosfi))
try:  # для теста логгирования с exception устанавливаем исключение для деление на 0
    u / i
    logging.info(f"u/i successful with result: {u / i}.")
except ZeroDivisionError as err:
    logging.exception("ZeroDivisionError")
print('Величина сопротивления, Ом - ', pc.res(u, i))
