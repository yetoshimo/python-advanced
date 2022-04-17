# 01. Store
class Store:
    def __init__(self, name: str, type: str, capacity: int):
        self.capacity = capacity
        self.type = type
        self.name = name
        self.items = {}  # stores name of an item and its quantity
        self.item_count = 0  # counter of items

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @staticmethod
    def can_add_item(_item_count, _capacity):
        return _item_count <= _capacity

    @staticmethod
    def can_remove_item(_items, _item_name, _amount):
        return _item_name in _items and _amount <= _items[_item_name]

    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        return cls(name, type, size // 2)

    def add_item(self, item_name: str):
        if not self.can_add_item(self.item_count, self.capacity):
            return f"Not enough capacity in the store"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        self.item_count += 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name: str, amount: int):
        if not self.can_remove_item(self.items, item_name, amount):
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        self.item_count -= amount
        return f"{amount} {item_name} removed from the store"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))

# 02. Integer
# class Integer:
#
#     def __init__(self, value: int):
#         self.value = value
#
#     @staticmethod
#     def is_float(_value):
#         return isinstance(_value, float)
#
#     @staticmethod
#     def int_from_str(_value):
#         return isinstance(_value, float)
#
#     @staticmethod
#     def roman_to_integer(_value):
#         roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
#                          'XC': 90, 'CD': 400, 'CM': 900}
#         i = 0
#         num = 0
#         while i < len(_value):
#             if i + 1 < len(_value) and _value[i:i + 2] in roman_numbers:
#                 num += roman_numbers[_value[i:i + 2]]
#                 i += 2
#             else:
#                 num += roman_numbers[_value[i]]
#                 i += 1
#         return num
#
#     @staticmethod
#     def is_integer_instance(_integer):
#         return type(_integer) == Integer
#
#     @classmethod
#     def from_float(cls, value):
#         if not cls.is_float(value):
#             return f"value is not a float"
#         return cls(int(value))
#
#     @classmethod
#     def from_string(cls, value):
#         if cls.int_from_str(value):
#             return f"wrong type"
#         return cls(int(value))
#
#     @classmethod
#     def from_roman(cls, value):
#         return cls(cls.roman_to_integer(value))
#
#     def add(self, integer):
#         if not self.is_integer_instance(integer):
#             return f"number should be an Integer instance"
#         return self.value + integer.value

# 03. Calculator
# class Calculator:
#     @staticmethod
#     def add(*args):
#         return sum(args)
#
#     @staticmethod
#     def multiply(*args):
#         _result = 1
#         for _ in args:
#             _result *= _
#         return _result
#
#     @staticmethod
#     def divide(first_number, *args):
#         _result = first_number
#         for _ in args:
#             _result /= _
#         return _result
#
#     @staticmethod
#     def subtract(first_number, *args):
#         _result = first_number
#         for _ in args:
#             _result -= _
#         return _result
