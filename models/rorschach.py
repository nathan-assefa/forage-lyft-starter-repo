from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from datetime import date
from .car import Car
""" Implementing Rorschach car """


class Rorschach(Car):
    """
    Rorschach car class with three different attributes
        1. last_service_date
        2. current_mileage
        3. last_service_mileage 
    """
    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        super().__init__(engine, battery)