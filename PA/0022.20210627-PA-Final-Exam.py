# Problem 1
# from collections import deque
#
# chocolates = [int(i) for i in input().split(", ")]  # stack
# cups_of_milk = deque([int(i) for i in input().split(", ")])  # queue
#
# milkshakes = 0
#
# while chocolates and cups_of_milk and milkshakes != 5:
#
#     next_chocolate = chocolates.pop()
#     next_milk = cups_of_milk.popleft()
#
#     # If any of the values are equal to or below 0,
#     # you should remove them from the records before trying to mix it with the other ingredient.
#     if next_chocolate <= 0:
#         cups_of_milk.appendleft(next_milk)
#
#     elif next_milk <= 0:
#         chocolates.append(next_chocolate)
#
#     # If their values are equal, you should make a milkshake and remove both ingredients.
#     elif next_chocolate == next_milk:
#         milkshakes += 1
#
#     # Otherwise you should move the cup of milk at the end of the sequence and
#     # decrease the value of the chocolate by 5 without moving it from its position.
#
#     else:
#         cups_of_milk.append(next_milk)
#         chocolates.append(next_chocolate - 5)
#
# print(f"Great! You made all the chocolate milkshakes needed!" if milkshakes == 5 else "Not enough milkshakes.")
# print(f"Chocolate: {', '.join([str(i) for i in chocolates])}" if len([str(i) for i in chocolates if i > 0]) > 0 else "Chocolate: empty")
# print(f"Milk: {', '.join([str(i) for i in cups_of_milk])}" if len([str(i) for i in cups_of_milk if i > 0]) > 0 else "Milk: empty")

# Problem 2
# def find_player(_matrix):
#     for p_r, row in enumerate(_matrix):
#         for p_c, column in enumerate(row):
#             if column == "A":
#                 return p_r, p_c
#
#
# def find_targets(_matrix):
#     _targets = []
#     for p_r, row in enumerate(_matrix):
#         for p_c, column in enumerate(row):
#             if column == "x":
#                 _targets.append((p_r, p_c))
#     return _targets
#
#
# def move_player(_matrix, p_r, p_c, n_r, n_c):
#     if 0 <= n_r < 5 and 0 <= n_c < 5:
#         if _matrix[n_r][n_c] == ".":
#             _matrix[p_r][p_c] = "."
#             _matrix[n_r][n_c] = "A"
#             p_r = n_r
#             p_c = n_c
#             return _matrix, p_r, p_c
#         return _matrix, p_r, p_c
#     return _matrix, p_r, p_c
#
#
# def shoot_left(_matrix, p_r, p_c, _hit_targets):
#     while 0 <= p_c < 5:
#         if _matrix[p_r][p_c] == "x":
#             _hit_targets.append((p_r, p_c))
#             _matrix[p_r][p_c] = "."
#             return _hit_targets
#         p_c -= 1
#     return _hit_targets
#
#
# def shoot_right(_matrix, p_r, p_c, _hit_targets):
#     while 0 <= p_c < 5:
#         if _matrix[p_r][p_c] == "x":
#             _hit_targets.append((p_r, p_c))
#             _matrix[p_r][p_c] = "."
#             return _hit_targets
#         p_c += 1
#     return _hit_targets
#
#
# def shoot_up(_matrix, p_r, p_c, _hit_targets):
#     while 0 <= p_r < 5:
#         if _matrix[p_r][p_c] == "x":
#             _hit_targets.append((p_r, p_c))
#             _matrix[p_r][p_c] = "."
#             return _hit_targets
#         p_r -= 1
#     return _hit_targets
#
#
# def shoot_down(_matrix, p_r, p_c, _hit_targets):
#     while 0 <= p_r < 5:
#         if _matrix[p_r][p_c] == "x":
#             _hit_targets.append((p_r, p_c))
#             _matrix[p_r][p_c] = "."
#             return _hit_targets
#         p_r += 1
#     return _hit_targets
#
#
# whole_matrix = [[i for i in input().split()] for _ in range(5)]
#
# player_r, player_c = find_player(whole_matrix)
#
# hit_targets = []
#
# for _ in range(int(input())):
#
#     if not find_targets(whole_matrix):
#         break
#
#     commands = input().split(" ")
#
#     if commands[0] == "move":
#         direction = commands[1]
#         steps = int(commands[2])
#
#         if direction == "right":
#             whole_matrix, player_r, player_c = move_player(whole_matrix, player_r, player_c, player_r, player_c + steps)
#         elif direction == "left":
#             whole_matrix, player_r, player_c = move_player(whole_matrix, player_r, player_c, player_r, player_c - steps)
#         elif direction == "up":
#             whole_matrix, player_r, player_c = move_player(whole_matrix, player_r, player_c, player_r - steps, player_c)
#         elif direction == "down":
#             whole_matrix, player_r, player_c = move_player(whole_matrix, player_r, player_c, player_r + steps, player_c)
#
#     elif commands[0] == "shoot":
#         direction = commands[1]
#
#         if direction == "up":
#             hit_targets = shoot_up(whole_matrix, player_r, player_c, hit_targets)
#         elif direction == "down":
#             hit_targets = shoot_down(whole_matrix, player_r, player_c, hit_targets)
#         elif direction == "right":
#             hit_targets = shoot_right(whole_matrix, player_r, player_c, hit_targets)
#         elif direction == "left":
#             hit_targets = shoot_left(whole_matrix, player_r, player_c, hit_targets)
#
# print(f"Training completed! All {len(hit_targets)} targets hit." if not find_targets(whole_matrix)
#       else f"Training not completed! {len(find_targets(whole_matrix))} targets left.")
# [print(list(i)) for i in hit_targets]

