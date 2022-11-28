# Arguments order - 

# "/"- wszystkie argumenty przed slashem muszą zostać wprowadzone zgodnie z kolejnością w def funkcji 
        # i nie mogą być nazwane. / to parametr pozycyjny

# "*"- wszystkie argumenty po gwwiazdce muszą zostać wprowadzone jako argumenty nazwane 
        # ( i mogą być wprowadzone w różnej kolejności )

def printCar(brand, / ,name = "concept", * , year = 1960, color = "black"):
    print(brand, name, year, color)

printCar("Ford", "Mustang", year = 1963, color = "blue") # Ford Mustang 1963 blue
printCar("Ford", name = "Mustang", color = "blue", year = 1963) # Ford Mustang 1963 blue
# printCar(brand = "Ford", "Mustang", year = 1963, color = "blue") - błąd (przed "/" parametr nie może być nazwany)
# printCar("Ford", "Mustang", year = 1963, "blue") - błąd (po "*" parametr musi być nazwany)

print()

def funkcja(arg1, arg2 = "World!", *args, **kwargs): # * przed argumentem (*args) - oznacza to, że możemy podać dowolną 
# liczbę argumentów (lub żadnego), i trafią one do krotki (tak zostaną wyświetlone). Jeśli nie będzie żadnego,
# print wyświetli pustą krotkę (). 1 taki argument dostaje indrks po ostatnim określonym normalnie argumencie.
# ** przed argumentem (**args) - oznacza, że możemy dodać od 0 do nieskończenie wielu argumwntów w postaci 
# klucz : wartość i zostaną one wyświetlone jako słownik {dictionary}
    print(arg1, arg2, args, kwargs)
    print(len(args)) # możemy przy pomocy len wyświetlić ilość takich argumentów w krotce
    for x in args:   # możemy iterować po takiej krotce za pomocą pętli for
        print(x)
    for y,z in kwargs.items():   # możemy iterować po takim słowniku za pomocą pętli for
        print(y, ":", z)

funkcja("Hello") # Hello World! () {}
funkcja("Hi", "Youtube!") # Hi Youtube! () {}
funkcja("Hi", "Youtube!", "$$$", ":-)", autor = "Michał", rok = "2022") 
# Hi Youtube! ('$$$', ':-)') {'autor': 'Michał', 'rok': '2022'}
