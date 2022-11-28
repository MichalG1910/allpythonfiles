from pickle import TRUE
import time
import datetime
while True:
    dateTimeNow = time.time()

    print("Chcesz wiedzieć ile sekund minęło od jakiejś daty do teraz? ")
    data1 = input("wpisz exit, aby wyjść lub podaj datę i godzinę w formacie [12/10/1984 14:45:00]: ")
    if data1 == "exit": break
    def ver_format(data1):
        try:
            time.strptime(data1, "%d/%m/%Y %H:%M:%S")
            return TRUE
        except ValueError:
            return False
    if ver_format(data1) == False:
        print(" ")
        print("Błędny format daty!!!\n")
        continue
    
    timeData = time.strptime(data1, "%d/%m/%Y %H:%M:%S") 

    rok = int(timeData.tm_year)
    miesiac = int(timeData.tm_mon)
    dzien = int(timeData.tm_mday)
    godzina = int(timeData.tm_hour)
    minuta = int(timeData.tm_min)
    sekunda = int(timeData.tm_sec)
    dateTimeHistoric = datetime.datetime(rok,miesiac,dzien,godzina,minuta,sekunda) 
    stampDateTimeHistoric = dateTimeHistoric.timestamp() 

    INTstampDateTimeHistoric = int(stampDateTimeHistoric)
    INTdateTimeNow = int(dateTimeNow)
    resultSecond = abs(INTdateTimeNow - INTstampDateTimeHistoric)

    print(" ")
    print("Minęło:     ", (resultSecond), "sekund")
    resultDay = int(resultSecond / 86400)
    resultHour = int(resultSecond / 3600)
    resultMinut = int(resultSecond / 60)
    result = int(resultSecond % 60)

    if resultSecond < 60:
        result1 = resultSecond
    else:
        result1 = result


    print("albo minęło:", int(abs(resultMinut)), "minut", int(abs(result1)), "sekund")
    print("albo minęło:", int(abs(resultHour)), "godzin", int(abs(resultMinut % 60)), "minut", int(abs(result1)), "sekund")
    print("albo minęło:", int(abs(resultDay)), "dni", int(abs(resultHour % 24)), "godzin", int(abs(resultMinut % 60)), "minut", int(abs(result1)), "sekund")
    print(" ")
