from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity: int, memory: int):
        result = PowerHardware(name, capacity, memory)
        System._hardware.append(result)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for h in System._hardware:
            if hardware_name == h.name:
                software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                try:
                    h.install(software)
                    System._software.append(software)
                except Exception:
                    return "Software cannot be installed"

                return

        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for h in System._hardware:
            if hardware_name == h.name:
                software = LightSoftware(name, capacity_consumption, memory_consumption)
                try:
                    h.install(software)
                    System._software.append(software)
                except Exception:
                    return "Software cannot be installed"

                return

        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        h = [h for h in System._hardware if h.name == hardware_name]
        s = [s for s in System._software if s.name == software_name]
        if h and s:
            h[0].uninstall(s[0])
            System._software.remove(s[0])

        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        total_memory = sum([h.memory for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])
        used_memory = sum([s.memory_consumption for s in System._software])
        used_capacity = sum([s.capacity_consumption for s in System._software])
        result += f"Total Operational Memory: {used_memory:.0f} / {total_memory:.0f}\n"
        result += f"Total Capacity Taken: {used_capacity:.0f} / {total_capacity:.0f}"
        return result

    @staticmethod
    def system_split():
        final_result = ""
        for component in System._hardware:
            result = f"Hardware Component - {component.name}\n"
            result += f"Express Software Components: " \
                      f"{len([s for s in component.software_components if type(s) == ExpressSoftware])}\n"
            result += f"Light Software Components: " \
                      f"{len([s for s in component.software_components if type(s) == LightSoftware])}\n"
            total_memory = component.memory
            total_capacity = component.capacity
            used_memory = sum([s.memory_consumption for s in component.software_components])
            used_capacity = sum([s.capacity_consumption for s in component.software_components])
            result += f"Memory Usage: {used_memory:.0f} / {total_memory:.0f}\n"
            result += f"Capacity Usage: {used_capacity:.0f} / {total_capacity:.0f}\n"
            result += f"Type: {component.type}\n"
            if component.software_components:
                result += f"Software Components: {', '.join([s.name for s in component.software_components])}"
            else:
                result += f"Software Components: {None}"
            final_result += result
        return final_result
