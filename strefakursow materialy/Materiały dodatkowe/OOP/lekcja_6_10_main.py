import lekcja_6_10 as Animal

myduck = Animal.Duck(4, "Krzyzowka")

print("----- Live Duck ------")
myduck.fly()
myduck.say()
myduck.go_to()

mytoy = Animal.DuckToy("zielona", "aluminiowa")

print("----- Toy Duck -------")
mytoy.fly()
mytoy.say()
mytoy.go_to()
