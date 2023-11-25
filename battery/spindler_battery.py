from .battery import Battery


class SpindlerBattery(Battery):
    """ SpindlerBattery battery will be serviced every 2 years """
    def needs_service(self):
        return self.check_service_threshold(2)