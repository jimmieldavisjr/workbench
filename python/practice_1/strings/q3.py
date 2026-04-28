# ============================================
# Practice Question 3: Removing Characters from a String
# ============================================

serial = "SN-4587-XX"

# TODO:
# Create a NEW string with all hyphens (-) removed
#
# Store the result in a variable named clean_serial
# and print it.
#
# Expected output:
# SN4587XX

# YOUR CODE HERE

clean_serial = ""

for char in serial:
    if char != "-":
        clean_serial += char
    
print(clean_serial)