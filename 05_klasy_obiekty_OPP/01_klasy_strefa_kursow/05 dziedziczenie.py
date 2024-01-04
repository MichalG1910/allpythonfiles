import klasa05dziedziczenie as Animal  # importujemy moduł z naszymi klasami i nadajemy mu alias Animal

boy = Animal.Boy(3, "Adam", "Grabarz")


boy.print_information() # 3, Adam, I'm mammal - klasa Boy dziedziczy print_information z klasy Mammal

print()

boy.give_voice()
boy.go_to()

animal = Animal.Animal(5, "Ciapek")
animal.print_information()
animal.give_voice() # def give_voice(self): raise NotImplementedError()
# wywołanie tej funkcji spowoduje wyświetlenie naszego zdefiniwanego błędu:
#Traceback (most recent call last):
# File "d:/python/basics/strefakursow/klasy/05 dziedziczenie.py", line 15, in <module>
#   animal.give_voice() # def give_voice(self): raise NotImplementedError()
# File "d:\python\basics\strefakursow\klasy\klasa05dziedziczenie.py", line 9, in give_voice
#   raise NotImplementedError() # definiujemy obsługę błędu, jeśli odniesiemy się do tej funkcji, to ją wywołamy
#NotImplementedError




