
# Bubble sort - sortowanie bąbelkowe
# poniższa lista sortuje argumenty listy od najmniejszej do największej (liczby, litery, słowa)
def sortowanie_babelkowe(lista):
    n = len(lista)
    
    while n > 1:
        zamien = False
        for v in range(0, n-1):
            #print(lista) #- zobaczysz jak to działa
            if lista[v] > lista[v+1]:
                lista[v], lista[v+1] = lista[v+1], lista[v]
                zamien = True
        #print(" ")       
        n -= 1
        
        if zamien == False: break
        
    return print(lista)
        
sortowanie_babelkowe(["ac", "aa", "az", "azz", "azb", "abc", "aba"])
    