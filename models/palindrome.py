from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from datetime import date
from .car import Car
""" Implementing Palindrome class """


class Palindrome(Car):
    """
    Palindrome car class with three different attributes
        1. last_service_date
        2. warning_light_on: This determines if the SpindlerBattery
        battery needs service.
    """
    def __init__(self, last_service_date: date, warning_light_on: bool):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        super().__init__(engine, battery)