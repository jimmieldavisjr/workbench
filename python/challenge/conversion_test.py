# Instructions:
# Create a Python solution for the following task. Ensure the solution produces output in exactly the same format as the given sample, including capitalization and white space.
# To test your program, first click Run. 
# If your program requires input to produce output, you must enter the input into the console where indicated and press Enter or Return. Some programs may require multiple inputs. 
# Be sure to enter a value for each input. It is recommended you test your program with a variety of possible inputs to ensure your solution is robust across a range of solutions.
 
# Task:
# Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the value of the input ounces. There are 16 ounces in a pound and 2,000 pounds in a ton.
# The solution output should be in the format:
# Tons: value_1 Pounds: value_2 Ounces: value_3
 
# Sample Input and Output:
# If the input is
# 32500
# then the expected output is
# Tons: 1 Pounds: 31 Ounces: 4

print("Enter amount of ounces:")
ounces = int(input())

tons, remainder = divmod(ounces,32000)
pounds, remaining_ounces = divmod(remainder,16)

print(f"Tons: {tons}\nPounds: {pounds}\nOunces: {remaining_ounces}")