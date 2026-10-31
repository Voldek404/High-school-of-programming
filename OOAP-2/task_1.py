# Родительский класс единицы электротехнического оборудования с наследуемым методом 
# сигнализации перегрузки
class Transformer:
    def check_overload(self, value, limit):
        if value > limit:
            print("Перегрузка!")


class VoltageTransformer(Transformer):
    def measure(self):
        return 230


class CurrentTransformer(Transformer):
    def measure(self):
        return 5


class PowerMeter:
    def __init__(self):
        # Композиция: счётчик создаёт и содержит объекты двух трансформаторов.
        self.voltage_transformer = VoltageTransformer()
        self.current_transformer = CurrentTransformer()

    def count_full_power(self):
        voltage = self.voltage_transformer.measure()
        current = self.current_transformer.measure()
        return voltage * current


meter = PowerMeter()

# Полиморфизм: одинаковый вызов measure() для разных типов трансформаторов.
for transformer in [meter.voltage_transformer, meter.current_transformer]:
    print("Измеряемая величина равна:", transformer.measure())

print(meter.count_full_power())  # 1150

meter.current_transformer.check_overload(
    meter.current_transformer.measure(), limit=4
)  # Перегрузка!
