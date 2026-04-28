age = int(input("Enter your age"))
has_ticket = True
price = 10.00

if age >= 18 and age < 65:
    print("Adult")
elif age >= 65:
    print("Senior Citizen")
elif age > 0 and age < 18:
    print("Child")
elif age <= 0:
    ("Age must be a number and greater than 0")
else:
    print("Input error")

if has_ticket:
    print("Ticket confirmed. Please continue")
else:
    print("No ticket available. Please purchase then continue")
