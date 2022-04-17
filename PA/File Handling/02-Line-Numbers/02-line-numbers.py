from re import sub

with open("text.txt") as file:
    data = file.readlines()

with open("output.txt", "w") as output:
    for count, string in enumerate(data):
        characters = len([char for char in string if char.isalpha()])
        punctuation = len(sub(r"[A-Za-z\s]", "", string))
        if count != len(data) - 1:
            output.write(f"Line {count + 1}: {string.strip()} ({characters})({punctuation})\n")
        else:
            output.write(f"Line {count + 1}: {string.strip()} ({characters})({punctuation})")
