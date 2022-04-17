from system import System


def zero_test():
    # (name, "Power", int(capacity * 0.25), int(memory * 1.75))
    System.register_power_hardware("HDD", 200, 200)  # HDD 50 capacity 350 memory
    # (name, "Heavy", capacity * 2, int(memory * 0.75))
    System.register_heavy_hardware("SSD", 400, 400)  # SSD 800 capacity 300 memory
    print(System.analyze())
    # (name, "Light", int(capacity_consumption * 1.5), int(memory_consumption * 0.5))
    System.register_light_software("HDD", "Test", 0, 10)
    # (name, "Express", capacity_consumption, memory_consumption * 2)
    print(System.register_express_software("HDD", "Test2", 100, 100))
    System.register_express_software("HDD", "Test3", 50, 100)
    System.register_light_software("SSD", "Windows", 20, 50)
    System.register_express_software("SSD", "Linux", 50, 100)
    System.register_light_software("SSD", "Unix", 20, 50)
    print(System.analyze())
    System.release_software_component("SSD", "Linux")
    print(System.system_split())


if __name__ == "__main__":
    zero_test()
