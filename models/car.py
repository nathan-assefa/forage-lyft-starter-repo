from serviceable import Serviceable
""" Common interface for car-related class """


class Car(Serviceable):
    """
    Car class with two properities
        1. engine: The car engine
        2. battery: The car battery
    """
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        """
        This method sends the car to the service if either the engine
        or the battery needs service
        """
        return self.engine.needs_service() or self.battery.needs_service()