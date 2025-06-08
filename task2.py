filename = "output.txt"

try:
    first_input = input("Enter text to write to the file: ")
    with open(filename, "w") as file:
        file.write(first_input + "\n")
    print(f"Data successfully written to {filename}.")
    second_input = input("\nEnter additional text to append: ")
    with open(filename, "a") as file:
        file.write(second_input + "\n")
    print("Data successfully appended.")
    print(f"\nFinal content of {filename}:")
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

except Exception as e:
    print(f"Error: {e}")
