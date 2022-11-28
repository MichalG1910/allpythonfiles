plik = open("d:\\python\\basics\\inne\\test.txt", "a") # utworzy plik na podanej przez nas ścieżce pliku.
# podanie tylko samej nazwy pliku(plik = open("test.txt", "w")) utworzy nam plik w katalogu głównym (basics)

# drugi argument oznacza: 
# w (write) - plik do zapisu, (za każdym razem otwarcie pliku w formie do zapisu powoduje wyzerowanie 
# poprzedniej zawartości tego pliku)
# r (read) - plik do odczytu, 
# a (append) dołączać - pozwoli na dołączenie do pliku dalszego tekstu bez usuwania starego
if plik.writable():
    ile = plik.write(input("wprowadź tekst: ") + "\n")
    print("Zawartość: ", ile) # zmienna utworzona na funkcji write zwraca nam ilość znaków wprowadzonego
                              # np. michal - Zawartość: 7 (pamietaj o znaku zmiany linii \n) 
plik.close()

plik = open("d:\\python\\basics\\inne\\test.txt", "r")
if plik.readable():
    tekst = plik.read() # odczytanie pliku do zmiennej tekst
    print("\nZawartość pliku:\n" + tekst)
plik.close()

plik = open("d:\\python\\basics\\inne\\test.txt", "r")
if plik.readable():
    tekst = plik.readlines() # tworzy listę z poszczeglnych wierszy w pliku txt
    print(tekst)
    for v in tekst:
        print(v)
plik.close()
