
imie = ""
nazwisko = "Koska"

imie_nieznane = imie or "NN"
nazwisko_nieznane = nazwisko or "NN"
nazwisko_jednak_jest = nazwisko and "Nasz gość jednak ma nazwisko"

if not imie:
    print("Nasz gość nie ma imienia.")

if imie and nazwisko:
    print("Nasz gość - imie: {}, nazwisko {}".format(imie_nieznane,nazwisko_nieznane))
    print("Logiczna wartość dla imie {} logiczna dla nazwisko: {}".format(bool(imie),bool(nazwisko)))
else:
    print("Nie ma imienia: {} i nazwiska: {}".format(imie_nieznane,nazwisko_nieznane))
    print(nazwisko_jednak_jest)
