# Problem 1
# # firework = "5, 6, 4, 16, 11, 5, 30, 2, 3, 27"
# # firework = "-15, -8, 0, -16, 0, -22"
#
# firework_effects = [int(i) for i in input().split(", ")]  # queue
#
# # explosive = "1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22"
# # explosive = "10, 5"
#
# explosive_power = [int(i) for i in input().split(", ")]  # stack
#
# palm_firework = 0
# willow_firework = 0
# crossette_firework = 0
# next_firework = 0
# next_explosive = 0
# is_perfect = False
#
# while firework_effects and explosive_power:
#
#     next_firework = firework_effects[0]
#     next_explosive = explosive_power[-1]
#
#     if next_firework <= 0:
#         firework_effects.pop(0)
#
#     elif next_explosive <= 0:
#         explosive_power.pop()
#
#     elif (next_firework + next_explosive) % 15 == 0:
#         crossette_firework += 1
#         firework_effects.pop(0)
#         explosive_power.pop()
#
#     elif (next_firework + next_explosive) % 5 == 0:
#         willow_firework += 1
#         firework_effects.pop(0)
#         explosive_power.pop()
#
#     elif (next_firework + next_explosive) % 3 == 0:
#         palm_firework += 1
#         firework_effects.pop(0)
#         explosive_power.pop()
#
#     else:
#         firework_effects.pop(0)
#         firework_effects.append(next_firework - 1)
#
#     if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
#         is_perfect = True
#         break
#
# if is_perfect:
#     print(f"Congrats! You made the perfect firework show!")
# else:
#     print(f"Sorry. You can’t make the perfect firework show.")
# if firework_effects:
#     print(f"Firework Effects left: {', '.join([str(i) for i in firework_effects])}")
# if explosive_power:
#     print(f"Explosive Power left: {', '.join([str(i) for i in explosive_power])}")
# print(f"Palm Fireworks: {palm_firework}")
# print(f"Willow Fireworks: {willow_firework}")
# print(f"Crossette Fireworks: {crossette_firework}")

# Problem 2
# from math import floor
#
#
# def find_player():
#     for row in whole_matrix:
#         for column in row:
#             if column == "P":
#                 _player_row = whole_matrix.index(row)
#                 _player_column = row.index(column)
#                 return _player_row, _player_column
#
#
# def move(_next_row, _next_column, _last_row, _last_column, _total_coins):
#
#     _is_ended = False
#
#     if 0 <= _next_row < matrix_size and 0 <= _next_column < matrix_size:
#         if whole_matrix[_next_row][_next_column] != "X":
#             _total_coins += int(whole_matrix[_next_row][_next_column])
#             return _next_row, _next_column, _total_coins, _is_ended
#         _is_ended = True
#         return _last_row, _last_column, _total_coins * 0.5, _is_ended
#     _is_ended = True
#     return _last_row, _last_column, _total_coins * 0.5, _is_ended
#
#
# matrix_size = int(input())
# whole_matrix = [[x for x in input().split()] for _ in range(matrix_size)]
#
# player_path = []
#
# total_coins = 0
#
# last_row, last_column = find_player()
#
# is_ended = False
#
# while total_coins < 100:
#
#     next_command = input()
#
#     if next_command == "down":
#         next_row = last_row + 1
#         next_column = last_column
#         last_row, last_column, total_coins, is_ended = move(next_row, next_column, last_row, last_column, total_coins)
#         if is_ended:
#             break
#         player_path.append([last_row, last_column])
#
#     if next_command == "right":
#         next_row = last_row
#         next_column = last_column + 1
#         last_row, last_column, total_coins, is_ended = move(next_row, next_column, last_row, last_column, total_coins)
#         if is_ended:
#             break
#         player_path.append([last_row, last_column])
#
#     if next_command == "up":
#         next_row = last_row - 1
#         next_column = last_column
#         last_row, last_column, total_coins, is_ended = move(next_row, next_column, last_row, last_column, total_coins)
#         if is_ended:
#             break
#         player_path.append([last_row, last_column])
#
#     if next_command == "left":
#         next_row = last_row
#         next_column = last_column - 1
#         last_row, last_column, total_coins, is_ended = move(next_row, next_column, last_row, last_column, total_coins)
#         if is_ended:
#             break
#         player_path.append([last_row, last_column])
#
# if is_ended:
#     print(f"Game over! You've collected {floor(total_coins)} coins.")
# else:
#     print(f"You won! You've collected {floor(total_coins)} coins.")
#
# print(f"Your path:")
# for _ in player_path:
#     print(_)

# 1 X 7 9 11
# X 14 46 62 0
# 15 33 21 95 X
# P 14 3 4 18
# 9 20 33 X 0

# 13 18 9 7 24 41 52 11
# 54 21 19 X 6 4 75 6
# 76 5 7 1 76 27 2 37
# 92 3 25 37 52 X 56 72
# 15 X 1 45 45 X 7 63
# 1 63 P 2 X 43 5 1
# 48 19 35 20 100 27 42 80
# 73 88 78 33 37 52 X 22

# Problem 3
# def stock_availability(inventory_list: list, action, *args):
#     if action == "delivery":
#
#         for element in args:
#             inventory_list.append(element)
#
#     if action == "sell":
#
#         if args:
#
#             if type(args[0]) == int:
#
#                 for i in range(int(args[0])):
#                     inventory_list.pop(0)
#
#             else:
#
#                 for i in args:
#                     while i in inventory_list:
#                         inventory_list.remove(i)
#
#         else:
#
#             inventory_list.pop(0)
#
#     return inventory_list


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
