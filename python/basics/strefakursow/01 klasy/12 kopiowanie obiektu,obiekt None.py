import copy

class MyClass:
    def __init__(self):
        self.a = 0

obiekt = MyClass()
obiekt2 = copy.copy(obiekt) # tworzenie kopii obiektu

print(id(obiekt)) # 2262127195424
print(id(obiekt2)) # 2262127194800

def example(x):
    if x > 0:
        return True
    elif x < 0:
        return False
    else:
        pass

a, b, c = example(3), example(-3), example(0) 

print(f"a: {a}, b: {b}, c: {c}") # a: True, b: False, c: None
print(type(c)) # <class 'NoneType'>
