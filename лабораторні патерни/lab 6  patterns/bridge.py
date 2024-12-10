class Appliance:
    """Base class for devices."""
    def activate(self):
        raise NotImplementedError

    def deactivate(self):
        raise NotImplementedError


class RemoteController:
    """Controller for managing devices."""
    def __init__(self, appliance: Appliance):
        self.appliance = appliance

    def enable(self):
        return self.appliance.activate()

    def disable(self):
        return self.appliance.deactivate()
