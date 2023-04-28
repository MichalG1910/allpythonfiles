import glob
import os
import shutil
import json
import re

try:
    os.mkdir("./strefakursow/processed")
except OSError:
    print("'./processed' directory already exist")

receipts = [f for f in glob.glob('./strefakursow/receipts/receipt- [0-9]*.json') if re.match('./strefakursow/receipts/receipt- [0-9]*[02468].json', f)]
print(receipts)
# match(dopasuj) - domślnie szuka 1 argument w 2 argumencie na jego początku. jeśli go tam nie znajdzie, zwraca None.
# w naszym przypadku re.match szuka ścieżki d:\\python\\basics... w zmiennej f (która został ziterowana pętlą for) 
# zostaną one zapisane w postaci listy. dodanie klasy [02468] da nam tylko parzyste z przedziału 0-9
# PRZYP. metoda glob powoduje przeszukanie lokalizacji wskazanej w nawiasie i zwrócenie wszystkich pasujących
# wyników (receipt - [0-9]*.json - wyrażenie regularne, dopasuje wszystkie pliki receipt - 0 do 9.json)
subtotal = 0.0
for path in receipts: # tworzymy pętlę, która iteruje z naszej listy receipts pojedyńcze argumenty
    with open(path) as f: # w każdym przejściu petli for otworzy dopasowany plik (z listy receipts)(as f - dla ułatwienia zmienna path będzie dostępna jako f)
        content = json.load(f) # json.load - ładujemy zawartość otwartego pliku do zmiennej content
        subtotal += float(content["value"]) # zwiększamy nasz rachunek subtotal o wartość "value" zawartą w naszym pliku receipt - [0-9]*.json    
    destination = path.replace("receipts", "processed") # nasza nowa ścieżka (path- jest to ścieżka do pliku).
    # funkcja replace zamienia w ścieżce string "receipts" na "processed"
    shutil.move(path, destination) # shutil.move - przeniesie nasz iterowany plik z lokalizacji path do destination
    print(f"moved '{path}' to '{destination}'")
print("Receipt subtotal (rachunek całkowity): $%.2f" % subtotal)