from abc import ABC

from project.survivor import Survivor


class Supply(ABC):

    def __init__(self, needs_increase: int):
        self.__needs_increase = needs_increase

    @staticmethod
    def __validate_needs_increase(needs_increase):
        if needs_increase < 0:
            raise ValueError(f"Needs increase cannot be less than zero.")

    @property
    def needs_increase(self):
        return self.__needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        self.__validate_needs_increase(value)
        self.__needs_increase = value

    def apply(self, survivor: Survivor):
        """Method should increase the needs property of the given survivor with the supply's needs_increase value"""
        survivor.needs += self.needs_increase
