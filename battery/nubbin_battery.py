from .battery import Battery


class NubbinBattery(Battery):
    """ Nubbin battery will be serviced every 4 years """
    def needs_service(self):
        return self.check_service_threshold(4)