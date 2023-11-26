from battery.nubbin_battery import NubbinBattery
from datetime import datetime


import unittest

class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        current_date = today
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())