import csv
from datetime import datetime
today = datetime.now().strftime("%d.%m.%Y")
today_day = datetime.now().strftime("%d")
today_month = datetime.now().strftime("%m")
today_year = datetime.now().strftime("%Y")

print(f"today in {today}, Checks if someone has a birthday...")

def class_names():
    birthday_found = False
   
    with open("names.txt", 'r') as csv_file:
        for line in csv_file:
            parts = line.strip().split(",")
            full_name = parts[0] 
            birth_date = parts[-1].strip().split(".")
            birth_day = birth_date[0]
            birth_month = birth_date[1]
            birth_year = birth_date[2]
            
            
            age = int(today_year) - int(birth_year) 
            if (birth_month, birth_day) > (today_month, today_day):
                age -= 1
    
       
            if int(birth_day) == int(today_day) and int(birth_month) == int(today_month):
                print(f"Heppy birthday, {full_name} for your {age} birthday ")
                birthday_found = True
                
    if not birthday_found:
            print("Nobody has a birthday today")

            
class_names()
