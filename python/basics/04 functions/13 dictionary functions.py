# dictionary functions - funkcje słownika

data = {"name"  : "ola", "city" : "waw"} # {"name(key)" : "ola(value)"}
print(data["name"]) # ola - dla klucza "name" zwróci wartość "ola"

dataPostalCode = "postal code"
data[dataPostalCode] = 12345 # dodanie rekordu do słownika 'postal code': 12345
print(data) # {'name': 'ola', 'city': 'waw', 'postal code': 12345}
print(len(data)) # 3 - liczba elementów słownika

del data["city"] # kasowanie elementu słownika
print(data) # {'name': 'ola', 'postal code': 12345}
print(data.pop("postal code")) # kasowanie elementu słownika (2 metoda)
print(data) # {'name': 'ola'}
data["city"] = "Rad" # dodanie rekordu do słownika 'city': 'Rad'
print(data) # {'name': 'ola', 'city': 'Rad'}
data.clear() # {} skasowanie wszystkiego w słowniku
print(data) 

print(" ")

data = {"name"  : "kasia", "city" : "Krk"}
dataCopy = data.copy() # utworzenie kopi (płytkiej) słownika data
print(dataCopy)
print(data["name"] is dataCopy["name"]) # True, widzimy, że ten sam element w slowniku data i dataCopy są 
                                        # w tym samym miejscu w pamięci (dlatego jest to płytka kopia)
print( data is dataCopy) # False - zmienna data i dataCopy jako słownik są w innym miejscu w pamięci 
                         # (w odróżnieniu od elementów zawartych w tych słownikach)
print(" ")

data2 = dict.fromkeys(("name", "city", "code"))# tworzenie nowego słownika po zadeklarowanych kluczach
print(data2) # {'name': None, 'city': None, 'code': None}. Wartości values przyjmują "None"

data3 = dict.fromkeys(("name", "city", "code"), "|MG|" )# tworzenie nowego słownika po zadeklarowanych kluczach
print(data3) # {'name': '|MG|', 'city': '|MG|', 'code': '|MG|'}. Wartości values przyjmują |MG|

print(" ")

print( data2.get("x", "DEFAULT")) # DEFAULT- sprawdzenie, czy slownik data2 ma klucz "x", jeśli nie to DEFAULT
print( data3.get("city", "code doesnt exist")) # |MG|- jeśli tak, to zwróci wartość (value) dla tego klucza
print("name" in data2) # true- sprawdzenie, czy slownik data2 ma klucz "name", TAK- True, NIE- False
print(data2.keys()) # dict_keys(['name', 'city', 'code']) - zwraca wszystkie keys
print(data2.values()) # dict_values([None, None, None]) - zwraca wszystkie values

print("\nPętla:")

for v in data3: # lub [for v in data3.keys():]
    print(v) # iteracja słownika po kluczu
for v in data3.values(): 
    print(v) # iteracja słownika po wartości

print("\nUsuwanie zawartości ze slownika(metoda 2). Można użyć też del (patrz wiersz 11)")
print(data3)               # {'name': '|MG|', 'city': '|MG|', 'code': '|MG|'}
print(data3.pop("name"))   # |MG|
print(data3)               # {'city': '|MG|', 'code': '|MG|'}

print()

dict1 = dict(ford = 1950, opel = 1940, mercedes = 1932) #n tworzenie slownika
print(dict1) # {'ford': 1950, 'opel': 1940, 'mercedes': 1932}

dict2 = dict([("ford", 1950), ("opel", 1940), ("mercedes", 1932)]) #n tworzenie slownika [lista(tupli)]
print(dict2) # {'ford': 1950, 'opel': 1940, 'mercedes': 1932}



