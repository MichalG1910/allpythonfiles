# data i godzina
import time             #import bibliotek/modułów dotyczących czasu i daty
import datetime

ticks = time.time() # czas, jaki upłynął od 1 stycznia 1970 roku podawany w sekundach (stempel czasu)
print(ticks)

timeData = time.localtime() # wynikiem będzie krotka(tzw nazwana krotka) z aktualną datą i czasem
print(timeData) 
# przykładowa: time.struct_time(tm_year=2022, tm_mon=8, tm_mday=16, tm_hour=22, tm_min=56, tm_sec=59, 
# tm_wday=1, tm_yday=228, tm_isdst=1)
# tm_wday=1 - dzień tygodnia(0 - poniedziałek, 1 - wtorek itd.)
# tm_yday=228 - 228 dzień roku 
# tm_isdst=1 - czy python zarządza czasem letnim(1), czy zimowym(0)
print(timeData.tm_year) # 2022 - pobieramy z krotki np. rok

timeData = time.localtime(10) # przekazanie stempla czas( krotka będzie zawierać dane z 10 sekund 
# od rozpoczęcia 1 stycznia 1970 roku)
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=0, tm_sec=10, tm_wday=3, 
# tm_yday=1, tm_isdst=0)
print(timeData)

print(" ")

result = time.asctime( time.localtime()) # wyświetlenie daty i godziny w bardziej przystępny sposób
print(result)
timeData = time.localtime()
print(time.strftime("%d/%m/%Y %H:%M:%S",timeData)) # formatowanie daty/godziny według upodobań
# %d/%m/%Y %H:%M:%S - day, month, year, hours, minutes, seconds)(znaki / : wstawione między %d zostaną pokazane)
# pełny opis do metody strftime()
"""
%a	    Abbreviated weekday name.	                                                            Sun, Mon, ...
%A	    Full weekday name.	                                                                    Sunday, Monday, ...
%w	    Weekday as a decimal number.	                                                        0, 1, ..., 6
%d	    Day of the month as a zero-padded decimal.	                                            01, 02, ..., 31
%-d	    Day of the month as a decimal number.	                                                1, 2, ..., 30
%b	    Abbreviated month name.	                                                                Jan, Feb, ..., Dec
%B	    Full month name.	                                                                    January, February, ...
%m	    Month as a zero-padded decimal number.	                                                01, 02, ..., 12
%-m	    Month as a decimal number.	                                                            1, 2, ..., 12
%y	    Year without century as a zero-padded decimal number.	                                00, 01, ..., 99
%-y	    Year without century as a decimal number.	                                            0, 1, ..., 99
%Y	    Year with century as a decimal number.	                                                2013, 2019 etc.
%H	    Hour (24-hour clock) as a zero-padded decimal number.	                                00, 01, ..., 23
%-H	    Hour (24-hour clock) as a decimal number.	                                            0, 1, ..., 23
%I	    Hour (12-hour clock) as a zero-padded decimal number.	                                01, 02, ..., 12
%-I	    Hour (12-hour clock) as a decimal number.	                                            1, 2, ... 12
%p	    Locale's AM or PM.	                                                                    AM, PM
%M	    Minute as a zero-padded decimal number.	                                                00, 01, ..., 59
%-M	    Minute as a decimal number.	                                                            0, 1, ..., 59
%S	    Second as a zero-padded decimal number.	                                                00, 01, ..., 59
%-S	    Second as a decimal number.	                                                            0, 1, ..., 59
%f	    Microsecond as a decimal number, zero-padded on the left.	                            000000 - 999999
%z	    UTC offset in the form +HHMM or -HHMM.	 
%Z	    Time zone name.	 
%j	    Day of the year as a zero-padded decimal number.	                                    001, 002, ..., 366
%-j	    Day of the year as a decimal number.	                                                1, 2, ..., 366
%U	    Week number of the year (Sunday as the first day of the week). 
        All days in a new year preceding the first Sunday are considered to be in week 0.	    00, 01, ..., 53
%W	    Week number of the year (Monday as the first day of the week). 
        All days in a new year preceding the first Monday are considered to be in week 0.	    00, 01, ..., 53
%c	    Locale's appropriate date and time representation.	                                    Mon Sep 30 07:06:05 2013
%x	    Locale's appropriate date representation.	                                            09/30/13
%X	    Locale's appropriate time representation.	                                            07:06:05
%%	    A literal '%' character.	                                                            %
"""
print(" ")

timeStr = "12:10:45 12.10.1984" # wprowadzamy z sami datę i godzinę
timeData = time.strptime(timeStr, "%H:%M:%S %d.%m.%Y") # przeformatowanie daty  do krotk (taką jak dla time.localtime())
print(timeData)

i = 0

while i < 12:
    time.sleep(0.5) # funkcja sleep usypia działanie pętli o podaną wartość (w tym przypadku o 0,5 s)
    print(time.asctime(time.localtime())) # będzie nam wyświetlało co 0.5 s datę i godzinę 
    i += 1


tStart = time.perf_counter() # czas początku wykonywania np.kodu
time.sleep(1.2)
tEnd = time.perf_counter() # czas końca wykonywania np.kodu
print("Code took: ", (tEnd - tStart), "seconds") # wynikiem będzie czas wykonania kodu time.sleep(1.2)

print(" ")
dateTimeObj = datetime.datetime.now() # zwraca aktulną datę i czas
print(dateTimeObj)

dateTimeObj = datetime.datetime(2025, 3, 10)
dateTimeObj = datetime.datetime(2025, 3, 10, 22, 45, 45)

print(" ")

print("date(): ", dateTimeObj.date()) # date():  2025-03-10
print("time(): ", dateTimeObj.time()) # time():  22:45:45
print("timestamp(): ", dateTimeObj.timestamp()) # aktualny znak czasu
print("today(): ", dateTimeObj.today()) # aktualna data i godzina
print("year: ", dateTimeObj.year) # aktualny rok
print("month: ", dateTimeObj.month) # aktualny miesiąc
print("day: ", dateTimeObj.day) # aktualny dzień
print("hour: ", dateTimeObj.hour) # aktualny godzina
print("minute: ", dateTimeObj.minute) # aktualna minuta
print("second: ", dateTimeObj.second) # aktualna sekunda

print("format: ", dateTimeObj.strftime("%H:%M:%S %d.%m.%Y")) # formatowanie zmiennej na bardziej przystępną
                                                             # 22:45:45 10.03.2025

dateTimeObj = dateTimeObj.now()
print("format: ", dateTimeObj.strftime("%H:%M:%S %d.%m.%Y")) # formatowanie zmiennej na bardziej przystępną
                                                               # 00:20:50 18.08.2022

print(" ")

dateTime1 = datetime.datetime( 2025, 1, 1, 23,59,59) # porównywanie dat
dateTime2 = datetime.datetime( 2030, 1, 1, 23,59,59)

print(dateTime1 < dateTime2) # True
print(dateTime1 > dateTime2) # False

date1 = datetime.date(2025,1,1)
date2 = datetime.date(2027,1,1)

print(date1 < date2) # True
print(date1 > date2) # False
print(date2 - date1) # 730 days, 0:00:00

def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

print(getYesterday()) # 2023-01-16



