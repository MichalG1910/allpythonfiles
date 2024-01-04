contacts = {"Ola": "ola@exaple.com", "Daniel": 30, "Ania": "ania@example.com", "Rafał": "rafał@example.com"}

print(contacts["Ola"])  # ola@exaple.com - wywołanie ze słownika rekordu Ola
print(contacts["Daniel"])  # 30
print(type(contacts))  # wywołanie typy <class 'dict'>
print(len(contacts))  # 4 - ilość rekordów w słowniku (klucz + wartość)

print(" ")

print(contacts.keys())  # dict_keys(['Ola', 'Daniel', 'Ania', 'Rafał']) wyświetla wszystkie klucze ze słownika
print(contacts.values())  # dict_values(['ola@exaple.com', 30, 'ania@example.com', 'rafał@example.com']) wyświetla wszystkie wartości (values) ze słownika

print(" ")

for key in contacts:  # iterowanie po zmiennej key???
    print(key + " " + str(contacts[key]))  # funkcja str zamienia liczbę na łańcuch znaków

print(" ")

for key, value in contacts.items():  # iterowanie po zmiennych key, value???
    print(key, " ", value)  # items - użycie wszystkich elementów słownika

print()
contacts.update({"Adam": "brzdąc 1", "Filip": 5, "Karolina": "mama drani"})  # update - doda do słownika contacts nowe pary kluczy i wartości (powiększy słownik o kilka par)
# update może też zmienić wartość , jeśli podany klucz już istnieje w słowniku
print(
    contacts)  # {'Ola': 'ola@exaple.com', 'Daniel': 30, 'Ania': 'ania@example.com', 'Rafał': 'rafał@example.com', 'Adam': 'brzdąc 1', 'Filip': 5, 'Karolina': 'mama drani'}
