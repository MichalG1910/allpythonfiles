
data = ("Ala", "Ola", "Kasia") # krotka(inaczej tablica), jest niemutowalna, nie można jej zmieniać ani edytować
                               # data[0]="Rafał" - pokaże błąd
names = data + ("Rafał",) # ('Ala', 'Ola', 'Kasia', 'Rafał')
print(names)
print(len(names)) # 4
print(type(names)) # <class 'tuple'>

numbers = 1, 2, 3 # krotkę można utworzyć bez nawiasów, jeśli ma ona posiadać kilka elementów
print(numbers)
print(type(numbers))

emptyTuple = () # pusta krotka
print(emptyTuple)
print(type(emptyTuple))

print(names[1]) # Ola
print(names[-1]) # Rafał - wyświetla od końca krotki
print(names[1:3]) # ('Ola', 'Kasia')

cars = (("Dodge", "Ford"), ("Pontiac",)) # krotka złożona z 2 krotek
print(cars[0][0]) # wyświetli Dodge
print(cars[0][1]) # wyświetli Ford
print(cars[1][0]) # wyświetli Pontiac

if "Ford" in cars[0]:
    print("Ford jest w krotce nr 1")

    del cars # kasowanie krotki, odniesienie się do nie po skasowaniu wywoła błąd
    # print(cars) - wyświetli błąd, kod nie zadziała
    # del names[0] - wyświetli błąd, kod nie zadziała. Nie można skasować elementu krotki, KROTKA JEST NIEMUTOWALNA

tupleX3 = names * 3 # zwielokrotnienie krotki razy 3
print(tupleX3)
