"""
Лабораторна робота № 5: Симулятор енергомережі «ЕнергоБаланс»
"""

from abc import ABC, abstractmethod


class PowerPlant(ABC):
    """Базовий абстрактний клас для електростанцій."""

    def __init__(self, plant_id: int, name: str, max_capacity: float):
        self.plant_id = plant_id
        self.name = name
        self.max_capacity = max_capacity
        self.current_output = 0.0

    @abstractmethod
    def get_info(self) -> str:
        """Повертає інформацію про тип станції."""
        pass

    def __str__(self) -> str:
        return f"{self.name} — Потужність: {self.current_output}/{self.max_capacity} МВт"


class ThermalPlant(PowerPlant):
    """Теплова електростанція (ТЕС)."""

    def __init__(self, plant_id: int, name: str, max_capacity: float, fuel_type: str):
        super().__init__(plant_id, name, max_capacity)
        self.fuel_type = fuel_type

    def get_info(self) -> str:
        return f"ТЕС на паливі: {self.fuel_type}"


class NuclearPlant(PowerPlant):
    """Атомна електростанція (АЕС)."""

    def __init__(self, plant_id: int, name: str, max_capacity: float, reactors: int):
        super().__init__(plant_id, name, max_capacity)
        self.reactors = reactors

    def get_info(self) -> str:
        return f"АЕС (кількість реакторів: {self.reactors})"


class RenewablePlant(PowerPlant):
    """Відновлювана електростанція (СЕС / ВЕС)."""

    def __init__(self, plant_id: int, name: str, max_capacity: float, source: str):
        super().__init__(plant_id, name, max_capacity)
        self.source = source  # 'сонце', 'вітер' тощо

    def get_info(self) -> str:
        return f"ВДЕ (джерело: {self.source})"


class GridManager:
    """Клас-менеджер для управління всіма станціями."""

    def __init__(self, name: str):
        self.name = name
        self.plants = []

    def add_plant(self, plant: PowerPlant):
        self.plants.append(plant)

    def remove_plant(self, plant_id: int):
        self.plants = [p for p in self.plants if p.plant_id != plant_id]

    def get_all(self):
        return self.plants

    def get_total_capacity(self):
        return sum(p.max_capacity for p in self.plants)

    def get_total_output(self):
        return sum(p.current_output for p in self.plants)

    def filter_by_type(self, plant_type):
        return [p for p in self.plants if isinstance(p, plant_type)]

    def sort_by_capacity(self):
        return sorted(self.plants, key=lambda p: p.max_capacity, reverse=True)

    def __str__(self) -> str:
        return f"Енергомережа '{self.name}' (Станцій: {len(self.plants)})"