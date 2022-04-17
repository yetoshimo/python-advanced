from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:

    def __init__(self):
        self.survivors = []  # empty list upon initialization that will contain all the survivors (objects)
        self.supplies = []  # empty list upon initialization that will contain all the supplies (objects)
        self.medicine = []  # empty list upon initialization that will contain all the medicine (objects)
        self.__food = []
        self.__water = []
        self.__painkillers = []
        self.__salves = []

    @property
    def food(self):
        return self.__get_food_items()

    def __get_food_items(self):
        __food_items = [item for item in self.supplies if item.__class__.__name__ == "FoodSupply"]
        if __food_items:
            return __food_items
        raise IndexError(f"There are no food supplies left!")

    @property
    def water(self):
        return self.__get_water_items()

    def __get_water_items(self):
        __water_items = [item for item in self.supplies if item.__class__.__name__ == "WaterSupply"]
        if __water_items:
            return __water_items
        raise IndexError(f"There are no water supplies left!")

    @property
    def painkillers(self):
        return self.__get_painkillers()

    def __get_painkillers(self):
        __painkillers = [item for item in self.medicine if item.__class__.__name__ == "Painkiller"]
        if __painkillers:
            return __painkillers
        raise IndexError(f"There are no painkillers left!")

    @property
    def salves(self):
        return self.__get_salves()

    def __get_salves(self):
        __salves = [item for item in self.medicine if item.__class__.__name__ == "Salve"]
        if __salves:
            return __salves
        raise IndexError(f"There are no salves left!")

    def add_survivor(self, survivor: Survivor):
        self.__validate_survivor(survivor)
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            medicine_to_apply = self.__get_last_medicine(medicine_type)
            medicine_to_apply.apply(survivor)
            self.medicine.remove(medicine_to_apply)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            sustenance_to_apply = self.__get_last_sustenance(sustenance_type)
            sustenance_to_apply.apply(survivor)
            self.supplies.remove(sustenance_to_apply)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        self.__reduce_needs_of_survivors(self.survivors)
        self.__sustain_survivors(self.survivors)

    def __validate_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")

    def __get_last_medicine(self, medicine_type):
        if medicine_type == "Painkiller":
            if self.painkillers:
                painkiller_to_apply = self.painkillers.pop()
            return painkiller_to_apply
        elif medicine_type == "Salve":
            if self.salves:
                salve_to_apply = self.salves.pop()
            return salve_to_apply

    def __get_last_sustenance(self, sustenance_type):
        if sustenance_type == "FoodSupply":
            if self.food:
                food_supply_to_apply = self.food.pop()
            return food_supply_to_apply
        elif sustenance_type == "WaterSupply":
            if self.water:
                water_supply_to_apply = self.water.pop()
            return water_supply_to_apply

    @staticmethod
    def __reduce_needs_of_survivors(survivors):
        for person in survivors:
            person.needs -= person.age * 2

    def __sustain_survivors(self, survivors):
        for person in survivors:
            self.sustain(person, "FoodSupply")
            self.sustain(person, "WaterSupply")
