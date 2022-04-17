# 01. Scheduling
# from collections import deque
#
# jobs_as_integers = [int(i) for i in input().split(", ")]
#
# jobs_as_integers_indexes = [i for i in range(len(jobs_as_integers))]
#
# job_cycles = list(zip(jobs_as_integers, jobs_as_integers_indexes))
#
# index_of_the_job = int(input())
#
# sorted_jobs_as_integers = deque(sorted(job_cycles, key=lambda kv: kv[0]))
#
# total_cycles = 0
#
# for i in range(len(jobs_as_integers)):
#     _next_cycle = sorted_jobs_as_integers.popleft()
#     if _next_cycle[0] != jobs_as_integers[index_of_the_job]:
#         total_cycles += _next_cycle[0]
#     elif _next_cycle[0] == jobs_as_integers[index_of_the_job] and _next_cycle[1] != index_of_the_job:
#         total_cycles += _next_cycle[0]
#     else:
#         total_cycles += _next_cycle[0]
#         break
#
# print(total_cycles)

# 02. Checkmate
# def find_king():
#     for row in whole_matrix:
#         for column in row:
#             if column == "K":
#                 _king_row = whole_matrix.index(row)
#                 _king_column = row.index(column)
#                 return _king_row, _king_column
#
#
# def find_queens():
#     _queens = []
#     for row in whole_matrix:
#         for column in row:
#             if column == "Q":
#                 _queens.append((whole_matrix.index(row), row.index(column)))
#     return _queens
#
#
# def go_right(_next_row, _next_column):
#     _matching_queens = []
#     while 0 <= _next_row < 8 and 0 <= _next_column < 8:
#         if whole_matrix[_next_row][_next_column] == "Q":
#             _matching_queens.append([_next_row, _next_column])
#         _next_column += 1
#
#     if _matching_queens:
#         capture_queens.append(_matching_queens[0])
#
#     return capture_queens
#
#
# def go_left(_next_row, _next_column):
#     _matching_queens = []
#     while 0 <= _next_row < 8 and 0 <= _next_column < 8:
#         if whole_matrix[_next_row][_next_column] == "Q":
#             _matching_queens.append([_next_row, _next_column])
#         _next_column -= 1
#
#     if _matching_queens:
#         capture_queens.append(_matching_queens[0])
#
#     return capture_queens
#
#
# def go_up(_next_row, _next_column):
#     _matching_queens = []
#     while 0 <= _next_row < 8 and 0 <= _next_column < 8:
#         if whole_matrix[_next_row][_next_column] == "Q":
#             _matching_queens.append([_next_row, _next_column])
#         _next_row -= 1
#
#     if _matching_queens:
#         capture_queens.append(_matching_queens[0])
#
#     return capture_queens
#
#
# def go_down(_next_row, _next_column):
#     _matching_queens = []
#     while 0 <= _next_row < 8 and 0 <= _next_column < 8:
#         if whole_matrix[_next_row][_next_column] == "Q":
#             _matching_queens.append([_next_row, _next_column])
#         _next_row += 1
#
#     if _matching_queens:
#         capture_queens.append(_matching_queens[0])
#
#     return capture_queens
#
#
# def go_first_diagonal(_king_row, _king_column):
#     _matching_queens = []
#     _next_row = _king_row
#     _next_column = _king_column
#     # GO UP LEFT
#     while 0 <= _next_row < 8 and 0 <= _next_column < 8:
#         if whole_matrix[_next_row][_next_column] == "Q":
#             _matching_queens.append([_next_row, _next_column])
#         _next_row -= 1
#         _next_column -= 1
#
#     if _matching_queens:
#         capture_queens.append(_matching_queens[0])
#
#     _matching_queens = []
#     _next_row = _king_row
#     _next_column = _king_column
#
#     # GO DOWN RIGHT
#
#     while 0 <= _next_row < 8 and 0 <= _next_column < 8:
#         if whole_matrix[_next_row][_next_column] == "Q":
#             _matching_queens.append([_next_row, _next_column])
#         _next_row += 1
#         _next_column += 1
#
#     if _matching_queens:
#         capture_queens.append(_matching_queens[0])
#
#     return capture_queens
#
#
# def go_second_diagonal(_king_row, _king_column):
#     _matching_queens = []
#     _next_row = _king_row
#     _next_column = _king_column
#     # GO UP RIGHT
#     while 0 <= _next_row < 8 and 0 <= _next_column < 8:
#         if whole_matrix[_next_row][_next_column] == "Q":
#             _matching_queens.append([_next_row, _next_column])
#         _next_row -= 1
#         _next_column += 1
#
#     if _matching_queens:
#         capture_queens.append(_matching_queens[0])
#
#     _matching_queens = []
#     _next_row = _king_row
#     _next_column = _king_column
#
#     # GO DOWN LEFT
#
#     while 0 <= _next_row < 8 and 0 <= _next_column < 8:
#         if whole_matrix[_next_row][_next_column] == "Q":
#             _matching_queens.append([_next_row, _next_column])
#         _next_row += 1
#         _next_column -= 1
#
#     if _matching_queens:
#         capture_queens.append(_matching_queens[0])
#
#     return capture_queens
#
#
# whole_matrix = [[x for x in input().split()] for _ in range(8)]
#
# queen_coordinates = find_queens()
# king_row, king_column = find_king()
#
# capture_queens = []
#
# go_right(king_row, king_column + 1)
#
# go_left(king_row, king_column - 1)
#
# go_up(king_row - 1, king_column)
#
# go_down(king_row + 1, king_column)
#
# go_first_diagonal(king_row, king_column)
#
# go_second_diagonal(king_row, king_column)
#
# if capture_queens:
#     print(*capture_queens, sep='\n')
# else:
#     print(f"The king is safe!")

# 03. List Pureness
# def best_list_pureness(list_of_numbers: list, number_k: int):
#     _best_pureness = [0, 0]
#     _new_pureness = 0
#     _rotation_counter = 0
#     for i in range(number_k + 1):
#         for j in list_of_numbers:
#             _new_pureness += j * list_of_numbers.index(j)
#         if _new_pureness > _best_pureness[0]:
#             _best_pureness = (_new_pureness, _rotation_counter)
#         _new_pureness = 0
#         _rotate_number = list_of_numbers.pop()
#         list_of_numbers.insert(0, _rotate_number)
#         _rotation_counter += 1
#     return f"Best pureness {_best_pureness[0]} after {_best_pureness[1]} rotations"


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)
