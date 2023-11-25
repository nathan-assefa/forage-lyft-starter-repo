from abc import ABC, abstractmethod
from datetime import datetime


class Battery(ABC):
    """ This is the base class for all battery-related classes """
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        """
        abstruct method to determine whether a battery needs service
        """
        pass

    def calculate_service_threshold_date(self, years):
        """
        This method calculates the limitation or the boundary
        for the battry service.
        """
        return self.last_service_date.replace(
            year=self.last_service_date.year + years
            )
    
    def check_service_threshold(self, threshold_years):
        """
        This method decides if a battery needs a service if and only
        if the service threshold date is less than the current date
        """
        service_threshold_date = self.calculate_service_threshold_date(threshold_years)
        current_date = datetime.today().date()
        return service_threshold_date < current_date
