
plik = open("d:\\python\\basics\\inne\\analizatekstu.txt", "r")
tekst = plik.read()
plik.close()

def policz(txt, znak): # definicja pozwala nam policzyć ilość wystąpień danego znaku w tekscie
    licznik = 0
    for z in txt:
        if z == znak:
            licznik += 1
    return licznik

print(policz(tekst, "a")) # wyświetla ilość danej liter, w tym przypadku a
print(policz(tekst, "A")) # wyświetla ilość danej liter, w tym przypadku A
print(policz(tekst, "a") + policz(tekst, "A")) # wyświetla ilość danej litery, a małe + A duże
print(policz(tekst.lower(), "a")) # suma a + A (to samo co wyżej, tylko uproszczony zapis dzięki metodzie lower)

print("________________________________________________________________________________________\n")

for z in "abcdefghijklmnoprstuwxyz,.-+=:;@!#$%":
    ile = policz(tekst.lower(), z)  # lower - powoduje zamianę wszystkich liter w tekście na małe, dzięki czemu 
                                    # otrzymujemy ilość wystąpień każdej z liter bez względu na to czy jest 
                                    # duża czy mała
    procent = 100 * ile / len(tekst)
    print("{0} - {1} - {2}%".format(z.upper(), ile, round(procent, 2)))

# powyżej sprawdzamy cały tekst i otrzymujemy wynik dla każdej litery z ciągu znaków
# ( który jest tak naprawdę listą) w postaci ilości wystąpień i procentowego udzialu w całym tekscie

print("_______________________________________________________________________________\n")

lista = ("the", "always", "install", "you", "has", "is", "michal")
for z in lista:
    tekst = tekst.lower()
    ile = tekst.count(z)
    print("{0} - {1}".format(z, ile))
# sprawdza ilość wystąpień poszczególnych wyrazów w tekście (bez względu na wielkość liter(lower))
