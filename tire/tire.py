from abc import ABC, abstractmethod
from typing import List, Union


class Tire(ABC):
    def __init__(self, tire_wear_sensors: List[Union[float, int]]):
        # Validate that each element is a float between 0 and 1 inclusive
        if not all(0 <= num <= 1 for num in tire_wear_sensors):
            raise ValueError("All tire wear sensor values must be floats between 0 and 1.")
        
        self.tire_wear_sensors: List[float, int] = tire_wear_sensors

    @abstractmethod
    def needs_service(self):
        pass