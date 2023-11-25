from .engine import Engine


class SternmanEngine(Engine):
    """
    SternmanEngine engine will be serviced whenever the signal
    warning_light_is_on is on
    """
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
