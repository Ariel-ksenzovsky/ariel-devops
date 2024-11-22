from flask import Flask, render_template
import requests
import csv
from datetime import datetime
   
app = Flask(__name__)

def check_birthdays():
    today_day = int(datetime.now().strftime("%d"))
    today_month = int(datetime.now().strftime("%m"))
    today_year = int(datetime.now().strftime("%Y"))
    birthday_messages = []

    try:
        with open("names.txt", 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                full_name, birth_date = row[0], row[-1].strip()
                birth_date_obj = datetime.strptime(birth_date, "%d.%m.%Y")
                
                birth_day = birth_date_obj.day
                birth_month = birth_date_obj.month
                birth_year = birth_date_obj.year

                if birth_month == today_month and birth_day == today_day:
                    age = today_year - birth_year
                    birthday_messages.append(f"Happy birthday, {full_name}, for your {age} birthday!")
        
        if not birthday_messages:
            birthday_messages.append("Nobody has a birthday today.")
        
    except FileNotFoundError:
        birthday_messages.append("Error: 'names.txt' file not found.")
    
    return birthday_messages

@app.route('/')
def home():
    birthday_messages = check_birthdays()
    return render_template('home.html', messages=birthday_messages)

if __name__ == '__main__':
    app.run(debug=True)
    # print(__name__)