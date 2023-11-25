from abc import ABC, abstractmethod

class Engine(ABC):
    """ This is the base class for all engine-related classes """
    @abstractmethod
    def needs_service(self):
        """
        This abstruct method forces all subclasses to implement
        this method 
        """
        pass