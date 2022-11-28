class Func:

    def __init__(self, value):
        self.value = value

    def __call__(self, times):
        if type(self.value) == int:
            return self.value * times
        elif type(self.value) == str:
            return self.value * times
        else:
            return self.value

liczba = Func(4)
print(liczba(10))

napis = Func("_Piotr Koska_")
print(napis(6))