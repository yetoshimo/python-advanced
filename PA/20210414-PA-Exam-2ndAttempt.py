# 01. Problem
# from collections import deque
#
# pizza_orders = deque([int(i) for i in input().split(", ")])
# employees = [int(i) for i in input().split(", ")]
#
# total_pizzas = 0
#
# while pizza_orders and employees:
#
#     next_pizza = pizza_orders.popleft()
#     next_employee = employees.pop()
#
#     if next_pizza > 10:
#         employees.append(next_employee)
#     elif next_pizza <= 0:
#         employees.append(next_employee)
#     elif next_pizza <= next_employee:
#         total_pizzas += next_pizza
#     elif next_pizza > next_employee:
#         temp_pizza = next_pizza
#         next_pizza -= next_employee
#         while next_pizza > 0 and employees:
#             next_pizza -= employees.pop()
#         if next_pizza > 0:
#             pizza_orders.appendleft(next_pizza)
#         else:
#             total_pizzas += temp_pizza
#
# if not pizza_orders:
#     print(f"All orders are successfully completed!")
#     print(f"Total pizzas made: {total_pizzas}")
#     print(f"Employees: {', '.join([str(i) for i in employees])}")
# else:
#     print(f"Not all orders are completed.")
#     print(f"Orders left: {', '.join([str(i) for i in pizza_orders])}")

# 02. Problem
# def throw_dart(_matrix, throw_r, throw_c, c_score):
#     _is_finished = False
#     if 0 <= throw_r < 7 and 0 <= throw_c < 7:
#
#         if _matrix[throw_r][throw_c] == "B":
#             _is_finished = True
#             return c_score, _is_finished
#
#         elif _matrix[throw_r][throw_c] == "D":
#             return double(_matrix, throw_r, throw_c, c_score), _is_finished
#
#         elif _matrix[throw_r][throw_c] == "T":
#             return triple(_matrix, throw_r, throw_c, c_score), _is_finished
#
#         else:
#             return c_score - int(_matrix[throw_r][throw_c]), _is_finished
#
#     return c_score, _is_finished
#
#
# def double(_matrix, throw_r, throw_c, c_score):
#     c_score -= (int(_matrix[throw_r][0]) + int(_matrix[throw_r][-1]) + int(_matrix[0][throw_c]) + int(_matrix[-1][throw_c])) * 2
#     return c_score
#
#
# def triple(_matrix, throw_r, throw_c, c_score):
#     c_score -= (int(_matrix[throw_r][0]) + int(_matrix[throw_r][-1]) + int(_matrix[0][throw_c]) + int(_matrix[-1][throw_c])) * 3
#     return c_score
#
#
# player_1, player_2 = input().split(", ")
#
# whole_matrix = [input().split() for i in range(7)]
#
# scores = {player_1: 501, player_2: 501}
# turns = {player_1: 0, player_2: 0}
#
# turn = 1
#
# is_finished = False
#
# current_player = None
#
# while scores[player_1] > 0 and scores[player_2] > 0 and not is_finished:
#
#     if turn % 2 != 0:
#         current_player = player_1
#     else:
#         current_player = player_2
#
#     turns[current_player] += 1
#
#     t_r, t_c = [int(i) for i in input().strip("()").split(", ")]
#
#     scores[current_player], is_finished = throw_dart(whole_matrix, t_r, t_c, scores[current_player])
#
#     if is_finished:
#         break
#
#     if scores[current_player] <= 0:
#         break
#
#     turn += 1
#
# print(f"{current_player} won the game with {turns[current_player]} throws!")

# 03. Problem
# def flights(*args):
#     flight_dict = {}
#     for item in range(len(args)):
#         if args[item] == "Finish":
#             return flight_dict
#         if isinstance(args[item], int):
#             flight_dict[args[item - 1]] += args[item]
#         elif args[item] not in flight_dict:
#             flight_dict[args[item]] = 0
#
#     return flight_dict
#
#
# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
