# Problem 1
# from collections import deque
#
# firework_effects = deque([int(i) for i in input().split(", ")])
# explosive_power = [int(i) for i in input().split(", ")]
#
# firework_dict = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
#
# is_ready = False
#
# while firework_effects and explosive_power and not is_ready:
#
#     next_firework = firework_effects.popleft()
#     next_explosive = explosive_power.pop()
#
#     if next_firework <= 0:
#         explosive_power.append(next_explosive)
#     elif next_explosive <= 0:
#         firework_effects.appendleft(next_firework)
#     elif (next_firework + next_explosive) % 15 == 0:
#         firework_dict["Crossette Fireworks"] += 1
#     elif (next_firework + next_explosive) % 3 == 0:
#         firework_dict["Palm Fireworks"] += 1
#     elif (next_firework + next_explosive) % 5 == 0:
#         firework_dict["Willow Fireworks"] += 1
#     else:
#         firework_effects.append(next_firework - 1)
#         explosive_power.append(next_explosive)
#
#     if firework_dict["Palm Fireworks"] >= 3 and firework_dict["Willow Fireworks"] >= 3 and firework_dict[
#         "Crossette Fireworks"] >= 3:
#         is_ready = True
#
# if is_ready:
#     print(f"Congrats! You made the perfect firework show!")
# else:
#     print(f"Sorry. You can't make the perfect firework show.")
#
# if firework_effects:
#     print(f"Firework Effects left: {', '.join([str(i) for i in firework_effects])}")
# if explosive_power:
#     print(f"Explosive Power left: {', '.join([str(i) for i in explosive_power])}")
# for key, value in firework_dict.items():
#     print(f"{key}: {value}")

# Problem 2
# from math import floor
#
#
# def find_player(_matrix):
#     for p_r, row in enumerate(_matrix):
#         for p_c, column in enumerate(row):
#             if column == "P":
#                 return p_r, p_c
#
#
# def move_player(p_r, p_c, n_r, n_c, _matrix, _size, _coins, _path):
#     _is_finished = False
#     if 0 <= n_r < _size and 0 <= n_c < _size and _matrix[n_r][n_c] != "X":
#         _coins += int(_matrix[n_r][n_c])
#         _path.append([n_r, n_c])
#         p_r = n_r
#         p_c = n_c
#         return p_r, p_c, _matrix, _is_finished, _coins, _path
#     _is_finished = True
#     _coins = floor(_coins * 0.5)
#     return p_r, p_c, _matrix, _is_finished, _coins, _path
#
#
# field_size = int(input())
#
# whole_matrix = [input().split() for i in range(field_size)]
#
# player_r, player_c = find_player(whole_matrix)
#
# total_coins = 0
#
# is_finished = False
#
# player_path = []
#
# while total_coins < 100 and not is_finished:
#
#     command = input()
#
#     if command == "up":
#         player_r, player_c, whole_matrix, is_finished, total_coins, player_path = move_player(player_r, player_c,
#                                                                                               player_r - 1, player_c,
#                                                                                               whole_matrix, field_size,
#                                                                                               total_coins, player_path)
#     elif command == "down":
#         player_r, player_c, whole_matrix, is_finished, total_coins, player_path = move_player(player_r, player_c,
#                                                                                               player_r + 1, player_c,
#                                                                                               whole_matrix, field_size,
#                                                                                               total_coins, player_path)
#
#     elif command == "right":
#         player_r, player_c, whole_matrix, is_finished, total_coins, player_path = move_player(player_r, player_c,
#                                                                                               player_r, player_c + 1,
#                                                                                               whole_matrix, field_size,
#                                                                                               total_coins, player_path)
#
#     elif command == "left":
#         player_r, player_c, whole_matrix, is_finished, total_coins, player_path = move_player(player_r, player_c,
#                                                                                               player_r, player_c - 1,
#                                                                                               whole_matrix, field_size,
#                                                                                               total_coins, player_path)
#
# if total_coins >= 100:
#     print(f"You won! You've collected {total_coins} coins.")
# else:
#     print(f"Game over! You've collected {total_coins} coins.")
# print(f"Your path:")
# [print(i) for i in player_path]

# Problem 3
# def stock_availability(inventory: list, command: str, *args):
#
#     if command == "delivery":
#         for i in args:
#             inventory.append(i)
#         return inventory
#
#     if command == "sell":
#         if not args:
#             return inventory[1:]
#         if isinstance(args[0], int):
#             for i in range(int(args[0])):
#                 inventory = inventory[1:]
#             return inventory
#         else:
#             for item in args:
#                 while item in inventory:
#                     inventory.remove(item)
#             return inventory


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
