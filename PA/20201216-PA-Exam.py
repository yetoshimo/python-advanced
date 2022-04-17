# Problem 1
# from collections import deque
#
# males = [int(i) for i in input().split()]  # stack
# females = deque([int(i) for i in input().split()])  # queue
# matches = 0
#
# while males and females:
#
#     m_try = males[-1]
#     f_try = females[0]
#
#     if m_try <= 0:
#         males.pop()
#
#     elif f_try <= 0:
#         females.popleft()
#
#     # TODO - Special case - if someone’s value divisible by 25 without remainder
#     elif m_try % 25 == 0:
#         males.pop()  # TODO - you should remove him/her
#         males.pop()  # TODO - and the next person of the same gender.
#
#     # TODO - Special case - if someone’s value divisible by 25 without remainder
#     elif f_try % 25 == 0:
#         females.popleft()  # TODO - you should remove him/her
#         females.popleft()  # TODO - and the next person of the same gender.
#
#     elif m_try == f_try:
#         males.pop()
#         females.popleft()
#         matches += 1
#
#     else:
#         females.popleft()
#         males[-1] -= 2
#
# print(f"Matches: {matches}")
#
# if males:
#     print(f"Males left: {', '.join([str(i) for i in reversed(males)])}")
# else:
#     print(f"Males left: none")
#
# if females:
#     print(f"Females left: {', '.join(str(i) for i in females)}")
# else:
#     print(f"Females left: none")

# Problem 2
# from collections import deque
#
# string_to_add = input()
# size_of_field = int(input())
#
#
# def find_player(_whole_matrix):
#     for _row_index, _row in enumerate(_whole_matrix):
#         for _column_index, _column in enumerate(_row):
#             if _column == "P":
#                 return _row_index, _column_index
#
#
# def move(_next_row, _next_column, _last_row, _last_column, _whole_matrix, _string):
#     _whole_matrix[_last_row][_last_column] = "-"
#     if 0 <= _next_row < size_of_field and 0 <= _next_column < size_of_field:
#         if _whole_matrix[_next_row][_next_column] != "-":
#             _string += _whole_matrix[_next_row][_next_column]
#             _whole_matrix[_next_row][_next_column] = "P"
#             return _next_row, _next_column, _string
#         return _next_row, _next_column, _string
#     if _string:
#         _string = _string[:-1]
#     _whole_matrix[_last_row][_last_column] = "P"
#     return _last_row, _last_column, _string
#
#
# whole_matrix = [[x for x in list(input())] for _ in range(size_of_field)]
#
# last_row, last_column = find_player(whole_matrix)
#
#
# _commands = deque([input() for _ in range(int(input()))])
#
# while _commands:
#
#     next_command = _commands.popleft()
#
#     if next_command == "down":
#         next_row = last_row + 1
#         next_column = last_column
#         last_row, last_column, string_to_add = move(next_row, next_column, last_row, last_column, whole_matrix, string_to_add)
#
#     if next_command == "right":
#         next_row = last_row
#         next_column = last_column + 1
#         last_row, last_column, string_to_add = move(next_row, next_column, last_row, last_column, whole_matrix, string_to_add)
#
#     if next_command == "up":
#         next_row = last_row - 1
#         next_column = last_column
#         last_row, last_column, string_to_add = move(next_row, next_column, last_row, last_column, whole_matrix, string_to_add)
#
#     if next_command == "left":
#         next_row = last_row
#         next_column = last_column - 1
#         last_row, last_column, string_to_add = move(next_row, next_column, last_row, last_column, whole_matrix, string_to_add)
#
#
# print(string_to_add)
# [print(''.join(row)) for row in whole_matrix]

# Problem 3
# def get_magic_triangle(n: int):
#
#     triangle = [[1 for i in range(x)] for x in range(1, n + 1)]
#
#     if n == 2:
#         return triangle
#
#     for row in range(2, n):
#
#         triangle[row][0] = 1
#         triangle[row][-1] = 1
#
#         for column in range(1, row):
#
#             triangle[row][column] = triangle[row - 1][column - 1] + triangle[row - 1][column]
#
#     return triangle
