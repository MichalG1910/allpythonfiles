
class Func:
    def __init__(self, value):
        self.value = value

    def __call__(self, times): # __call__ - metoda powoduje, że obiekt, ktory utworzymy będzie można wywołać jak funkcję
        if type(self.value) == int:
            return self.value * times
        elif type(self.value) == str:
            return self.value * times
        else:
            return self.value


liczba = Func(4)
print(liczba(10)) # 40 - wywołujemy obiekt jak funkcję (__call__). W tym przypadku times = 10

napis = Func("_Michał Grabarz_")
print(napis(6)) # _Michał Grabarz__Michał Grabarz__Michał Grabarz__Michał Grabarz__Michał Grabarz__Michał Grabarz_