from abc import ABC, abstractmethod

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

    def __init__(self, age, breed):
        self.age = age
        self.breed = breed

    def fly(self):
        super().fly()

    def say(self):
         super().say()

    def go_to(self):
         super().go_to()

class Toy:

    def __init__(self, material, color):
         self.color = color
         self.material = material

class DuckToy(Toy, DuckBehaviori):

    def fly(self):
        super().fly()

    def say(self):
        super().say()

    def go_to(self):
        super().go_to()

class Cat():

    def go_to(self):
        super().go_to()
