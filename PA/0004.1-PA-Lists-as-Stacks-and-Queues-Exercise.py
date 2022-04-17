# # 01. Reverse Numbers with a Stack
# input_numbers = [i for i in input().split(" ")]
#
# stack = []
#
# for item in input_numbers:
#     stack.append(item)
#
# while stack:
#     print(f"{stack.pop()}", end=" ")
#
# 02. Maximum and Minimum Element
# total_lines = int(input())
#
# stack = []
#
# for counter in range(total_lines):
#     command_input = input().split(" ")
#
#     command = command_input[0]
#
#     if command == "1":
#         stack.append(command_input[1])
#
#     if command == "2" and stack:
#         stack.pop()
#
#     if command == "3" and stack:
#         print(max([int(i) for i in stack]))
#
#     if command == "4" and stack:
#         print(min([int(i) for i in stack]))
#
# to_print = []
#
# while stack:
#     to_print.append(stack.pop())
#
# print(', '.join(to_print))
#
# 03. Fast Food
# from collections import deque
#
# # First, you will be given the quantity of the food that you have for the day
# # an integer in the range [0, 1000]
# food_quantity = int(input())
#
# # Next, you will be given a sequence of integers, each representing the quantity of an order.
# # Keep the orders in a queue.
# # sequence of integers, representing each order, separated by a single space
# quantity_of_orders = deque(int(i) for i in input().split(" "))
#
# incomplete_orders = []
#
# # Find the biggest order and print it.
# print(max(quantity_of_orders))
#
# while quantity_of_orders:
#     # You will begin servicing your clients from the first one that came.
#     next_order = quantity_of_orders.popleft()
#
#     # Before each order, check if you have enough food left to complete it.
#     if next_order <= food_quantity:
#         # If you have, remove the order from the queue and reduce the amount of food you have.
#         # next_order already removed it from the queue
#         food_quantity -= next_order
#     else:
#         # if food_quantity is not enough, keep the order as incomplete
#         # AND STOP SERVING REST OF THE CUSTOMERS INCLUDING CURRENT ONE
#         incomplete_orders.append(next_order)
#         break
#
# if incomplete_orders:
#     while quantity_of_orders:
#         incomplete_orders.append(quantity_of_orders.popleft())
#     print(f"Orders left: {' '.join([str(i) for i in incomplete_orders])}")
# else:
#     print(f"Orders complete")
#
# 04. Fashion Boutique
# clothes_in_box = [int(i) for i in input().split(" ")]
# RACK_CAPACITY = int(input())
#
# current_rack = RACK_CAPACITY
#
# rack_count = 1
#
# while clothes_in_box:
#     next_item = clothes_in_box.pop()
#
#     if next_item <= current_rack:
#         current_rack -= next_item
#     else:
#         rack_count += 1
#         current_rack = RACK_CAPACITY
#         clothes_in_box.append(next_item)
#
# print(rack_count)
#
# 05. Truck Tour
# from collections import deque
#
# number_of_pumps = int(input())
#
# station_visits = []
#
# for i in range(number_of_pumps):
#     input_command = input().split(" ")
#     petrol_amount = int(input_command[0])
#     to_next_pump = int(input_command[1])
#
#     station_visits.append(petrol_amount)
#     station_visits.append(to_next_pump)
#
# index_number = 0
#
# travel_list = deque(station_visits)
#
# while travel_list:
#
#     to_fill = travel_list.popleft()
#     to_go = travel_list.popleft()
#
#     if to_fill < to_go:
#         station_visits.append(station_visits.pop(0))
#         station_visits.append(station_visits.pop(0))
#
#     elif to_fill >= to_go:
#         fuel_left = to_fill - to_go
#
#         while travel_list:
#             next_to_fill = travel_list.popleft()
#             next_to_go = travel_list.popleft()
#
#             if fuel_left + next_to_fill >= next_to_go:
#                 fuel_left = fuel_left + next_to_fill - next_to_go
#             else:
#                 station_visits.append(station_visits.pop(0))
#                 station_visits.append(station_visits.pop(0))
#                 fuel_left = -1
#                 break
#
#         if fuel_left >= 0:
#             print(index_number)
#             break
#
#     index_number += 1
#     travel_list = deque(station_visits)
#
# 06. Balanced Parentheses
# parentheses_sequence = input()
#
# stack_front = []
#
# open_parenthesis = ""
# closed_parentheses = ""
#
# for i in parentheses_sequence:
#
#     if i == "{" or i == "(" or i == "[":
#         stack_front.append(i)
#     elif i == "}" or i == ")" or i == "]":
#         closed_parentheses = i
#
#         if stack_front:
#             open_parenthesis = stack_front.pop()
#         else:
#             break
#
#         if open_parenthesis == "{" and closed_parentheses == "}":
#             closed_parentheses = ""
#             continue
#         elif open_parenthesis == "[" and closed_parentheses == "]":
#             closed_parentheses = ""
#             continue
#         elif open_parenthesis == "(" and closed_parentheses == ")":
#             closed_parentheses = ""
#             continue
#         else:
#             break
#
# if stack_front or closed_parentheses != "":
#     print("NO")
# else:
#     print("YES")
#
# 07. Robotics
# from collections import deque
# from datetime import datetime
# from datetime import timedelta
#
#
# def add_robot_to_the_queue(name, time, available):
#     robot = {'name': name, 'time': time, 'available': available}
#     robots.append(robot)
#     available_robots.append(robot)
#     return
#
#
# # On the first line, you will get the names of the robots and their processing times in format
# # "robotName-processTime;robotName-processTime;robotName-processTime"
# string_to_add = input().split(";")
#
# # On the second line, you will get the starting time in format "hh:mm:ss"
# start_time = datetime.strptime(input(), "%H:%M:%S")
#
# # The robots are standing on the line in the order of their appearance.
# robots = deque([])
# available_robots = deque([])
#
# for i in string_to_add:
#     add_robot_to_the_queue(i.split("-")[0], int(i.split("-")[1]), start_time.time())
#
# product_queue = deque()
#
# # Next, until the "End" command, you will get a product on each line.
# next_product = input()
#
# while next_product != "End":
#     product_queue.append(next_product)  # product name
#
#     next_product = input()
#
# # A product is coming from the line each second (so the first product should appear at [start time + 1 second])
# start_time += timedelta(seconds=1)
#
# while product_queue:
#     # Each robot processes a product coming from the assembly line.
#     next_line_product = product_queue.popleft()
#
#     # Each robot has a processing time, the time it needs to process a product.
#     # When a robot is free it should take a product for processing and log his name, product and processing start time.
#     if available_robots:
#         current_robot = available_robots.popleft()
#
#         next_robot_name = current_robot['name']
#
#         print(f"{next_robot_name} - {next_line_product} [{start_time.time()}]")
#
#         current_robot['available'] = start_time + timedelta(seconds=current_robot['time'])
#
#         # update robots list for the next available check
#         [el for el in robots if el == current_robot][0]['available'] = current_robot['available']
#
#     else:
#         for r in robots:
#             if start_time >= r['available']:
#                 available_robots.append(r)
#
#         # If a product passes the line and there is not a free robot to take it,
#         # it should be queued at the end of the line again.
#         if not available_robots:
#             product_queue.append(next_line_product)
#         else:
#             current_robot = available_robots.popleft()
#
#             next_robot_name = current_robot['name']
#
#             print(f"{next_robot_name} - {next_line_product} [{start_time.time()}]")
#
#             current_robot['available'] = start_time + timedelta(seconds=current_robot['time'])
#
#             # update robots list for the next available check
#             [el for el in robots if el == current_robot][0]['available'] = current_robot['available']
#
#     start_time += timedelta(seconds=1)
#
# 08. Crossroads
# from collections import deque
#
# # On the first line, you will receive the duration of the green light in seconds – an integer in the range [1-100]
# GREEN_TIME = int(input())
#
# # On the second line, you will receive the duration of the free window in seconds – an integer in the range [0-100]
# FREE_TIME = int(input())
#
# green_current = GREEN_TIME
# free_current = FREE_TIME
#
# # The road Sam is on has a single lane where cars queue up until the light goes green.
# road_queue = deque()
#
# # On the following lines, until you receive the "END" command, you will receive one of two things:
# # A car – a string_to_add containing the model of the car, or
# # The command "green" which indicates the start of a green light cycle
# traffic_command = input()
#
# current_cross = deque()
#
# cars_counter = 0
#
# is_accident = False
#
# while traffic_command != "END":
#     if traffic_command == "green":
#         if road_queue:
#             next_traffic = road_queue.popleft()
#             green_current = GREEN_TIME - len(next_traffic)
#
#             while green_current > 0:
#                 cars_counter += 1
#                 if road_queue:
#                     next_traffic = road_queue.popleft()
#                     green_current -= len(next_traffic)
#                 else:
#                     break
#
#             if green_current == 0:
#                 cars_counter += 1
#
#             if free_current >= abs(green_current):
#                 if green_current < 0:
#                     cars_counter += 1
#
#             else:
#                 hit_index = green_current + free_current
#                 print(f"A crash happened!")
#                 print(f"{next_traffic} was hit at {next_traffic[hit_index]}.")
#                 is_accident = True
#                 break
#
#     else:
#         road_queue.append(traffic_command)
#
#     traffic_command = input()
#
# if not is_accident:
#     print(f"Everyone is safe.")
#     print(f"{cars_counter} total cars passed the crossroads.")
#
# 09. Key Revolver
# from collections import deque
#
# # On the first line of input, you will receive the price of each bullet – an integer in the range [0-100]
# bullet_price = int(input())
# # On the second line, you will receive the size of the gun barrel – an integer in the range [1-5000]
# BARREL_SIZE = int(input())  # reloading trigger
# # On the third line, you will receive the bullets – a space-separated integer sequence with [1-100] integers
# bullets = [int(i) for i in input().split(" ")]  # stack - total number of bullets
# # On the fourth line, you will receive the locks – a space-separated integer sequence with [1-100] integers
# locks = [int(i) for i in input().split(" ")]  # queue
# # On the fifth line, you will receive the value of the intelligence – an integer in the range [1-100000]
# intelligence_value = int(input())
#
# locks_original = deque(locks)
#
# TOTAL_BULLETS = len(bullets)
#
# number_of_bullets = len(bullets)
#
# current_barrel = BARREL_SIZE
#
# locks = deque(locks)
#
# while bullets:
#     # through the bullets back-to-front
#     next_bullet = bullets.pop()
#     number_of_bullets -= 1
#     if current_barrel > 0:
#         current_barrel -= 1
#     elif number_of_bullets >= 0:
#         print("Reloading!")
#         if not locks:
#             bullets.append(next_bullet)
#             break
#         current_barrel = BARREL_SIZE
#         current_barrel -= 1
#
#     # he starts to shoot the locks front-to-back
#     if locks:
#         next_lock = locks.popleft()
#     else:
#         bullets.append(next_bullet)
#         break
#
#     # If the bullet has a smaller or equal size to the current lock, print "Bang!",
#     # then remove the lock
#     if next_bullet <= next_lock:
#         print(f"Bang!")
#         locks_original.popleft()
#     # If not, print "Ping!", leaving the lock intact.
#     # The bullet is removed in both cases
#     else:
#         print(f"Ping!")
#         locks = deque(locks_original)
#
# if not locks and bullets:
#     total_earned = intelligence_value - ((TOTAL_BULLETS - len(bullets)) * bullet_price)
#     print(f"{len(bullets)} bullets left. Earned ${total_earned}")
# elif not bullets and locks:
#     print(f"Couldn't get through. Locks left: {len(locks)}")
# elif not bullets and not locks:
#     total_earned = intelligence_value - (TOTAL_BULLETS * bullet_price)
#     print(f"{len(bullets)} bullets left. Earned ${total_earned}")
#
# 10. Cups and Bottles
# from collections import deque
#
# cup_capacity = deque([int(i) for i in input().split(" ")])
# bottle_capacity = [int(i) for i in input().split(" ")]
#
# wasted_amount = 0
#
# while cup_capacity and bottle_capacity:
#     first_cup = cup_capacity.popleft()
#     last_bottle = bottle_capacity.pop()
#
#     while first_cup > 0:
#         if last_bottle - first_cup >= 0:
#             wasted_amount += last_bottle - first_cup
#             break
#         else:
#             first_cup -= last_bottle
#             last_bottle = bottle_capacity.pop()
#
# if cup_capacity:
#     print(f"Cups: {' '.join([str(i) for i in cup_capacity])}")
#     print(f"Wasted litters of water: {wasted_amount}")
# elif bottle_capacity:
#     print(f"Bottles: {' '.join([str(i) for i in bottle_capacity])}")
#     print(f"Wasted litters of water: {wasted_amount}")
