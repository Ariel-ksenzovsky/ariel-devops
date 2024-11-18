import csv
from datetime import datetime

today = datetime.now().strftime("%d.%m")
today_year = datetime.now().strftime("%Y")

print(f"today in {today}, Checks if someone has a birthday...")

def class_names():
    birthday_found = False
   
    with open("names.txt", 'r') as csv_file:
        for line in csv_file:
            parts = line.strip().split(",")
            full_name = parts[0] 
            birth_date = parts[-1].strip()

            if len(birth_date) != 10 or birth_date[2] != '.' or birth_date[5] != '.':
                print(f"Skipping invalid birth date: {birth_date}")
                continue
        
            birth_day_month = birth_date[:5]
            birth_year = birth_date[-4:]
            age = int(today_year) - int(birth_year) 
    
       
            if birth_day_month == today:
                print(f"Heppy birthday, {full_name} for your {age} birthday ")
                birthday_found = True
                
    if not birthday_found:
            print("Nobody has a birthday today")

            
class_names()
