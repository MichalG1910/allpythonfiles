
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

print("\nWycinki: ")#####################  |WYCINKI|  #############################################
print(lista[1:5]) # [2, 3, 4, 'd'] - wycinek listy(krotki też)od indeksu 1 do 4 (kończący 5 nie jest wyświetlany)
krotka = (1,2,4,8,16,32,64,128,256,512,1024)
print(krotka)
print(krotka[-6:-2]) # (32, 64, 128, 256) - możemy pobrać wycinek listy od końca. Indeksowanie wtedy zaczynamy
# od -1( w tym przypadku 1024). Podobnie jak w normalnym wycinku drugi indeks(-2 czyli 512) nie jest wyświetlany
print(krotka[6:])# (64, 128, 256, 512, 1024) - pokaże wycinek listy od 6 do ostatniego
print(krotka[::3])# (1, 8, 64, 512) - pokaże co 3 wartość z listy z uwzględnieniem 1 indeksu
print(krotka[2:11:2])# (4, 16, 64, 256, 1024) - pokaże co 2 wartość z wycinka z uwzględnieniem 1 indeksu 
print(krotka[::-1])# (1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1) - odwróci kolejność argumentów w liście 

print(" ")
lista.append("f") # append - metoda dodaje do listy argument (na samym końcu)
print(lista) # [1, 2, 3, 4, 'd', 'e', 'f']
print(lista.append(["g", "h"])) # dołączenie do listy innej listy
print(lista) # [1, 2, 3, 4, 'd', 'e', 'f', ['g', 'h']]
lista_1 = [-1,0,1,2,3,4,5,6,7,8]
print(lista_1.pop()) # usuwa z listy ostatni argument
print(lista_1) # [-1, 0, 1, 2, 3, 4, 5, 6, 7]
lista_1[1:3] = "A", "B" # zamienimy indeks 1 i 2 (czyli drugą{0} i trzecią cyfrę{1}) na litery A i B
print(lista_1) # [-1, 'A', 'B', 2, 3, 4, 5, 6, 7]
lista_1[3:5] = "A", "B", "C" # jeśli ilośc deklarowanych do zmiany argumentów jest wieksza(3), niż to wynika z zakresu 
                             #([3:5] - 2 arg), to te 2 zostaną nadpisane, a nadmiarowy argument zostanie dodany do listy
print(lista_1) # [-1, 'A', 'B', 'A', 'B', 'C', 4, 5, 6, 7]
lista_1[4:] = [] # usuniemy z listy od 4 argumentu do końca (a właściwie dodamy pustą listę)
print(lista_1) # [-1, 'A', 'B', 'A']
lista_1 += lista # do lista_1 dodamy lista
print(lista_1) # [-1, 'A', 'B', 'A', 1, 2, 3, 4, 'd', 'e', 'f', ['g', 'h']]

print()

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
print(lista2) # [6, 5, 4, 1, 0, -2, -8]
lista3.reverse()
print(lista3) # ['zenon', 'rafał', 'grzegorz', 'filip', 'ala', 'aga', 'adam']


lista2.clear() # czyszczenie listy
print(lista2) # []

# metoda split służy do utworzenia listy z ciągu znaków ( wprowadzonych z klawiatury za pomocą polecenia input) 
# z pominięciem separatorów występujących w tym ciągu
value1 = input("podaj cyfry po przecinku: ") # 1,2,345,ola,w2
value2 = input("podaj cyfry po separatorze | : ") # 1|67|ghj
list1 = value1.split(",") 
list2 = value2.split("|")
print(list1) # ['1', '2', '345', 'ola', 'w2']
print(list2) # ['1', '67', 'ghj']

# metoda wyciągnięcia z listy argumentów listy
color_list = ["Red","Green","White" ,"Black"]
a = "%s %s"%(color_list[0],color_list[-1])# Red Black
print(a)

color_list = ["Red","Green","White" ,"Black"]
print( "%s %s %s %s"%(color_list[0],color_list[1],color_list[2],color_list[3])) # Red Green White Black





