name = "Jimmie"
age = 30
gpa = 4.5
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# int > str 
age = str(age)

# float > int
gpa = int(gpa)

# bool > str
is_student = str(is_student)

print(type(age))
print(type(gpa))
print(type(is_student))