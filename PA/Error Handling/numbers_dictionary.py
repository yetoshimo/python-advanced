numbers_dictionary = {}

# errors that might occur:
# Passing non-integer type to the variable number - Handled in Line26
# Searching for a non-existent number - Handled in Line51
# Removing a non-existent number - Handled in Line67

# On the first several lines, until you receive the command "Search",
# you will receive on separate lines the number as text and the number as integer
# line = input("Please enter the Number as Text or start the 'Search': ") < CAN be added for clear console request
line = input()


def add_number(number):
    number = int(number)
    numbers_dictionary[number_as_string] = number


while line != "Search":

    number_as_string = line

    try:
        # add_number(input("Please enter the Number as Integer: "))
        add_number(input())
    except ValueError:
        print("The variable number must be an integer")

        # # TODO - Try to get the correct value and loop until it is correct < NOT compatible with the example outputs
        # while True:
        #     try:
        #         add_number(input("Please enter the Number as Integer: "))
        #         break
        #     except ValueError:
        #         pass

    # line = input("Please enter the Number as Text or start the 'Search': ")
    line = input()

# When you receive "Search" on the next several lines until you receive the command "Remove",
# you will be given the searched number as text and you need to print it on the console
# line = input("Please enter the Number to Search or start the 'Remove': ")
line = input()

while line != "Remove":

    searched = line

    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    # line = input("Please enter the Number to Search or start the 'Remove': ")
    line = input()

# line = input("Please enter the Number to Remove or 'End' the process: ")
line = input()

# When you receive "Remove" on the next several lines until you receive "End"
# you will be given the searched number as text and you need to remove it from the dictionary
while line != "End":
    searched = line

    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

    # line = input("Please enter the Number to Remove or 'End' the process: ")
    line = input()

# At the end you need to print what is left from the dictionary
print(numbers_dictionary)
