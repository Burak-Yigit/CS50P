month_list = [
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
    date = input("Date: ")
    if "," in date:
        month, day, year = date.replace(",", "").split(" ")
        if day.isdigit():
            day = int(day)
            year = int(year)
            if month in month_list and day > 0 and day <=31:
                month_index = month_list.index(month) + 1
                print(f"{year}-{month_index:02}-{day:02}")
                break
    elif "/" in date:
        month, day, year = date.split("/")
        if month.isalpha():
            continue
        else:
             day = int(day)
             month = int(month)
             year = int(year)
             if month >=1 and month <= 12 and day > 0 and day <= 31 :
                 print(f"{year}-{month:02}-{day:02}")
                 break



