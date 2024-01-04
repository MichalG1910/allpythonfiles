# przypomnienie
print("Hello " + "World!") # Hello World!
print("Hello " * 3) # Hello Hello Hello

string = "Hello World!"
print( string[0]) # H - podaje pierwszy znak w łańcuch znaków (numerowane od 0)
print( string[2:10]) # llo Worl - podaje rzeczywisty zakres od 3 do 9

print( "Hello" in string) # True - czy hello jest w łańcuchu znaków (zmiennej string)
print( "Hello" not in string) # False - czy hello niema w łańcuchu znaków (zmiennej string)

multiline = """line 1
line 2
line 3
"""
print(multiline)
# koniec przypomnienia

print(" ")

string = "Hello World!"

print("ala".capitalize()) # Ala - zamienia pierwszą literę łańcucha znaków na wielką
print("ola ma kota, ola ma psa".count("ola")) # 2 - sprawdza ilość wystąpienia słowa w łańcuchu znaków
print(" Hello ".center(112,"*")) # centruje łańcuch znaków(112 - ilość znaków w nowym łańcuchu, * -dodatkowe znaki) 
# **************************************************** Hello *****************************************************
print("ola ma kota, ola ma psa".title()) # Ola Ma Kota, Ola Ma Psa - każdy ciąg po białym znaku z wielkiej litery

print( string.startswith("Hello")) # True - czy łańcuch znaków string zaczyna sie łańcuchem Hello
print( string.endswith("World!")) # True - czy łańcuch znaków string kończy sie łańcuchem World!

print(" ")

print(string.find("l")) # 2 -  szuka l w łańcuchu string i zwraca indeks wystąpienia 
print(string.find("Ola")) # -1 -  szuka wyraz Ola w łańcuchu znaków string, jeśli nie ma zwraca wynik: -1 
print(string.find("World")) # 6 - zwraca jego początek w łańcuchu znaków ("W" jest 6 licząc od 0)
pozycjaLitery = string.find("d")
print("Pozycja liter d: {}".format(pozycjaLitery)) # Pozycja liter d: 10
print("10 litera w naszym stringu to: {}".format(string[10])) # 10 litera w naszym stringu to: d
print("ola ma psa, ola ma kota".find("ola")) # 0
print("ola ma psa, ola ma kota".rfind("ola")) # 12 - rfind - rozpoczyna szukanie od prawej strony łańcucha znaków,
                                              # zwraca początek zaczynając od 0 od lewej strony łańcucha

print(" ")

print( "23456789".isalnum()) # True - sprawdza, czy łańcuch znaków składa sie z samych liter i cyfr
print( "23456789.5".isalnum()) # False
print( "23456789 ".isalnum()) # False
print( "23456789 k".isalnum()) # False
print( "23456789kKK".isalnum()) # True

print(" ")

print("kotek".isalpha()) # True - sprawdza, czy łańcuch znaków składa sie z samych liter
print("123kotek".isalpha()) # False
print(" kotek".isalpha()) # False

print("\ndigit")
print("123kotek".isdigit()) # False - sprawdza, czy łańcuch znaków składa sie z samych cyfr
print("123789".isdigit()) # True
print(" 1234 ".isdigit()) # False

print(" ")

print("test".islower()) # True - sprawdza, czy łańcuch znaków składa sie z samych małych liter
print("tesT".islower()) # False
print("123test".islower()) # True
print("TEST".isupper()) # True - sprawdza, czy łańcuch znaków składa sie z samych wielkich liter
print("TESt".isupper()) # False
print("123TEST".isupper()) # True

print(" ")

print("test".isspace()) # False- sprawdza, czy łańcuch znaków zawiera same białe znaki(spacja, tabulator, nowa linia)
print("   \n\n\t   ".isspace()) # True

print(" ")

print("-|-".join(["ala", "ola", "adam", "ania"])) # ala-|-ola-|-adam-|-ania - łączy wartości w liście z wcześniej 
 # join - lącz                                                 # ustalonym przez nas łańcuchem znaków (np. -|-)
print("Hello World!".lower()) # hello world! - wszystkie litry w łańcuchu znaków zamienia na małe
print("Hello World!".upper()) # HELLO WORLD! - wszystkie litry w łańcuchu znaków zamienia na WIELKIE
print("Hello World!".swapcase()) # hELLO wORLD! - zamienia liter małe na wielkie/ wielkie na małe w łańcuchu znaków
user = "Michał Grbarz" # michał grbarz
print(user.lower())
print(" ")

print("   \n \t Hello    World! \n \t   ".strip()) # Hello    World! - usuwa wszystkie białe znaki z łańcucha znaków
                                                   # (bez białych znaków między tekstem)
print("   \n \t Hello World! \n \t   ".lstrip()) # usuwa wszystkie białe znaki po lewej stronie
print("   \n \t Hello World! \n \t   ".rstrip()) # usuwa wszystkie białe znaki po prawej stronie

print(" ")

print("ola ma kota, ola ma psa".replace("ola", "Adam")) # Adam ma kota, Adam ma psa - zamienia łańcuch znaków innym 
                                                        # łańcuchem (ola zamienia się na Adam) 
print(" ")

print("My name is {myName}, I'm from {country}".format(myName = "Michał", country = "Poland"))
print("My name is {myName}, my postal code {code}, I'm from {country}".format(myName = "Michał", code = 26600, country = "Poland"))
print("My name is {0}, my postal code {1}, I'm from {2}".format("Michał", 26600, "Poland"))
print("My name is {}, my postal code {}, I'm from {}".format("Michał", 26600, "Poland"))
# przykłady użycia funkcji format służącej do formatowania tekstu

print(" ")
argument = ["Michał", 38]
tekst = "My name is {0}, I've {1} years old. {0}{1}".format(argument[0], argument[1])
print(tekst)
tekst = "My name is {imie}, I've {wiek} years old. {imie}{wiek}".format(imie = argument[0], wiek = argument[1])
print(tekst)
moje_imie = "Michał"
moj_wiek = 38
print(f"My name is {moje_imie}, I've {moj_wiek}. {argument}")
print(f"My name is {moje_imie}, I've {moj_wiek}. {argument[0]}{argument[1]}")
# kolejne przykłady użycia funkcji format służącej do formatowania tekstu (pobieramy argumenty ze zmiennej)
path, destination, subtotal = "ass", "work", 0.0
print(f"moved {path} to {destination}") # moved ass to work
print("rachunek całkowity: $%.2f" % subtotal) # rachunek całkowity: $0.00 - %.2f % subtotal - wyświetli liczbę 2 miejsca po przecinku 

