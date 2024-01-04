# immutable: int, float, bool, str, tuple, frozenset

def modifyStr(strData):
    print(id(strData))  # adres w pamięci
    print(strData)      # Hello
    strData += "!"      # dodajemy ! do łańcucha znaków
    print(id(strData))  # nowy adres w pamięci
    print(strData)      # Hello!

string = "Hello"
print(id(string))
modifyStr(string)
# przekazany do funkcji łańcuch znaków po modyfikacji tworzy nowy łańcuch znaków w innym miejscu w pamięci tzn
# jest niemutowalny

print(" ")              
# offtopic, krótki program podający sumę cyfr z id zmiennej string

id1 = str(id(string))
print(id1)
idList = list(id1)
print(idList)
result = 0
for v in idList:
    result += int(v)
print(result)

# koniec offtopic
print(" ")

# mutable types: list, set, dict

def modifyList(listData):
    print(id(listData))     # adres w pamięci przed zmianą listy
    listData.append(10)     # dodajemy do listy argument 10
    print(id(listData))     # adres w pamięci po zmianie listy =  adres w pamięci przed zmianą listy

listValue = [0,1,2] 
print(id(listValue)) # adres w pamięci zmiennej listValue
modifyList(listValue)
# modyfikując listę przekazaną do funkcji nie zmieniamy adresu w pamięci tej listy(jest ona mutowalna). 
# Wszystkie 3 id wyświetlone w prograie będą takie same







