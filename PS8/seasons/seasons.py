import sys
import re
import inflect
import calendar
from datetime import MAXYEAR, MINYEAR, date

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_date(birth_date)
    except:
        sys.exit("Invalid date")
    
    if MINYEAR > int(year) or int(year) > MAXYEAR:
        sys.exit("Invalid date")
    if 1 > int(month) or int(month) > 12:
        sys.exit("Invalid date")
    total_days = calendar.monthrange(int(year), int(month))[1]
    if 1 > int(day) or int(day) > total_days:
        sys.exit("Invalid date")
    dob = date(int(year), int(month), int(day))
    curr_date = date.today()
    age = curr_date - dob
    age_in_minutes = age.days * 24 * 60
    age_in_words = p.number_to_words(age_in_minutes, andword="")
    print(age_in_words.capitalize() + " minutes")

def check_date(birth_date):
    match = re.search(r"^^(\d{4})-(\d{2})-(\d{2})$", birth_date)
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        return year, month, day
    
if __name__ == "__main__":
    main()