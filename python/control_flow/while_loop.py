name = input("Enter your name:")
while name == "":
    name = input("Name can not be blank. \n Enter your name:")
print(f"Hello {name}")

age = int(input("Enter your age"))
while age <= 0:
    age = int(input("Age must be greater than 0. \n Enter your age:"))
print(f"{name}'s age is {age}")