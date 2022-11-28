class Animal:
    def __init__(self, age, name):
        self.name = name
        self.age = age
    def print_information(self):
        print(self.age)
        print(self. name)
    def give_voice(self):
        raise NotImplementedError() # definiujemy obsługę błędu, jeśli odniesiemy się do tej funkcji, to ją wywołamy

class Mammal(Animal): # mammal - ssak
    def __init__(self, age,name):
        Animal.__init__(self, age, name)

    def go_to(self):
        print("go go go")
    
    def print_information(self):
        Animal.print_information(self) # klasa Mammal dziedziczy print_information z klasy Animal
        print("I'm mammal")

class Boy(Mammal):
    def __init__(self, age, name, surname):
        Mammal.__init__(self, age, name)
        self.surname = surname

    def give_voice(self):
        print("Little boy wants to play.")

    def print_information(self):
        Mammal.print_information(self) # klasa Boy dziedziczy print_information z klasy Mammal(a klasa Mammal z klasy Animal) 
        print(self.surname)
        print("i'm a boy")
        