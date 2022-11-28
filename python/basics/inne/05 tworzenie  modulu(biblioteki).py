
from mymodule import my_module # stworzyłem moduł my_module, który zapisany jest w katalogu /mymodule
# dodawanie modułow można zrobić przez dodanie ich do katalogu Lib w katalogu z zainstalowanym pythonem
# u mnie jest to C:\Users\graba\AppData\Local\Programs\Python\Python310\Lib

import mymodule.lekcja_5_5 as lek # użycie "as" daje możliwość zdefiniowania nowego krótszzego i bardziej 
# przystepnego odnśnika do naszego zdefiniowanego modułu

from mymodule import __init1__ , __mich__

msg = my_module.my_function("Michał")
print(msg)
print(my_module.x)
print(dir(my_module))

print("-------------------------------------------------")

print(lek.string) # zastosowanie skróconej nazwy do naszego modułu lekcja_5_5

__init1__.myNext(20, 25)
__mich__.mich_func(4, 7)



