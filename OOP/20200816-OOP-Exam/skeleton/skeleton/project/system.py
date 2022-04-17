from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return f"Hardware does not exist"
        except Exception as context:
            return str(context)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return f"Hardware does not exist"
        except Exception as context:
            return str(context)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return f"Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {sum([h.used_memory for h in System._hardware])} / {sum([h.memory for h in System._hardware])}\n" \
               f"Total Capacity Taken: {sum([h.used_capacity for h in System._hardware])} / {sum([h.capacity for h in System._hardware])}"

    @staticmethod
    def system_split():
        result = ""
        for element in System._hardware:
            result += f"Hardware Component - {element.name}\n"
            result += f"Express Software Components: {len([s for s in element.software_components if s.__class__.__name__ == 'ExpressSoftware'])}\n"
            result += f"Light Software Components: {len([s for s in element.software_components if s.__class__.__name__ == 'LightSoftware'])}\n"
            result += f"Memory Usage: {element.used_memory} / {element.memory}\n"
            result += f"Capacity Usage: {element.used_capacity} / {element.capacity}\n"
            result += f"Type: {element.type}\n"
            s_components = ', '.join([s.name for s in element.software_components])
            result += f"Software Components: {s_components if s_components else None}"
        return result
