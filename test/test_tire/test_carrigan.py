import unittest
from tire.carrigan import Carrigan


class TestCarriganShouldBeServiced(unittest.TestCase):
    def test_only_one_sensor(self):
        tire_wear_sensors = [0.5, 0.4, 0.6, 0.9]
        tire = Carrigan(tire_wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_only_two_sensors(self):
        tire_wear_sensors = [0.5, 0.4, 1, 0.9]
        tire = Carrigan(tire_wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_three_sensors(self):
        tire_wear_sensors = [0.5, 0.9, 1, 0.9]
        tire = Carrigan(tire_wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_all_four_sensors(self):
        tire_wear_sensors = [1, 1, 1, 0.9]
        tire = Carrigan(tire_wear_sensors)
        self.assertTrue(tire.needs_service())


class TestInvalidValue(unittest.TestCase):
    def test_more_than_one_value(self):
        tire_wear_sensors = [0.4, 1, 0.9, 9]
        with self.assertRaises(ValueError):
            Carrigan(tire_wear_sensors)

    def test_less_than_one_value(self):
        tire_wear_sensors = [0.4, 1, 0.9, -9]
        with self.assertRaises(ValueError):
            Carrigan(tire_wear_sensors)


class TestCarriganShouldNotBeServiced(unittest.TestCase):
    def test_all_four_sensors(self):
        tire_wear_sensors = [0.4, 0.5, 0.6, 0.7]
        tire = Carrigan(tire_wear_sensors)
        self.assertFalse(tire.needs_service())