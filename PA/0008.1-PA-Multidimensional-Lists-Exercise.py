# 01. Diagonal Difference
# matrix_size = int(input())
# row = matrix_size
# column = matrix_size
#
# whole_matrix = []
#
# primary_diagonal = 0
# secondary_diagonal = 0
#
# for i in range(row):
#     single_row = [int(j) for j in input().split(" ")]
#     whole_matrix.append(single_row)
#
# for i in range(matrix_size):
#     primary_diagonal += whole_matrix[i][i]
#
# y = matrix_size - 1
#
# for x in range(matrix_size):
#     secondary_diagonal += whole_matrix[x][y]
#     y -= 1
#
# print(abs(primary_diagonal - secondary_diagonal))

# 02. 2x2 Squares in Matrix
# def extract_sub_matrix(x_value, y_value):
#     sub_matrix = []
#     for x in range(x_value, x_value + 2):
#         for y in range(y_value, y_value + 2):
#             sub_matrix.append(whole_matrix[x][y])
#     return sub_matrix
#
#
# matrix_size = input().split(" ")
# row = int(matrix_size[0])
# column = int(matrix_size[1])
# whole_matrix = []
#
# sub_matrix = []
# square_count = 0
#
# for i in range(row):
#     single_row = [j for j in input().split(" ")]
#     whole_matrix.append(single_row)
#
# for i in range(row - 1):
#     for j in range(column - 1):
#         temp_matrix = extract_sub_matrix(i, j)
#
#         if all(element == temp_matrix[0] for element in temp_matrix):
#             square_count += 1
#
# print(square_count)

# 03. Maximum Sum
# def extract_sub_matrix(x_value, y_value):
#     for x in range(x_value, x_value + 3):
#         for y in range(y_value, y_value + 3):
#             sub_matrix.append(whole_matrix[x][y])
#     return sub_matrix
#
#
# matrix_size = input().split(" ")
# row = int(matrix_size[0])
# column = int(matrix_size[1])
# whole_matrix = []
#
# sub_matrix = []
#
# max_matrix = None
# max_value = None
#
# for i in range(row):
#     single_row = [int(j) for j in input().split()]
#     whole_matrix.append(single_row)
#
# for i in range(row - 2):
#     for j in range(column - 2):
#         temp_matrix = extract_sub_matrix(i, j)
#         temp_value = sum(temp_matrix)
#
#         if max_value:
#             if temp_value > max_value:
#                 max_value = temp_value
#                 max_matrix = temp_matrix
#         else:
#             max_value = temp_value
#             max_matrix = temp_matrix
#         sub_matrix = []
#
# if max_matrix:
#     print(f"Sum = {max_value}")
#     print(' '.join(map(str, max_matrix[:3])))
#     print(' '.join(map(str, max_matrix[3:6])))
#     print(' '.join(map(str, max_matrix[6:])))
# else:
#     print(f"Sum = {max_value}")
#     [print(' '.join(map(str, row))) for row in whole_matrix]

# 04. Matrix Shuffling
# matrix_size = input().split(" ")
# row = int(matrix_size[0])
# column = int(matrix_size[1])
#
# whole_matrix = []
#
# for i in range(row):
#     single_row = [j for j in input().split()]
#     whole_matrix.append(single_row)
#
# input_command = input()
#
# is_correct = True
#
# while input_command != "END":
#     is_correct = True
#     if "swap" in input_command and len(input_command.split(" ")) == 5:
#         row1 = int(input_command.split(" ")[1])
#         col1 = int(input_command.split(" ")[2])
#         row2 = int(input_command.split(" ")[3])
#         col2 = int(input_command.split(" ")[4])
#         if row1 > row or row2 > row or col1 > column or col2 > column:
#             print(f"Invalid input!")
#             is_correct = False
#             pass
#         if is_correct:
#             temp_value = whole_matrix[row1][col1]
#             whole_matrix[row1][col1] = whole_matrix[row2][col2]
#             whole_matrix[row2][col2] = temp_value
#             [print(' '.join(map(str, row))) for row in whole_matrix]
#     else:
#         print(f"Invalid input!")
#
#     input_command = input()

