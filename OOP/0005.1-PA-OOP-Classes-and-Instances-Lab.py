# 01. Smartphone
# class Smartphone:
#     def __init__(self, memory: int):
#         self.memory = memory
#         self.apps = []
#         self.is_on = False
#
#     def power(self):
#         self.is_on = not self.is_on
#
#     def install(self, app, memory):
#         if self.memory - memory >= 0 and self.is_on:
#             self.apps.append(app)
#             self.memory -= memory
#             return f"Installing {app}"
#         elif self.memory - memory >= 0 and not self.is_on:
#             return f"Turn on your phone to install {app}"
#         else:
#             return f"Not enough memory to install {app}"
#
#     def status(self):
#         return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
#
#
# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())

# 02. Vet
# class Vet:
#     animals = []  # it will store the total amount of animals for all vets
#     space = 5
#
#     def __init__(self, name: str):
#         self.name = name
#         self.animals = []
#
#     def register_animal(self, animal_name):
#         if not Vet.space:
#             return f"Not enough space"
#         Vet.animals.append(animal_name)
#         Vet.space -= 1
#         self.animals.append(animal_name)
#         return f"{animal_name} registered in the clinic"
#
#     def unregister_animal(self, animal_name):
#         if animal_name not in Vet.animals:
#             return f"{animal_name} not in the clinic"
#         Vet.animals.remove(animal_name)
#         Vet.space += 1
#         self.animals.remove(animal_name)
#         return f"{animal_name} unregistered successfully"
#
#     def info(self):
#         return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"
#
#
# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())

# 01. Vehicle
# class Vehicle:
#
#     def __init__(self, mileage, max_speed=150):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.gadgets = []


# car = Vehicle(20)
# print(car.max_speed)
# print(car.mileage)
# print(car.gadgets)
# car.gadgets.append('Hudly Wireless')
# print(car.gadgets)

# 02. Point
# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_x(self, new_x):
#         self.x = new_x
#
#     def set_y(self, new_y):
#         self.y = new_y
#
#     def __str__(self):
#         return f"The point has coordinates ({self.x},{self.y})"


# p = Point(2, 4)
# print(p)
# p.set_x(3)
# p.set_y(5)
# print(p)

# 03. Circle
# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius: int):
#         self.radius = radius
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#
#     def get_area(self):
#         return self.radius ** 2 * Circle.pi
#
#     def get_circumference(self):
#         return self.radius * 2 * Circle.pi
#
#
# circle = Circle(10)
# circle.set_radius(12)
# print(circle.get_area())
# print(circle.get_circumference())

# 04. Glass
# class Glass:
#     capacity = 250
#
#     def __init__(self):
#         self.content = 0
#
#     def fill(self, ml):
#         if not Glass.capacity - ml >= 0:
#             return f"Cannot add {ml} ml"
#         self.content += ml
#         Glass.capacity -= ml
#         return f"Glass filled with {ml} ml"
#
#     def empty(self):
#         Glass.capacity += self.content
#         self.content = 0
#         return f"Glass is now empty"
#
#     def info(self):
#         return f"{Glass.capacity} ml left"
#
#
# glass = Glass()
# print(glass.fill(100))
# print(glass.fill(200))
# print(glass.empty())
# print(glass.fill(200))
# print(glass.info())

