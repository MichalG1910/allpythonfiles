from klasa10dekoratory_statyczneklasowe import Numbers
from klasa101dekoratory_statyczneklasowe import Animal

przykład = Numbers() # tworzymy obiekt (klasa Numbers)

przykład.addNumber(3)  # korzystając z def add.number() dodajemy elementy do naszej listy self.numbers = numbers
przykład.addNumber(5)
przykład.addNumber(6)
przykład.addNumber(7)
przykład.addNumber(8)
przykład.addNumber(13)
przykład.addNumber(2)

print(przykład.sumNumbers()) # korzystamy z naszych def z klasy Numbers
print(przykład.multiNumbers())

print(Numbers.subtractNumbers(15, 5)) # metoda statyczna - korzystamy z naszej klasy pomijając tworzenie instancji(obiektu)

print("Pole w klasie:")
print(przykład.my_numbers) # 10
print(Numbers.my_numbers) # 10

print("Zmienione przez classmethod:")
Numbers.printInformation() # metoda klasyczna możę pobierać dane z naszej klasy
# nasz printInformation() ma cls.my_numbers +=1, więc dodaje 1 do pola my_numbers
# po wywołaniu metody klasycznj printInformation() każde odniesienie do my_numbers będzie +1  
print("Pole w klasie:")
print(przykład.my_numbers) # 11
print(Numbers.my_numbers) # 11

print("----------------------------------------------------------------")

kot1 = Animal(Animal,"Łapek") # Tworzymy obiekt. Ponieważ metoda klasowa ma wbudowany inicjalizator( a nie klasa głowna)
kot2 = Animal(Animal,"Łapek") # tworząc obiekt na klasie Animal, musimy dla naszej  @classmethod podać rownież, że korzysta ona z klasy Animal
kot3 = Animal(Animal,"Łapek")
kot4 = Animal(Animal,"Łapek")
kot5 = Animal(Animal,"Łapek")

print(kot5.howManyAnimal) # metoda cls.howManyAnimal po każdym utworzonym obiekcie będzie zwiększała o 1 nasze pole(zmienną) howManyAnimal 
                          # znajdującą się bezpośrednio w naszej klasie






