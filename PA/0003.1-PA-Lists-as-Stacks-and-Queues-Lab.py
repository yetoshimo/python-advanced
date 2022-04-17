# 01. Reverse Strings
# input_string = input()
# stack = []
#
# for i in input_string:
#     stack.append(i)
#
# while stack:
#     print(stack.pop(), end="")

# 02. Matching Parentheses
# expression = input()
# stack = []
#
# for i in range(len(expression)):
#
#     if expression[i] == "(":
#         stack.append(i)
#
#     elif expression[i] == ")":
#         start_index = stack.pop()
#         print(expression[start_index:i + 1])

# 03. Supermarket
# from collections import deque
#
# input_name = input()
# queue = deque()
#
#
# while input_name != "End":
#     if not input_name == "Paid":
#         queue.append(input_name)
#     else:
#         while queue:
#             print(queue.popleft())
#
#     input_name = input()
#
# print(f"{len(queue)} people remaining.")

# 04. Water Dispenser
# from collections import deque
#
# water_quantity = int(input())
# people_queue = deque()
#
# name = input()
#
# while name != "Start":
#     people_queue.append(name)
#     name = input()
#
# command_input = input()
#
# while command_input != "End":
#     if command_input.isdigit():
#         if int(command_input) <= water_quantity:
#             print(f"{people_queue.popleft()} got water")
#             water_quantity -= int(command_input)
#         else:
#             print(f"{people_queue.popleft()} must wait")
#     elif "refill" in command_input:
#         water_quantity += int(command_input.split(" ")[1])
#
#     command_input = input()
#
# print(f"{water_quantity} liters left")

# 05. Hot Potato
# from collections import deque
#
# children = input().split(" ")
# tosses = int(input())
#
# players = deque(children)
#
# counter = 1
#
# while len(players) > 1:
#     person = players.popleft()
#
#     if counter == tosses:
#         print(f"Removed {person}")
#         counter = 0
#     else:
#         players.append(person)
#
#     counter += 1
#
# print(f"Last is {players.pop()}")
