
class Animal:                       # klasa bazowa (rodzic)
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):                  # klasa dziedzicząca (dziecko) od klasy animal
    def voice(self):
        print("How How")

class Wolf(Dog):                    # klasa wolf dziedziczy od klasy Dog (i przez klasę Dog od klasy Animal)
    def getVoice(self):
        print("Jestem wilkiem, ")
        super().voice()             # super - funkcja przeszukuje klasę bazową w poszukiwaniu metody (voice)

class Cat(Animal):
    def getVoice(self):
        print("Meow Meow")

dog = Dog("Reksio", 10) # tworzymy obiekt oparty na klasie Dog, jednak ma on też dostępne metody 
                        # (name, age) z klasy bazowej Animal
print(dog.name) # Reksio
print(dog.age) # 10
dog.voice() # How How

print("-------------------------------------------------------------------------------")

cat = Cat("Klakier", 7)

print(cat.name) # Klakier
print(cat.age) # 7
cat.getVoice() # Meow Meow

print("-------------------------------------------------------------------------------")

wolf = Wolf("Geralt", 25)
print(wolf.name)# Geralt
print(wolf.age) # 25
wolf.getVoice() # Jestem wilkiem, How How
        