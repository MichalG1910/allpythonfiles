# operacje na listach
lista = list(range(10)) # tworzy listę [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

nowaLista = [i * 2 for i in lista] # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] - wykonuje iterację każdego elementu 
# listy i wykonuje dla niego operację ( w tym przypadku i*2)
print("Nowa lista: ", nowaLista)

nowaLista2 = [i + 2 for i in lista if i % 2 == 0] # [2, 4, 6, 8, 10]
nowaLista3 = [i + 1 for i in lista if i % 2 == 0] # [1, 3, 5, 7, 9]
# przypadki powyżej: iteracja wykonywana jest dopiero wtedy, gdy zostanie spełniony warunek if. Co ciekawe, 
# jak pokazuje nowaLista3, kolejność odczytywania operacji jest taka, że najpierw sprawdzany jest warunek 
# if ( i%2 == 0 co oznacza reszta z dzielenia przez 2 rowna 0) i tylko te wartości są iterowane, które 
# go spełnią ( w tym przypadku 0,2,4,6,8)
print("Nowa lista 2:", nowaLista2)
print("Nowa lista 3:", nowaLista3)

print(" ")
# metoda all sprawdza czy założony warunek (i % 2 == 0) jest spelniony dla wsystkich argumentów listy. 
# Jeśli tak, zwraca True, jeśli nie, zwraca False
# poniżej zastosowano instrukcję if, wiec zwróci nam odpowiedni łańcuch znaków
lista = [11,20,25,30,41]
if all([i % 2 == 0 for i in lista]): 
    print("Wszystkie parzyste")
else:
    print("Niewszystkie parzyste")

# podobnie jak wyżej, tylko any szuka chociaż jednego argumentu, który spełnia założony warunek
if any([i % 2 == 0 for i in lista]): 
    print("Chociaż jedna parzysta")
else:
    print("Wszystkie nieparzyste")


print(" ")
# enumerate numeruje nam od 0 każdy argument z listy. Wynikiem jest krotka składająca się numeru przypisanego 
# przez enumerate i argumentu listy
for i in enumerate(lista):
    print(i)
# poniżej dokonaliśmy sformatowania wyniku na bardziej przejżysty i zaczynający się od 1 (a nie 0)
for i in enumerate(lista):
    print(i[0] + 1, "-", i[1])

print()

# metoda difference (różnica) dla zbiorów, lista też jest zbiorem. 
# Aby zadziałało na liście, trzeba ją przerobić na zbiór (set)

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2)) # zwraca różnice dla zbiorów
print(color_list_2.difference(color_list_1))
