from battery.spindler_battery import SpindlerBattery
from datetime import datetime


import unittest

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_should_be_serviced(self):
        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 2)

        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())