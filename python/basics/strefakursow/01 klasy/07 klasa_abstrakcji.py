import klasa07klasa_abstrakcji as Animal  # importujemy moduł z naszymi klasami i nadajemy mu alias Animal

boy = Animal.Boy(3, "Adam", "Grabarz")
boy.print_information() # klasa Boy dziedziczy print_information z klasy Mammal

print()

boy.give_voice()
boy.go_to()

animal = Animal.Animal()  
animal.print_information()
animal.give_voice() 
 
# linie po usunięciu komentarza odnoszą się do klasy abstrakcyjnej, pow wywołaniu spowodują wyświetlenie błędu

# Jeśli nie skorzystamy z (from abc import ABC, abstractmethod), to będzie nasz zdefiniowany błąd:
''' 
File "d:/python/basics/strefakursow/klasy/07 klasa_abstrakcji.py", line 13, in <module>
    animal = Animal.Animal()
  File "d:\python\basics\strefakursow\klasy\klasa07klasa_abstrakcji.py", line 5, in __init__
    raise Exception("Unable to create object of a abstract class")
Exception: Unable to create object of a abstract class 
'''

# Jeśli  skorzystamy z (from abc import ABC, abstractmethod), to będzie :
'''
Traceback (most recent call last):
  File "d:/python/basics/strefakursow/klasy/07 klasa_abstrakcji.py", line 13, in <module>
    animal = Animal.Animal()
TypeError: Can't instantiate abstract class Animal with abstract methods give_voice
'''





