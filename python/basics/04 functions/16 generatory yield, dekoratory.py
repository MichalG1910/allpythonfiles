

# generator yield
from tkinter import N


def gen():
    i = 0
    while i < 5:
        yield i # generator yield - zwraca wynik funkcji while, ale w odróżnieniu od return nie przerywa 
        i += 1  # działania funkcji
for i in gen(): # taka iteracja po zdefiniowanej przez nas funkcji jest możliwa tylko, gdy w definiowanej 
    print(i)    # funcji użyjemy pętli z generatorem yield

print(list(gen())) # [0, 1, 2, 3, 4] - chcąc wyświetlić wynik funkcji gen musimy dodać ją do jakiejś kolekcji (np listy). W innym 
# razie funkcja print wyświetli nam informację o przechowaniu w pamięci wyniku tej funkcji 
# <generator object gen at 0x000001C660301EE0>

print()

def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0: # sprawdzi wszystkie argumenty czy są parzyste (reszta z dzielenia przez 2 = 0)
            yield i
        i += 1
for i in parzyste(16):
    print(i) 
print(list(parzyste(16))) # [0, 2, 4, 6, 8, 10, 12, 14, 16]

print(" ")

print()

def number_generator(end):
    n = 1
    while n < end:
        yield n
        n += 1

values = number_generator(25)
print(next(values)) # 1 - aby wywołać generator stosujemy funkcję next. Każde jej użycie generuje wykonanie 
print(next(values)) # 2- ednego obejścia i generuje 1 liczbę z naszego zakresu funkcji number_generator
print(next(values)) # 3
print(next(values)) # 4
print(next(values))

print()

# dekoratory
def decorator(func): # tworzymy naszą funkcję z dekoratorem
    def wrapper():
        print("------------")
        func()
        print("------------")
    return wrapper
def hello(): # tworzymy funkcję zwracającą dowolny string
    print("hello world")

hello = decorator(hello) # tworzymy obiekt na naszej def decorator
hello() # ------------
        # hello world
        # ------------

print()

@decorator  # można też tak odnieść się do naszego dekoratora  
def witaj():
    print("witaj świecie")

witaj() # ------------
        # witaj świecie
        # ------------

print()

witaj2 = witaj
witaj()


        
    