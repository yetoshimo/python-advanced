# 01. Absolute Values
# print([abs(float(i)) for i in input().split()])

# 02. Rounding
# print([round(float(i)) for i in input().split()])

# 03. Multiplication Function
# from functools import reduce

# def multiply(*args):
#     result = 1
#     for element in args:
#         result *= element
#     return result
#
#
# multiply()


# def multiply(*args):
#     return reduce(lambda x, y: x * y, args)
#
#
# print(multiply(1, 4, 5))
# print(multiply(4, 5, 6, 1, 3))
# print(multiply(2, 0, 1000, 5000))

# 04. Operate
# from functools import reduce


# def operate(operator, *args):
#     return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)
#
#
# operator_mapper = {
#     "+": lambda x, y: x + y,
#     "-": lambda x, y: x - y,
#     "*": lambda x, y: x * y,
#     "/": lambda x, y: x / y
# }
#
#
# def operate(operator, *args):
#     return reduce(operator_mapper[operator], args)
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))

# 05. Person Info
# def get_info(name, age, town):
#     return f"This is {name} from {town} and he is {age} years old"

# 06. Character Combinations
# from itertools import permutations
#
#
# def character_permutation(text):
#     return permutations(text)
#
#
# [print(''.join(row)) for row in character_permutation(list(input()))]

# 07. Chairs
# from itertools import combinations
#
#
# def seating_plan(_names, _number_of_chairs):
#     return list(combinations(_names, _number_of_chairs))
#
#
# [print(', '.join(row)) for row in seating_plan([name for name in input().split(", ")], int(input()))]

# 08. Expressions
# def expressions(numbers, current_sum=0, expression=""):
#     if not numbers:
#         return [(expression, current_sum)]
#
#     result_plus = expressions(numbers[1:], current_sum + numbers[0], f"{expression}+{numbers[0]}")
#     result_minus = expressions(numbers[1:], current_sum - numbers[0], f"{expression}-{numbers[0]}")
#     return result_plus + result_minus
#
#
# numbers = [int(i) for i in input().split(", ")]
#
# print(*[f"{el[0]}={el[1]}" for el in expressions(numbers)], sep='\n')
