
print("Enter the name of the input file:")
filename = input()

with open(filename, "r") as file:
    read_content = file.read()

with open(filename, "a") as file:
    formatted = read_content.split()
    formatted = " ".join(formatted)
    file.write(f"\n{formatted}")

with open(filename, "r") as file:
    final = file.read()

print(final)


