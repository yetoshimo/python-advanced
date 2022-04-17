# 01. Unique Usernames
# usernames = set()
#
# for i in range(int(input())):
#     usernames.add(input())
#
# for j in usernames:
#     print(j)

# 02. Sets of Elements
# set_m = set()
# set_n = set()
#
# set_lengths = input().split(" ")
#
# for i in range(int(set_lengths[0])):
#     set_m.add(input())
#
# for j in range(int(set_lengths[1])):
#     set_n.add(input())
#
# for k in set_m.intersection(set_n):
#     print(k)

# 03. Periodic Table
# elements_set = set()
#
# for i in range(int(input())):
#     input_elements = input().split(" ")
#
#     for j in input_elements:
#         elements_set.add(j)
#
# print("\n".join(elements_set))

# 04. Count Symbols
# characters_dictionary = {}
#
# input_string = input()
#
# for i in range(len(input_string)):
#     if input_string[i] not in characters_dictionary:
#         characters_dictionary[input_string[i]] = 1
#     else:
#         characters_dictionary[input_string[i]] += 1
#
# for key, value in sorted(characters_dictionary.items()):
#     print(f"{key}: {value} time/s")

# 05. Phonebook
# phonebook = {}
#
# name_and_number = input()
#
# while not name_and_number.isdigit():
#     name = name_and_number.split("-")[0]
#     number = name_and_number.split("-")[1]
#
#     phonebook[name] = number
#
#     name_and_number = input()
#
# for i in range(int(name_and_number)):
#     dial_name = input()
#
#     if dial_name in phonebook:
#         print(f"{dial_name} -> {phonebook[dial_name]}")
#     else:
#         print(f"Contact {dial_name} does not exist.")

# 06. Longest Intersection
# max_length = 0
# first_set = set()
# second_set = set()
#
# number_of_sets = int(input())
#
# for i in range(number_of_sets):
#     two_ranges = input().split("-")
#
#     first_begin = int(two_ranges[0].split(",")[0])
#     first_end = int(two_ranges[0].split(",")[1])
#
#     for j in range(first_begin, first_end + 1):
#         first_set.add(j)
#
#     second_begin = int(two_ranges[1].split(",")[0])
#     second_end = int(two_ranges[1].split(",")[1])
#
#     for k in range(second_begin, second_end + 1):
#         second_set.add(k)
#
#     if len(first_set.intersection(second_set)) > max_length:
#         max_length = len(first_set.intersection(second_set))
#         max_set = first_set.intersection(second_set)
#
#     first_set = set()
#     second_set = set()
#
# print(f"Longest intersection is [{', '.join(map(str, max_set))}] with length {max_length}")

# 07. Battle of Names
# number_of_names = int(input())
# odd_set = set()
# even_set = set()
#
# for i in range(1, number_of_names + 1):
#     name = input()
#     sum_name = 0
#
#     for letter in name:
#         sum_name += ord(letter)
#
#     if sum_name / i % 2 == 0:
#         even_set.add(int(sum_name / i))
#     else:
#         odd_set.add(int(sum_name / i))
#
# if sum(even_set) == sum(odd_set):
#     print(f"{', '.join(map(str, (odd_set.union(even_set))))}")
# elif sum(odd_set) > sum(even_set):
#     print(f"{', '.join(map(str, (odd_set.difference(even_set))))}")
# elif sum(even_set) > sum(odd_set):
#     print(f"{', '.join(map(str, (odd_set.symmetric_difference(even_set))))}")
