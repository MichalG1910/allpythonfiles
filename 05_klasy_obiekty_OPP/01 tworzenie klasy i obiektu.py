# OPP - object oriented programming
# klasa jest to zbiór zmiennych i funcji (w klasach nazywanych metodami), które tworzą gotowy szablon rozwiązań, które możemy wykorzystać do stworzenia np. obiektu

class czlowiek:
    imie = "sebastian"
    def przedstawSie(self):
        return "Cześć, mam na imie " + self.imie
# zmienne i definicje funkcji zawarte w klasie stają się metodami dla obiektów, które utworzymy na ich bazie 

obiekt = czlowiek() # tworzymy odwołanie do naszej klasy czlowiek
print(obiekt.imie) # sebastian ( korzystamy ze zdefiniowanej przez nas metody imie)
print(obiekt.przedstawSie()) # Cześć, mam na imie sebastian ( korzystamy ze zdefiniowanej przez nas metody przedstawSie)
print(type(obiekt)) # <class '__main__.czlowiek'>

obiekt2 = czlowiek()
obiekt2.imie = "Adrian" # zmieniamy imie dla nowego obiektu obiekt2 
print(obiekt2.przedstawSie()) # Cześć, mam na imie Adrian
print(obiekt.przedstawSie()) # Cześć, mam na imie sebastian

print("____________________________________________1______________________________________________________\n")


class czlowiek1:
    imie = "sebastian"
    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + " , mam na imie " + self.imie
# w tym przypadku tworzymy zmienną powitanie, do ktorej będzie się odnosiła zdefiniowana przez nas funkcja przedstawSie
# NALEŻY PAMIETAĆ, ŻE DO PIERWSZEGO ARGUMENTU W NASZEJ ZDEFINIOWANEJ FUNKCJI(self) NIE MOŻEMY SIĘ ODNIEŚĆ. JEST ON TAK
# JAKBY ZABLOKOWANY. DO KAŻDEGO KOLEJNEGO JUŻ MOŻEMY TO ZROBIĆ PAMIĘTAJĄC, ŻE ODNOSIMY SIĘ DO NIEGO JAKBY BYŁ PIERWSZY
obiekt = czlowiek1() 
print(obiekt.przedstawSie()) # Cześć , mam na imie sebastian

obiekt2 = czlowiek1()
obiekt2.imie = "Adrian" 
print(obiekt2.przedstawSie()) # Cześć , mam na imie Adrian
print(obiekt.przedstawSie("Witaj")) # Witaj , mam na imie sebastian
print(obiekt2.przedstawSie("Dzień dobry")) # Dzień dobry , mam na imie Adrian

print("______________________________________________2____________________________________________________\n")

class czlowiek2:
    def __init__(self, imie, wiek): # specjalna metoda inicjalizacji danych (konstruktor). Obiekt powstały w 
                                    # oparciu klasę z konstruktorem __init__ przejmuje jego parametry (bez self)
        self.imie = imie # zmienna self.imie (self odnosi się do pierwszego argumentu def __init__) to zmienna 
                         # globalna dla całej klasy, natomiast imie do zmienna lokalna dla def __init__
        self.wiek = wiek
    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + " , mam na imie " + self.imie + " lat " + str(self.wiek) + "."

obiekt = czlowiek2("Adam", 2) # jeżeli korzystamy  w klasie z konstruktora, to tworzony w oparciu o klasę obiekt 
                              # musi wykorzystać wszystkie zmienne (bez self) zawarte w tym konstruktorze 
                              # (innaczej wystąpi błąd) 
print(obiekt.przedstawSie())  # Cześć , mam na imie Adam lat 2.

obiekt2 = czlowiek2("Filip", 5) 
print(obiekt2.imie) # Filip
print(obiekt2.wiek) # 5
print(obiekt2.przedstawSie()) # Cześć , mam na imie Filip lat 5.
print(obiekt.przedstawSie("Witaj")) # Witaj , mam na imie Adam lat 2.
print(obiekt2.przedstawSie("Dzień dobry")) # Dzień dobry , mam na imie Filip lat 5.

print("____________________________________________3______________________________________________________\n")


# atrybuty klasy

class Point:
    points_counter = 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Point.points_counter += 1 #  spowoduje zwiększenie o 1 points_counter po każdym wywołaniu __init__
                                  # w praktyce każde utworzenie nowego obiektu na tej klasie wywoła tą funcję i 
                                  # points_counter się zwiększy (counter - z ang. licznik)
    
    def move_to_new_coords(self, x, y): # wywołanie tej metody w obiekcie pozwoli nadać nowe koordynaty obiektu(punktu)
        self.x = x
        self.y = y


p1 = Point(4,5)
p2 = Point(10,25)
print(p1.x, p1.y) # 4 5
print(p2.x, p2.y) # 10 25
print(Point.points_counter) # 2

p1.move_to_new_coords(1,1)
print(p1.x, p1.y) # 1 1

        


