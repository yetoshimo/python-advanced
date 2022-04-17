# 01. Taxi Express
# from collections import deque
#
#
# # Each number from the customer list represents how much time it takes to drive the customer to his/her destination.
# # Each time you tend customers you should put the first customer in the last taxi until there are no customers left.
# org_list_of_customers = deque([int(i) for i in input().split(", ")])  # QUEUE
# # Keep track of the total time passed to drive all the customers to their destinations (values of all customers).
#
# list_of_taxis = [int(i) for i in input().split(", ")]  # STACK
#
#
# is_finished = False
# no_customer = False
# no_taxi = False
# total_time = 0
#
#
# def tend_customer(_current_customer, _list_of_taxis):
#     while _list_of_taxis:
#         _current_taxi = _list_of_taxis.pop()
#         if _current_customer <= _current_taxi:
#             return True
#         else:
#             return tend_customer(_current_customer, _list_of_taxis)
#     return False
#
#
# while not is_finished:
#     list_of_customers = org_list_of_customers.copy()
#     current_customer = list_of_customers.popleft()
#
#     if tend_customer(current_customer, list_of_taxis):
#         total_time += current_customer
#         org_list_of_customers = list_of_customers.copy()
#         pass
#     else:
#         is_finished = True
#
#     if not org_list_of_customers:
#         is_finished = True
#         no_customer = True
#
#     if not list_of_taxis:
#         is_finished = True
#         no_taxi = True
#
# if no_customer:
#     print(f"All customers were driven to their destinations")
#     print(f"Total time: {total_time} minutes")
# if no_taxi and not no_customer:
#     print(f"Not all customers were driven to their destinations")
#     print(f"Customers left: {', '.join([str(time) for time in org_list_of_customers])}")

# 02. Minesweeper Generator
# from re import findall
#
# field_size = int(input())
# mine_positions = []
#
# for _ in range(int(input())):
#     matches = findall(r"\d+", input())
#     mine_x, mine_y = [int(i) for i in matches]
#     mine_positions.append([mine_x, mine_y])
#
# whole_matrix = [[0 for cell in range(field_size)] for row in range(field_size)]
#
# mine_neighbours = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
#
#
# def place_mines(_field_size, _mines, _whole_matrix):
#     _mine_positions = _mines.copy()
#     for x in range(field_size):
#         for y in range(field_size):
#             for item in mine_positions:
#                 if [x, y] != item:
#                     pass
#                 else:
#                     _mine_positions.remove(item)
#                     _whole_matrix[x][y] = "*"
#     return _whole_matrix
#
#
# def set_mine_neighbours(_whole_matrix, _mine_positions, _mine_neighbours, _field_size):
#     for (_mine_x, _mine_y) in _mine_positions:
#         for (_neighbour_x, _neighbour_y) in _mine_neighbours:
#             if 0 <= _mine_x + _neighbour_x < _field_size and 0 <= _mine_y + _neighbour_y < _field_size:
#                 if whole_matrix[_mine_x + _neighbour_x][_mine_y + _neighbour_y] != "*":
#                     whole_matrix[_mine_x + _neighbour_x][_mine_y + _neighbour_y] += 1
#     return _whole_matrix
#
#
# whole_matrix = place_mines(field_size, mine_positions, whole_matrix)
#
# whole_matrix = set_mine_neighbours(whole_matrix, mine_positions, mine_neighbours, field_size)
#
# [print(*row) for row in whole_matrix]

# 03. Numbers Search
# def numbers_searching(*args):
#     _duplicate_list = []
#     _total_list = []
#     _whole_list = list(args).copy()
#
#     _remove_duplicates = list(dict.fromkeys(_whole_list))
#
#     for item in _remove_duplicates:
#         if _whole_list.count(item) > 1:
#             _duplicate_list.append(item)
#
#     _missing_number = [x for x in range(sorted(_remove_duplicates)[0], sorted(_remove_duplicates)[-1]+1) if x not in sorted(_remove_duplicates)]
#
#     _total_list.append(_missing_number[0])
#     _total_list.append(sorted(_duplicate_list))
#
#     return _total_list
#
#
# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
