# 01. ASCII Values
# input_string = input().split(", ")
#
# print({item: ord(item) for item in input_string})

# 02. No Vowels
# input_string = input()
#
# print(''.join([char for char in input_string if char.lower() not in ("a", "o", "u", "e", "i")]))

# 03. Even Matrix
# whole_matrix = [list(map(int, input().split(", "))) for _ in range(int(input()))]
# even_matrix = [[item for item in whole_matrix[row] if item % 2 == 0] for row in range(len(whole_matrix))]
#
# print(even_matrix)

# 04. Flattening Matrix
# whole_matrix = [list(map(int, input().split(", "))) for _ in range(int(input()))]
# print([item for row in whole_matrix for item in row])

# 05. Filter Numbers
# start = int(input())
# end = int(input()) + 1
# print(list({item for item in range(int(input()), int(input()) + 1) for division in range(2, 11) if item % division == 0}))