# 05. Snake Moves
# matrix_size = input().split(" ")
# row = int(matrix_size[0])
# column = int(matrix_size[1])
#
# snake = input()
#
# modulo = len(snake)
#
# whole_matrix = []
#
# index_counter = 0
#
# row_value = ""
#
# for i in range(row):
#     if i % 2 == 0:
#         while len(row_value) < column:
#             row_value += snake[index_counter % modulo]
#             index_counter += 1
#         whole_matrix.append(row_value)
#         row_value = ""
#     else:
#         while len(row_value) < column:
#             row_value += snake[index_counter % modulo]
#             index_counter += 1
#         whole_matrix.append(''.join(list(reversed(row_value))))
#         row_value = ""
#
# [print(''.join(map(str, row))) for row in whole_matrix]

# 06. Knight Game
# matrix_size = int(input())
# row = matrix_size
# column = matrix_size
#
# whole_matrix = []
#
# for i in range(row):
#     whole_matrix.append(list(input()))
#
# to_be_removed = {}
#
#
# def k_check(target_row, target_column, current_row, current_column):
#     if 0 <= target_row < row and 0 <= target_column < column:
#         if whole_matrix[target_row][target_column] == "K":
#             if (current_row, current_column) not in to_be_removed:
#                 to_be_removed[(current_row, current_column)] = [target_row, target_column]
#             else:
#                 to_be_removed[(current_row, current_column)].append(target_row)
#                 to_be_removed[(current_row, current_column)].append(target_column)
#     return
#
#
# def strongest_knight():
#     if to_be_removed:
#         return max(to_be_removed, key=lambda kv: len(to_be_removed[kv]))
#     else:
#         return None
#
#
# knight_moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
#
# strongest_exists = True
#
# knight_count = 0
#
# while strongest_exists:
#     for row_number in range(row):
#         for column_number in range(column):
#             if whole_matrix[row_number][column_number] == "K":
#                 for (row_move, column_move) in knight_moves:
#                     k_check(row_number + row_move, column_number + column_move, row_number, column_number)
#
#     strongest_knight_check = strongest_knight()
#
#     if strongest_knight_check:
#         whole_matrix[strongest_knight_check[0]][strongest_knight_check[1]] = "0"
#         to_be_removed = {}
#         knight_count += 1
#     else:
#         strongest_exists = False
#
# print(knight_count)

# 07. Bombs
# from collections import deque
#
# matrix_size = int(input())
# row = matrix_size
# column = matrix_size
#
# whole_matrix = []
#
# for i in range(row):
#     whole_matrix.append([int(i) for i in input().split(" ")])
#
# bomb_coordinates = deque(input().split(" "))
#
# collateral_pieces = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
#
# collateral_row = 0
# collateral_column = 0
#
# while bomb_coordinates:
#     to_explode = bomb_coordinates.popleft().split(",")
#
#     explosion_row = int(to_explode[0])
#     explosion_column = int(to_explode[1])
#
#     target_bomb_value = whole_matrix[explosion_row][explosion_column]
#
#     if target_bomb_value > 0:
#         whole_matrix[explosion_row][explosion_column] = 0
#
#         for around_piece in collateral_pieces:
#             collateral_row = explosion_row + int(around_piece[0])
#             collateral_column = explosion_column + int(around_piece[1])
#
#             if 0 <= collateral_row < row and 0 <= collateral_column < column:
#                 if whole_matrix[collateral_row][collateral_column] > 0:
#                     whole_matrix[collateral_row][collateral_column] -= target_bomb_value
#
# alive_cells = 0
# sum_of_cells = 0
#
# for rows in whole_matrix:
#     for element in rows:
#         if element > 0:
#             alive_cells += 1
#             sum_of_cells += element
#
# print(f"Alive cells: {alive_cells}")
# print(f"Sum: {sum_of_cells}")
# [print(' '.join(map(str, row))) for row in whole_matrix]

