class power_meter():  # счетчики электроэнергии
    equip = 'Меркурий234 '
    nominal_voltage_V = 100  # номинальное напряжение
    nominal_current_A = 5  # номинальный ток
    precision_class = "0.5S"  # класс точности
    protocol_type = 'SPODES'  # протокол обмена
    poveren = True  # наличие поверки


class current_transformer():  # трансформаторы тока
    tip = ' ТЛМ - 10'
    nominal_current_A = 5  # номинальный ток
    precision_class = "0.5S"  # класс точности
    nominal_load_tt_VA = 5  # номинальная нагрузка вторичной обмотки
    mpi_years = 8  # межповерочный интервал
    poveren = True  # наличие поверки


class voltage_transformer():  # трансформаторы напряжения
    tip = 'НТМИ - 6 '
    nominal_voltage_V = 100  # номинальное напряжение
    precision_class = "0.5"  # класс точности
    nominal_load_tn_VA = 5  # номинальная нагрузка вторичной обмотки
    mpi_years = 8  # межповерочный интервал
    poveren = False  # наличие поверки


tn = voltage_transformer()
print(tn.nominal_voltage_V)
tt = current_transformer()
print(tt.nominal_load_tt_VA)
meter = power_meter()
print(meter.protocol_type)
