from os import remove

command = input()


def create_file(_file_name):
    with open(_file_name, "w"):
        pass


def add_content(_file_name, _content):
    try:
        with open(_file_name, "a") as file:
            file.write(_content + "\n")
    except FileNotFoundError:
        with open(_file_name, "w") as file:
            file.write(_content + "\n")


def replace_content(_file_name, _old_string, _new_string):
    try:
        with open(_file_name) as file:
            content = file.read()

        with open(_file_name, "w") as file:
            content = content.replace(_old_string, _new_string)
            file.write(content)
    except FileNotFoundError:
        print(f"An error occurred")


def delete_file(_file_name):
    try:
        remove(_file_name)
    except FileNotFoundError:
        print(f"An error occurred")


while command != "End":
    func, *rest = command.split("-")

    if func == "Add":
        add_content(rest[0], rest[1])  # filename and content
    elif func == "Replace":
        replace_content(rest[0], rest[1], rest[2])  # filename, old string and new string
    elif func == "Create":
        create_file(rest[0])  # filename
    elif func == "Delete":
        delete_file(rest[0])  # filename

    command = input()
