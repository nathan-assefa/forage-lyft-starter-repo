from abc import ABC, abstractmethod
"""
This is the base class that determines whether a car needs
service or not
"""


class Serviceable(ABC):
    """
    Abstruct base class to force subclasses to implement
    needs_service method
    """
    @abstractmethod
    def needs_service(self) -> bool:
        """ Determine whether a car needs service or not """
        pass