from datetime import date

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year1 = int(input("Enter Year:"))
month1 = int(input("Enter Month in number:"))
date1 = int(input("Enter Date:"))
entry1 = date(year1, month1, date1)

print("First date entered is:", entry1)

year2 = int(input("Enter Year:"))
month2 = int(input("Enter Month in number:"))
date2 = int(input("Enter Date:"))
entry2 = date(year2, month2, date2)

print("Second date entered is:", entry2, "\n")

days_difference = (entry2 - entry1).days
print("Total no. of days between the two dates is:", days_difference)

total_months = (entry2.year - entry1.year) * 12 + entry2.month - entry1.month

if entry2.day < entry1.day:
    total_months -= 1
print("Total no. of months between the two dates is:", total_months)

total_years = entry2.year - entry1.year

if entry2.month < entry1.month or (entry2.month == entry1.month and entry2.day < entry1.day):
    total_years -= 1
print("Total no. of years between the two dates is:", total_years)

leap_years = sum(1 for year in range(entry1.year, entry2.year + 1) if is_leap_year(year))
print("Total no. of Leap Years between the two dates is:", leap_years)

