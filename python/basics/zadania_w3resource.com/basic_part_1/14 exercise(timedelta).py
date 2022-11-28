# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

import datetime
import time

d1 = input("Podaj pierwszą datę(Y,M,d): ")
d2 = input("Podaj drugą datę(Y,M,d): ")

dated1 = time.strptime(d1, "%Y,%m,%d") 
rokd1 = int(dated1.tm_year)
miesiacd1 = int(dated1.tm_mon)
dziend1 = int(dated1.tm_mday)
date1 = datetime.date(rokd1,miesiacd1,dziend1)

dated2 = time.strptime(d2, "%Y,%m,%d") 
rokd2 = int(dated2.tm_year)
miesiacd2 = int(dated2.tm_mon)
dziend2 = int(dated2.tm_mday)
date2 = datetime.date(rokd2,miesiacd2,dziend2)

days = abs(date2 - date1)

print("Minęło: " + str(days.days) + " days")

# 2 sposób

d1 = input("Podaj pierwszą datę(Y,M,d): ")
d2 = input("Podaj drugą datę(Y,M,d): ")
dateFormat = "%Y,%M,%d"

dated1 = datetime.datetime.strptime(d1, dateFormat) 
dated2 = datetime.datetime.strptime(d2, dateFormat) 

days = abs(dated2 - dated1)

print("Minęło: " + str(days.days) + " days")

# w obydwu przypadkach użyto obiektu timedelta. Obiekt timedelta jest obiektem, który przedstawia różnicę czasu pomiędzy dwoma datami i czasami lub czas, który upłynął. 
# Posiada informacje w dniach, sekundach i mikrosekundach i można do niego uzyskać dostęp przy pomocy atrybutów days, seconds i microseconds. Możliwe jest również uzyskanie 
# całkowitej liczby sekund za pomocą metody total_seconds().


