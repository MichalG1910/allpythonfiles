
# for - pętla,którą możemy wykorzystać do iteracji tylko : listy, krotki, zbioru, słownika, łańcucha znaków

for v in [1,2,3,4]:                 # iteracja listy
    print( v * 2 )

for v in ( "Ania", "Ola", "Ala"):   #iteracja krotki
    print(v + " jest")
for v in ("Ania", "Ola", "Ala", "Adam", "Filip"):    
    print(v, end = (", ")) # umożliwia wydrukowanie iterowanych argumentów w jednym wierszu
print("")

for el in { 3,4,5,6,7, "Ola" }:     # iteracja zbioru
    print(el)

for v in "hello world":             # iteracja łańcucha znaków znaków
    print(v)
else:
    print( "pętla zakończona")


dictionaryData = { "Ania" : "ania@exaple.com", "Ola" : "ola@example.com", "Jan" : "jan@wp.pl"} 

for key in dictionaryData:          # iteracja po kluczu slownika
    print(key)
for key in dictionaryData.keys():   # i to samo inaczej zapisane
    print(key)

for key in dictionaryData.keys():   # przy takim zapisie otrzymamy wartości dla każdego klucza
    print( dictionaryData[key] )

for key, value in dictionaryData.items(): # iteracja po kluczu i wartości slownika jednocześnie
    print( key, " : ", value)

for values in dictionaryData.values(): # iteracja po wartości slownika
    print(values)

for v in "string": # iteracja łąncucha znaków
    print(v)       # otrzymamy wydruk każdej litery naszego string

shopShelf = [1,2,3,4,5,6]
for product in shopShelf:
    print(product, end = " ") # 1 2 3 4 5 6

# użycie end = " " powoduje wyświetlenie wyniku tej pętli w jednym wierszu. Poszczególne elementy                      
			  # naszej listy są wyświetlane w odstępach spacji (może być to też inny znak)







   





