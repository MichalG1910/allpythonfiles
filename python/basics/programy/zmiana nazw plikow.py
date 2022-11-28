
import os
location = str(input('podaj lokalizację katalogu do zmiany nazwy plików np. (D:\python turtorial 2"): '))
toConvert = str(input('co ma być zmienione np. (X2Download.com-): '))
numeration = input("czy chcesz numerować pliki w katalogu?(tak - podaj cyfrę początku numeracji/nie): ")
afterConvert = str(input('na co ma być zmienione ("zmiana"): '))
objs = os.listdir(location)
if numeration == "nie":
    a = None
else:
    a = int(numeration)
for src in objs:
    full_src = os.path.join(location, src)
    if os.path.isfile(full_src):
        
        if afterConvert == "" and a != None:
            afterCon = "0" + str(a) + ". " if a < 10 else str(a) + ". "
            dst = src.replace(toConvert, afterCon)
            a += 1
        elif afterConvert == "" and a == None:
            dst = src.replace(toConvert, afterConvert)
        elif a == None:
            dst = src.replace(toConvert, afterConvert)    
        else:
            # dst = src.replace(toConvert, ( str(a)+ ". " + afterConvert))
            afterCon = "0" + str(a) + ". " + afterConvert if a < 10 else str(a) + ". " + afterConvert
            dst = src.replace(toConvert, afterCon)
            a += 1

    if src != dst:
        full_dst = os.path.join(location, dst)
        os.rename(full_src, full_dst)