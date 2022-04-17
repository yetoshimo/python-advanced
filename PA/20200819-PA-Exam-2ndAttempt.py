# 01. Taxi Express
# from collections import deque
#
# list_of_customers = deque([int(i) for i in input().split(", ")])  # queue
# list_of_taxis = [int(i) for i in input().split(", ")]  # stack
#
# total_time = 0
#
# while list_of_customers and list_of_taxis:
#
#     next_customer = list_of_customers.popleft()
#     next_taxi = list_of_taxis.pop()
#
#     if next_taxi >= next_customer:
#         total_time += next_customer
#     else:
#         list_of_customers.appendleft(next_customer)
#
# if not list_of_customers:
#     print(f"All customers were driven to their destinations")
#     print(f"Total time: {total_time} minutes")
# else:
#     print(f"Not all customers were driven to their destinations")
#     print(f"Customers left: {', '.join([str(i) for i in list_of_customers])}")

# 02. Minesweeper Generator
# from re import findall
#
#
# matrix_size = int(input())
# number_of_bombs = int(input())
# bombs = []
# TODO - number can be 2 digits
# for _ in range(number_of_bombs):
#     b_x, b_y = [int(i) for i in findall(r"\d+", input())]
#     bombs.append([b_x, b_y])
#
# whole_matrix = [[0 for i in range(matrix_size)] for _ in range(matrix_size)]
#
# bomb_adjacent = [
#     [0, -1],  # left
#     [0, 1],  # right
#     [-1, 0],  # up
#     [1, 0],  # down
#     [-1, -1],  # up left
#     [-1, 1],  # up right
#     [1, -1],  # down left
#     [1, 1]  # down right
# ]
#
#
# def place_numbers(_b_row, _b_column, _numbers, _matrix, _size):
#     for i in _numbers:
#         next_row = _b_row + i[0]
#         next_column = _b_column + i[1]
#
#         if 0 <= next_row < _size and 0 <= next_column < _size:
#             if _matrix[next_row][next_column] != "*":
#                 _matrix[next_row][next_column] += 1
#
#     return _matrix
#
#
# for (b_x, b_y) in bombs:
#     whole_matrix[b_x][b_y] = "*"
#
#
# while bombs:
#
#     next_bomb = list(bombs.pop())
#
#     b_row, b_column = next_bomb[0], next_bomb[1]
#
#     whole_matrix = place_numbers(b_row, b_column, bomb_adjacent, whole_matrix, matrix_size)
#
#
# [print(*row) for row in whole_matrix]

# 03. Numbers Search
# def find_missing(lst):
#     return sorted(set(range(lst[0], lst[-1])) - set(lst))
#
#
# def numbers_searching(*args):
#     missing_number = find_missing(sorted(args))[-1]
#     set_numbers = {item for item in args}
#     duplicates = []
#     for number in set_numbers:
#         if args.count(number) > 1:
#             duplicates.append(number)
#     return [missing_number, sorted(duplicates)]
#
#
# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
