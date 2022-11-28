def print_twice(a):     # def pozwala stworzyć własną funkcję (np. print_twice)
    print(str(a) + "    " + str(a) + "    " + str(a) + "    " + str(a))

from itertools import repeat
import math # import biblioteki math
print(" ")
print_twice("Pi = " + str(math.pi)) # odwołanie do naszej funkcji print_twice
print(" ")
reset = True
obliczane = ["pole", "obwód", "objętość", "promień"]

while True:
    if reset == True:
        działanie = str(input("Podaj co chcesz liczyć dla koła/kuli: " + str(obliczane)+ " " + "lub exit: "))

    if działanie == "exit": break

    if not działanie in obliczane:
        print("Wprowadzona operacja jest błędna!")
        continue
    
    def is_number(numTest):
        try:
            float(numTest)
            return True
        except ValueError:
            return False

    if działanie == "pole":
        promien = (input("podaj promień koła (cm): "))
        numTest = promien
        while is_number(numTest) == False:
            print("błędny promień, promień musi być liczbą rzeczywistą!!!")
            promien = (input("podaj promień koła (cm): "))
            numTest = promien
        else:
           result = math.pi * float(promien) ** 2
           print("Pole koła o promieniu " + str(promien) + " cm równe jest:\n" + str(result) + " cm kwadratowych") 
       
            
    
    if działanie == "obwód":
        promien = (input("podaj promień koła (cm): "))
        numTest = promien
        while is_number(numTest) == False:
            print("błędny promień, promień musi być liczbą rzeczywistą!!!")
            promien = (input("podaj promień koła (cm): "))
            numTest = promien
        else:
            result = 2 * math.pi * float(promien)
            print("Obwód koła o promieniu " + str(promien) + " cm równy jest:\n" + str(result) + " cm")
    
    if działanie == "objętość":
        promien = (input("podaj promień kuli (cm): "))
        numTest = promien
        while is_number(numTest) == False:
            print("błędny promień, promień musi być liczbą rzeczywistą!!!")
            promien = (input("podaj promień kuli (cm): "))
            numTest = promien
        else:
            result = (4/3) * math.pi * pow(float(promien),3)
            print("Objętość kuli o promieniu " + str(promien) + " cm równa jest:\n" + str(result) + " cm sześciennych")
    
    if działanie == "promień":
        zCzegoLiczysz = ["z pola", "z obwodu", "z objętości"]
        zCzego = str(input("Podaj, z czego chcesz policzyć promień" + str(zCzegoLiczysz) + ": "))
        
        if zCzego == "z pola":
            pole = (input("Podaj pole koła (cm kwadrat): "))
            numTest = pole
            while is_number(numTest) == False:
                print("błędne pole, pole musi być liczbą rzeczywistą!!!")
                pole = (input("Podaj pole koła (cm kwadrat): "))
                numTest = pole
            else:
                result = math.sqrt(float(pole)/ math.pi)
                print("Promień koła o polu " + str(pole) + " cm kwadratowych równy jest:\n" + str(result) + " cm")

        elif zCzego == "z obwodu":
            obwod = (input("Podaj obwód koła (cm): "))
            numTest = obwod
            while is_number(numTest) == False:
                print("błędny obwód, obwód musi być liczbą rzeczywistą!!!")
                obwod = (input("Podaj obwód koła (cm): "))
                numTest = obwod
            else:
                result = float(obwod)/(2 * math.pi)
                print("Promień koła o obwodzie " + str(obwod) + " cm równy jest:\n" + str(result) + " cm")

        elif zCzego == "z objętości":
            objetosc = (input("Podaj objętoć kuli (cm sześcienny): "))
            numTest = objetosc
            while is_number(numTest) == False:
                print("błędna objetość, objętość musi być liczbą rzeczywistą!!!")
                objetosc = (input("Podaj objętość kuli (cm sześcienny): "))
                numTest = objetosc
            result = pow(((3/4 * float(objetosc)) / math.pi), (1 / 3))
            print("Promień kuli o objętości " + str(objetosc) + " cm sześciennych równy jest:\n" + str(result) + " cm")












