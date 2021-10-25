from project.software.software import Software


class LightSoftware(Software):

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Light", capacity_consumption, memory_consumption)

        self.memory_consumption = int(memory_consumption * 0.5)
        self.capacity_consumption = int(capacity_consumption * 1.5)
