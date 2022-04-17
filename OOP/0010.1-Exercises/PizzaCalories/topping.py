class Topping:

    def __init__(self, topping_type: str, weight: float):
        self.__topping_type = topping_type
        self.__weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @property
    def weight(self):
        return self.__weight

    @topping_type.setter
    def topping_type(self, _topping_type):
        self.__topping_type = _topping_type

    @weight.setter
    def weight(self, _weight):
        self.__weight = _weight
