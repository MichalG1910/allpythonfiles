import klasa08dziedz_wielokrotne as Animal



kaczka = Animal.Duck(3, "Dziwaczka")
zabawka = Animal.DuckToy("metalowa", "czerwony")
kotek = Animal.Cat()
lista = [kaczka, zabawka, kaczka, zabawka, kotek]

for obiekt in lista:
    if hasattr(obiekt, "fly"): 
        obiekt.fly()
# hasattr(zmienna, szukany atrybut) - szuka w naszym iteracji "obiekt", czy posiada taki atrybut. Jeśli tak, zwraca nam 
# obiekt.fly(), jeśli nie posiada, pomija ten "obiekt". Jeśli nie zastosowalibyśmy hasattr(), to uzyskalibyśmy błąd:
"""Traceback (most recent call last):
  File "d:/python/basics/strefakursow/klasy/09 polimorfizm.py", line 8, in <module>
    obiekt.fly()
AttributeError: 'Cat' object has no attribute 'fly'"""
print ()

for obiekt in lista:
    try: 
        obiekt.fly()
    except AttributeError:
        print(f"Obiekt {obiekt} nie posiada metody 'fly'")
# to samo uzyskamy stosując metodę try:except
