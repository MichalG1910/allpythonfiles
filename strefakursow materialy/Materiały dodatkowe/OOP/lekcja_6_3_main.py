from lekcja_6_3 import Person

Person1 = Person("Piotr", "Koska", "piotr@koska.loc", "Piotr12")
Person1.printPersonInformation()

print("")

Person2 = Person("Piotr", "Koska", "piotr@koska.loc", "Piotr12")
Person1.printPersonInformation()

Person3 = Person1

print("")
print(Person1 == Person3)

print("")
print(Person1)
print(Person3)
