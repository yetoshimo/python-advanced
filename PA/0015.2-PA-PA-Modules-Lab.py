# 01. Calculate Logarithm
# from math import log
#
# received_number = int(input())
#
# given_base = input()
#
# if given_base == "natural":
#     print(f"{log(received_number):.2f}")
# else:
#     print(f"{log(received_number, int(given_base)):.2f}")

# 02. ASCII Art
# from pyfiglet import figlet_format
#
#
# def print_art(given_message):
#     print(figlet_format(given_message))
#
#
# print_art("Mahmut")

# 03. Triangle
# def print_triangle(size):
#     line = ""
#     for i in range(1, size + 1):
#         line += str(i)
#         print(' '.join(list(line)))
#
#     for j in range(size, 0, -1):
#         line = line[:-1]
#         print(' '.join(list(line)))
#
#
# print_triangle(5)

# 04. Mathematical Operations
# number_1, math_sign, number_2 = input().split()
#
# number_1 = float(number_1)
# number_2 = float(number_2)
#
# if math_sign == "/":
#     print(f"{number_1 / number_2:.2f}")
# elif math_sign == "*":
#     print(f"{number_1 * number_2:.2f}")
# elif math_sign == "-":
#     print(f"{number_1 - number_2:.2f}")
# elif math_sign == "+":
#     print(f"{number_1 + number_2:.2f}")
# elif math_sign == "^":
#     print(f"{number_1 ** number_2:.2f}")

# 05. Fibonacci Sequence
# command, *rest = input().split()
#
# while command != "Stop":
#
#     if command == "Create":
#         sequence = []
#         count = int(rest[1])
#         a = 0
#         b = 1
#         for i in range(count):
#             sequence.append(str(a))
#             a, b = b, a + b
#         print(' '.join(sequence))
#
#     elif command == "Locate":
#         number = rest[0]
#         if number in sequence:
#             print(f"The number - {number} is at index {sequence.index(number)}")
#         else:
#             print(f"The number - {number} is not in the sequence")
#
#     command, *rest = input().split()
