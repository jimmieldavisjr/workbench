import csv

with open(r"csv_handling\data\animals.csv", "r") as file:
    reader = csv.reader(file)

    animal_list = list(reader)

    animal_list[1][1] = animal_list[5][1]
    print(animal_list[1][1])



