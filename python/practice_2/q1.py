# ============================================
# Practice Question 1: CSV File I/O (Read / Write / Append)
# ============================================

import csv

filename = "students.csv"

# TODO:
# 1) Read the CSV file and store ALL rows in a list named `rows`
# 2) Append a NEW row: ["Alice", "Computer Science", "Senior"]
# 3) Write ALL rows back to the CSV file so the new row is added
#
# Notes:
# - Use the csv module
# - Do NOT overwrite existing rows accidentally
# - Use newline="" when writing
#
# Expected behavior:
# - Original data remains
# - New row appears at the bottom of the CSV

# YOUR CODE HERE

filename = r"C:\Dev\1_Projects\SoftwareEngineeringWorkbench\practice_2\students.csv"
rows = []

with open(filename, "r", newline="") as file:
    reader = list(csv.reader(file))
    for row in reader:
        rows.append(row)

rows.append(["Alice", "Computer Science", "Senior"])
        
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)


