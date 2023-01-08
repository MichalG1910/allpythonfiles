
# funkcja lambda - jednolinijkowa funkcja bez nazwy (użycie również: map, filter)
from functools import reduce # import funkcji reduce, aby można było z niej skorzystać
sum = lambda a,b: a + b

print(sum(4,5)) # 9
print(sum(14,5)) # 19
print(type(sum)) # <class 'function'>

def generateLambda(num):
    return lambda a: a * num # funkcja lambda przekazana do naszej definiowanej funkcji generateLambda

doubler = generateLambda(2) # doubler = lambda a: a * 2
print(doubler(4)) # 8

print("______________________________________________________________________________________\n")
# kilka sposobów zapisu jednej funkcji liczącej to samo (w tym przypadku kwadrat liczby) z wykorzystaniem lambda
# 1
def funkcja(f,liczba):
    return f(liczba)
print(funkcja(lambda x: x * x, 3))
# 2
def kwadrat(x):
    return x * x
print(kwadrat(3))
# 3
wyn = (lambda x: x * x)(3)
print(wyn)
# 4
wyn = lambda x: x * x
print(wyn(3))


print("______________________________________________________________________________________\n")


print(" ")

listData = [0,1,2,3]
result = list( map(lambda a: a * 3, listData)) # instrukcja map powoduje w tym przypadku przejście po każdym
print(result) # [0,3,6,9]                      # elemencie listData i wykonanie na nim funkcji lambda

def funkcja(a):                                # to samo co wyżej, tylko z użyciem def funkcji
    return a * 3
result = map(funkcja, listData)
print(list(result)) # [0,3,6,9]

print(" ")

result = list(filter(lambda a: a > 1, listData))# imstrukcja filter powoduje przejście po każdym elemencie listData
print(result) # [2,3]                           # i sprawdzeniu go, czy jest > 1. Jeśli tak, zwraca true, co 
                                                # powoduje że przekazywany jest on do naszej nowej listy result

result = reduce( lambda x,y: x + " " + y, ("Ola", "Ania", "baba")) # funkcja reduce redukuje nam w tym momencie listę 
print(result) # Ola Ania baba                                      # ("Ola", "Ania", "baba") do łańcucha znaków


# przykłady na filtr imion listy i na sumę elementów listy
print("\n inne przykłady \n ")

listData = ["ola", "włodzimierz", "benedykt", "kasia", "ania", "jarosław"]
result = filter( lambda x: len(x) <= 5, listData)# filtruje imiona i zwraca te, kóre mają 5 lub mniej liter
print(list(result)) # ['ola', 'kasia', 'ania']

numSum = reduce( lambda x,y: x + y, [0,1,2,3,4,5,6,]) # wynik będzie sumą elementów listy [0,1,2,3,4,5,6,]
print(numSum) # 21
print(type(numSum))

kwadrat_liczby = sorted(range(-5,13), key = lambda x: x**2) # [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, 6, 7, 8, 9, 10, 11, 12]
print(kwadrat_liczby)

#Funkcja ta, jak sama nazwa wskazuje, służy do sortowania. Warto zauważyć, że sorted() zwraca listę, chociaż jako argument przyjmuje obiekt iterowalny.
print(sorted("AnalityK")) # ['A', 'K', 'a', 'i', 'l', 'n', 't', 'y']

print(sorted("Analityk", reverse=True)) # ['y', 't', 'n', 'l', 'k', 'i', 'a', 'A'] - parametr reverse sortuje wszystko w odwrotnej kolejności 

print(sorted(["ac", "aa", "az", "azz", "azb", "abc", "aba"])) # ['aa', 'aba', 'abc', 'ac', 'az', 'azb', 'azz']