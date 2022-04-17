# 01. Word Filter
# even_words = [word for word in input().split(" ") if len(word) % 2 == 0]
# for _ in even_words:
#     print(_)

# 02. Words Lengths
# words = {item: str(len(item)) for item in input().split(", ")}
# print(', '.join(['{0} -> {1}'.format(key, value) for key, value in words.items()]))

# 03. Capitals
# country_capital = {country: capital for country, capital in zip(input().split(", "), input().split(", "))}
# for country, capital in country_capital.items():
#     print(f"{country} -> {capital}")

# 04. Number Classification
# numbers_input = [int(i) for i in input().split(", ")]
# numbers = {'Positive': [item for item in numbers_input if item >= 0],
#            'Negative': [item for item in numbers_input if item < 0],
#            'Even': [item for item in numbers_input if item % 2 == 0],
#            'Odd': [item for item in numbers_input if item % 2 != 0]}
#
#
# for key, value in numbers.items():
#     print(f"{key}: {', '.join(map(str, value))}")

# 05. Diagonals
# whole_matrix = [[int(item) for item in input().split(", ")] for _ in range(int(input()))]
# diagonals = {'First diagonal': [whole_matrix[i][i] for i in range(len(whole_matrix))],
#              'Second diagonal': [whole_matrix[i][len(whole_matrix) - 1 - i] for i in range(len(whole_matrix))]}
# for key, value in diagonals.items():
#     print(f"{key}: {', '.join(map(str, value))}. Sum: {sum(value)}")

# 06. Matrix of Palindromes
# ascii_a = 97
# row, column = [int(i) for i in input().split()]
# matrix = [[chr(ascii_a + i) + chr(ascii_a + i + j) + chr(ascii_a + i) for j in range(column)] for i in range(row)]
# for item in matrix:
#     print(' '.join(item))

# 07. Flatten Lists
# input_string = [item.split() for item in input().split("|")[::-1]]
# print(*[element for item in input_string for element in item])

# 08. Heroes Inventory
# heroes = {hero_name: {} for hero_name in input().split(", ")}
#
# input_command = input()
#
# while input_command != "End":
#     hero_name, item_name, item_cost = input_command.split("-")
#
#     if not heroes.get(hero_name):
#         heroes[hero_name] = {}
#
#     if not heroes[hero_name].get(item_name):
#         heroes[hero_name].update({item_name: int(item_cost)})
#
#     input_command = input()
#
# for key, value in heroes.items():
#     print(f"{key} -> Items: {len(value)}, Cost: {sum(value.values())}")

# 09. Bunker
from re import findall


# class BunkerObject:
#     def __init__(self, item_name, item_quantity, item_quality):
#         self.item_name = item_name
#         self.item_quantity = item_quantity
#         self.item_quality = item_quality
#
#
# bunker = {item_name: {} for item_name in input().split(", ")}
#
# for _ in range(int(input())):
#     # item_line = findall(r"(\w+)", input())
#     item_line = input().split()
#     name = item_line[0]
#     item = item_line[2]
#     quantity = int(item_line[4].split(";")[0].split(":")[1])
#     quality = int(item_line[4].split(";")[1].split(":")[1])
#
#     if name in bunker:
#         bunker[name].update({item: BunkerObject(item, quantity, quality)})
#
# print(f"Count of items: {sum([v.item_quantity for value in bunker.values() for v in value.values()])}")
# print(f"Average quality: {sum([v.item_quality for value in bunker.values() for v in value.values()]) / len(bunker):.2f}")
# for key, value in bunker.items():
#     print(f"{key} -> {', '.join([kv for kv in value])}")

# 10. Matrix Modification
# whole_matrix = [[int(row) for row in input().split(" ")] for _ in range(int(input()))]
#
# input_command = input()
#
# while input_command != "END":
#     command, row, column, value = input_command.split(" ")
#
#     if 0 <= int(row) < len(whole_matrix) and 0 <= int(column) < len(whole_matrix):
#         if command == "Add":
#             whole_matrix[int(row)][int(column)] += int(value)
#         else:
#             whole_matrix[int(row)][int(column)] -= int(value)
#     else:
#         print(f"Invalid coordinates")
#
#     input_command = input()
#
# [print(*row) for row in whole_matrix]
