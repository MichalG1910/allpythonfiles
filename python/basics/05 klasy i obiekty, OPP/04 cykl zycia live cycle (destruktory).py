
class test:
    def __del__(sel): # metoda wykonywana jest na sam koniec skryptu i służy wyczyszczeniu pamięci. 
                      # Nawet jeśli wywołamy obiekt, który powstał na bazie klasy z tą magiczną metodą,
                      # a po nim pojawi się dalsza część kodu, to i tak obiekt zostanie wywołany na końcu skryptu
        print("Bye class")
# /1/
print("/1/ --------------------------------")
obj = test()
print("koniec")
del obj
# konsola wyświetli: koniec
#                    Bye class

# /2/
print("\n/2/ -------------------------------")
obj = test()
del obj         # usuwamy obiekt obj przed wywołaniem print("koniec"), więc nie odwróci on kolejności 
print("koniec") # wyświetlenia (wykonania) jak dla przypadku wyżej /1/ 
# konsola wyświetli: Bye class
#                    koniec

# /3/
print("\n/3/ -------------------------------")
obj = test()
obj2 = obj     # tworzymy kolejny obiekt obj2, który powstaje na bazie obiektu obj (tworzymy uchwyt do klasy), 
del obj        # więc wywołanie funkcji del nie spowoduje calkowitego usunięcia obiektu obj (uchwyt pozostanie)
print("koniec")
del obj2
# konsola wyświetli: koniec
#                    Bye class

# /4/
print("\n/4/ -------------------------------")
obj = test()
obj2 = obj 
lista = [obj2] # sytuacja jak /3/, utworzona lista ma uchwyt do klasy (obj, obj2 są nie calkowicie usunięte)
del obj
del obj2        
print("koniec")
del lista[0]
# konsola wyświetli: koniec
#                    Bye class

# /5/
print("\n/5/ -------------------------------")
obj = test()
obj2 = obj 
lista = [obj2] 
del obj
del obj2 
del lista[0]      
print("koniec")
# konsola wyświetli: Bye class
#                    koniec


# Zasada usuwania obiektów jest taka, że jśli jakiś inny obiekt odnosi się do kasowanego funkcją del obiektu,
# to ten obiekt nie zostanie skasowany całkowice i pozostawi uchwyt do klasy. 
# Całkowite kasowanie obiektu jest możliwe tylko wtedy, gdy nie ma on relacji z żadnym innym obiektem

