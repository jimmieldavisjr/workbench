predef_list = [4, -27, 15, 33, -10]

print("Enter the number to check for in the list:")
user_input = int(input())
present = False

def is_in_list(predef_list):
    if user_input in predef_list:
        present = True
        print(f"Is the input present in the list? {present}")
    else:
        present = False
        print(f"Is the input present in the list? {present}")

is_in_list(predef_list)