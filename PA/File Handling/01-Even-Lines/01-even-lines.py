from re import sub

with open("text.txt") as file:
    data = [sub(r"([-,.!?])", "@", i) for i in file.readlines()]

# not too readable
# [print(" ".join(list(reversed(i.split())))) for i in [j.replace("\n", "") for j in data if data.index(j) % 2 == 0]]

to_print = [j.replace("\n", "") for j in data if data.index(j) % 2 == 0]

[print(" ".join(list(reversed(i.split())))) for i in to_print]
