# List Mutation Operations

## List
fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)

## Item assignment -  index
fruits[0] = "fig"
print("Fig replaced apple")
print(fruits)

## Append operation - value
fruits.append("blackberry")
print("blackberry added to end of list")
print(fruits)

## Remove operation - value
fruits.remove("banana")
print("banana removed from list")
print(fruits)

## Pop operation - index
fruits.pop(1)
print("orange: index 1 removed from list")
print(fruits)


for fruit in fruits:
    print(fruit, end=" ")