# Рефлексия к ООП ч.2.
# Достигнуто понимание формирования классов и и методов, информация в голове структурирована.
# Пришло осознание того, насколько ООП мощный инструмент, прёт куда сильнее любой философии
class uspd:  # устройства сбора и передачи данных
    def __init__(self, uspd_mark, gsm, direct, watchdog, work):
        self.__mark = uspd_mark
        self.__gsm = gsm  # наличие GSM - канала
        self.__direct = direct  # наличие прямого опроса через ВОЛС
        self.__watchdog = watchdog  # положение watchdog в момент обращения к УСПД
        self.__work = work  # исправность

    def work_on(self, new_work_status):
        self.__work = new_work_status

    def direct_on(self, new_direct_status):
        self.__direct = new_direct_status

    def watchdog_on(self, new_watchdog_status):
        self.__watchdog = new_watchdog_status


class power_meter:  # счетчики электроэнергии
    def __init__(self, meter_mark, total_cons, protocol_type, link_status, accounting_status):
        self.__meter_type = meter_mark  # Марка прибора учёта
        self.__total = total_cons  # Суммарные показания, кВт*ч
        self.__protocol = protocol_type  # Протокол обмена для интерфейса 485
        self.__link = link_status  # Наличие связи
        self.__accounting = accounting_status  # Допущен в качестве расчетного

    def link_rebuild(self, new_link_status):  # Для допуска прибора учёта требуется восстановить связь
        self.__link = new_link_status

    def change_protocol(self, new_protocol):  # метод изменения протокола обмена по требованию субъекта рынка ЭЭ для дальнейшего допуска
        self.__protocol = new_protocol

    def make_account(self, new_accounting_status):  # После изменения протокола допустимо использовать прибор в качестве расчетного
        self.__accounting = new_accounting_status


meter_1 = power_meter('Меркурий234', 43543, 61850, False, False)
uspd_1 = uspd('SICON70', True, False, False, False)
uspd_1.work_on(True)  # Восстанавливаем работоспособность
uspd_1.direct_on(True)  # Налаживаем прямой канал опроса через ВОЛС
uspd_1.watchdog_on(True)  # Настраиваем перезагрузку резервного канала при бездействии передающего устройства
uspd_1  # вывод
meter_1.link_rebuild(True)  # Восстанавливаем связь со счетчиком
meter_1.change_protocol('SPODES')  # Меняем протокол на СПОДЭС универсальный
meter_1.make_account(True)  # Составляем акт о допуске прибора учета
meter_1  # вывод

print(meter_1.work) # в связи с тем. что все запривачено - 'power_meter' object has no attribute 'work'