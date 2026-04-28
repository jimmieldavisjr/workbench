filename = r"C:\Dev\1_Projects\SoftwareEngineeringWorkbench\practice_1\data_handling\animals.txt"
content = None

with open(filename, "r") as file:
    content = file.readlines()
    