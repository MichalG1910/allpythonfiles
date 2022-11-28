import lekcja_6_10 as Animal

kaczka = Animal.Duck(3, "Dziwaczka")
zabawka = Animal.DuckToy("czewony", "metalowa")
kotek = Animal.Cat()

lista = [kaczka, zabawka, kaczka, zabawka, kotek]

for obiekt in lista:
    try:
        obiekt.fly()
    except AttributeError:
        print("Obiekt", obiekt, "nie posiada mety fly")
