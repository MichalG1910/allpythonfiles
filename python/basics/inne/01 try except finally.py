
# try,except czyli przechwytywanie wyjątków
x = 12
y = 0
# instrukcje try/except sprawdzają poprawność kodu i w razie znalezienia błędu zwracają określony przez 
# programistę komunikat nie przerywając działania programu
try:
    print( x / y )
    print( "działa/nie działa")
except ZeroDivisionError:                               # except(exception) oczekiwany błąd
    print("niemożliwe jest dzielenie przez 0!!!")

print("dalsze instrukcje\n")


# możliwe jest podanie kilku oczekiwanych błędów do sprawdzenia w kilku instrukcjach except( pierwszy znaleziony 
# błąd przerywa sprawdzanie dalszego kodu)
try:
    print( x + "!") # błąd typów
    print( x / y )
    print( "działa/nie działa")
except ZeroDivisionError: 
    print("niemożliwe jest dzielenie przez 0!!!")
except TypeError:
    print("błąd typów danych!!!")

print("dalsze instrukcje\n")


# możliwe jest podanie kilku oczekiwanych błędów do sprawdzenia w jednej instrukcji except( pierwszy znaleziony 
# błąd przerywa sprawdzanie dalszego kodu) 
try:
    print( x + y)
    print( x / y )
    print( x + "!")
    print( "działa/nie działa")
except (ZeroDivisionError, TypeError): 
    print("błędny 1 z 3 warunków!!!")

print("dalsze instrukcje\n")

# możliwe jest też nie podanie nazwy oczekiwanego błędu. W takim wypadku instrukcja po except zostanie wykonana, 
# jeśli pojawi się jakikolwiek error
try:
    lista = []
    print(lista[0])
    print( x + y)
    print( x / y )
    print( x + "!")
    print( "działa/nie działa")
except:
    print("błędny fragment kodu!!!")
finally:
    print("finally wykona się w przypadku wykrycia błędu jak i nie" )

print("dalsze instrukcje\n")

