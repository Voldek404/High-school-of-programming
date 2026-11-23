from typing import Generic, TypeVar


```python
class Transformer:
    """Общий тип трансформатора."""

    def __init__(self, name: str):
        self.name = name


class CurrentTransformer(Transformer):
    """Трансформатор тока."""

    def measure_current(self) -> float:
        return 5.0


class VoltageTransformer(Transformer):
    """Трансформатор напряжения."""

    def measure_voltage(self) -> float:
        return 100.0
```


# КОВАРИАНТНОСТЬ:
# producer создает и возвращает.
```python
T_co = TypeVar(
    "T_co",
    bound=Transformer,
    covariant=True,
)


class TransformerProvider(Generic[T_co]):
    def get(self) -> T_co:
        raise NotImplementedError


class CurrentTransformerProvider(
    TransformerProvider[CurrentTransformer]
):
    def get(self) -> CurrentTransformer:
        return CurrentTransformer("ТТ-100")


# Поставщик конкретных ТТ может использоваться
# как поставщик любых трансформаторов.
provider: TransformerProvider[Transformer]
provider = CurrentTransformerProvider()

transformer = provider.get()

print(transformer.name)
```


# КОНТРАВАРИАНТНОСТЬ:
# consumer принимает и обрабатывает значение.
```python
T_contra = TypeVar(
    "T_contra",
    bound=Transformer,
    contravariant=True,
)


class TransformerInspector(Generic[T_contra]):
    def inspect(self, transformer: T_contra) -> None:
        raise NotImplementedError


class GeneralTransformerInspector(
    TransformerInspector[Transformer]
):
    def inspect(self, transformer: Transformer) -> None:
        print(f"Проверен: {transformer.name}")


# Универсальный проверяющий может использоваться
# как проверяющий конкретных трансформаторов тока.
inspector: TransformerInspector[CurrentTransformer]
inspector = GeneralTransformerInspector()

current_transformer = CurrentTransformer("ТТ-200")

inspector.inspect(current_transformer)
```

# Ассоциативно продюссер - создает и возвращает объекты
# Консьюмер принимает и обрабатывает
Использование ковариантности и контравариантности позволяет сохранять открытость для расширения и подстановки компонентов + контроль типов, а также повторное использование.

Ковариантность нужна для компонентов, которые выдают специализированные объекты через общий интерфейс.

Контравариантность нужна для компонентов, которые умеют принимать более общий тип и поэтому могут обработать его специализации.
