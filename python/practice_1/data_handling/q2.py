import csv

filename = r"C:\Dev\1_Projects\SoftwareEngineeringWorkbench\practice_1\data_handling\input_1.csv"

with open(filename, "r") as file:
    content = csv.reader(file)
    data = list(content)
    for row in data:
        print(row)

