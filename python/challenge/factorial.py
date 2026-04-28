#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is greater than identified comparison value

#import math module and call factorial()
import math

print("Enter a number to calculate its factorial:")
factorial_num = int(input())

print("Enter a number to compare with the factorial:")
comparison_num = int(input())

result = math.factorial(factorial_num)

is_greater = False

if result > comparison_num:
    is_greater = True
else:
    is_greater = False

print(f"The factorial value of {factorial_num} is {result}")
print(is_greater)

