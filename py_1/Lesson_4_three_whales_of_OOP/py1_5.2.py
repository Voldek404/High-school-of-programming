# Первая иерарихия основана на существующей у меня на работе
class personel:
    def __init__(self, l, p, d, s):
        self.location = l  # Номер подстанции, где находится юнит
        self.protection = p  # Тип защитной одежды
        self.driving = d  # Право управления ТС
        self.salary = s  # Оклад


class ovb(personel):  # Определение класса-наследника "Электромонтер оперативно-выездной бригады"
    def __init__(self, n, ss, l, p, d, s):
        super().__init__(l, p, d, s)
        self.name = n
        self.switch = ss

    def move(self, new_point):  # Перемещение юнита на новый объект
        self.location = new_point

    def swtch(self, new_switch):  # Переключение выключателя
        if new_switch == 1:
            self.switch = 1
        else:
            self.switch = 0


class slesar(personel):  # Определение класса-наследника "Слесарь"
    def __init__(self, n, oq, l, p, d, s):
        super().__init__(l, p, d, s)
        self.name = n
        self.oil = oq  # статус операции по отбору масла 1 - выполнена, 0 - не выполнена

    def otbor(self, oil_take):
        if oil_take == 1:
            self.oil = oil_take

    def up(self, upper_prof):
        self.name = upper_prof

    def upgrade(self, drive_on):  # Присвоение права управления ТС для возможности самостоятельно отвезти пробу масла
        self.driving = drive_on

    def income_plus(self, up_salary):  # Установление надбавки за управление ТС
        if self.driving == True:
            self.salary += up_salary
        else:
            print('Надбавка уже установлена')


ovb_unit = ovb('Monter OVB', 0, 357, 'Термостойкая', 1, 25000)
ovb_unit.move(190)  # В соответствии с заданием диспетчера переместиться на ПС - 190
ovb_unit.swtch(1)  # Включить выключатель присоединения
print('Расположение юнита - ПС - ', ovb_unit.location, 'Положение выключателя - ', ovb_unit.switch)
slesar_unit = slesar('Slesar', 0, 357, 'Термостойкая', 0, 20000)
slesar_unit.otbor(1)  # Произвести отбор масла
slesar_unit.upgrade(True)  # Присвоить надбавку за управление ТС
slesar_unit.income_plus(5000)  # Установить доплату
slesar_unit.up('Monter OVB')
print('Статус отбора пробы масла', slesar_unit.oil, 'Статус наличия надбавки за совмещение ', slesar_unit.driving,
      'Текущая зарплата', slesar_unit.salary, 'Должность после повышения - ', slesar_unit.name)


class parent:  # буквально класс - "Родитель"
    def __init__(self, w, h, a, iq):
        self.weight = w
        self.height = h
        self.age = a
        self.iq = iq

    def grow_pr(self, age):
        self.age += age
        if age >= 1:
            self.iq += 5 * age


class son(parent):  # Наследственный класс "Сын"
    def __init__(self, n, ds, rel, w, h, a, iq):
        super().__init__(w, h, a, iq)
        self.name = n
        self.doing_sport = ds
        self.relations = rel

    def pairing(self, new_stat):  # Находится ли в отношениях
        self.relations = new_stat

    def sport_stat(self, sport_stat_ch): # Занимается ли спортом
        self.doing_sport = sport_stat_ch
        self.iq += 20 #Эффект от занятия спортом на айкью


class daughter(parent): # Наследственный класс "Дочь"
    def __init__(self, n, f, pr, w, h, a, iq):
        super().__init__(w, h, a, iq)
        self.name = n
        self.surname = f
        self.old_surname = f # Резервируем старую фамилию на случай развода
        self.pregnancy = pr

    def bride(self, new_surn, new_preg): #Имитируем выход замуж с новой фамилией и беременностью
        if self.surname != new_surn:
            self.surname = new_surn
        self.pregnancy += new_preg

    def divorce(self): #Имитируем развод с возвратом старой фамилии
        self.surname = self.old_surname


child_1 = son('Артем', 0, 0, 60, 160, 18, 140)
child_2 = daughter('Наташа', 'Королева', 0, 60, 160, 18, 140)
child_1.pairing(1)
child_1.sport_stat(1)
child_2.bride('Петрова', 1)
print('Занялся ли спортом сын - ',child_1.doing_sport, 'Нашел ли сын девушку - ',child_1.relations, 'Как все это сказалось на айкью - ',child_1.iq)
print(child_2.pregnancy, child_2.surname)
child_2.divorce() # имитируем развод и девичью фамилию
print(child_2.surname)
