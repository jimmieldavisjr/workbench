import csv

print("Enter the name of the file along with its extension:")
file_name = input()

with open(file_name, "r") as csv_file:
    content = csv.reader(csv_file)

    new_list = []
    for row in content:
        row.reverse()
        print(row)
