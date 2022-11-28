
contacts = {                    # słownik od dictionary <class 'dict'>
    "Ola" : "ola@exaple.com",
    "Daniel" : 30,
    "Ania" : "ania@example.com"
}

contacts["Rafał"] = "rafał@example.com" # dodanie kolejnego rekordu do słownika
print(contacts["Ola"])                  # ola@exaple.com - wywołanie ze słownika rekordu Ola 
print(contacts["Daniel"])               # 30
print(type(contacts))                   # wywołanie typy <class 'dict'>
print(len(contacts))                    # 4 - ilość rekordów w słowniku (klucz + wrtość)

print(" ")

print( contacts.keys())                 # dict_keys(['Ola', 'Daniel', 'Ania', 'Rafał']) wyświetla wszystkie klucze ze słownika 
print( contacts.values())               # dict_values(['ola@exaple.com', 30, 'ania@example.com', 'rafał@example.com']) wyświetla wszystkie wartości (values) ze słownika

print(" ")

for key in contacts:                    # iterowanie po zmienej key???
    print(key + " " + str(contacts[key])) # funkcja str zamienia liczbę na łańcuch znaków 

print(" ")

for key, value in contacts.items():     # iterowanie po zmiennych key, value???
    print(key, " ", value)              # items - użycie wszystkich elementów słownika
    
print()
contacts.update({"Adam": "brzdąć 1", "Filip": 5, "Karolina": "mama drani"}) # update - doda do słownika contacts nowe pary kluczy i wartości (powiększy słownik o kilka par)
# update może też zmienić wartość , jeśli podany klucz już istnieje w słowniku
print(contacts) # {'Ola': 'ola@exaple.com', 'Daniel': 30, 'Ania': 'ania@example.com', 'Rafał': 'rafał@example.com', 'Adam': 'brzdąć 1', 'Filip': 5, 'Karolina': 'mama drani'}