# 08. Miner
# from collections import deque
#
# matrix_size = int(input())
# row = matrix_size
# column = matrix_size
#
# commands = deque(input().split(" "))
#
# whole_matrix = []
#
# for i in range(row):
#     whole_matrix.append([i for i in input().split()])
#
#
# def find_start(x, y):
#     for i in whole_matrix:
#         for j in i:
#             if j == "s":
#                 x = whole_matrix.index(i)
#                 y = i.index(j)
#                 whole_matrix[x][y] = "*"
#                 break
#     return x, y
#
#
# def boundary_check(target_row, target_column):
#     if 0 <= target_row < row and 0 <= target_column < column:
#         return True
#     else:
#         return False
#
#
# def current_position_check(position_row, position_column):
#     if whole_matrix[current_row][current_column] == "e":
#         print(f"Game over! {current_row, current_column}")
#         return False
#     elif whole_matrix[current_row][current_column] == "k":
#         whole_matrix[current_row][current_column] = "*"
#         return True
#     elif whole_matrix[current_row][current_column] == "*":
#         return True
#
#
# current_row = 0
# current_column = 0
# to_go_row = 0
# to_go_column = 0
#
# start_row, start_column = find_start(current_row, current_column)
#
# current_row = start_row
# current_column = start_column
#
# is_ended = False
#
# while commands:
#     to_move = commands.popleft()
#
#     if to_move == "up":
#         to_go_row = current_row - 1
#         to_go_column = current_column
#
#         if boundary_check(to_go_row, to_go_column):
#             current_row = to_go_row
#             current_column = to_go_column
#
#             if current_position_check(current_row, current_column):
#                 continue
#             else:
#                 is_ended = True
#                 break
#
#     if to_move == "down":
#         to_go_row = current_row + 1
#         to_go_column = current_column
#
#         if boundary_check(to_go_row, to_go_column):
#             current_row = to_go_row
#             current_column = to_go_column
#
#             if current_position_check(current_row, current_column):
#                 continue
#             else:
#                 is_ended = True
#                 break
#
#     if to_move == "left":
#         to_go_row = current_row
#         to_go_column = current_column - 1
#
#         if boundary_check(to_go_row, to_go_column):
#             current_row = to_go_row
#             current_column = to_go_column
#
#             if current_position_check(current_row, current_column):
#                 continue
#             else:
#                 is_ended = True
#                 break
#
#     if to_move == "right":
#         to_go_row = current_row
#         to_go_column = current_column + 1
#
#         if boundary_check(to_go_row, to_go_column):
#             current_row = to_go_row
#             current_column = to_go_column
#
#             if current_position_check(current_row, current_column):
#                 continue
#             else:
#                 is_ended = True
#                 break
#
# coal_count = 0
#
# if not is_ended:
#     for i in whole_matrix:
#         for j in i:
#             if j == "k":
#                 coal_count += 1
#
# if coal_count:
#     print(f"{coal_count} coals left. {current_row, current_column}")
# else:
#     print(f"You collected all coals! {current_row, current_column}")

