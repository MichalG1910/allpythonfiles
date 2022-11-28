
# identity operators - operatory tożsamości is, is not

strData = "test"

print( dir(strData) ) # dir - każda zmienna w praktyce jest obiektem, więc polecenie dir otwiera 
# listę dostępnych dla danego obiektu funkcji ułatwiających z nim pracę
print( strData.upper() ) # upper - jedna z funkcji - konwertuje tekst na wielkie litery

intData = 10

print( dir(intData) ) # inny przykład funkcji dla liczby całkowitej

# is - operator sprawdza, czy 2 zmienne odnoszą się do tego samego miejsca w pammięci
a = [1,2,3,4,5]
b = a
print( a is b) # True


# metody sprawdzenia

print(a) ; print(id(a))
print(b) ; print(id(b))

if id(a) == id(b):
    print("to samo miejsce w pamięci")
if id(a) != id(b):
    print("inne miejsce w paięci")

a.append(77) # append - dodać ( w tym przypadku dodajemy kolejną wartość do listy a)
print(a) 
print(b) # jak widać, do listy b została dodana liczba 77, więc adres w pamięci a i b jest taki sam
print( 77 in b)

if 77 in b:
    print( "77 jest w zmiennej b, więc zajmuje ona te samo miejsce w pamięci co zmienna a" )

print( a is not b ) # False - operator is not sprawdza, czy zmienne nie odnoszą sie do tego samego miejsca w pamięci

c = [3,4,5]
print( a is c ) # False
print( a is not c) # True