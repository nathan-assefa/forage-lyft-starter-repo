from .tire import Tire


class Carrigan(Tire):
    def needs_service(self):
        return any(num >= 0.9 for num in self.tire_wear_sensors)