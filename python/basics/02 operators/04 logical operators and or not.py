
import os
# logical operators (operatory logiczne)- and(i), or(lub) not(nie)

print( True and True) # True
print( True and False) # False
print( False and True) # False
print( False and False) # False
# operator and zwraca True tylko jeśli po obu stronach jest True

print ( 10 >= 5 and 3 < 9) # True
print ( 12 < 20 and 5 < 3) # False
print ( 10 == 5 and 3 >= 9) # False

taskCompleted = True
linesOfCodeWritten = 100

if taskCompleted == True and linesOfCodeWritten >= 50:
    print("Go home")
hourOfDay = 15
if taskCompleted == True and linesOfCodeWritten >= 60 and hourOfDay >= 15:
    print("Go home")

# or
print( True or True ) # True
print( True or False ) # True
print( False or True ) # True
print( False or False ) # False
# operator or zwraca True jeśli warunek po jednej stronie jest spełniony

print ( 10 >= 5 or 3 < 9) # True
print ( 12 < 20 or 5 < 3) # True
print ( 10 != 10 or 3 >= 9) # False

if 10 > 5 or "Ania" != "Ola":
    print( "True or True" )

if 3 == 5 or "Ania" == "Ola":
    print ( "False or False" ) # nie zostanie wyświetlone ponieważ oba warunki są False

# not
print( not True) # False
print( not False) # True
# odwraca znaczenie warunku i wyświetla przeciwne

print( not( 3 == 3 ) ) # False
print( not( 5 > 10 ) ) # True
print( not( 10 >= 5 and "Ania" != "Ola")) # False

taskCompleted = False
if taskCompleted == True: # operator if żeby zostal spełniony oczekuje wartości True, więc warunek nie jest spełniony
    print("go home")      # i nie zostanie wyświetlony

if not taskCompleted:     # jeśli taskCompleted jest "false", operator "not" go odwraca na "true" i wtedy warunek
    print("Stay a bit longer and finish") # if jest spelniony i wyrażenie zostanie wyświetlone

input("ENTER ---> dalej")
os.system("cls")

print("------------------------------------------------------------------------")

# program wykorzystujący operatory and or not. Zwróć uwagę na różnice wykorzystania if elif else
# jeśli daz same if to program będzie je wykonywał po kolei(mimo wykonania którejś instrukcji)
# jeśli dasz if  a poźniej elif, jeśli wykona if to elif nie zostanie wykonana 
while True:
    exit = input(str("exit? t jeśli tak: "))
    if exit == "t": break
    
    imie = input("podaj imie: ")
    nazwisko = input("podaj nazwisko: ")
    imieNieznane = imie or "NN"
    nazwiskoNieznane = nazwisko or "NN"

    if not imie and not nazwisko:
        os.system("cls")
        print("Nie ma imienia i nazwiska")
        print("imie: {}, nazwisko: {}".format(imieNieznane, nazwiskoNieznane)) # zapis kompatybilny z python 2
        
    elif imie and nazwisko:
        os.system("cls")
        print("imie: ", imieNieznane, ", ","nazwisko: ", nazwiskoNieznane) # python 3

    else: 
        os.system("cls")
        print("Niepełne dane osobowe!")
        print("imie: {}, nazwisko: {}".format(imieNieznane, nazwiskoNieznane))
    
    input("\nENTER ---> dalej")
    os.system("cls")




