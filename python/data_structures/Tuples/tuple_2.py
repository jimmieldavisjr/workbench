# Tuple
employee_info = ("Mike", "Jamison", 40, "mjamison@company.com", "555-555-5555", "IT Analyst Lead")
contact_info = (employee_info[3], employee_info[4])

print(employee_info[0])
print(contact_info)

employee_info.count("Mike")
employee_info.index("555-555-5555")

print(employee_info.__add__(contact_info))

employee_info.__class__(contact_info)

employee_info_string = employee_info.__str__() 
print(employee_info_string)