class current_transformer():  # трансформаторы тока
    tip = ' ТЛМ - 10'
    nominal_current_A = 5  # номинальный ток
    precision_class = "0.5S"  # класс точности
    nominal_load_VA = 5  # номинальная нагрузка вторичной обмотки
    mpi_years = 8  # межповерочный интервал
    poveren = True  # наличие поверки
    slice_zone = [1,2]# территориальная принадлежность


# Наиболее напглядным примером для себя любимого выбран пример с отображением id
tt_1 = current_transformer()
print(id(tt_1))
tt_2 = tt_1
tt_3 = tt_2
print(id(tt_3))
# отображаются одинаковые id, что доказывает, что объект не копируется,
# а лишь получает ссылку на оригинальный
tt_1_nominal = current_transformer.nominal_current_A
print(id(tt_1_nominal))
tt_2_nominal = tt_1_nominal
print(id(tt_2_nominal))
# в каждом из этих случаев по ссылке передалось значение оригинального объекта
tt_2_nominal = tt_2_nominal + 5
print(tt_1_nominal, tt_2_nominal)
print(id(tt_1_nominal), id(tt_2_nominal))
#при изменении переприсвоенного объекта оригинальный объект не поменялся
tt_1_nominal = tt_1_nominal + 5
print(tt_1_nominal, tt_2_nominal)
#при изменении оригинального объекта поменялось и значение переменных-ссылок на данный оригинальный объект