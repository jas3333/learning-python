
def leap_year(check_leap):
    if check_leap % 4 == 0:
        if check_leap % 100 == 0:
            if check_leap% 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False 

def days_in_month(year_check, month_check):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_in_year = ["January", "February", "March", "April", "May", "June", "July", "August",
                      "September", "October", "November", "December"]
    if month_check not in months_in_year:
        return f"{month_check} is not an option."
    year_checker = leap_year(year_check)
    if year_checker == True and month_check == months_in_year[1]:
        return 29 
    for month in months_in_year:
        if month == month_check:
            month_index = months_in_year.index(month)
            day = month_days[month_index]
    return day
     
year = int(input("Enter a year: "))
month = input("Enter a month: ").title()

days = days_in_month(year, month)

print(days)
        
