# 01. Bombs
# from collections import deque
#
# # You need to start from the first bomb effect - QUEUE
# bomb_effects = deque(int(i) for i in input().split(", "))
#
# # and try to mix it with the last bomb casing. - STACK
# bomb_casings = [int(i) for i in input().split(", ")]
#
# bomb_mapping = {
#     40: "Datura Bombs",
#     60: "Cherry Bombs",
#     120: "Smoke Decoy Bombs"
# }
#
#
# bomb_pouch = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
#
#
# is_finished = False
# full_pouch = False
#
#
# def bomb_creator(_bomb_effect, _bomb_casing):
#     if _bomb_effect + _bomb_casing in bomb_mapping:
#         return bomb_mapping[_bomb_effect + _bomb_casing]
#     else:
#         return bomb_creator(_bomb_effect, _bomb_casing - 5)
#
#
# def bomb_pouch_checker(**kwargs):
#     if kwargs["Datura Bombs"] >= 3 and kwargs["Cherry Bombs"] >= 3 and kwargs["Smoke Decoy Bombs"] >= 3:
#         return True
#     else:
#         return False
#
#
# while not is_finished:
#     next_bomb_effect = bomb_effects.popleft()
#     next_bomb_casing = bomb_casings.pop()
#
#     created_bomb = bomb_creator(next_bomb_effect, next_bomb_casing)
#
#     if created_bomb not in bomb_pouch:
#         bomb_pouch[created_bomb] = 1
#     else:
#         bomb_pouch[created_bomb] += 1
#
#     if not bomb_effects or not bomb_casings:
#         is_finished = True
#
#     if bomb_pouch_checker(**bomb_pouch):
#         is_finished = True
#         full_pouch = True
#
# if full_pouch:
#     print(f"Bene! You have successfully filled the bomb pouch!")
# else:
#     print(f"You don't have enough materials to fill the bomb pouch.")
# if bomb_effects:
#     print(f"Bomb Effects: {', '.join([str(i) for i in bomb_effects])}")
# else:
#     print(f"Bomb Effects: empty")
# if bomb_casings:
#     print(f"Bomb Casings: {', '.join([str(i) for i in bomb_casings])}")
# else:
#     print(f"Bomb Casings: empty")
#
# for key, value in sorted(bomb_pouch.items()):
#     print(f"{key}: {value}")

# 02. Snake
# def find_start():
#     for i in whole_matrix:
#         for j in i:
#             if j == "S":
#                 start_x = whole_matrix.index(i)
#                 start_y = i.index(j)
#                 return start_x, start_y
#
#
# def find_burrows(_burrow_list=[]):
#     for i in whole_matrix:
#         for j in i:
#             if j == "B":
#                 start_x = whole_matrix.index(i)
#                 start_y = i.index(j)
#                 _burrow_list.append((start_x, start_y))
#     return _burrow_list
#
#
# whole_matrix = []
#
# number_of_turns = int(input())
#
# for _ in range(number_of_turns):
#     whole_matrix.append(list(input()))
#
# current_row, current_column = find_start()
# burrows = find_burrows()
#
# is_finished = False
# is_out = False
# is_food = False
# food_eaten = 0
#
# direction = input()
#
# while not is_finished:
#     whole_matrix[current_row][current_column] = "."
#     last_row = current_row
#     last_column = current_column
#
#     if direction == "up":
#         current_row -= 1
#     elif direction == "down":
#         current_row += 1
#     elif direction == "left":
#         current_column -= 1
#     elif direction == "right":
#         current_column += 1
#
#     if current_row < 0 or current_row >= number_of_turns or current_column >= number_of_turns or current_column < 0:
#         is_finished = True
#         is_out = True
#     else:
#         if whole_matrix[current_row][current_column] == "B":
#             burrows.remove((current_row, current_column))
#             whole_matrix[current_row][current_column] = "."
#             current_row, current_column = burrows[0]
#             whole_matrix[current_row][current_column] = "S"
#         elif whole_matrix[current_row][current_column] == "*":
#             whole_matrix[current_row][current_column] = "S"
#             food_eaten += 1
#             if food_eaten == 10:
#                 is_finished = True
#                 is_food = True
#         else:
#             whole_matrix[current_row][current_column] = "S"
#
#     if is_finished:
#         break
#
#     direction = input()
#
# if is_food:
#     print(f"You won! You fed the snake.")
#     print(f"Food eaten: {food_eaten}")
# elif is_out:
#     print(f"Game over!")
#     print(f"Food eaten: {food_eaten}")
#
# [print(''.join(i)) for i in whole_matrix]

# 03. List Manipulator
# from collections import deque
#
#
# def list_manipulator(_list_of_numbers, _add_remove, _begin_end, *args):
#     if _add_remove == "add":
#         if _begin_end == "beginning":
#             return list(args) + _list_of_numbers
#         else:
#             return _list_of_numbers + list(args)
#     else:
#         _list_of_numbers = deque(_list_of_numbers)
#         _remove_count = args[0] if args else 1
#         fn = _list_of_numbers.popleft if _begin_end == "beginning" else _list_of_numbers.pop
#
#         for _ in range(_remove_count):
#             fn()
#
#         return list(_list_of_numbers)
#
#
# print(list_manipulator([1, 2, 3], "remove", "end"))
# print(list_manipulator([1, 2, 3], "remove", "beginning"))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20))
# print(list_manipulator([1, 2, 3], "add", "end", 30))
# print(list_manipulator([1, 2, 3], "remove", "end", 2))
# print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
