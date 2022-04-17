# 01. Problem
# # pizza_test = "11, 6, 8, 1"
# # pizza_test = "10, 9, 8, 7, 5"
# # pizza_test = "12, -3, 14, 3, 2, 0"
# pizza_orders = [int(i) for i in input().split(", ")]  # queue
#
# # employee_test = "3, 1, 9, 10, 5, 9, 1"
# # employee_test = "5, 10, 9, 8, 7"
# # employee_test = "10, 15, 4, 6, 3, 1, 22, 1"
# employee_capacity = [int(i) for i in input().split(", ")]  # stack
#
# total_pizza = 0
#
# while pizza_orders and employee_capacity:
#
#     next_pizza = pizza_orders[0]
#     next_employee = employee_capacity[-1]
#
#     if next_pizza > 10:
#         pizza_orders.pop(0)
#
#     elif next_pizza <= 0:
#         pizza_orders.pop(0)
#
#     elif next_pizza <= next_employee:
#         total_pizza += next_pizza
#         pizza_orders.pop(0)
#         employee_capacity.pop(-1)
#
#     elif next_pizza > next_employee:
#         pizza_orders[0] -= next_employee
#         total_pizza += next_employee
#         employee_capacity.pop(-1)
#
# if not pizza_orders:
#     print(f"All orders are successfully completed!\n"
#           f"Total pizzas made: {total_pizza}\n"
#           f"Employees: {', '.join([str(i) for i in employee_capacity])}")
# else:
#     print(f"Not all orders are completed.\n"
#           f"Orders left: {', '.join([str(i) for i in pizza_orders])}")

# 02. Problem
# def throw_dart(_current_player, _current_player_score, _next_row, _next_column):
#     _bullseye_score = 501
#
#     if 0 <= _next_row < 7 and 0 <= _next_column < 7:
#
#         try:
#             if isinstance(int(whole_matrix[_next_row][_next_column]), int):
#                 return _current_player_score - int(whole_matrix[_next_row][_next_column])
#         except ValueError:
#             pass
#
#         if whole_matrix[_next_row][_next_column] == "D":
#             _row_decrement = int(whole_matrix[_next_row][0]) + int(whole_matrix[_next_row][6]) + \
#                              int(whole_matrix[0][_next_column]) + int(whole_matrix[6][_next_column])
#             return _current_player_score - (_row_decrement * 2)
#
#         if whole_matrix[_next_row][_next_column] == "T":
#             _row_decrement = int(whole_matrix[_next_row][0]) + int(whole_matrix[_next_row][6]) + \
#                              int(whole_matrix[0][_next_column]) + int(whole_matrix[6][_next_column])
#             return _current_player_score - (_row_decrement * 3)
#
#         if whole_matrix[_next_row][_next_column] == "B":
#             return _current_player_score - _bullseye_score
#
#     return _current_player_score
#
#
# # def get_next_player(_current_player, _players_dictionary):
# #     for key in _players_dictionary:
# #         if key != _current_player:
# #             _current_player = key
# #             break
# #     return _current_player
#
#
# # def increment_player_turns(_current_player, _player_turns):
# #     _player_turns[_current_player] += 1
# #     return _player_turns
#
#
# player1, player2 = input().split(", ")
# players_dictionary = {player1: 501, player2: 501}
# player_turns = {player1: 0, player2: 0}
# whole_matrix = [[x for x in input().split()] for _ in range(7)]
# # for row in range(7):
# #     for column in range(7):
# #         try:
# #             whole_matrix[row][column] = int(whole_matrix[row][column])
# #         except ValueError:
# #             pass
#
#
# current_player = None
#
#
# while min(players_dictionary.values()) > 0:
#
#     for key in players_dictionary:
#         if key != current_player:
#             current_player = key
#             break
#
#     # current_player = get_next_player(current_player, players_dictionary)
#
#     current_player_score = players_dictionary[current_player]
#
#     next_row, next_column = [int(i) for i in input().strip("()").split(", ")]
#
#     current_player_score = throw_dart(current_player, current_player_score, int(next_row), int(next_column))
#
#     players_dictionary[current_player] = current_player_score
#
#     player_turns[current_player] += 1
#
#     # player_turns = increment_player_turns(current_player, player_turns)
#
#
# print(f"{current_player} won the game with {player_turns[current_player]} throws!")

# 03. Problem
# def flights(*args):
#     _flight_dictionary = {}
#
#     if len(args) % 2 != 0:
#         args = args + tuple("Z")
#
#     for i in range(0, len(args), 2):
#
#         destination, passenger = args[i], args[i + 1]
#
#         if destination == "Finish":
#             break
#
#         if destination not in _flight_dictionary:
#             _flight_dictionary[destination] = passenger
#         else:
#             _flight_dictionary[destination] += passenger
#
#     return _flight_dictionary
#
#
# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
