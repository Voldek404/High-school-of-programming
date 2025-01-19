# Task 11. Время жизни переменных


1) Класс переименован в соответствии с рекомендациями, выполнено корректное наследованние (введен конструктор), публичные атрибуты, которые не должны меняться никогда - заменены на приватные
```python
class CurrentTransformer:
    tip = ' ТЛМ - 10'
    nominal_current_A = 5
    precision_class = "0.5S"
    nominal_load_tt_VA = 5
    mpi_years = 8
    poveren = True
///
class CurrentTransformer:
    def __init__(self, tip='ТЛМ - 10', nominal_current_A=5, precision_class="0.5S", 
                 nominal_load_tt_VA=5, mpi_years=8, poveren=True):
        self.__tip = tip  # Приватный атрибут
        self.__nominal_current_A = nominal_current_A  
        self.__precision_class = precision_class  
        self.__nominal_load_tt_VA = nominal_load_tt_VA 
        self.__mpi_years = mpi_years  
        self.__poveren = poveren  

```


2) Класс назван был неверно, приведено к соответствию. Все атрибуты сделаны приватными, для примера введен геттер для приватного атрибута link
```python
class power_meter:  # счетчики электроэнергии
    def __init__(self, meter_mark, total_cons, protocol_type, link_status, accounting_status):
        self.meter_type = meter_mark  # Марка прибора учёта
        self.total = total_cons  # Суммарные показания, кВт*ч
        self.protocol = protocol_type  # Протокол обмена для интерфейса 485
        self.link = link_status  # Наличие связи
        self.accounting = accounting_status 
///
class PowerMeter:  # Счетчики электроэнергии
    def __init__(self, meter_mark, total_cons, protocol_type, link_status, accounting_status):
        self.meter_type = meter_mark  # Марка прибора учета
        self.total = total_cons  # Суммарные показания, кВт*ч
        self.protocol = protocol_type  # Протокол обмена для интерфейса 485
        self.__link = link_status  # Приватный атрибут
        self.accounting = accounting_status  # Допущен в качестве расчетного

    def link_rebuild(self, new_link_status):
        self.__link = new_link_status  

    def get_link(self):
        return self.__link

```


3) Выполнена группировка добавленных сеттеров. 
```python
class personel:
    def __init__(self, l, p, d, s):
        self.location = l  # Номер подстанции, где находится юнит
        self.protection = p  # Тип защитной одежды
        self.driving = d  # Право управления ТС
        self.salary = s  # Оклад
///
class personel:
    def __init__(self, location, protection_type, driving_status, salary_grade):
        self.__location = self.set_location(location)
        self.__protection = self.set_protection(rotection_type)
        self.__driving = self.set_driving(driving_status)
        self.__salary = self.set_salary(salary_grade)
        
    def set_location(self, location):
        # проверка на инвариант
        return location
    
    def set_protection(self, protection):
        # проверка на инвариант
        return protection
    
    def set_driving(self, driving):
        # проверка на инвариант
        return driving
    
    def set_salary(self, salary):
        # проверка на инвариант
        return salary


```


4) Взаимодействие с классом через вновь созданный интерфейс, добавлен конструктор
```python
class voltage_transformer():  # трансформаторы напряжения
    tip = 'НТМИ - 6 '
    nominal_voltage_V = 100  # номинальное напряжение
    precision_class = "0.5"  # класс точности
    nominal_load_tn_VA = 5  # номинальная нагрузка вторичной обмотки
    mpi_years = 8  # межповерочный интервал
    poveren = False  # наличие поверки
tn = voltage_transformer()
print(tn.nominal_voltage_V)
///
class VoltageTransformer:
    def __init__(self, tip='НТМИ - 6', nominal_voltage_V=100, precision_class="0.5", nominal_load_tn_VA=5, mpi_years=8, poveren=False):
        self._tip = tip
        self._nominal_voltage_V = nominal_voltage_V
        self._precision_class = precision_class
        self._nominal_load_tn_VA = nominal_load_tn_VA
        self._mpi_years = mpi_years
        self._poveren = poveren

    def get_nominal_voltage(self):
        return self._nominal_voltage_V

    def print_info(self):
        print(f"Тип: {self._tip}, Напряжение: {self.get_nominal_voltage()}")
    def get_nominal_voltage(self):
        return self._nominal_voltage_V

    def print_info(self):
        print(f"Тип: {self._tip}, Напряжение: {self.get_nominal_voltage()}")

tn = VoltageTransformer()
tn.print_info()

```

