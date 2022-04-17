# 01. Even Numbers
# print(list(filter(lambda x: x % 2 == 0, [int(i) for i in input().split(" ")])))

# 02. Sort
# print(sorted([int(i) for i in input().split(" ")]))

# 03. Min Max and Sum
# numbers = [int(i) for i in input().split(' ')]
# print(f"The minimum number is {min([int(i) for i in numbers])}")
# print(f"The maximum number is {max([int(i) for i in numbers])}")
# print(f"The sum number is: {sum([int(i) for i in numbers])}")

# 04. Negative vs Positive
# numbers = [int(i) for i in input().split(' ')]
# positives = [i for i in numbers if i >= 0]
# negatives = [i for i in numbers if i < 0]
# print(f"{sum(negatives)}")
# print(f"{sum(positives)}")
# if abs(sum(negatives)) > sum(positives):
#     print(f"The negatives are stronger than the positives")
# else:
#     print(f"The positives are stronger than the negatives")

# 05. Odd or Even
# def odd_calculate(*args):
#     return sum([int(i) for i in list(filter(lambda x: int(x) % 2 != 0, *args))]) * \
#            len(list(map(lambda x: x, *args)))
#
#
# def even_calculate(*args):
#     return sum([int(i) for i in list(filter(lambda x: int(x) % 2 == 0, *args))]) * \
#            len(list(map(lambda x: x, *args)))
#
#
# command = input()
#
# if command == "Odd":
#     print(odd_calculate(input().split()))
# else:
#     print(even_calculate(input().split()))

# 06. Arguments Length
# def args_length(*args):
#     return len(list(map(lambda x: x, args)))
#
#
# print(args_length(1, 32, 5))
# print(args_length("john", "peter"))
# print(args_length([1, 2, 3]))

# 07. Concatenate
# def concatenate(*args):
#     return ''.join(args)
#
#
# print(concatenate("Soft", "Uni", "Is", "Great", "!"))

# 08. Even or Odd
# def even_odd(*args):
#     if args[-1] == "odd":
#         return list(filter(lambda x: x % 2 != 0, args[:-1]))
#     else:
#         return list(filter(lambda x: x % 2 == 0, args[:-1]))

#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# 09. Function Executor
# def func_executor(*args, _function_results=[]):
#     for _function, _arguments in args:
#         _function_results.append(_function(*_arguments))
#     return _function_results
#
#
# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

# 10. Keyword Arguments Length
# def kwargs_length(**kwargs):
#     return len(kwargs)
#
#
# dictionary = {'name': 'Peter', 'age': 25}
#
# print(kwargs_length(**dictionary))

# 11. Age Assignment
# def age_assignment(*args, **kwargs):
#     return {name: kwargs[name[0]] for name in args}
#
#
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

# 12. Recursion Palindrome
# def palindrome(_word, _index=0):
#     if _word == _word[::-1]:
#         return f"{_word} is a palindrome"
#     else:
#         return f"{_word} is not a palindrome"
#
#
# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))

# 13. Recursive Power
# def recursive_power(_number, _power):
#     return _number ** _power
#
#
# print(recursive_power(2, 10))
# print(recursive_power(10, 100))
