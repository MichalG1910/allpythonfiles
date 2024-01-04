# pętla while - będzie się wykonywała dopóki spełniony będzie warunek. Jak warunek przestanie być spełniony,
#program przejdzie do dalszego kodu

number = 5
while number > 0:
    print( number )
    number = number - 1 # można też zapisać number -= 1
print( "kod po pętli" )

number = 1
while number < 6:
    print( number )
    number += 1

# tworzenie pętli nieskończonej while

num = 0
while True:
    print( "wprowadź liczbę lub exit, aby zakończyć ")
    strData = input() # polecenie input() zażąda wprowadzenia danych z terminala już po uruchomieniu programu
    if strData == "exit" : break # taki zapis umożliwi zaknięcie pętli (break), jeśli wpiszemy w terminalu exit
    num = num + int(strData) # jeśli nie będzie polecenia exit (zakończenie pętli), musimy zmienną strData 
    #  na liczbę całkowitą integer(int)
    print( "Wartość po dodaniu liczby: " + str(num))


number = 3
while number > 0:
    print(number)
    number -= 1
else:               # jednorazowo można użyć instrukcji warunkowej else, która zostanie wykonana po pętli
    print( "number po pętli: " + str(number))