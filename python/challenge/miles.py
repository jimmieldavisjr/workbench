print("Enter the number of days Employee A travels to job:")
employee_a = int(input())
a_total = 15.62 * employee_a

print("Enter the number of days Employee B travels to job:")
employee_b = int(input())
b_total = 41.85 * employee_b

print("Enter the number of days Employee C travels to job:")
employee_c = int(input())
c_total = 32.67 * employee_c

total = a_total + b_total + c_total

print(f"Distance: {total:.2f} miles")
