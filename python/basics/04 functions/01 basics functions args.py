
def addNumbers(a,b):  # definiujemy funkcę (def), addNumbers - nazwa nowej funkcji, (a,b) - argumenty funcji
    return a + b      # funcja zwróci nam sumę a + b 
print(addNumbers(3,4))# 7 - wywołanie funkcji

def subNumbers(a,b): 
    return a - b

def multiplyNumbers(a,b):
    return a * b

def add4numbers(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    return result   # funkcja zwróci nam zmienną, która będzie sumą argumentów tej funkcji

print(addNumbers(10,5)) # 15

number = subNumbers(100,56)
print(number) # 44

number = multiplyNumbers(33,4)
print(number) # 132

sum = add4numbers(1, number, addNumbers(10,6), 9)
print(sum) # 158



# domyślne wartości funkcji - w funkcji z góry możemy ustalić domyślne argumenty, ktore zostaną wykonane, jeżeli
# odniesienie do naszej funkcji(wykonanie jej) nie będzie ich zawierało

def printCar(brand, name = "concept", year = 1960, color = "black"):
    print(brand, name, year, color)

printCar("Ford") # podanie tylko 1 parametru powoduje, że 3 kolejne są dodawane domyślne (takie jak w funkcji)
                 # wynik: Ford concept 1960 black
printCar("Ford", "Mustang") # wynik: Ford Mustang 1960 black
printCar("Ford", "Mustang", 1970) # wynik: Ford Mustang 1970 black
printCar("Ford", "Mustang", 1970, "red") # wynik: Ford Mustang 1970 red

def fn(a=0, b=0):
    print(a + b)

fn() # 0
fn(4) # 4
fn(4,6) # 10

print()

def fn(a, *args, **dict_args): # *args - możemy wprowadzić dowolną ilość argumentów, zostaną one wyświetlone w postaci krotki (tuple)
                               # **dict_args - możemy wprowadzić dowolną ilość kluczy i wartości, zostaną one wyświetlone w postaci sownika (dictionary)
    print(a)      # 3
    print(args)   # (6, 8, 9, True, 'cx')
    print(args[0])   # 6
    print(dict_args)   # {'user': 'admin', 'hasło': 'password'}

fn(3, 6, 8, 9, True, "cx", user = "admin", hasło = "password")

print()

def fn(a, *args, **dict_args): # w takiej funkcji możemy argumenty *args i **dict_args iterować za pomoća pętli for  

    print(a)  
    for arg in args:
        print(arg)
    for key in dict_args:
        print(dict_args[key])

# 3
# 6
# 8
# 9
# True
# cx
# admin
# password


fn(3, 6, 8, 9, True, "cx", user = "admin", hasło = "password")

print()

def fn(a, b):
    return a + b, a * b, a - b # instrukcja return zwraca kilka wartości i zostaną one zwrócone w postaci krotki
# pamiętaj, że return konczy działanie funcji i wszystko co będzie poniżej return nie zostanie wykonane
result = fn(3, 4)
print(result) # (7, 12, -1)

print()

# funkcja też jest obiektem, więc funkcja dir wywołana do naszej funkcji fn wyświetli nam listę wszystkich 
# dostępnych metod dla tej funkcji (podobnie jak przy zmiennej)

print(dir(fn)) 
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__',
#  '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__',
#  '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__',
#  '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

def add(x :int = 0, y :int = 0) -> str: # możemy określić podpowiedź jaki typ powinien mieć argument funkcji(otrzymamy podpowiedz w tyrakcie korzystania z funkcji)
    return str(x + y)                   # jeśli wprowadzimy inny typ argumentu, funkcja i tak się wykona 

print(add(10, 10)) # 20

print(add.__name__) # add - __name__ - wyświetlinazwę naszej funkcji
print(add) # <function add at 0x00316348> - pokaże adres naszej funkcji

def function_generator(nochange, ifUpper):
    def repeatText(text, how_many_repeat = 1):
        return text * how_many_repeat
    def repeatUpper(text :str, how_many_repeat = 1):
        return text.upper() * how_many_repeat
    def repeatLower(text :str, how_many_repeat = 1):
        return text.lower() * how_many_repeat

    if nochange: # jeżeli nochange = True 
        return repeatText # wykona się
    else: # jeżeli nochange = False
        if ifUpper: # jeżeli ifUpper = True
            return repeatUpper # wykona się
        else: # jeżeli ifUpper = False
            return repeatLower # wykona się

functionUpper = function_generator(False, True)
print(functionUpper("Michał Grabarz ", 2)) # MICHAŁ GRABARZ MICHAŁ GRABARZ

functionLower = function_generator(False, False)
print(functionLower("Michał Grabarz", 2)) # michał grabarzmichał grabarz


