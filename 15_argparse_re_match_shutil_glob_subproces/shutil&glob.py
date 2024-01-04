import glob
import os
import shutil
import json


try:
    os.mkdir("d:\\python\\basics\\strefakursow\\processed")
except OSError:
    print("'./processed' directory already exist")
receipts = glob.glob("d:\\python\\basics\\strefakursow\\receipts\\receipt- [0-9]*.json")
print(receipts)
# medoda glob powoduje przeszukanie lokalizacji wskazanej w nawiasie i zwrócenie wszystkich pasujących
# wyników (receipt - [0-9]*.json - wyrażenie regularne, dopasuje wszystkie pliki receipt - 0 do 9.json)
# zostaną one zapisane w postaci listy
subtotal = 0.0
for path in receipts: # tworzymy pętlę, która iteruje z naszej listy receipts pojedyńcze argumenty
    with open(path) as f: # w każdym przejściu petli for otworzy dopasowany plik (z listy receipts)(as f - dla ułatwienia zmienna path będzie dostępna jako f)
        content = json.load(f) # json.load - ładujemy zawartość otwartego pliku do zmiennej content
        subtotal += float(content["value"]) # zwiększamy nasz rachunek subtotal o wartość "value" zawartą w naszym pliku receipt - [0-9]*.json
    name = path.split("\\")[-1] # spowoduje pobranie nazwy naszego pliku. Path po iteracji będzie to ścieżka(cała) do pliku. 
                                   # aby wziąć samą nazwę, Dzielimy ścieżkę split("\\") i bieżemy pierwszy argument od końca[-1]
    destination = f"d:\\python\\basics\\strefakursow\\processed\\{name}" # nasza nowa ścieżka
    shutil.move(path, destination) # shutil.move - przeniesie nasz iterowany plik z lokalizacji path do destination
    print(f"moved '{path}' to '{destination}'")
print("Receipt subtotal (rachunek całkowity): $%.2f" % subtotal)

