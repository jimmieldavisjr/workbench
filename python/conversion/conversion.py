print("Enter amount in ounces:")

ounces = int(input())

tons, remainder = divmod(ounces,32000)
pounds, ounces = divmod(remainder,16)

print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces}")