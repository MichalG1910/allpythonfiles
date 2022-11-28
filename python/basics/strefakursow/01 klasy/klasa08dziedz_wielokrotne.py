from abc import ABC, abstractmethod # korzystamy z klasy wbudowanej w python abc i metody abstractmethod

class DuckBehaviori(ABC):
   
    @abstractmethod
    def fly(self):
        print("Ja lecę")
    
    @abstractmethod
    def say(self):
        print("Kwa Kwa")

    @abstractmethod
    def go_to(self):
        print("Ide ide kaczym krokiem")

class Duck(DuckBehaviori):
    def __init__(self, age, breed): # breed - gatunek
        self.age = age
        self.breed = breed
    def fly(self):
        super().fly() # metoda super() spowoduje przeszukanie klasy matki i dopasowanie odpowiedniej funkcji fly()

    def say(self):
        super().say()

    def go_to(self):
        super().go_to()

class Toy:
    def __init__(self, material, color):
        self.material = material
        self.color = color

class DuckToy(Toy, DuckBehaviori):
    def fly(self):
        super().fly()

    def say(self):
        super().say()

    def go_to(self):
        super().go_to()

class Cat:
    def go_to(self):
        super().go_to()

# z zasady do klasy abstrakcyjnej nie możemy się odnieść bezpośrednio, możemy to zrobić przy pomocy funkcji super()
# definiujemy odpowiednie funkcje w klasie córce np. super().fly(), i wtedy możemy wykożystać z klasy matki 
# @abstractmethod def fly(self):






    

    