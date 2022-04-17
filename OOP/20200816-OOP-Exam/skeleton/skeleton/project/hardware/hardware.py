from project.software.software import Software


class Hardware:

    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.memory = memory
        self.capacity = capacity
        self.type = type
        self.name = name
        self.software_components = []

    def install(self, software: Software):
        if software.capacity_consumption <= self.available_capacity \
                and software.memory_consumption <= self.available_memory:
            self.software_components.append(software)
        else:
            raise Exception(f"Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def available_memory(self):
        return self.memory - self.used_memory

    @property
    def available_capacity(self):
        return self.capacity - self.used_capacity

    @property
    def used_capacity(self):
        return sum([s.capacity_consumption for s in self.software_components])

    @property
    def used_memory(self):
        return sum([s.memory_consumption for s in self.software_components])
