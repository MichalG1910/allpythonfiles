#!/usr/bin/python3

# Rewolwerowiec - Simple "Game"

import os

os.system('cls')
print("Dawno, dawno temu na dzikim zachodzie żył sobie pewien rewolwerowiec. Był on najszybszy na całym Dzikim Zachodzie")
input("Naciśnij aby kontynuować opowieść")
os.system('cls')

print("Pewnego dnia jeden śmiałek rzucił mu wyzwanie...\nStaneli razem w samo południe twarzą w twarz w samo południe. Kabury były odbezpieczone, z dwunastym wybiciem dzwonu mieli oddać strzał. Na Dzikim zachodzie nie ma miejsca dla dwóch rewolwerowców...")
input("Naciśnij aby kontynuować opowieść")
os.system('cls')

print("Dong")
input("Dong...")
os.system('cls')

print("Dong")
input("Dong...")
os.system('cls')

print("Dong")
input("Dong...")
os.system('cls')

print("Dong")
input("Dong...")
os.system('cls')

wybor = input("Co robisz?(strzał, uciekam, uciekam1) ")
gracz = str(wybor)

if gracz == "strzał":
    print("Rewolwerowiec nieżyje - wygrałeś")
    stan_gry = "wygrałeś"
elif gracz == "uciekam":
    print("Jesteś pośmiewiskiem całego dzikiego zachodu")
    stan_gry = "Przegrałeś i jesteś pośmiewiskiem"
elif gracz == "uciekam1":
    print("Wpadasz do wodopoju")
    stan_gry = "Przegrałeś i jesteś mokry"
else:
    print("Rewolwerowiec był szybszy - nie żyjesz :(")
    stan_gry = "Przegrałeś. Nie żyjesz."

print("Koniec Gry: {}".format(stan_gry))
