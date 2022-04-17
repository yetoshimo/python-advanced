class Dough:

    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @property
    def weight(self):
        return self.__weight

    @flour_type.setter
    def flour_type(self, _flour_type):
        self.__flour_type = _flour_type

    @baking_technique.setter
    def baking_technique(self, _baking_technique):
        self.__baking_technique = _baking_technique

    @weight.setter
    def weight(self, _weight):
        self.__weight = _weight
