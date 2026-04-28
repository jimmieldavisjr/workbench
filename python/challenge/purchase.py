purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

print("Enter the item to purchase:")
item = input()

print("Enter the quantity of that item:")
quantity = int(input())

total = 0
discount = 0

if quantity < 10:
    discount = 0.00
if quantity in range(10,21):
    discount = 0.05
if quantity >= 21:
    discount = 0.10

total = (purchase[item] - (purchase[item] * discount)) * quantity


print(f"{quantity} {item} total cost: ${total:.2f}")