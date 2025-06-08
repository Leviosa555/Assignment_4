filename = "sample.txt"

try:
    print("Reading file content:\n")
    with open(filename, "r") as file:
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
