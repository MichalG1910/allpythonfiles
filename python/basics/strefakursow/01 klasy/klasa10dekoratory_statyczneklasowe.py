
class Numbers:

    my_numbers = 10

    def __init__(self, numbers = []):
        self.numbers = numbers

    def sumNumbers(self): # funkcja ma zsumować wszystkie elementy listy self.numbers
        summary = 0
        for x in self.numbers:
            summary += x
        return summary

    def multiNumbers(self): # przemnoży przez siebie wszystkie elementy listy self.numbers
        product = 1
        for x in self.numbers:
            product *= x
        return product

    def addNumber(self, number): # funkcja pozwoli dodać argumenty do listy self.numbers 
        self.numbers.append(number)

    @staticmethod # tworzymy funkcję(metodę) statycznie. Będziemy mogli z niej korzystać bez tworzenia instancji(obiektu)
    def subtractNumbers(a,b):
        return a - b

    @classmethod # metoda klasowa może uzyskać dane z naszej klasy (w odróżnieniu od @staticmethod )
    def printInformation(cls): # (cls) - musi być w metodzie, żeby mogła uzyskać dane z naszej klasy
        print("Jestem class method")
        print ("na rzecz klasy", cls.__name__) # cls.__name__ - wyświetli nazwę naszej klasy
        
        cls.my_numbers +=1 # w metodzie klasycznej możemy odnosić się do pól z naszej klasy np. my_numbers i je zmieniać


