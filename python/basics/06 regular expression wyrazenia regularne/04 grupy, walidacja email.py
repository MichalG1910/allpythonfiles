
import re

wynik = re.match(r"^(Hello) (Wor(ld))$", "Hello World") # zastosowanie () we wzorze tworzy tzw. grupę (nienazwaną)
                                                        # tworząc grupy możemy je w sobie zagnieżdżać
if wynik:
    print("Dopasowano!")
    print(wynik.group()) # Hello World
    print(wynik.group(0)) # Hello World
    print(wynik.group(1)) # Hello
    print(wynik.group(2)) # World
    print(wynik.group(3)) # ld
    print(wynik.groups()) # ('Hello', 'World', 'ld') # wyświetla wszystkie grupy
else:
    print("Nie dopasowano!")

print("|2|-----------------------------------------------------------------------")


wynik = re.match(r"^(Hello) (World)+$", "Hello WorldWorld") # plus stojący przed grupą powoduje, że musi ona 
# wystąpić w przeszukiwanym tekście conajmniej 1 raz, ale może nieskończenie wiele razy

if wynik:
    print("Dopasowano!")
    print(wynik.group()) # Hello WorldWorld
    
else:
    print("Nie dopasowano!")


print("|3|-----------------------------------------------------------------------")


wynik = re.match(r"^((?:He)(?P<first>ll)o) (World)$", "Hello World") # (?P<first>ll) - grupa nazwana (nazwa : first)
# jakbyśmy stworzyli we wzorze taką grupę (?:He) - nię będzie ona indeksowana (nie zostanie też wyświetlona)
if wynik:
    print("Dopasowano!")
    print(wynik.group()) # Hello World
    print(wynik.group(0)) # Hello World
    print(wynik.group(1)) # Hello
    print(wynik.group(2)) # ll
    print(wynik.group(3)) # World
    print(wynik.groups()) # ('Hello', 'll', 'World') 
    print(wynik.group("first")) # ll - do grupy nazwanej możemy się odnieść za pomocą jego nazwy (first)
    
else:
    print("Nie dopasowano!")


print("|4|-----------------------------------------------------------------------")


wynik = re.match(r"^((?:He)(?P<first>ll)o)( World)+(!|\.)$", "Hello World World World.") # (!|\.) na końcy tekstu 
# ma wystąpić albo ! albo "." Przed kropką musi być \ (inaczej kropka by nam wskazywała na każdy znak (!|.))
# | - oznacza lub

if wynik:
    print("Dopasowano!")
    print(wynik.group()) # Hello World World World.
    print(wynik.group(0)) # Hello World World World.
    print(wynik.group(1)) # Hello
    print(wynik.group(2)) # ll
    print(wynik.group(3)) # World
    print(wynik.groups()) # ('Hello', 'll', ' World', '.') 
    print(wynik.group("first")) # ll 
    
else:
    print("Nie dopasowano!")

print("|5|---------------walidacja adresu email----------------------------------")
# poniższe wyrażenie sprawdza, czy adres email jest prawidłowy

if re.match(r"^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9-\.]+[A-Za-z0-9])\.[A-Za-z0-9]+()$", "grabarz.michal@gmail.com"):
    print("Dopasowano!")
else:
    print("Nie dopasowano!")