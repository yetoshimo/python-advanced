class Pizza:

    def __init__(self, name: str, dough, toppings_capacity: int):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}  # topping type as a key and the topping's weight as a value

    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @property
    def toppings(self):
        return self.__toppings

    @name.setter
    def name(self, _name):
        self.__name = _name

    @dough.setter
    def dough(self, _dough):
        self.__dough = _dough

    @toppings_capacity.setter
    def toppings_capacity(self, _toppings_capacity):
        self.__toppings_capacity = _toppings_capacity

    @toppings.setter
    def toppings(self, _topping, _weight):
        self.__toppings[_topping] = _weight

    @staticmethod
    def __is_capacity_enough(_current_toppings, _total_capacity):
        return len(_current_toppings) < _total_capacity

    def add_topping(self, topping):
        if not self.__is_capacity_enough(self.__toppings, self.__toppings_capacity):
            raise ValueError(f"Not enough space for another topping")

        if topping.topping_type not in self.__toppings:
            self.__toppings[topping.topping_type] = topping.weight
        else:
            self.__toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        return sum([i for i in self.__toppings.values()]) + self.dough.weight
