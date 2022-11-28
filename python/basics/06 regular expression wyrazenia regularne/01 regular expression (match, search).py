
import re
wzor = r"banan\nbanan\tbanan" # banan\nbanan\tbanan # r - row czyli surowy(nie będzie czytało znaków specjalnych \n \t)
print(wzor)
print()

wzor = r"banan"
tekst = r"gruszkabananjabłko"
tekst1 = r"banangruszkabananjabłko"

print("|1|")
print(re.match(wzor, tekst)) # None # match(dopasuj) - domślnie szuka 1 argument w 2 argumencie na jego początku.
# jeśli go tam nie znajdzie, zwraca None. 
print(re.match(wzor, tekst1)) # <re.Match object; span=(0, 5), match='banan'>
if re.match(wzor, tekst):
    print("Dopasowano!")
else:
    print("Nie dopasowano!")


print("|2|")
print(re.match(r".*" + wzor + r".*", tekst)) # zastosowanie r".*" powoduje, że match szuka w całym tekście
                                             # <re.Match object; span=(0, 18), match='gruszkabananjabłko'>
if re.match(r".*" + wzor + r".*", tekst):    # Dopasowano!
    print("Dopasowano!")
else:
    print("Nie dopasowano!")


print("|3|")
print(re.search(wzor, tekst)) # search(szukaj) -przeszukuje cały tekst i znajduje szukany wyraz nawet w środku
                              # <re.Match object; span=(7, 12), match='banan'>              
if re.search(wzor, tekst):    # Dopasowano!
    print("Dopasowano!")
else:
    print("Nie dopasowano!")


print("|4|")
wzor = r"banan"
tekst1 = r"gruszkabananjabłkogruszkabananjabłkogruszkabananjabłko"
print(re.findall(wzor, tekst1)) # findall - znajduje wszystkie dopasowania w tekście i zwraca je w postaci listy
                               # ['banan', 'banan', 'banan']


print("|5|")
wzor = r"banan"
tekst = r"gruszkabananjabłko"

dopasowanie = re.search(wzor, tekst)# jeśli nasze wyrażenie przypiszemy do zmiennej, zachowuje się ono jak obiekt

if dopasowanie:
    print(dopasowanie.group()) # banan - group wskazuje wszystkie grupy, które udało się dopasować
    print(dopasowanie.start()) # 7 - początek szukanego słowa w stringu
    print(dopasowanie.end()) # 12 - koniec szukanego słowa w stringu
    print(dopasowanie.span()) # (7, 12) -krotka z początkiem i końcem szukanego słowa w stringu (span -łącznik)


print("|6|")
wzor = r"banan"
tekst = r"gruszkabananjabłko"

tekst2 = re.sub(wzor, "JAGODA", tekst) # sub - wyszukuje nasz wyraz(argument 1 - wzor) w naszym tekście 
                                       #(arg 3 - tekst) i zastępuje go nowym wyrazem (arg 2 - "JAGODA")
print(tekst2) # gruszkaJAGODAjabłko