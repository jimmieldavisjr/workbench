# ============================================
# Practice Question 5: Mixed String Manipulation
# ============================================

email = "student123@wgu.edu"

# TODO:
# Extract ONLY the username portion of the email
# (everything before the '@')
#
# Then create a NEW string by appending "_verified"
# to the username.
#
# Store the final result in a variable named verified_user
# and print it.
#
# Expected output:
# student123_verified

# YOUR CODE HERE

index = email.find("@")

verified_user = email[0:index] + "_verified"

print(verified_user)

email = "student123@wgu.edu"
username = email.split("@")[0]
print(username)