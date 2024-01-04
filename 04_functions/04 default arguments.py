# domylne wartości funkcji - w funkcji z góry możemy ustalić domyślne argumenty, ktore zostaną wykonane, jeżeli
# odniesienie do naszej funkcji(wykonanie jej) nie będzie ich zawierało

def printCar(brand, name = "concept", year = 1960, color = "black"):
    print(brand, name, year, color)

printCar("Ford") # podanie tylko 1 parametru powoduje, że 3 kolejne są dodawane domyślne (takie jak w funkcji)
                 # wynik: Ford concept 1960 black
printCar("Ford", "Mustang") # wynik: Ford Mustang 1960 black
printCar("Ford", "Mustang", 1970) # wynik: Ford Mustang 1970 black
printCar("Ford", "Mustang", 1970, "red") # wynik: Ford Mustang 1970 red

