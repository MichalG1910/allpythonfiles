class Obiekt:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __eq__(self, other):
        return self.value1 == other.value1 and self.value2 == other.value2

    def __str__(self):
        return f"value1: {self.value1}, value2: {self.value2}"

    def __repr__(self):
        text = repr(Obiekt)
        idobj = id(Obiekt)
        return f"{text} {idobj}\nvalue1: {self.value1}, value2: {self.value2}"

obiekt1 = Obiekt(1,2)
obiekt2 = Obiekt(1,2)

print(obiekt1 == obiekt2)
print(obiekt1)
print(repr(obiekt1))
#print(id(obiekt1))
#print(id(obiekt2))
