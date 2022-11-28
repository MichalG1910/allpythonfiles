def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def apply(fn, a, b):
    return fn(a, b)

r1 = apply(add, 4, 5)
r2 = apply(multiply, 4, 8)
print(r1, r2)