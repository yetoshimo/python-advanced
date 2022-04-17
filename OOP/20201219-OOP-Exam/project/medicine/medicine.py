from abc import ABC

from project.survivor import Survivor


class Medicine(ABC):

    def __init__(self, health_increase: int):
        self.__health_increase = health_increase

    @property
    def health_increase(self):
        return self.__health_increase

    @health_increase.setter
    def health_increase(self, value):
        self.__validate_health_increase(value)
        self.__health_increase = value

    def apply(self, survivor: Survivor):
        """Method should increase the health property of the given survivor with the medicine's health_increase value"""
        survivor.health += self.health_increase

    @staticmethod
    def __validate_health_increase(health_increase):
        if health_increase < 0:
            raise ValueError(f"Health increase cannot be less than zero.")
