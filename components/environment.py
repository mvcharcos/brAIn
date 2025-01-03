class Environment:
    def __init__(self):
        self.lamp1 = "off"
        self.lamp2 = "off"
        self.lux = 0
        self.consumption1 = 0
        self.consumption2 = 0

    def set_state(self, lamp1=None, lamp2=None, lux=None, consumption1=None, consumption2=None):
        if lamp1 is not None: self.lamp1 = lamp1
        if lamp2 is not None: self.lamp2 = lamp2
        if lux is not None: self.lux = lux
        if consumption1 is not None: self.consumption1 = consumption1
        if consumption2 is not None: self.consumption2 = consumption2

    def get_state(self):
        return {
            "lamp1": self.lamp1,
            "lamp2": self.lamp2,
            "lux": self.lux,
            "consumption1": self.consumption1,
            "consumption2": self.consumption2,
        }
