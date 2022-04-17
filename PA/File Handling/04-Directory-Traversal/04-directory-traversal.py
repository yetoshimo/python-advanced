from os import walk, path

directory_path, sub_directories, files = next(walk(input()))

extensions = {}

for file in files:
    if file.split(".")[-1] not in extensions:
        extensions[file.split(".")[-1]] = []

    extensions[file.split(".")[-1]].append(file)

# WRITTEN FOR WINDOWS

with open(path.expanduser("~\\Desktop\\report.txt"), "w") as out_file:
    for ext, files in sorted(extensions.items(), key=lambda kv: kv[0]):
        out_file.write(f".{ext}\n")

        for line in sorted(files):
            out_file.write(f"- - - {line}\n")
