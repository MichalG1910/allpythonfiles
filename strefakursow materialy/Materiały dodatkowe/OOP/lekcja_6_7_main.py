from lekcja_6_7 import *

kwadrat = Square(10)
prostokat = Rectangle(10, 20)

slownik = {
        "kwadrat":kwadrat,
        "prostokat":prostokat
        }

for key, figura in slownik.items():
    print(f"Pole {key} wynosi: ", figura.area())
    print(f"Obwod {key} wynosi: ", figura.perimeter())


