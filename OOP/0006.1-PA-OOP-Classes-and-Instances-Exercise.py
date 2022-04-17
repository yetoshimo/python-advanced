# 01. Point
# from math import sqrt
#
#
# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#
#     def set_x(self, new_x):
#         self.x = new_x
#         return
#
#     def set_y(self, new_y):
#         self.y = new_y
#         return
#
#     def distance(self, to_x, to_y):
#         _distance = sqrt((to_x - self.x) ** 2 + (to_y - self.y) ** 2)
#         return _distance
#
#
# p = Point(2, 4)
# p.set_x(3)
# p.set_y(5)
# print(p.distance(10, 2))

# 03. Account
# class Account:
#     def __init__(self, id: int, name: str, balance: int = 0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if self.balance - amount < 0:
#             return f"Amount exceeded balance"
#         self.balance -= amount
#         return self.balance
#
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance"


# account = Account(1234, "George", 1000)
# print(account.credit(500))
# print(account.debit(1500))
# print(account.info())

# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())

# 04. Employee
# class Employee:
#     def __init__(self, id: int, first_name: str, last_name: str, salary: int):
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def get_annual_salary(self):
#         return self.salary * 12
#
#     def raise_salary(self, amount):
#         self.salary += amount
#         return self.salary


# employee = Employee(744423129, "John", "Smith", 1000)
# print(employee.get_full_name())
# print(employee.raise_salary(500))
# print(employee.get_annual_salary())

# 05. Time
# class Time:
#     max_hours = 23
#     max_minutes = 59
#     max_seconds = 59
#
#     def __init__(self, hours: int, minutes: int, seconds: int):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def set_time(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self):
#         return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
#
#     def next_second(self):
#         if self.seconds + 1 <= Time.max_seconds:
#             self.seconds += 1
#             return Time.get_time(self)
#         else:
#             self.seconds = self.seconds - Time.max_seconds
#             if self.minutes + 1 <= Time.max_minutes:
#                 self.minutes += 1
#                 return Time.get_time(self)
#             else:
#                 self.minutes = self.minutes - Time.max_minutes
#                 if self.hours + 1 <= Time.max_hours:
#                     self.hours += 1
#                     return Time.get_time(self)
#                 else:
#                     self.hours = self.hours - Time.max_hours
#                     return Time.get_time(self)


# time = Time(9, 30, 59)
# print(time.next_second())
#
# time = Time(10, 59, 59)
# print(time.next_second())
#
# time = Time(23, 59, 59)
# print(time.next_second())
#
# time = Time(16, 35, 54)
# print(time.next_second())
#
# time = Time(1, 20, 30)
# print(time.next_second())
#
# time = Time(1, 59, 59)
# print(time.next_second())
#
# time = Time(0, 0, 0)
# print(time.next_second())

# 06. Pizza Delivery
# class PizzaDelivery:
#     ordered = False  # if not present runtime error
#
#     def __init__(self, name: str, price: float, ingredients: dict):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#         self.ordered = False
#
#     def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             self.ingredients[ingredient] = quantity
#             self.price += ingredient_price * quantity
#             return
#         self.ingredients[ingredient] += quantity
#         self.price += quantity * ingredient_price
#         return
#
#     def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
#         if quantity > self.ingredients[ingredient]:
#             return f"Please check again the desired quantity of {ingredient}!"
#         self.ingredients[ingredient] -= quantity
#         self.price -= quantity * ingredient_price
#         return
#
#     def make_order(self):
#         PizzaDelivery.ordered = True
#         self.ordered = True
#         return f"You've ordered pizza {self.name} prepared with {', '.join([key+': '+str(value) for key, value in self.ingredients.items()])} and the price will be {self.price}lv."

