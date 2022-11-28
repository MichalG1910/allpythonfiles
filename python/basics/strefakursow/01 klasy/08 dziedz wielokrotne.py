import klasa08dziedz_wielokrotne as Animal

myduck = Animal.Duck(4, "Krzyżówka")
print("--------Live Duck----------")
print(f"wiek: {myduck.age}, gatunek: {myduck.breed}")
myduck.fly() # wywołujemy funkcję z klasy class DuckBehaviori(ABC), która jest abstrakcyjna
myduck.say() # możemy to zrobić, ponieważ (patrz opis w pliku z naszą klasą klasa08dziedz_wielokrotne)
myduck.go_to()

mytoy = Animal.DuckToy("plastik", "zielona")
print("--------Toy Duck----------")
print(f"{mytoy.material}owa {mytoy.color} kaczka")
mytoy.fly()
mytoy.say()
mytoy.go_to()