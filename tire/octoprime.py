from .tire import Tire


class Octoprime(Tire):
    def needs_service(self):
        return sum(self.tire_wear_sensors) >= 3