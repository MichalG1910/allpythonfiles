import random
import json

# skrypt utworzy 10 plików w formacie json, biorąc losowe dane z pliku txt

count = 10
words = [word.strip() for word in open("d:\\python\\basics\\inne\\slowa.txt").readlines()] 
# otwieramy nasz plik, z którego bedziemy pobierać dane( readlines - czytany linia po linii)

for id in range(count): # petla wygeneruje i zapisze pliki (count = 10, wiec od 0 do 9)
    amount = random.uniform(1.0, 1500) # value losowo od 1 do 1500
    content = {                         # nasz generowany produkt 
        "topic" : random.choice(words), # losowo wybiera z txt nazwę naszego produktu
        "value" : "%.2f" %amount        # value(wartość) w formatowaniu do 2 miejsc po przecinku ("%.2f")
                                        # zostanie pobrana ze zmiennej amount(wygenerowanej losowo)
              }
    with open(f"d:\\python\\basics\\strefakursow\\receipts\\receipt- {id}.json", "w") as f: # tworzymy plik json 
    # i nazywamy go na podstawie naszego id - przypisujemy mu odniesienie do prostszego zapisu( as f ) 
        json.dump(content, f) # zapisujemy (dump) nasz plik z danymi zawartymi w zmiennej content
        # json.dump(arg1, arg2): arg1 - dane do zapisu, arg2 - plik do którego zapisujemy  
