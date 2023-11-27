import unittest
from tire.octoprime import Octoprime


class TestOctoprimeShouldBeServiced(unittest.TestCase):
    def test_is_sum_greater_than_three_one(self):
        tire_wear_sensors = [1, 1, 1, 1]
        tire = Octoprime(tire_wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_is_sum_greater_than_three_two(self):
        tire_wear_sensors = [0.9, 0.9, 0.9, 0.9]
        tire = Octoprime(tire_wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_is_sum_greater_than_three_three(self):
        tire_wear_sensors = [0.9, 0.9, 1, 1]
        tire = Octoprime(tire_wear_sensors)
        self.assertTrue(tire.needs_service())

    def test_is_sum_greater_than_three_four(self):
        tire_wear_sensors = [0.5, 0.8, 1, 0.9]
        tire = Octoprime(tire_wear_sensors)
        self.assertTrue(tire.needs_service())


class TestInvalidValue(unittest.TestCase):
    def test_more_than_one_value(self):
        tire_wear_sensors = [0.4, 1, 0.9, 9]
        with self.assertRaises(ValueError):
            Octoprime(tire_wear_sensors)

    def test_less_than_one_value(self):
        tire_wear_sensors = [0.4, 1, 0.9, -9]
        with self.assertRaises(ValueError):
            Octoprime(tire_wear_sensors)


class TestOctoprimeShouldNotBeServiced(unittest.TestCase):
    def test_is_sum_less_than_three_one(self):
        tire_wear_sensors = [0.5, 0.5, 0.5, 0.5]
        tire = Octoprime(tire_wear_sensors)
        self.assertFalse(tire.needs_service())

    def test_is_sum_less_than_three_two(self):
        tire_wear_sensors = [0.5, 0.5, 0.6, 0.6]
        tire = Octoprime(tire_wear_sensors)
        self.assertFalse(tire.needs_service())

    def test_is_sum_less_than_three_three(self):
        tire_wear_sensors = [0.1, 0.1, 1, 0.9]
        tire = Octoprime(tire_wear_sensors)
        self.assertFalse(tire.needs_service())

    def test_is_sum_less_than_three_four(self):
        tire_wear_sensors = [0.2, 0.3, 0.4, 0.5]
        tire = Octoprime(tire_wear_sensors)
        self.assertFalse(tire.needs_service())