# def shooting(player, direction, matrix):
#     x, y = direction
#     current_player_direction_x, current_player_direction_y = player
#     target_hit = []
#     while True:
#         current_player_direction_x += x
#         current_player_direction_y += y
#         if current_player_direction_x in range(5) and current_player_direction_y in range(5):
#             if matrix[current_player_direction_x][current_player_direction_y] == 'x':
#                 matrix[current_player_direction_x][current_player_direction_y] = '.'
#                 target_hit = [current_player_direction_x, current_player_direction_y]
#                 break
#         else:
#             break
#     return target_hit, matrix
#
#
# def find_player(matrix):
#     for i in range(5):
#         for j in range(5):
#             if matrix[i][j] == 'A':
#                 return [i, j]
#
#
# def check_for_targets(matrix):
#     targets = []
#     for i in range(5):
#         for j in range(5):
#             if matrix[i][j] == 'x':
#                 targets.append([i, j])
#     return targets
#
#
# def move(player, command, matrix):
#     direction = command[1]
#     steps = int(command[2])
#     if direction == 'up' or direction == 'down':
#         if direction == 'up':
#             if player[0] - steps in range(5):
#                 if matrix[player[0] - steps][player[1]] == '.':
#                     matrix[player[0]][player[1]] = '.'
#                     matrix[player[0] - steps][player[1]] = 'A'
#                     player = [player[0] - steps, player[1]]
#         elif direction == 'down':
#             if player[0] + steps in range(5):
#                 if matrix[player[0] + steps][player[1]] == '.':
#                     matrix[player[0]][player[1]] = '.'
#                     matrix[player[0] + steps][player[1]] = 'A'
#                     player = [player[0] + steps, player[1]]
#     elif direction == 'left' or direction == 'right':
#         if direction == 'left':
#             if player[1] - steps in range(5):
#                 if matrix[player[0]][player[1] - steps] == '.':
#                     matrix[player[0]][player[1]] = '.'
#                     matrix[player[0]][player[1] - steps] = 'A'
#                     player = [player[0], player[1] - steps]
#         elif direction == 'right':
#             if player[1] + steps in range(5):
#                 if matrix[player[0]][player[1] + steps] == '.':
#                     matrix[player[0]][player[1]] = '.'
#                     matrix[player[0]][player[1] + steps] = 'A'
#                     player = [player[0], player[1] + steps]
#
#     return player, matrix
#
#
# def shoot(player, command, matrix):
#     direction = command[1]
#     hit_target = []
#     if direction == 'up' or direction == 'down':
#         if direction == 'up':
#             target, matrix = shooting(player, [-1, 0], matrix)
#             hit_target.append(target)
#         elif direction == 'down':
#             target, matrix = shooting(player, [1, 0], matrix)
#             hit_target.append(target)
#     elif direction == 'left' or direction == 'right':
#         if direction == 'left':
#             target, matrix = shooting(player, [0, -1], matrix)
#             hit_target.append(target)
#         elif direction == 'right':
#             target, matrix = shooting(player, [0, 1], matrix)
#             hit_target.append(target)
#     return player, matrix, hit_target
#
#
# matrix = [[x for x in input().split()] for _ in range(5)]
# player = find_player(matrix)
# num = int(input())
# hit_targets = []
# for _ in range(num):
#     targets = check_for_targets(matrix)
#     if not targets:
#         break
#     command = input().split(' ')
#     if command[0] == 'move':
#         player, matrix = move(player, command, matrix)
#     elif command[0] == 'shoot':
#         player, matrix, targetss = shoot(player, command, matrix)
#         for i in targetss:
#             if len(i) > 0:
#                 hit_targets.append(i)
# if check_for_targets(matrix):
#     print(f"Training not completed! {len(check_for_targets(matrix))} targets left.")
# else:
#     print(f"Training completed! All {len(hit_targets)} targets hit.")
# for i in hit_targets:
#     print(i)

# Problem 3
# def math_operations(*args, **kwargs):
#     index = 0
#     numbers = list(args)
#     while index < len(numbers):
#         if index % 4 == 0:
#             kwargs["a"] += int(numbers[index])
#         elif index % 4 == 1:
#             kwargs["s"] -= int(numbers[index])
#         elif index % 4 == 2:
#             try:
#                 kwargs["d"] /= int(numbers[index])
#             except ZeroDivisionError:
#                 # numbers.pop(index)
#                 pass
#         elif index % 4 == 3:
#             kwargs["m"] *= int(numbers[index])
#         index += 1
#     return kwargs
#
#
# print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
# print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
# print(math_operations(6, a=0, s=0, d=0, m=0))
