# 01. Count Same Values
# number_string = (float(i) for i in input().split(" "))
#
# number_occur = {}
#
# for i in number_string:
#     if i not in number_occur:
#         number_occur[i] = 0
#     number_occur[i] += 1
#
# for key, value in number_occur.items():
#     print(f"{key} - {value} times")

# 02. Average Student Grades
# number_of_students = int(input())
#
# students_dictionary = {}
#
# for i in range(number_of_students):
#     input_command = input().split(" ")
#     name = input_command[0]
#     grade = float(input_command[1])
#
#     if name not in students_dictionary:
#         students_dictionary[name] = [grade]
#     else:
#         students_dictionary[name].append(grade)
#
# for key, (values) in students_dictionary.items():
#     print(f"{key} -> {' '.join(map('{:.2f}'.format, tuple(values)))} (avg: {sum(values)/len(values):.2f})")

# 03. Record Unique Names
# names = set()
#
# for i in range(int(input())):
#     names.add(input())
#
# for j in names:
#     print(j)

# 04. Parking Lot
# registration = set()
# number_of_cars = int(input())
# for i in range(number_of_cars):
#     command = input().split(", ")
#
#     direction = command[0]
#     car = command[1]
#
#     if direction == "IN":
#         registration.add(car)
#     else:
#         registration.remove(car)
#
# if registration:
#     for i in registration:
#         print(i)
# else:
#     print(f"Parking Lot is Empty")

# 05. SoftUni Party
# vip_list = set()
# regular_list = set()
#
# for i in range(int(input())):
#     reservation = input()
#
#     if reservation[0].isdigit():
#         vip_list.add(reservation)
#     else:
#         regular_list.add(reservation)
#
# guest = input()
#
# while guest != "END":
#     if guest in vip_list:
#         vip_list.remove(guest)
#     elif guest in regular_list:
#         regular_list.remove(guest)
#     guest = input()
#
# print(f"{len(vip_list) + len(regular_list)}")
#
# for i in sorted(vip_list):
#     print(i)
# for j in sorted(regular_list):
#     print(j)
