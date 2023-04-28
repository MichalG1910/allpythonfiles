class Obiekt:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __eq__(self, other): # metoda porównuje 1 obiekt do drugiego (adresy ich)
        return self.value1 == other.value1 and self.value2 == other.value2 # taki zapis spowoduje, że porównywane będą wartości obiektów

    def __str__(self): # metoda przy wydruku obiektu powoduje wyświetlenie jego typu i adresu
        return f"value1: {self.value1}, value2: {self.value2}" # nadpisanie spowoduje odpowiednie wyświetlenie danych

    def __repr__(self):
        text = repr(Obiekt) # wyświetli typ klasy i adres naszego klasy
        idobj = id(Obiekt) # wyświetli id naszego obiektu
        return f"{text} {idobj}\nvalue1: {self.value1}, value2: {self.value2}"

obiekt1 = Obiekt(1,2)
obiekt2 = Obiekt(1,2)

print(obiekt1 == obiekt2) # True - gdyby nie było metody __eq__, byłoby False
print(obiekt1) # value1: 1, value2: 2
print()
print(repr(obiekt1)) # <class '__main__.Obiekt'> 2119270505120
                     # value1: 1, value2: 2


print()

print(id(obiekt1)) # 2284623413200
print(id(obiekt2)) # 2284623412912
