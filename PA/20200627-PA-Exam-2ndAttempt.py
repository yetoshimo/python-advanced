# 01. Bombs
# from collections import deque
#
#
# bomb_effects = deque([int(i) for i in input().split(', ')])  # queue
#
# bomb_casings = [int(i) for i in input().split(', ')]  # stack
#
# bombs = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
#
# bomb_pouch = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
#
# has_all = False
#
# while bomb_effects and bomb_casings and not has_all:
#
#     next_bomb_effect = bomb_effects.popleft()
#     next_bomb_casing = bomb_casings.pop()
#
#     if next_bomb_effect + next_bomb_casing in bombs:
#         bomb_pouch[bombs[next_bomb_effect + next_bomb_casing]] += 1
#
#         if bomb_pouch['Datura Bombs'] >= 3 and \
#                 bomb_pouch['Cherry Bombs'] >= 3 and \
#                 bomb_pouch['Smoke Decoy Bombs'] >= 3:
#             has_all = True
#
#     else:
#         bomb_effects.appendleft(next_bomb_effect)
#         bomb_casings.append(next_bomb_casing - 5)
#
#     if has_all:
#         break
#
#
# if has_all:
#     print(f"Bene! You have successfully filled the bomb pouch!")
# else:
#     print(f"You don't have enough materials to fill the bomb pouch.")
#
# if bomb_effects:
#     print(f"Bomb Effects: {', '.join([str(i) for i in bomb_effects])}")
# else:
#     print(f"Bomb Effects: empty")
#
# if bomb_casings:
#     print(f"Bomb Casings: {', '.join([str(i) for i in bomb_casings])}")
# else:
#     print(f"Bomb Casings: empty")
#
# for bomb, number in sorted(bomb_pouch.items()):
#     print(f"{bomb}: {number}")

# 02. Snake
# def find_snake(_matrix):
#     for row_number, row in enumerate(_matrix):
#         for column_number, column in enumerate(row):
#             if column == "S":
#                 return row_number, column_number
#
#
# def find_burrows(_matrix):
#     _burrows = []
#     for row_number, row in enumerate(_matrix):
#         for column_number, column in enumerate(row):
#             if column == "B":
#                 _burrows.append((row_number, column_number))
#     return _burrows
#
#
# def find_food(_matrix):
#     _food = []
#     for row_number, row in enumerate(_matrix):
#         for column_number, column in enumerate(row):
#             if column == "*":
#                 _food.append((row_number, column_number))
#     return _food
#
#
# def move_snake(_current_row, _current_column, _next_row, _next_column, _matrix, _matrix_size, _food):
#     _is_out = False
#     _matrix[_current_row][_current_column] = "."
#     if 0 <= _next_row < _matrix_size and 0 <= _next_column < _matrix_size:
#         if _matrix[_next_row][_next_column] == "*":
#             _matrix[_next_row][_next_column] = "S"
#             _food += 1
#         elif _matrix[_next_row][_next_column] == "-":
#             _matrix[_next_row][_next_column] = "S"
#         elif _matrix[_next_row][_next_column] == "B":
#             _matrix[_next_row][_next_column] = "."
#             _burrows = find_burrows(_matrix)
#             _next_row, _next_column = _burrows[0]
#             _matrix[_next_row][_next_column] = "S"
#         else:
#             _matrix[_next_row][_next_column] = "S"
#
#     else:
#         _is_out = True
#
#     return _next_row, _next_column, _matrix, _is_out, _food
#
#
# matrix_size = int(input())
# whole_matrix = [[i for i in input()] for _ in range(matrix_size)]
#
# food_eaten = 0
#
# current_row, current_column = find_snake(whole_matrix)
# food = find_food(whole_matrix)
# next_row = None
# next_column = None
# is_out = False
#
# while food_eaten < 10 and not is_out:
#
#     command = input()
#
#     if command == "left":
#         next_row = current_row
#         next_column = current_column - 1
#     elif command == "right":
#         next_row = current_row
#         next_column = current_column + 1
#     elif command == "up":
#         next_row = current_row - 1
#         next_column = current_column
#     elif command == "down":
#         next_row = current_row + 1
#         next_column = current_column
#
#     current_row, current_column, whole_matrix, is_out, food_eaten = move_snake(current_row, current_column, next_row, next_column, whole_matrix, matrix_size, food_eaten)
#
#     if is_out:
#         break
#
# if is_out:
#     print(f"Game over!")
# else:
#     print(f"You won! You fed the snake.")
# print(f"Food eaten: {food_eaten}")
# [print(''.join(i)) for i in whole_matrix]

# 03. List Manipulator
# def list_manipulator(numbers: list, first: str, second: str, *args):
#
#     if first == "add":
#         if second == "beginning":
#             return list(args) + numbers
#         elif second == "end":
#             return numbers + list(args)
#     elif first == "remove":
#         if second == "beginning":
#             if args:
#                 return numbers[args[0]:]
#             else:
#                 return numbers[1:]
#         elif second == "end":
#             if args:
#                 return numbers[:-args[0]]
#             else:
#                 return numbers[:-1]
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
