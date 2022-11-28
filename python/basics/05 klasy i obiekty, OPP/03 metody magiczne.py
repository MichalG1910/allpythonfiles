
import math

class punkt2D:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.odleglosc = math.sqrt(x**2 + y**2) # liczymy przeciwprostokątną trójkąta prostokątnego
                                                # a2+b2=c2 -> c=pierwiastek(a2+b2). (X , Y) jest to punkt
                                                # w układzie współrzędnych wiec c będzie to odległość do 
                                                # początku układu współrzędnych
    def __add__(self, drugi):
        return punkt2D(self.x + drugi.x, self.y + drugi.y) # definiujemy tak, aby policzyć p3 = p1 + p2

    def __lt__(self, drugi):                    # __lt__ - less then - mniejsze od
        return self.odleglosc < drugi.odleglosc

    def __le__(self, drugi):                    # __le__ - less equal - mniejsze rowne od
        return self.odleglosc <= drugi.odleglosc

    def __eq__(self, drugi):                    # __eq__ - equal - równe
        return self.x == drugi.x and self.y == drugi.y 

    def __len__(self):                          # __len__ - długość - w tym przypadku od początku układu współrz.
        return int(round(self.odleglosc, 0))
    
    def __str__(self):
        return f"współrzędna x: {self.x}, współrzędna y: {self.y}"

    def __repr__(self):
        text = repr(punkt2D) # wyświetli typ klasy i adres naszej klasy
        idobj = id(punkt2D) # wyświetli id naszego obiektu
        return f"typ: {text}\nid obiektu: {idobj}\nwspółrzędne punktu: {self.x}, {self.y}"


p1 = punkt2D(2, 5)
p2 = punkt2D(4, 5)
p3 = p1 + p2 # możliwe dzięki def __add__(self, drugi):
print(p3.x) # 6
print(p3.y) # 10

print()

print(p1.odleglosc) # 5.385164807134504
print(p2.odleglosc) # 6.4031242374328485
print(p1 < p2) # True, możliwe dzięki def __lt__(self, drugi):
print(p1 == p2) # False, możliwe dzięki def __eq__(self, drugi):
print(p2 == p2) # True,możliwe dzięki def __eq__(self, drugi):

print()

print(len(p3)) # 12, możliwe dzięki def __len__(self): 
print(p3.odleglosc) # 11.661903789690601

print(p1) # współrzędna x: 2, współrzędna y: 5 , możliwe dzięki def __str__(self):
print(repr(p1)) # typ: <class '__main__.punkt2D'>
                # id obiektu: 2977001692512
                # współrzędne punktu: 2, 5

# MAGICZNE METODY

# __init__ - # specjalna metoda inicjalizacji danych (konstruktor). Obiekt powstały w oparciu klasę z 
             # konstruktorem __init__ przejmuje jego parametry (bez self)
# __add__ - dodawanie
# __lt__ - less then - mniejsze od
# __le__ - less equal - mniejsze rowne od
# __eq__ - equal - równe
# __gt__ - grader then - większe od
# __ge__ - grader equal - wieksze rowne od
# __ne__ - not equal - różne od
# __eq__ - equal - równe
# __len__ - długość 
# __del__ - delete - metoda wykonywana jest na sam koniec skryptu i służy wyczyszczeniu pamięci.
# __new__ - (przeznaczony dla zaawansowanych programistów)
# __str__ - Metoda __str__ odpowiedzialna jest za zwrócenie tekstu zdefiniowanego podczas tworzenia klasy.
# __repr__ zwraca reprezentację danego obiektu w postaci łańcucha znaków
