print("Enter Student Identification Number:")
int_identification_number = int(input())

str_identification_number = str(int_identification_number)

formatted = ""

i = 0
for char in str_identification_number:
    formatted += str_identification_number[i]
   
    if i == 2:
        formatted += "-"
    if i == 4:
        formatted += "-"
    i += 1

print(formatted)
