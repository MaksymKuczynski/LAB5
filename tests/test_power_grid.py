import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(file), '../src')))

from power_grid import GridManager, ThermalPlant, NuclearPlant, RenewablePlant, PowerPlant


class TestPowerGrid(unittest.TestCase):

    def setUp(self):
        self.grid = GridManager("Тестова мережа")
        self.tpp = ThermalPlant(1, "Тест ТЕС", 500, "газ")
        self.npp = NuclearPlant(2, "Тест АЕС", 1000, 2)
        self.solar = RenewablePlant(3, "Тест СЕС", 100, "сонце")

    def test_abstract_class(self):
        """Перевірка, що не можна створити екземпляр абстрактного класу."""
        with self.assertRaises(TypeError):
            PowerPlant(10, "Абстрактна", 100)

    def test_add_and_count_plants(self):
        """Перевірка додавання станцій у менеджер."""
        self.grid.add_plant(self.tpp)
        self.grid.add_plant(self.npp)
        self.assertEqual(len(self.grid.get_all()), 2)

    def test_total_capacity(self):
        """Перевірка підрахунку сумарної потужності."""
        self.grid.add_plant(self.tpp)
        self.grid.add_plant(self.npp)
        self.assertEqual(self.grid.get_total_capacity(), 1500)

    def test_filter_by_type(self):
        """Перевірка фільтрації за типом."""
        self.grid.add_plant(self.tpp)
        self.grid.add_plant(self.solar)
        thermals = self.grid.filter_by_type(ThermalPlant)
        self.assertEqual(len(thermals), 1)
        self.assertEqual(thermals[0].name, "Тест ТЕС")


if __name__ == '__main__':
    unittest.main(verbosity=2)