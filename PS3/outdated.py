months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").lstrip("\" ").rstrip(" \"")
        if "/" in date:
            month, day, year = date.split("/")
            if month.isdigit():
                month = int(month)
                if 1 <= month <= 12:
                    month_index = month
                    if day.isdigit():
                        day = int(day)
                        if 1 <= day <= 31:
                            break
            else:
                continue

        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            month = month.title()
            if month.isdigit():
                month = int(month)
                if 1 <= month <= 12:
                    month_index = month
                    if day.isdigit():
                        day = int(day)
                        if 1 <= day <= 31:
                            break
            else:
                if month in months:
                    month_index = months.index(month) + 1
                    day = int(day)
                    if 1 <= day <= 31:
                        break
        
        else:
            continue       
    except:
        break
print(f"{year}-{month_index:02}-{day:02}")
