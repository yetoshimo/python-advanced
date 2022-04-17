# Problem 1
# from collections import deque
#
# males = [int(i) for i in input().split()]
# females = deque([int(i) for i in input().split()])
#
# matches = 0
#
# while males and females:
#
#     next_male = males[-1]
#     next_female = females[0]
#
#     if next_female <= 0:
#         females.popleft()
#     elif next_male <= 0:
#         males.pop()
#     elif next_female % 25 == 0:
#         females.popleft()
#         females.popleft()
#     elif next_male % 25 == 0:
#         males.pop()
#         males.pop()
#     elif next_male == next_female:
#         males.pop()
#         females.popleft()
#         matches += 1
#     else:
#         females.popleft()
#         males[-1] -= 2
#
# print(f"Matches: {matches}")
# print(f"Males left: {', '.join([str(i) for i in males[::-1]]) if males else 'none'}")
# print(f"Females left: {', '.join([str(i) for i in females]) if females else 'none'}")

# Problem 2
# def find_player(_matrix):
#     for p_r, row in enumerate(_matrix):
#         for p_c, column in enumerate(row):
#             if column == "P":
#                 return p_r, p_c
#
#
# def move_player(_p_r, _p_c, _n_r, _n_c, _matrix, _size, _string):
#     if 0 <= _n_r < _size and 0 <= _n_c < _size:
#         _matrix[_p_r][_p_c] = "-"
#
#         if _matrix[_n_r][_n_c] != "-":
#             _string += _matrix[_n_r][_n_c]
#             _matrix[_n_r][_n_c] = "P"
#             _p_r = _n_r
#             _p_c = _n_c
#             return _p_r, _p_c, _matrix, _string
#         else:
#             _matrix[_n_r][_n_c] = "P"
#             _p_r = _n_r
#             _p_c = _n_c
#             return _p_r, _p_c, _matrix, _string
#
#     return _p_r, _p_c, _matrix, _string[:-1]
#
#
# given_string = input()
# matrix_size = int(input())
#
# whole_matrix = [list(input()) for _ in range(matrix_size)]
#
# p_row, p_column = find_player(whole_matrix)
#
# for _ in range(int(input())):
#
#     command = input()
#
#     if command == "up":
#         p_row, p_column, whole_matrix, given_string = move_player(p_row, p_column, p_row - 1, p_column, whole_matrix,
#                                                                   matrix_size, given_string)
#     elif command == "down":
#         p_row, p_column, whole_matrix, given_string = move_player(p_row, p_column, p_row + 1, p_column, whole_matrix,
#                                                                   matrix_size, given_string)
#     elif command == "right":
#         p_row, p_column, whole_matrix, given_string = move_player(p_row, p_column, p_row, p_column + 1, whole_matrix,
#                                                                   matrix_size, given_string)
#     elif command == "left":
#         p_row, p_column, whole_matrix, given_string = move_player(p_row, p_column, p_row, p_column - 1, whole_matrix,
#                                                                   matrix_size, given_string)
#
# print(given_string)
# [print(''.join(i)) for i in whole_matrix]

# # Problem 3
# # A O(n^2) time and O(n^2) extra
# # space method for Pascal's Triangle
# def get_magic_triangle(n: int):
#     # An auxiliary array to store
#     # generated pascal triangle values
#     arr = [[0 for x in range(n)]
#            for y in range(n)]
#
#     # Iterate through every line
#     # and print integer(s) in it
#     for line in range(0, n):
#
#         # Every line has number of
#         # integers equal to line number
#         for i in range(0, line + 1):
#
#             # First and last values
#             # in every row are 1
#             if i == 0 or i == line:
#                 arr[line][i] = 1
#                 print(arr[line][i], end=" ")
#
#             # Other values are sum of values
#             # just above and left of above
#             else:
#                 arr[line][i] = (arr[line - 1][i - 1] +
#                                 arr[line - 1][i])
#                 print(arr[line][i], end=" ")
#         print("\n", end="")

# def get_magic_triangle(n: int):
#     triangle = [[1 for i in range(x)] for x in range(1, n + 1)]
#
#     if n == 2:
#         return triangle
#
#     for row in range(2, n):
#
#         for column in range(1, row):
#
#             triangle[row][column] = triangle[row - 1][column - 1] + triangle[row - 1][column]
#
#     return triangle


# print(get_magic_triangle(5))
