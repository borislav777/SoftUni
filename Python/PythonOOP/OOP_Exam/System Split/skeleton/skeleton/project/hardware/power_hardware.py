from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", capacity, memory)
        self.type = "Power"
        self.capacity = int(capacity * 0.25)
        self.memory = int(memory * 1.75)
