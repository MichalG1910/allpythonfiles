# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
y = int(input("Podaj rok: "))
m = int(input("Podaj miesiąc: "))
print(calendar.month(y,m))