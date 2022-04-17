# 01. Scheduling
# jobs = [int(i) for i in input().split(", ")]
#
# job_index = int(input())
#
# jobs_dict = {}
#
# for i in range(len(jobs)):
#     jobs_dict[i] = jobs[i]
#
# total_cycles = 0
#
# is_finished = False
#
# sorted_dict = {k: v for k, v in sorted(jobs_dict.items(), key=lambda kv: kv[1])}
#
# for key, value in sorted_dict.items():
#
#     if key != job_index:
#         total_cycles += value
#     else:
#         total_cycles += value
#         break
#
# print(total_cycles)

# 02. Checkmate
# def find_king(_matrix):
#     for row_i, row in enumerate(_matrix):
#         for col_i, column in enumerate(row):
#             if column == "K":
#                 return row_i, col_i
#
#
# # def find_queens(_matrix):
# #     _queens = []
# #     for row_i, row in enumerate(_matrix):
# #         for col_i, column in enumerate(row):
# #             if column == "Q":
# #                 _queens.append((row_i, col_i))
# #
# #     return _queens
#
#
# def check_right(_matrix, k_r, k_c, _queens: list):
#     while 0 <= k_c < 8:
#         if whole_matrix[k_r][k_c] == "Q":
#             _queens.append((k_r, k_c))
#             return _queens
#         k_c += 1
#     return _queens
#
#
# def check_left(_matrix, k_r, k_c, _queens: list):
#     while 0 <= k_c < 8:
#         if whole_matrix[k_r][k_c] == "Q":
#             _queens.append((k_r, k_c))
#             return _queens
#         k_c -= 1
#     return _queens
#
#
# def check_down(_matrix, k_r, k_c, _queens: list):
#     while 0 <= k_r < 8:
#         if whole_matrix[k_r][k_c] == "Q":
#             _queens.append((k_r, k_c))
#             return _queens
#         k_r += 1
#     return _queens
#
#
# def check_up(_matrix, k_r, k_c, _queens: list):
#     while 0 <= k_r < 8:
#         if whole_matrix[k_r][k_c] == "Q":
#             _queens.append((k_r, k_c))
#             return _queens
#         k_r -= 1
#     return _queens
#
#
# def check_right_up_diagonal(_matrix, k_r, k_c, _queens: list):
#     while 0 <= k_r < 8 and 0 <= k_c < 8:
#         if whole_matrix[k_r][k_c] == "Q":
#             _queens.append((k_r, k_c))
#             return _queens
#         k_r -= 1
#         k_c += 1
#     return _queens
#
#
# def check_left_up_diagonal(_matrix, k_r, k_c, _queens: list):
#     while 0 <= k_r < 8 and 0 <= k_c < 8:
#         if whole_matrix[k_r][k_c] == "Q":
#             _queens.append((k_r, k_c))
#             return _queens
#         k_r -= 1
#         k_c -= 1
#     return _queens
#
#
# def check_right_down_diagonal(_matrix, k_r, k_c, _queens: list):
#     while 0 <= k_r < 8 and 0 <= k_c < 8:
#         if whole_matrix[k_r][k_c] == "Q":
#             _queens.append((k_r, k_c))
#             return _queens
#         k_r += 1
#         k_c += 1
#     return _queens
#
#
# def check_left_down_diagonal(_matrix, k_r, k_c, _queens: list):
#     while 0 <= k_r < 8 and 0 <= k_c < 8:
#         if whole_matrix[k_r][k_c] == "Q":
#             _queens.append((k_r, k_c))
#             return _queens
#         k_r += 1
#         k_c -= 1
#     return _queens
#
#
# whole_matrix = [input().split() for i in range(8)]
#
# is_safe = False
#
# k_row, k_column = find_king(whole_matrix)
#
# queens = []
#
# queens = check_right(whole_matrix, k_row, k_column, queens)
# queens = check_left(whole_matrix, k_row, k_column, queens)
# queens = check_up(whole_matrix, k_row, k_column, queens)
# queens = check_down(whole_matrix, k_row, k_column, queens)
# queens = check_left_down_diagonal(whole_matrix, k_row, k_column, queens)
# queens = check_left_up_diagonal(whole_matrix, k_row, k_column, queens)
# queens = check_right_down_diagonal(whole_matrix, k_row, k_column, queens)
# queens = check_right_up_diagonal(whole_matrix, k_row, k_column, queens)
#
# if queens:
#     [print(list(i)) for i in queens]
# else:
#     print(f"The king is safe!")

# 03. List Pureness
# from collections import deque
#
#
# def best_list_pureness(list_of_numbers: list, number_k: int):
#     list_of_numbers = deque(list_of_numbers)
#
#     max_pureness = 0
#     turns = 0
#
#     for i in range(number_k + 1):
#
#         current_pureness = sum([index * number for index, number in enumerate(list_of_numbers)])
#
#         if current_pureness > max_pureness:
#             max_pureness = current_pureness
#             turns = i
#
#         list_of_numbers.rotate()
#
#     return f"Best pureness {max_pureness} after {turns} rotations"


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
