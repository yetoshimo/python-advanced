# 04. Random List
# from random import choice
#
#
# class RandomList(list):
#
#     def get_random_element(self):
#         element = choice(self)
#         self.pop(self.index(element))
#         return element

# 05. Stack of Strings
# class Stack:
#
#     def __init__(self):
#         self.data = []
#
#     def __str__(self):
#         return f"[{', '.join(reversed(self.data))}]"
#
#     def push(self, item):
#         return self.data.append(item)
#
#     def pop(self):
#         return self.data.pop()
#
#     def peek(self):
#         return self.data[0]
#
#     def is_empty(self):
#         return len(self.data) == 0
