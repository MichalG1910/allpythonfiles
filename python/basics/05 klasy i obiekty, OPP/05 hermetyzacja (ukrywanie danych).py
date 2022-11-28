print("1 ------------------------------------------------------------\n")
class Test:
    _lista = []                     # _ podkreślenie oznacza, że lista jest prywatna (jest to tylko informacja,
    def dodaj(self, arg):           # (dalej możemy się do niej odnieść poza klasą)
        self._lista.append(arg)

    def zdejmij(self):
        if len(self._lista) > 0:
            return self._lista.pop(len(self._lista) - 1) # usuwa ostatni argument listy (pop)
        else:
            return

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj._lista.append("X") # zastosowanie _ podkreślenia powoduje, że możemy (w tym przypadku) dodać "X" do listy
print(obj._lista) # ['A', 'B', 'C', 'X']
print(obj.zdejmij()) # X
print(obj._lista) # ['A', 'B', 'C']

print("\n2 -----------------------------------------------------------\n")

class Test1:
    __lista = []                     # __podkreślenie oznacza, że lista jest prywatna (jest to tylko informacja,
    def dodaj(self, arg):           # (dalej możemy się do niej odnieść poza klasą)
        self.__lista.append(arg)

    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) - 1) # usuwa ostatni argument listy (pop)
        else:
            return

obj = Test1()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
# obj.__lista.append("X") # zapis nieprawidłowy, wywoła błąd
obj._Test1__lista.append("X") # zastosowanie odwołania do klasy _NAZWAKLASY (w naszym przypadku _Test1) daje nam 
                              # możliwość odniesienia się do naszej listy (utworzonej w klasie) poza klasą
print(obj.zdejmij()) # X
print(obj._Test1__lista) # ['A', 'B', 'C']
# print(obj.__lista) # zapis nieprawidłowy, wywoła błąd

# nie zastosowanie _Test1 w metodzie obj.__lista.append("X") spowoduje wywołanie błędu. W jakimś stopniu 
# zabezpiecza nam to naszą listę przed ingerencją w nią z poza klasy (trzeba wiedzieć czego użyć aby to zrobić)
# Daje to nam namiastkę hermetyzacji (ukrywania danych) w klasie