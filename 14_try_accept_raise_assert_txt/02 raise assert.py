
# raise, asser - wyrzucanie wyjątku (raise- z ang. wynieść, assertion - zapewniać)
# przypadek 1 - zastosowanie raise
"""
def dzielenie(x,y):
    if y == 0:
        raise ZeroDivisionError ("Dzielenie przez 0")
    print(x/y)
print(dzielenie(2,0))
"""
# Wyrzuci zdefiniowany przez nas błąd - ZeroDivisionError: Dzielenie przez 0


# przypadek 2 - zastosowanie raise z procedurą try except
"""
def dzielenie(x,y):
    if y == 0:
        raise ZeroDivisionError ("Dzielenie przez 0")
    print(x/y)
    
try:
    print(dzielenie(2,0))
except ZeroDivisionError:
    print("błąd, nie wolno dzielić przez 0")
    raise
"""
# najpierw wykona procedurę try except i wyświetli: błąd, nie wolno dzielić przez 0
# później z powodu zastosowania instrukcji wyrzucenia błędu wyświetli: ZeroDivisionError: Dzielenie przez 0

# przypadek 3 - zastosowanie assert
def dzielenie(x,y):
    assert y != 0, "y == 0" # zapis ten oznacza że y różne od 0, to program wykona się dalej, 
    if y == 0:              # jeśli y = 0 to wyrzuci błąd z naszym opisem AssertionError: y == 0
        raise ZeroDivisionError ("Dzielenie przez 0")
    print(x/y)
    
try:
    print(dzielenie(2,0))
except ZeroDivisionError:
    print("błąd, nie wolno dzielić przez 0")
    raise
# zastosowanie assert doprowadzi do wyrzucenia błędu: AssertionError: y == 0


