# Visitor на примере трансформаторов

Для примера взял трансформатор тока, трансформатор напряжения и силовой трансформатор. Задача простая — вывести по одной строке на каждый аппарат.

## Как было

В базовом классе `Transformer` объявил метод `report_line()`. Каждый наследник его переопределяет. У трансформатора тока в строку идут номинальные токи, у трансформатора напряжения — напряжения, у силового — мощность. Переопределение `report_line()` и есть то, что в задании называется «неистинным» наследованием.

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Transformer(ABC):
    name: str

    @abstractmethod
    def report_line(self) -> str:
        """Сформировать строку отчёта об оборудовании."""


@dataclass
class CurrentTransformer(Transformer):
    primary_a: int
    secondary_a: int

    def report_line(self) -> str:
        return f"{self.name} — номинальные токи {self.primary_a}/{self.secondary_a} А"


@dataclass
class VoltageTransformer(Transformer):
    primary_v: int
    secondary_v: int

    def report_line(self) -> str:
        return f"{self.name} — напряжения {self.primary_v}/{self.secondary_v} В"


@dataclass
class PowerTransformer(Transformer):
    rated_kva: int

    def report_line(self) -> str:
        return f"{self.name} — мощность {self.rated_kva} кВА"


equipment = [
    CurrentTransformer("ТТ-1", 600, 5),
    VoltageTransformer("ТН-1", 6000, 100),
    PowerTransformer("Т-1", 10000),
]

for transformer in equipment:
    print(transformer.report_line())
```

## Что поменял

Вынес сборку строк в `TransformerReportVisitor`. У каждого типа трансформатора там свой метод. В самом `Transformer` добавил общий `accept()`, который передаёт объект посетителю. Наследники используют этот метод как есть.

В классическом Visitor у каждого типа свой `accept()`. Здесь я сделал один на всех. Какой метод вызвать, решает `singledispatchmethod` по типу объекта. Например, когда передаю ТТ-1, срабатывает `visit_current_transformer()`.

```python
from dataclasses import dataclass
from functools import singledispatchmethod
from typing import Protocol


class TransformerVisitor(Protocol):
    def visit(self, transformer: "Transformer") -> str:
        ...


@dataclass
class Transformer:
    name: str

    def accept(self, visitor: TransformerVisitor) -> str:
        return visitor.visit(self)


@dataclass
class CurrentTransformer(Transformer):
    primary_a: int
    secondary_a: int


@dataclass
class VoltageTransformer(Transformer):
    primary_v: int
    secondary_v: int


@dataclass
class PowerTransformer(Transformer):
    rated_kva: int


class TransformerReportVisitor:
    @singledispatchmethod
    def visit(self, transformer: Transformer) -> str:
        raise TypeError(f"Нет обработчика для {type(transformer).__name__}")

    @visit.register
    def visit_current_transformer(self, transformer: CurrentTransformer) -> str:
        return (
            f"{transformer.name} — номинальные токи "
            f"{transformer.primary_a}/{transformer.secondary_a} А"
        )

    @visit.register
    def visit_voltage_transformer(self, transformer: VoltageTransformer) -> str:
        return (
            f"{transformer.name} — напряжения "
            f"{transformer.primary_v}/{transformer.secondary_v} В"
        )

    @visit.register
    def visit_power_transformer(self, transformer: PowerTransformer) -> str:
        return f"{transformer.name} — мощность {transformer.rated_kva} кВА"


equipment = [
    CurrentTransformer("ТТ-1", 600, 5),
    VoltageTransformer("ТН-1", 6000, 100),
    PowerTransformer("Т-1", 10000),
]
visitor = TransformerReportVisitor()

for transformer in equipment:
    print(transformer.accept(visitor))
```

## Что получилось

Запустил оба варианта на одном наборе трансформаторов. Вывод совпал.

```text
ТТ-1 — номинальные токи 600/5 А
ТН-1 — напряжения 6000/100 В
Т-1 — мощность 10000 кВА
```

## Стало ли лучше

Если отчёт один, я бы оставил первый вариант. Вызов `report_line()` короче, и по классу сразу видно, какая строка получится.

С Visitor удобнее добавлять новые операции. Если понадобится, например, выгрузка в CSV, я добавлю ещё одного посетителя и передам его в тот же `accept()`. Классы трансформаторов для этого трогать не придётся. Зато если появится новый тип трансформатора со своими полями, для него придётся дописать обработчик в каждом посетителе, где этот тип нужен.
