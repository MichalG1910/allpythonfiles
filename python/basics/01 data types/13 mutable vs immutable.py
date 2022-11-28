
#immutable: int, float, bool, str, tuple, frozenset - o ile możemy zmienić zmienną, to tak naprawdę tworzymy nową 
# zmienną w innym miejscu w pamięci

a = 1
print(a)
addr1 = id(a)
a += 1              # zwiększa zmienną o 1
print(a)
addr2 = id(a)

print(addr1)
print(addr2)
print(addr1 == addr2) # porównanie adresu w pamięci da wynik False


#mutable types: list, set, dict - przy zmianie zmiennej przechowywana ona jest w tym samym miejscu w pamięci
listData = [0,1,2]
print(listData)
addr1 = id(listData)

listData += [3,4,5]
print(listData)
addr2 = id(listData)

print(addr1)
print(addr2)
print(addr1 == addr2) # porównanie adresu w pamięci da wynik True


