
setData = {2,3,1,4,5} # set - zbiór. Tworzenie nieuporządkowanego zbióru unikalnych wartości
setData.add(22)       # dodanie wartości do zbioru (add)

setData.discard(1)    # kasowanie elementu ze zbioru (discard)
setData.remove(3)     # kasowanie elementu ze zbioru
print(type(setData))  # <class 'set'>
print(setData)        # {2, 4, 5, 22}
setData.add(5)        # liczba 5 nie została dodana, ponieważ już jest w zbiorze(zbiór zawiera unikalne wartości)
print(setData)        # {2, 4, 5, 22}
print(1 in setData)   # False - takie zapytanie daje zawsze albo True albo False
print(22 in setData)   # True

print()

for v in setData:     #iteracja - dodajemy zmienną v
    print(v)

setData = {2, 4, 5, 22,}
setData2 = {1,4,5,6,19,20,21,22}
print(setData | setData2) # {1, 2, 4, 5, 6, 19, 20, 21, 22} tworzy z dwóch zbiorów 1 zbiór przy zachowaniu 
                          # zasady unikalnych wartości
print(setData & setData2) # {4, 5, 22} tworzy nowy zbiór, w którym użyte będą tylko te wartości, które są zawarte 
                          # w obydwu łączonych zbiorach
print(setData2 - setData) # {1, 6, 19, 20, 21} od zbioru 2 odejmujemy zbiór 1
print(setData ^ setData2) # {1, 2, 6, 19, 20, 21} różnica symetryczna - bierze z 1 zbioru wartości nie 
                          # występujące w 2 zbiorze oraz bierze z drugiego zbioru wartości nie występujące w 
                          # pierwszym zbiorze i tworzy z nich nowy zbiór
print(setData.intersection(setData2)) # {4, 5, 22} - wyświetli zbiór, w którym będą tylko wartości zawarte zarówno w setData jak i setData2
print(setData.difference(setData2)) # {2} - wyświetli tylko wartość zbioru setData, ktorej nie ma w zbiorze setData2
print(setData2.difference(setData)) 
print(setData.union(setData2)) # {1, 2, 4, 5, 6, 19, 20, 21, 22} - wyświetli wszystkie wartości występujące w jednym jak i drugim zbiorze(bez powtarzania ich - zunifikuje je)
print(setData.symmetric_difference(setData2)) # {1, 2, 6, 19, 20, 21} - to samo co print(setData ^ setData2)



print()

frozenData = frozenset(setData) # niemutowalny zbiór wartości
print(type(frozenData))         # <class 'frozenset'>
#frozenData.add(22) - polecenie wywoła błąd, ponieważ zbiór jest niemutowalny

for value in frozenData:
    print(value)
