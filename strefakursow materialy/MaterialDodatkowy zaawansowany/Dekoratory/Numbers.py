class Numbers:

    my_numbers = 10

    def __init__(self, numbers = []):
        self.numbers = numbers

    def sumNumbers(self):
        summary = 0
        for x in self.numbers:
            summary += x
        return summary

    def multiNumbers(self):
        product = 1
        for x in self.numbers:
            product *= x
        return product

    def addNumber(self, number):
        self.numbers.append(number)

    @staticmethod
    def subtractNumbers(a,b):
        return a - b

    @classmethod
    def printInformation(cls):
        print("Jestem class method")
        print("Na rzecz klasy", cls.__name__)
        cls.my_numbers +=1