5) Реализована инкапсуляцию, введены корректные наименования класса в соответствии с конвенциональными договоренностями, добавлены сеттеры и сеттеры
```python
class uspd:  # устройства сбора и передачи данных
    def __init__(self, uspd_mark, gsm, direct, watchdog, work):
        self.mark = uspd_mark
        self.gsm = gsm  # наличие GSM - канала
        self.direct = direct  # наличие прямого опроса через ВОЛС
        self.watchdog = watchdog  # положение watchdog в момент обращения к УСПД
        self.work = work  # исправность

///
class USPD:  # устройства сбора и передачи данных
    def __init__(self, uspd_mark, gsm=False, direct=False, watchdog=False, work=False):
        self._mark = uspd_mark
        self._gsm = gsm
        self._direct = direct
        self._watchdog = watchdog
        self._work = work

    @property
    def mark(self):
        return self._mark

    @property
    def gsm(self):
        return self._gsm

    @gsm.setter
    def gsm(self, value):
        self._gsm = value

    @property
    def direct(self):
        return self._direct

    @direct.setter
    def direct(self, value):
        self._direct = value

    @property
    def watchdog(self):
        return self._watchdog

    @watchdog.setter
    def watchdog(self, value):
        self._watchdog = value

    @property
    def work(self):
        return self._work

    @work.setter
    def work(self, value):
        self._work = value

    def work_on(self, new_work_status):
        self.work = new_work_status

    def direct_on(self, new_direct_status):
        self.direct = new_direct_status

    def watchdog_on(self, new_watchdog_status):
        self.watchdog = new_watchdog_status



```


6)  Запилен отдельный метод, меняющий необходимые атрибутыю Улучшена читаемость, соблюдена компактность кода
```python
uspd_1.work_on(True)  # Восстанавливаем работоспособность
uspd_1.direct_on(True)  # Налаживаем прямой канал опроса через ВОЛС
uspd_1.watchdog_on(True) 
///
 def configure_device(self, gsm=False, direct=False, watchdog=False, work=False):
        self.gsm = gsm
        self.direct = direct
        self.watchdog = watchdog
        self.work = work
uspd_1.configure_device(gsm=True, direct=True, watchdog=True, work=True)

```


7)  Атрибуты были открыты для прямого изменения, сделаны приватными. Доступ ныне к ним осуществляется через методы
```python
self.weight = w
self.height = h
self.age = a
self.iq = iq
///
class Parent:
    def __init__(self, weight, height, age, iq):
        self._weight = weight
        self._height = height
        self._age = age
        self._iq = iq

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

```


8) Добавлена проверка на инвариант
```python
def grow_pr(self, age):
    self.age += age
    if age >= 1:
        self.iq += 5 * age
///
def grow_pr(self, age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    self.age += age
    if age >= 1:
        self.iq += 5 * age

```


9) Обработка инвариантных значений ( смена фамилии на существующую)
```python
def bride(self, new_surn, new_preg):  # Имитируем выход замуж
    if self.surname != new_surn:
        self.surname = new_surn
    self.pregnancy += new_preg
///
def bride(self, new_surn, new_preg):  # Имитируем выход замуж с новой фамилией и беременностью
    if self.surname == new_surn:
        print("Фамилия не изменена, она уже " + self.surname)
        return
    self.old_surname = self.surname
    self.surname = new_surn
    self.pregnancy += new_preg

```


10) Улучшение структуры вывода данных
```python
print('Занялся ли спортом сын - ',child_1.doing_sport, 'Нашел ли сын девушку - ',child_1.relations, 'Как все это сказалось на айкью - ',child_1.iq)
print(child_2.pregnancy, child_2.surname)
child_2.divorce() # имитируем развод и девичью фамилию
print(child_2.surname)
///
print(f"Сын {child_1.name}: Спорт: {child_1.doing_sport}, Отношения: {child_1.relations}, IQ: {child_1.iq}")
print(f"Дочь {child_2.name}: Беременность: {child_2.pregnancy}, Фамилия: {child_2.surname}")
child_2.divorce()  # имитируем развод
print(f"После развода фамилия дочери {child_2.name}: {child_2.surname}")


```


11) Доступность напрямую изменена. Организован доступ через методы
```python
class Personel():
    def __init__(self, Ovb, Slesar):
        self.Ovb = Ovb
        self.Slesar = Slesar
///
class Personel:
    def __init__(self, ovb, slesar):
        self._ovb = ovb
        self._slesar = slesar

    @property
    def ovb(self):
        return self._ovb

    @property
    def slesar(self):
        return self._slesar


```



12) Улучшение композиции метода "about" + проверка наличия атрибутов через геттеры
```python
def about(self):
    print('Первый класс композиции ', self.Ovb.char, 'Второй класс композиции - ', self.Slesar.char_s,
          'Расположение юнитов соответственно - ', 'Substation #', self.Ovb.location, 'Substation #',
          self.Slesar.location)
///
def about(self):
    ovb_char = self.ovb.char
    ovb_location = self.ovb.location
    slesar_char = self.slesar.char_s
    slesar_location = self.slesar.location
    return (f"Первый класс композиции: {ovb_char}, второй класс композиции: {slesar_char}, "
            f"Расположение юнитов соответственно: Substation #{ovb_location}, Substation #{slesar_location}")


```


13) Класс пересоздается с проверкой значений
```python
class Ovb:
    def __init__(self, char, location):
        self.char = char
        self.location = location
///
class Ovb:
    def __init__(self, char, location):
        if not isinstance(location, int) or location <= 0:
            raise ValueError("Location must be a positive integer")
        self.char = char
        self.location = location


```


14) Улучшение структуры вывода информации метода about
```python
print(personel.about())
///
personel_info = personel.about()
print(personel_info)


```


15) Неверное создание экземпляра класса В аргумент должно передаваться цифровое значение локации
```python
ovb = Ovb(Personel)
slesar = Slesar(Personel)
///

ovb = Ovb(357)  
slesar = Slesar(190)

```