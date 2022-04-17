class Survivor:
    MAX_HEALTH = 100
    MAX_NEEDS = 100

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        self.__health: int = self.MAX_HEALTH
        self.__needs: int = self.MAX_NEEDS

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    @property
    def health(self):
        self.__validate_max_health()
        return self.__health

    @health.setter
    def health(self, value):
        self.__validate_health(value)
        self.__health = value

    @property
    def needs(self):
        self.__validate_max_needs()
        return self.__needs

    @needs.setter
    def needs(self, value):
        self.__validate_needs(value)
        self.__needs = value

    @property
    def needs_sustenance(self):
        return self.needs < 100

    @property
    def needs_healing(self):
        return self.health < 100

    @staticmethod
    def __validate_name(name):
        if name == "" or name is None:
            raise ValueError(f"Name not valid!")

    @staticmethod
    def __validate_age(age):
        if age < 0:
            raise ValueError(f"Age not valid!")

    @staticmethod
    def __validate_health(value):
        if value < 0:
            raise ValueError(f"Health not valid!")

    @staticmethod
    def __validate_needs(value):
        if value < 0:
            raise ValueError(f"Needs not valid!")

    def __validate_max_health(self):
        if self.__health > 100:
            self.__health = self.MAX_HEALTH

    def __validate_max_needs(self):
        if self.__needs > 100:
            self.__needs = self.MAX_NEEDS
