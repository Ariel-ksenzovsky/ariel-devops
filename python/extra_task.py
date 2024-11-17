import csv
def class_names():
    with open("names.txt", 'r') as csv_file:
        csv_readr = csv.reader(csv_file)
        for names in csv_readr:
            print(names)
class_names()