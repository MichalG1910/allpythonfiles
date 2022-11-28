from klasa06dziedziczenie2 import *  # taki zapis też zaimportuje wszystko z naszego pliku modułu z naszymi klasami
kwadrat = Square(10)
prostokat = Rectangle(10, 20)

slownik = {
    "kwadrat":kwadrat,
    "prostokąt":prostokat
}

for key, figura in slownik.items():
    print(f"Pole {key} wynosi: ", figura.area())
    print(f"Obwód {key} wynosi: ", figura.perimeter())
# dla 1 iteracji:
# figura.area() jest to kwadrat.area
# figura.perimeter() jest to kwadrat.perimeter

# nasz obiekt kwadrat opart na klasie Square ma w tym funkcji __init__( self, a = 10)
# zapis z klasy Square(Rectangle) Rectangle.__init__(self, a, a) powoduje odziedziczenie
# z klasy Rectangle z __init__(self, a = 10, b = 10), więc wywołanie kwadrat.area
# 10 * 10 = 100.
# zapis z klasy Rectangle(Tetragon) Tetragone.__init__(self, a, b, a, b) powoduje odziedziczenie
# z klasy Tetragon  z __init__(self, a = 10, b = 10, c = 10, d = 10), więc wywołanie kwadrat.perimeter
# 10 + 10 + 10 + 10 = 40.

# kwadrat = Square(10)-->
# class Square(Rectangle): def __init__(self, a = 10):Rectangle.__init__(self, a = 10, a = 10) więc dziedziczy z class Rectangle -->
# class Rectangle(Tetragon): def __init__(self, a = 10, b = 10):Tetragon.__init__(self, a = 10, b = 10, a = 10, b = 10) więc dziedziczy z class Tetragon -->
# class Tetragon: def __init__(self, a = 10, b = 10, c = 10, d = 10)

# Rectangle.__init__(self, a, a) 
# Tetragon.__init__(self, a, b, a, b)
# zawarcie w klasie w def __init__ zapisów jak wyżej oznacza, że są one tak jakby danymi wejściowymi do 
# inicjalizatora klasy wyżej, z której mają dziedziczyć
