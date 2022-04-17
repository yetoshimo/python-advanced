# 01. Sum Matrix Elements
# matrix_size = input().split(", ")
# row = int(matrix_size[0])
# column = int(matrix_size[1])
# whole_matrix = []
# for i in range(row):
#     single_row = [int(j) for j in input().split(", ")]
#     whole_matrix.append(single_row)
#
# matrix_sum = 0
# for k in whole_matrix:
#     matrix_sum += sum(k)
#
# print(matrix_sum)
# print(whole_matrix)

# 02. Sum Matrix Columns
# matrix_size = input().split(", ")
# row = int(matrix_size[0])
# column = int(matrix_size[1])
# whole_matrix = []
#
# for i in range(row):
#     single_row = [int(j) for j in input().split(" ")]
#     whole_matrix.append(single_row)
#
# column_sum = 0
#
# for i in range(column):
#     for j in range(row):
#         column_sum += whole_matrix[j][i]
#     print(column_sum)
#     column_sum = 0

# 03. Primary Diagonal
# matrix_size = int(input())
# row = matrix_size
# column = matrix_size
#
# whole_matrix = []
#
# primary_diagonal = 0
#
# for i in range(row):
#     single_row = [int(j) for j in input().split(" ")]
#     whole_matrix.append(single_row)
#
# for i in range(matrix_size):
#     primary_diagonal += whole_matrix[i][i]
#
# print(primary_diagonal)

# 04. Symbol in Matrix
# matrix_size = int(input())
# row = matrix_size
# column = matrix_size
#
# whole_matrix = []
#
# for i in range(row):
#     single_row = list(input())
#     whole_matrix.append(single_row)
#
# symbol_entry = input()
#
# is_found = False
#
# for i in range(row):
#     if not is_found:
#         for j in range(column):
#             if whole_matrix[i][j] == symbol_entry:
#                 print(f"{i, j}")
#                 is_found = True
#                 break
#
# if not is_found:
#     print(f"{symbol_entry} does not occur in the matrix")

# 05. Square with Maximum Sum
# def extract_sub_matrix(x_value, y_value):
#     for x in range(x_value, x_value + 2):
#         for y in range(y_value, y_value + 2):
#             sub_matrix.append(whole_matrix[x][y])
#     return sub_matrix
#
#
# matrix_size = input().split(", ")
# row = int(matrix_size[0])
# column = int(matrix_size[1])
# whole_matrix = []
#
# sub_matrix = []
#
# max_matrix = []
# max_value = 0
#
# for i in range(row):
#     single_row = [int(j) for j in input().split(", ")]
#     whole_matrix.append(single_row)
#
# for i in range(row - 1):
#     for j in range(column - 1):
#         temp_matrix = extract_sub_matrix(i, j)
#         temp_value = sum(temp_matrix)
#         if temp_value > max_value:
#             max_value = temp_value
#             max_matrix = temp_matrix
#         sub_matrix = []
#
# print(' '.join(map(str, max_matrix[:2])))
# print(' '.join(map(str, max_matrix[2:])))
# print(sum(max_matrix))
