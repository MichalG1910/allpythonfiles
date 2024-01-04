from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        raise Exception("Unable to create object of a abstract class")
        
    def print_information(self):
        pass
    @abstractmethod   
    def give_voice(self):
        raise NotImplementedError() # definiujemy obsługę błędu, jeśli odniesiemy się do tej funkcji, to ją wywołamy

class Mammal(Animal): # mammal - ssak
    def __init__(self, age,name):
        self.name = name
        self.age = age

    def go_to(self):
        print("go go go")
    
    def print_information(self):
        print(self.name)
        print(self.age)
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
        