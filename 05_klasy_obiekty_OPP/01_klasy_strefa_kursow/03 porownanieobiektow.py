from klasa03porow_obiektow import Person

print("-------------------1---------------------")

person1 = Person("Michał", "Grabarz", "grabarzmichal@gmail.com", "bioly1910")
person1.printPersonInformation()

print("------------------2-------------------")

person2 = Person("Michał", "Grabarz", "grabarzmichal@gmail.com", "bioly1910")
person2.printPersonInformation()

print()
person3 = person1
print(person1 == person2) # False
print(person1 == person3) # True

print(person1) # <klasaporow_obiektow.Person object at 0x0000024691C37D60>
print(person2) # <klasaporow_obiektow.Person object at 0x0000024691D9BAF0>
print(person3) # <klasaporow_obiektow.Person object at 0x0000024691C37D60>

# Podsumowanie: jeśli mamy dwa obiekty utworzone na tej samej klasie, które mają takie same dane(w tym przypadku: 
# pname, surname, email, nickname), to dalej są to dwa różne obiekty(zajmują inne miejsce w pamięci)
# jeżeli utworzymy nową zmienną obiektową z istniejącego obiektu (person3 = person1), to będzie to w rzeczywistości 
# ten sam obiekt w tym samym miejscu w pamięci