# TODO - updated new question
# from collections import deque
#
# matrix_size = int(input())
# commands = deque(input().split(" "))
#
# whole_matrix = []
#
# for _ in range(matrix_size):
#     whole_matrix.append([i for i in input().split()])
#
#
# def find_start(_whole_matrix):
#     x = None
#     y = None
#     for i in _whole_matrix:
#         for j in i:
#             if j == "s":
#                 x = _whole_matrix.index(i)
#                 y = i.index(j)
#                 break
#     return x, y
#
#
# def coal_counter(_whole_matrix):
#     _coal_count = 0
#     for i in _whole_matrix:
#         for j in i:
#             if j == "c":
#                 _coal_count += 1
#     return _coal_count
#
#
# def boundary_check(_next_row, _next_column, _matrix_size):
#     if 0 <= _next_row < _matrix_size and 0 <= _next_column < _matrix_size:
#         return True
#     else:
#         return False
#
#
# def move_to_next(_next_row, _next_column, _current_row, _current_column, _whole_matrix, _coal_count):
#     _is_ended = False
#     if _whole_matrix[_next_row][_next_column] == "e":
#         _is_ended = True
#         return _next_row, _next_column, _coal_count, _is_ended
#
#     if _whole_matrix[_next_row][_next_column] == "*":
#         return _next_row, _next_column, _coal_count, _is_ended
#
#     if _whole_matrix[_next_row][_next_column] == "c":
#         _coal_count -= 1
#         _whole_matrix[_next_row][_next_column] = "*"
#         return _next_row, _next_column, _coal_count, _is_ended
#
#
# current_row, current_column = find_start(whole_matrix)
# whole_matrix[current_row][current_column] = "*"
# coal_count = coal_counter(whole_matrix)
# next_row = None
# next_column = None
# is_ended = False
# collected_coal = 0
#
# while commands and not is_ended:
#     next_command = commands.popleft()
#
#     if next_command == "up":
#         next_row = current_row - 1
#         next_column = current_column
#
#     elif next_command == "down":
#         next_row = current_row + 1
#         next_column = current_column
#
#     elif next_command == "right":
#         next_row = current_row
#         next_column = current_column + 1
#
#     elif next_command == "left":
#         next_row = current_row
#         next_column = current_column - 1
#
#     if boundary_check(next_row, next_column, matrix_size):
#         current_row, current_column, coal_count, is_ended = \
#             move_to_next(next_row, next_column, current_row, current_column, whole_matrix, coal_count)
#
#     if is_ended:
#         break
#
# if coal_count == 0:
#     print(f"You collected all coals! ({current_row}, {current_column})")
# elif is_ended:
#     print(f"Game over! ({current_row}, {current_column})")
# else:
#     print(f"{coal_count} coals left. ({current_row}, {current_column})")


# 09. Radioactive Mutate Vampire Bunnies


# def find_player(matrix):
#     for y, row in enumerate(matrix):
#         for x, value in enumerate(row):
#             if value == "P":
#                 return x, y
#
#
# def find_bunnies(matrix):
#     bunnies = []
#     for y, row in enumerate(matrix):
#         for x, value in enumerate(row):
#             if value == "B":
#                 bunnies.append((x, y))
#     return bunnies
#
#
# n, m = [int(x) for x in input().split(' ')]
# lair = [list(input()) for _ in range(n)]
# directions = input()
# player_x, player_y = find_player(lair)
# bunny_multiplications_directions = [
#     (0, 1),
#     (0, -1),
#     (1, 0),
#     (-1, 0),
# ]
#
# last_player_x, last_player_y = None, None
#
# won = False
# lost = False
#
# for direction in directions:
#     lair[player_y][player_x] = '.'
#     last_player_x = player_x
#     last_player_y = player_y
#
#     if direction == 'U':
#         player_y -= 1
#     elif direction == 'D':
#         player_y += 1
#     elif direction == 'L':
#         player_x -= 1
#     elif direction == 'R':
#         player_x += 1
#
#     if player_x < 0 or player_x >= m or player_y >= n or player_y < 0:
#         won = True
#     else:
#         at_position = lair[player_y][player_x]
#         if at_position == 'B':
#             lost = True
#             last_player_x = player_x
#             last_player_y = player_y
#         else:
#             lair[player_y][player_x] = 'P'
#
#     for bunny_x, bunny_y in find_bunnies(lair):
#         for delta_x, delta_y in bunny_multiplications_directions:
#             new_bunny_x = bunny_x + delta_x
#             new_bunny_y = bunny_y + delta_y
#             if 0 <= new_bunny_x < m and 0 <= new_bunny_y < n:
#                 at_position = lair[new_bunny_y][new_bunny_x]
#                 lair[new_bunny_y][new_bunny_x] = 'B'
#                 if at_position == 'P':
#                     lost = True
#                     last_player_x = player_x
#                     last_player_y = player_y
#
#     if won:
#         break
#     if lost:
#         break
#
# for row in lair:
#     print(''.join(row))
#
# if won:
#     print(f'won: {last_player_y} {last_player_x}')
# elif lost:
#     print(f'dead: {last_player_y} {last_player_x}')
