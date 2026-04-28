# ============================================
# Practice Question 2: TXT File I/O (Read / Manipulate / Append)
# ============================================

filename = "animals.txt"

# TODO:
# 1) Read the entire text file into a variable named `content`
# 2) Convert the file contents into a LIST of words
# 3) Reverse the order of the list
# 4) Join the reversed list back into a SINGLE string
# 5) Append the new string to the end of the file on a new line
#
# Notes:
# - Use with open(...)
# - Do NOT overwrite the file
# - Remember strings are immutable
#
# Expected behavior:
# - Original file content stays the same
# - A new line is added containing the reversed words

# YOUR CODE HERE

filename = r"C:\Dev\1_Projects\SoftwareEngineeringWorkbench\practice_2\animals.txt"
content = None

with open(filename, "r") as file:
    content = file.read()
    content = content.split()
    content.reverse()
    content = " ".join(content)

with open(filename, "a") as file:
    file.write(f"\n{content}")

