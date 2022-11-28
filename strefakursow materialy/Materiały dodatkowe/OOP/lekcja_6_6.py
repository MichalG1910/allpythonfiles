class Animal:

    def __init__(self, age, name):
        self.name = name
        self.age = age

    def print_information(self):
        print(self.age)
        print(self.name)

    def give_voice(self):
        raise NotImplementedError()

class Mammal(Animal):

    def __init__(self, age, name):
        Animal.__init__(self, age, name)

    def go_to(self):
        print("go go go")

    def print_information(self):
        Animal.print_information(self)
        print("I'm a mammal")

class Boy(Mammal):

    def __init__(self, age, name, surname):
        Mammal.__init__(self, age, name)
        self.surname = surname

    def give_voice(self):
        print("Littel Boy wants to play.")

    def print_information(self):
        Mammal.print_information(self)
        print(self.name)
        print(self.surname)
        print("I'm a boy")
