
lista = [10] * 12 # [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(lista)
# kolekcje
napis = "abracadabra" * 3
print(napis) # abracadabraabracadabraabracadabra

lista2 = [10 for i in range(10)]
print(lista2) # [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

# lista [wyrażenie for element in kolekcja]
lista3 = [litera for litera in "Michał Grabarz"]
print(lista3) # ['M', 'i', 'c', 'h', 'a', 'ł', ' ', 'G', 'r', 'a', 'b', 'a', 'r', 'z']

lista4 = [int(liczba) for liczba in "0123456789"]
print(lista4) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista5 = [int(liczba) for liczba in input("Podaj liczby oddzielone spacją: ").split()] # Podaj liczby oddzielone spacją: 3 5 7 9
print(lista5) # [3, 5, 7, 9]

x, y = [int(liczba) for liczba in input("Podaj liczby oddzielone spacją: ").split()] # Podaj liczby oddzielone spacją: 3 94
print(f"x: {x}, y: {y}") # x: 3, y: 94

slownik = {x: x*x for x in range(11)}
print(slownik) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

lista = [[x for x in range(3)] for y in range(5)]
print(lista) #  [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

lista = {y: [x for x in range(3)] for y in range(5)} # po modyfikacji stworzy słownik
print(lista) #  {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2]}

lista3 = [litera.lower() for litera in "Michał Grabarz"] # tylko małe litery
print(lista3) # ['m', 'i', 'c', 'h', 'a', 'ł', ' ', 'g', 'r', 'a', 'b', 'a', 'r', 'z']


lista4 = [x+y for x,y in ([2,2], [3,3])]
print(lista4) # [4, 6]

lista5 = [x+y for x,y in ([a,a+1] for a in range(10))]
print(lista5) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

parzyste = [x*x for x in range(20) if x % 2 == 0]
print(parzyste) # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

napis = "Michał Grabarz telefon +48739093883"
lista6 = [int(znak) for znak in napis if znak.isdigit()] # isdigit()- wyłapuję tylko ciągi liczb i je zwraca
print(lista6) # [4, 8, 7, 3, 9, 0, 9, 3, 8, 8, 3]
