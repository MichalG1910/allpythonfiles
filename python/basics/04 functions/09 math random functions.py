import math # import biblioteki(modułu) math
import random # import biblioteki random
# można zamaist pobierać całą bibliotekę pobrać tylko wybrany element z niej
# from math import pi - pobierzemy tylko wartość pi - przy urzyciu nie musimy pi poprzedzać math np print(pi)

# from math import sqrt as pierwiastek - pobieramy funkcję sqrt i oznaczamy ją nazwą pierwiastek. W skrypcie
# kożystamy  z naszej zdefiniowanej nazwy  dla tej funkcji (po słowie as)

print(type(str(12))) # konwersja liczby na łańcuch znaków 
print(type(str([1,2,3]))) # konwersja listy na łańcuch znaków

print(" ")

number = int("123") # konwersja łańcucha znaków na liczbę całkowitą
print(type(number))

floatNum = float("45.67") # konwersja z łańcucha znaków na liczbę rzeczywistą
print(type(floatNum))

print(" ")
# funkcja abs zwraca wartośc bezwzględną liczby
print( abs(9)) # 9          
print( abs(-9.1)) # 9.1

print(" ")
# math.ceil - funkcja zaokrągla do góry (ceil- sufit)
print( math.ceil(11.00000001)) # 12
print( math.ceil(9.999999999)) # 10
print( math.ceil(-1.00000111)) # -1
print( math.ceil(-1.99999999)) # -1

print(" ")
# math.floor - funkcja zaokrągla do dołu (floor - podłoga)
print( math.floor(11.00000001)) # 11
print( math.floor(9.999999999)) # 9
print( math.floor(-1.00000111)) # -2
print( math.floor(-1.99999999)) # -2

print(" ")
# funkcja max/min zwraca największy/najmniejszy z przekazanych argumentów
print(max(-1, 7, 23, 89, 63, -24)) # 89
print(max( [-1, 7, 23, 89, 63, -24] )) # 89
print(max( (-1, 7, 23, 89, 63, -24) )) # 89
print(min(-1, 7, 23, 89, 63, -24)) # -24
print(min( [-1, 7, 23, 89, 63, -24] )) # -24
print(min( (-1, 7, 23, 89, 63, -24) )) # -24

print(" ")
# funkcja pow - podnoszenie do poęgi ( to samo można uzyskać "**")
print(pow(4,3)) # 64

print(" ")
# funkcja math.sqrt - wyciąganie pierwiastka kwadratowego
print(math.sqrt(1024)) # 32.0

print(" ")
# funkcja round - zaokrąglanie do określonej liczby miejsc po przecinku
print( round(12.7891234, 3)) # 12.789
print( round(12.7891234, 2)) # 12.79
print( round(12.7891234, 1)) # 12.8

print(" ")
# funkcja random - losowy element
print( random.random() ) # losowa liczba zmiennoprzecinkowa od 0 do 0.9999999...
print( random.random() * 100 ) # losowa liczba zmiennoprzecinkowa od 0 do 9.9999999...
print( int(random.random() * 100) ) # losowa liczba całkowita od 0 do 99
print( random.randint(1,10)) # losowa liczba całkowita z przedziału od 1 do 10
print(" ")
print( random.choice([0,1,2,3,4,5,6])) # losowy element z listy (krotki, zbioru, łańcucha znaków)
print( random.choice(["ola", "ania", "adam", "filip"]))
print( random.choice("abecadło"))

print( random.randrange(-10, 30, 5)) # wartość losowa z zakresu (wartość początkowa -10, wartość końcowa 30, krok 5)

listData = [0,1,2,3,4,5,6,7]
random.shuffle(listData) # argumenty listData zostaną zwrócone w losowej kolejności 
print(listData)





