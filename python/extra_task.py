import csv
from datetime import datetime
today = datetime.now().strftime("%d.%m.%Y")

print(f"today in {today}, Checks if someone has a birthday...")
def class_names():
    birthday_found = False
   
    with open("names.txt", 'r') as csv_file:
        for line in csv_file:
            parts = line.strip().split(",")
            full_name = parts[0] 
            birth_date = parts[-1] 
        
            if birth_date.endswith(today):
                print(f"Heppy birth day {full_name}!")
                birthday_found = True
                
        if not birthday_found:
            print("Nobody has a birthday today")

        # csv_readr = csv.DictReader(csv_file)
        # for names in csv_readr:
        #     print(names)         
class_names()