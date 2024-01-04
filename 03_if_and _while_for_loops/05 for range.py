# pętla for z funkcją range - funkcja range zwraca listę liczb w danym zakresie

for v in range(5):  # zwraca sekwencję liczb [0,1,2,3,4] czyli wartość range (5) minus 1 
    print(v)

print ('') # wolny wiersz

for v in range(3,8): # zwraca sekwencję liczb [3,4,5,6,7] ( o 1 mniej niż druga wartość w range)
    print (v)
    
print ('')

for v in range(2,15,2): # zwróci sekwencję liczb [2,4,6,8,10,12,14] (o 2 mniej niż ostatnia wartość w range)
    print(v)
# opis przykład wyżej raange(2,-liczba początkowa,15- liczba końcowa[nie będzie zwrócona], 2- krok co 2)

a = list(range(8 , 0, -1)) # [8, 7, 6, 5, 4, 3, 2, 1] - zapis odwrócony - zwróci listę od największej do najmniejszej
print(a)


    


