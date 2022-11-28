
class Czlowiek:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw(self):
        print("Nazywam się " + self.imie)

    @classmethod                   # tak tworzymy metodę klasy
    def nowy_czlowiek(cls, imie):  #  argument cls działa podobnie jak self (jest on domyślny, nie wywołujemy go w obiekcie)
        return cls(imie)

    @staticmethod                  # metoda statyczna (nie przyjmuje żadnego domyślnego argumentu cls jak klasyczna metoda klasy)
    def przywitaj(arg):            # pierwszy argument w metodzie(tu arg) wywołujemy w obiekcie
        print("Cześć " + arg)
    
# standardowe utworzenie obiektu wyglądało by tak: cz1 = Czlowiek() 
cz1 = Czlowiek.nowy_czlowiek("Sebastian") # tworzymy obiekt- inacze jak do tej pory opieramy go na metodzie klasy
cz1.przedstaw()                           # @classmethod (nowy_czlowiek). Taki obiekt nabywa możliwość tworzenia kolejnych obiektów
cz2 = cz1.nowy_czlowiek("Adrian")         # tworzymy drugi obiekt na bazie pierwszego obiektu cz1
cz2.przedstaw()
Czlowiek.przywitaj("przyjacielu!")
cz2.przywitaj("chłopcze!")
