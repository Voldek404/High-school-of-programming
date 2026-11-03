from abc import ABC, abstractmethod


class ElectricalEquipment(ABC):
    """Абстрактная единица электротехнического оборудования."""

    def __init__(self, name: str):
        if not name:
            raise ValueError("Наименование оборудования не может быть пустым")

        self._name = name
        self._is_enabled = False

    def enable(self) -> None:
        """Постусловие: оборудование введено в работу."""
        self._is_enabled = True

    def disable(self) -> None:
        """Постусловие: оборудование выведено из работы."""
        self._is_enabled = False

    def is_enabled(self) -> bool:
        return self._is_enabled

    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def get_equipment_type(self) -> str:
        """Возвращает тип электротехнического оборудования."""
        pass


class MeasuringTransformer(ElectricalEquipment, ABC):
    """
    Расширение ElectricalEquipment.

    Добавляет коэффициент трансформации и операцию
    преобразования первичной величины во вторичную.
    """

    def __init__(self, name: str, ratio: float):
        if ratio <= 0:
            raise ValueError(
                "Коэффициент трансформации должен быть положительным"
            )

        super().__init__(name)
        self._ratio = ratio

    def get_ratio(self) -> float:
        return self._ratio

    def get_equipment_type(self) -> str:
        return "измерительный трансформатор"

    @abstractmethod
    def get_secondary_value(self, primary_value: float) -> float:
        """
        Предусловие: оборудование введено в работу.

        Постусловие: возвращена соответствующая вторичная величина.
        """
        pass


class CurrentTransformer(MeasuringTransformer):
    """Специализация измерительного трансформатора для измерения тока."""

    def get_equipment_type(self) -> str:
        return "трансформатор тока"

    def get_secondary_value(self, primary_current: float) -> float:
        if not self.is_enabled():
            raise RuntimeError("Трансформатор тока выведен из работы")

        if primary_current < 0:
            raise ValueError("Ток не может быть отрицательным")

        return primary_current / self.get_ratio()


class VoltageTransformer(MeasuringTransformer):
    """Специализация измерительного трансформатора для измерения напряжения."""

    def get_equipment_type(self) -> str:
        return "трансформатор напряжения"

    def get_secondary_value(self, primary_voltage: float) -> float:
        if not self.is_enabled():
            raise RuntimeError("Трансформатор напряжения выведен из работы")

        if primary_voltage < 0:
            raise ValueError("Напряжение не может быть отрицательным")

        return primary_voltage / self.get_ratio()
