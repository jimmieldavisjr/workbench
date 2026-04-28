purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

print("Enter the item to purchase:")
item_purchased = input()

print("Enter the quantity of that item:")
quantity = int(input())

total_purchase_cost = None
discount = None

if item_purchased in purchase:
    if quantity < 10:
        total_purchase_cost = quantity * purchase[item_purchased]
    elif quantity >= 10 and quantity <= 20:
        discount = purchase[item_purchased] * 0.05
        total_purchase_cost = (purchase[item_purchased] - discount) * quantity
    elif quantity > 21:
        discount = purchase[item_purchased] * 0.10
        total_purchase_cost = (purchase[item_purchased] - discount) * quantity



print(f"{quantity} {item_purchased} total cost: ${total_purchase_cost:.2f}")