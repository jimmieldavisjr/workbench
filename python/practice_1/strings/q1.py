# ============================================
# Practice Question 1: Accessing Values
# ============================================

course = "Introduction to Python"

# TODO:
# Write a single print statement that prints:
# 1) the first character of the string
# 2) the last character of the string
# 3) the word "Python" from the string
#
# Expected output (format does not have to match exactly):
# I n Python

# YOUR CODE HERE

print(f"{course[0]} {course[len(course) - 1]} {course[(len(course) - 6):len(course)]}")
