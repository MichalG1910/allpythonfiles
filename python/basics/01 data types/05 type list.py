
lista = [] # pusta lista
print(lista)

lista = [1, 2, 3, "c", "d", "e"] # lista może zawierać różne typy argumentów
print(lista)
print(type(lista)) # <class 'list'>

lista[3] = 4 # zmiana 4 elementu listy("c") na nowy element 4
print(lista)

print(lista + ["f", 'g']) # [1, 2, 3, 4, 'd', 'e', 'f', 'g'] - można dodać inną listę do już istniejącej
print(lista * 2) # [1, 2, 3, 4, 'd', 'e', 1, 2, 3, 4, 'd', 'e']- zwielokrotnienie listy 2 razy
print("ilość elementów: ", len(lista))# ilość elementów:  6

lista.append("f") # append - metoda dodaje do listy argument
print(lista) # [1, 2, 3, 4, 'd', 'e', 'f']1
print(lista.append(["g", "h"])) # dołączenie do listy innej listy
print(lista) # [1, 2, 3, 4, 'd', 'e', 'f', ['g', 'h']]

print(lista[7]) # ['g', 'h']
print(lista[7][1]) # h
lista.insert(4, 3) # insert - metoda dodająca w tym przypadku cyfrę 3 do listy nadając jej indeks 4
print(lista) # [1, 2, 3, 4, 3, 'd', 'e', 'f', ['g', 'h']]

print("ilość:", lista.count(3)) # ilość: 2 - count(liczyć, zliczać)- poda nam ilość wystąpienia w liście cyfry 3
print("index:", lista.index("f")) # index: 7 - podaje indeks wybranego argumentu listy( w tym przypadku "f")

lista.remove("e") # remove - usuwa argument z listy ( w tym przypadku "e")
print(lista) # [1, 2, 3, 4, 3, 'd', 'f', ['g', 'h']]

lista2 = [1,4,6,-2,5,0,-8]
lista3 = ["ala", "rafał", "adam", "zenon", "grzegorz", "filip", "aga"]

# wartości minimalne/maksymalne z listy
print("Min:", min(lista2)) # Min: -8
print("Max:", max(lista2)) # Max: 6
print("Min:", min(lista3)) # Min: adam
print("Max:", max(lista3)) # Max: zenon

# sortowanie listy od najmniejszej do największej
lista2.sort()
print(lista2) # [-8, -2, 0, 1, 4, 5, 6]
lista3.sort()
print(lista3) # ['adam', 'aga', 'ala', 'filip', 'grzegorz', 'rafał', 'zenon']

# odwrócenie kolejności listy ( przepisanie od końca po koleji do początku)
lista2.reverse()
print(lista2) # [-8, -2, 0, 1, 4, 5, 6]
lista3.reverse()
print(lista3) # ['adam', 'aga', 'ala', 'filip', 'grzegorz', 'rafał', 'zenon']


lista2.clear() # czyszczenie listy
print(lista2) # []



