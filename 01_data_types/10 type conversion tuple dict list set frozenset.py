
listData = [1,2,3,4,5,6]

tupleData = tuple(listData) #konwersja z typu list(lista) na tuple (krotka czyli tablica)
print(type(tupleData))
print(tupleData)

otherList = list(("Ola", 23, 234)) # konwersja z tuple (krotka) na list (lista)
print(otherList)
print(type(otherList))

setData = set(otherList) # konwersja z list (lista) na set( zbiór)
print(setData)
print(type(setData))

frozenSetData = frozenset(tupleData) # konwersja z tuple(krotka) na frozenset(zamrożony zbiór)
print(frozenSetData)
print(type(frozenSetData))

tupleData = (("Ola", 1234),("Adam", 23456))  
dictData = dict(tupleData) # konwersja z tuple(krotka) na dict (słownik)
print(dictData)
print(type(dictData))
print(dictData["Ola"]) # wywołanie kluczaze slownika - otrzymamy wartość przypisaną do tego klucza (1234)