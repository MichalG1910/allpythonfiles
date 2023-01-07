
# scope - zasięg zmiennej
number = 12 # zmienna globalna
def test1():
    print(number) # odwołamy się do zmiennej globalnej number
test1() # 12

print(" ")

def test2():
    number = 100 # utworzymy zmienną lokalną dostępną tylko z poziomu funkcji test2(), dla tej funkcji przesłoni 
                 # ona zmienną globalną
    print(number)
    if 1 == 1:
        print(number) # 100
        if 2 == 2:
            number = 50 # w tym przypadku zmieniamy tylko lokalną wartość zmiennej number (z funcji test2)
            print(number) # 50
    print(number)

test2() # 100 - odwołnie do zmiennej lokalnej zdefiniowanej w funkcji
print(number) # 12 - odwołanie do zmiennej globalnej

print(" ")

print("\n test3")
def test3():
    global number # odwołanie do zmiennej globalnej number - w takim wypadku zdefiniowanie zmiennej w funcji test3
    number = 5 # o nazwie number zmieni nam zmienną globalną, a nie utworzy lokalną na potrzeby zdefiniowanej funcji
    print("test3: ", number) # test3:  5
    if 3 == 3:
        number = 6
        print("test3: ", number) # test3:  6
test3()
print("global number after test 3: ", number) # global number after test 3: 6 

print(" ")

print("\n test4")

number = 10
def test4(number):
    print("test4 parametr: ", number) # test4 parametr:  33
    number = 20
    print("test4 after change: ", number) # test4 after change:  20
test4(33)
print("global number after test4: ", number) # global number after test4:  10

print(" ")

print("\n test5")

number = 10
def foo():
    print("foo() number: ", number) # foo() number: 10

def bar():
    number = 9
    print("bar() number: ", number) # bar() number: 9
    foo()

bar()
print("global number after foo() bar()", number)

print(" ")

print("\n check1 & check2")

number = 10
def check1():
    number = 12
    print("check1() number: ", number) # check1() number: 12
    def check2():
        print("check2() number: ", number) #  check2() number: 12
    check2()

check1()
print("global number after check1()", number)

print(" ")

print("\n if test")

if 1 == 1:
    data = 100 # utworzy zmienną globalną

print("data in global scope: ", data)

if 2 == 1:
    nextData = 15 # zmienna się nie utworzy ponieważ instrukcja if jest False (a wymaga True) 

# print("nextData in global scope: ", nextData) # name 'nextData' is not defined - odniesienie do zmiennej, 
                                                # która nie została zdefiniowana, ponieważ instrukcja if była 
                                                # Fail wygeneruje błąd






