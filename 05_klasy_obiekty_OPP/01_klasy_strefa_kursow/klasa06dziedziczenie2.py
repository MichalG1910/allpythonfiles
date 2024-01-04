class Tetragon: #tetragon z ang. czworobok
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def perimeter(self): # perimeter z ang. obwód
        return self.a + self.b + self.c + self.d

    def area(self):
        pass

class Rectangle(Tetragon): # rectangle z ang. prostokąt
    def __init__(self, a, b):
        Tetragon.__init__(self, a, b, a, b)
    
    def area(self):
        return self.a * self.b

class Square(Rectangle): # square z ang. kwadrat
    def __init__(self, a):
        Rectangle.__init__(self, a, a)

    

    

